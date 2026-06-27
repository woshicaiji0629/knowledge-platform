# 配置processor_appender插件为字段追加含模板变量的值-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/append-data-to-a-field

# 追加字段
您可以使用processor_appender插件为指定的字段（可以为不存在的字段）追加特定的值，支持在字段值中添加模板变量。该插件通常与input_prometheus、input_system_v2等时序监控相关的插件结合使用，用于给拉取到的Prometheus数据追加特定的值。
重要
Logtail 0.16.66及以上版本支持processor_appender插件。
## 参数说明
配置type为processor_appender，detail说明如下表所示。
表 1.插件说明
| 参数 | 类型 | 是否必选 | 参数说明 |
| --- | --- | --- | --- |
| Key | string | 是 | 字段名称。 |
| Value | string | 是 | 添加的字段值。日志服务支持在该字段值中添加模板变量。更多信息，请参见 [模板变量](append-data-to-a-field.md) 。 |
| SortLabels | boolean | 否 | 如果您要添加 __labels__ 字段，即配置 Key 为 __labels__ ，则需要设置 SortLabels 为 true ，用于对 Labels 进行重新排序，避免因为 Labels 不遵循字母序而导致查询异常。该值默认为 false。 |
表 2.模板变量
| 模板变量 | 说明 | 配置示例 | 结果示例 |
| --- | --- | --- | --- |
| {{__ip__}} | 替换为 Logtail 所在服务器的 IP 地址。 | "Value": "{{__ip__}}" | "Value": "192.0.2.1" |
| {{__host__}} | 替换为 Logtail 所在服务器的主机名。 | "Value": "{{__host__}}" | "Value": "logtail-ds-xdfaf" |
| {{$xxxx}} | 通过环境变量引用，需以美元符号（$）开头。替换为环境变量的取值。 | "Value": "{{$WORKING_GROUP}}" | "Value": "prod" |
## 示例
例如Logtail所在服务器的IP地址为192.0.2.1，主机名为david，存在环境变量WORKING_GROUP的值为prod。如果您需要为__labels__字段添加以上数据，可参见如下配置：
原始数据
"__labels__":"a#$#b"
Logtail插件处理配置
{ "processors":[ { "type":"processor_appender", "detail": { "Key": "__labels__", "Value": "|host#$#{{__host__}}|ip#$#{{__ip__}}|group#$#{{$WORKING_GROUP}}", "SortLabels": true } } ] }
处理结果
"__labels__":"a#$#b|group#$#prod|host#$#david|ip#$#192.0.2.1"
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
