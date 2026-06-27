# 如何对每个分组进行告警管理和事务管理-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/use-the-group-evaluation-feature

# 设置分组评估
分组评估是告警监控规则中的一个参数。当告警监控系统对查询和分析结果进行计算时，可基于特定字段进行分组，每个分组单独评估触发条件并触发告警。即您可以使用一条告警监控规则同时监控多个目标，并对每个分组进行独立的告警管理和事务管理。
重要
设置分组评估后，单次评估产生的告警分组最多为100个分组。超过100个分组时，会随机取其中100个发送到告警策略。
选择分组评估字段时，请选择具备标识监控实体特征的字段，字段的值可枚举。请勿选择不具备区分监控实体特征的字段。使用这些字段会产生很多分组，每个分组对应一个告警，造成告警风暴，导致错过重要的告警信息。
例如：选择Nginx日志中的host、method等字段，OSS访问日志中的bucket字段。请勿选择Nginx日志中的request_time、body_size等字段，错误日志中的err_cnt字段。
## 示例一：分组监控时序数据
例如您将多个服务器的指标数据存储在一个时序库中，但希望每个服务器的CPU使用率（cpu_util）超过95%时，日志服务可以分开发送每个服务器的告警信息。针对此需求，您可以在创建告警监控规则时设置分组评估。
具体配置如下：
查询统计：* | select promql_query_range('cpu_util') from metrics limit 1000
该查询和分析语句用于统计CPU的使用率。
分组评估：标签自动
时序数据的查询和分析结果支持自动分组。
触发条件：有数据匹配，value > 95，严重度：高
当查询和分析结果中存在value的值大于95时，触发高级别的告警。
添加标注：配置告警的标题和描述等标注信息，您可以在标注信息中引用字段变量（例如${host}）。更多信息，请参见[添加标签和标注](labels-and-annotations.md)。
其中，title填写为${host}主机的CPU使用率飙升，desc填写为${host}主机的CPU使用率达到${value}。
## 示例二：分组监控日志
例如您在监控OSS访问日志时，希望每分钟发生500错误超过1000次的Bucket可以分开告警。针对此需求，您可以在创建告警监控规则时设置分组评估。
具体配置如下：
查询统计：http_status=500 | select bucket,count(1) as pv group by bucket having pv >1000 order by pv desc
该查询和分析语句用于统计发生500错误超过1000次的Bucket。
分组评估：标签自定义，bucket
查询和分析结果将根据bucket进行分组。
触发条件：
条件1：有数据匹配，pv > 3000，严重度：高
当查询和分析结果中存在pv的值大于3000时，触发高级别的告警。
条件2：有数据，严重度：中
当查询和分析结果中存在数据时触发中级别的告警。
添加标注：配置告警的标题和描述等标注信息，您可以在标注信息中引用字段变量（例如${pv}）。更多信息，请参见[添加标签和标注](labels-and-annotations.md)。
其中，title设置为${bucket} Bucket发生500错误，desc设置为错误次数为${pv}。
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
