# ossimport数据迁移失败的常见报错原因与解决方案-对象存储-阿里云

Source: https://help.aliyun.com/zh/oss/solution-to-failure-to-migrate-oss-resources-by-using-the-data-migration-tool-ossimport

# 使用数据迁移工具ossimport迁移OSS资源失败的解决方法
## 问题描述
使用阿里云对象存储OSS时，将任意地域的本地存储数据、第三方存储数据、对象存储OSS数据迁移至任意地域的OSS中可以使用ossimport工具。本文介绍运用数据迁移工具ossimport迁移OSS资源失败的报错原因及解决方案。
## 问题原因
使用ossimport迁移失败的常见原因有以下几个：
- 上传过程中源目录的文件发生了修改，log/audit.log里会提示SIZE_NOT_MATCH相关字样的错误，这种情况下老的文件已经上传成功，新的修改没有上传到OSS。
- 源文件在上传过程中被删除，导致迁移失败。
- 源文件名不符合OSS命名规范（不能以/开头，不能为空），导致上传到OSS失败。
- 因网络异常、账号权限不足等原因导致的下载数据源文件失败，可查看logs/ossimport2.log或logs/import.log确定错误原因。
- 程序异常退出，任务状态为Abort 。这种情况请联系阿里云技术支持。
## 解决方案
当迁移失败时，执行bash console.sh stat命令查看迁移任务的状态，如果JobState为failed，则迁移任务失败，请查看迁移失败的日志，根据日志中的报错信息参见以下内容进行解决，您可以在解决这些问题后使用retry命令进行重试：
说明：OSS迁移失败的日志路径为master/jobs/[$JobName]/failed_tasks/[$TaskName]/audit.log。
- [$JobName]：任务名字，字符串。
- [$TaskName]：Task名称。
| 错误码 | 错误信息 | 报错原因 | 解决方案 |
| --- | --- | --- | --- |
| AccessDenied | The bucket you are attempting to access must be addressed using the specified endpoint | srcDomain 或 destDomain 填写错误。 | 请按照 [域名列表](user-guide/regions-and-endpoints.md) 填写正确的Endpoint。 |
| SignatureDoesNotMatch | The request signature we calculated does not match the signature you provided | destAccessKey 和 destSecretKey 有误。 | 请填写正确的AK信息。 |
| 无 | The bucket name “xxx/xx” is invalid | 配置项 destBucket 填写不正确。 | 检查配置项 destBucket 是否填写正确，Bucket名称是不带正斜线（/）以及路径的。 |
| ConnectionTimeout | Connect to xxx.oss-cn-beijing-internal.aliyuncs.com:80 timed out | 这个是连接超时的报错，通常原因是迁移用的设备非ECS实例或不是与OSS同地域的ECS实例，但是配置文件使用了OSS的内网域名。OSS内网域名仅支持同地域ECS实例访问。 | 该问题可以通过以下方法解决： 修改配置文件中域名为外网Endpoint，清除任务后重新提交任务。 使用与OSS同地域的ECS实例运行迁移任务。 |
| InvalidBucketName | The specified bucket is not valid | 配置文件里的 destDomian 配置的域名是Bucket所在地域的Endpoint地址，而不是带Bucket名称的二级域名。 | 填写正确的Bucket所在地域的Endpoint地址，例如Bucket在华北2（北京），应填写oss-cn-beijing.aliyuncs.com。详情请参见 [配置文件示例](overview-36.md) 。 |
| RequestTimeTooSkewed | Unable to execute HTTP request: The Difference between … is too large | 该报错可能是以下情况导致： 本地机器时间不对，与OSS服务器时间相差15分钟以上，该情况居多。 可能是并发太高，尤其是CPU占用率很高，导致并发上传慢。 | 该问题可以通过以下方法解决： 修改本地时间，与OSS服务器一致。 如果是并发问题，可以调整并发。您可以将 sys.properties 文件的 workerTaskThreadNum 参数值改小。 |
| 无 | The object key “/xxxxx.jpg” is invalid | 该报错可能是以下情况导致： srcPrefix 作为目录但没有以正斜线（/）结尾。 destPrefix 以正斜线（/）或者反斜线（\）开头。 | 该问题可以通过以下方法解决： 检查 srcPrefix 是否是作为目录但没有以正斜线（/）结尾。如果是目录，请以正斜线（/）结尾。 检查 destPrefix 是否以正斜线（/）或者反斜线（\）开头。如果是，请删除正斜线（/）或反斜线（\）， destPrefix 不能以正斜线（/）或反斜线（\）开头。 |
| 无 | No route to host | 这种情况一般是本地防火墙或者iptables等原因导致网络不通。 | 通过ping命令测试迁移服务器到源端和目的端网络是否正常。 若网络正常，可检查电脑防火墙和本地的防火墙设备是否有限制，可尝试关闭防火墙测试。 若网络异常，排查原因并处理后重试。 |
| 无 | Unknown http list file format | 使用HTTP模式迁移时，该问题是因为指定的HTTP列表文件格式不对或内容不符合规范。 | 该问题可以通过以下方法解决： 如果是从其它操作系统上拷过来的文件，Linux系统可以用mac2unix、dos2unix等相关命令转换文件格式；Windows系统可以使用转换工具转换格式。 如果是列表文件内容的格式不正确，请修改为正确的格式。列表文件内容的格式请参见 [列表文件](overview-36.md) 。 |
## 更多信息
部分文件迁移失败后反复重试都无法成功迁移的解决方案：
- 查看迁移失败文件列表master/jobs/[$JobName]/failed_tasks/[$TaskName]/error.list，获取失败文件的相对路径。
- 确认是否有这部分文件的权限访问、文件是否被删除、是否是软链接文件、文件名是否存在乱码等。
- 解决以上问题后，使用retry命令进行重试。
## 适用于
- 对象存储OSS
- ossimport
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
