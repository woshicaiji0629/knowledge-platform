# 通过查询慢日志分析性能瓶颈与慢查询-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/view-slow-logs

# 查询慢日志
若您希望分析云数据库 Tair（兼容 Redis）实例的性能，定位实例中的慢查询命令或潜在的性能瓶颈等问题，您可以通过查看慢日志对实例进行分析，找到解决性能问题、优化请求的线索。慢日志记录了执行时间超过指定阈值（slowlog-log-slower-than）的命令，默认为20毫秒，您也可以自定义该参数。
## 功能简介
实例的慢日志会记录执行时间超过指定阈值的请求，慢日志分为数据节点慢日志和代理慢日志。
说明
Redis开源版2.8版本实例不支持查询慢日志功能，您可以在CloudDBA>慢请求中查看慢日志，但Redis开源版2.8版本的慢日志不支持显示客户端地址等信息。
## 数据节点慢日志
数据节点慢日志中统计的命令执行时间仅包含命令在数据节点中的执行时间，不包含数据节点与代理或客户端的通信时间以及命令在单线程队列上的排队延迟等。
数据节点慢日志的保留时间为72小时，无数量限制。
由于实例性能出色，通常情况下，数据节点慢日志的数量较少。
相关参数
| 参数名 | 说明 |
| --- | --- |
| slowlog-log-slower-than | 设置数据节点慢日志阈值，默认为 20000 微秒（即 20 毫秒）。 说明 通常情况下您感知到的延迟实际会高于本参数设置的值，因为感知时间中包含了数据在客户端、代理、数据节点之间传输和处理所消耗的时间。 |
| slowlog-max-len | 设置最大慢日志条目数，默认为 1024。 |
参数设置方法请参见[设置实例参数](modify-the-values-of-parameters-for-an-instance.md)。
## 代理慢日志
代理慢日志中统计的命令执行时间从代理向数据节点发出请求开始，到代理从数据节点收到相应的回复为止，包含了命令在数据节点中的执行时间、数据在网络中的传输时间以及命令的排队延迟等。
代理慢日志的保留时间为72小时，无数量限制。
由于代理慢日志反映的延迟与您在应用端感受到的延迟更相近，在排查实例超时问题时，建议多关注此类日志。
说明
标准架构实例不提供代理慢日志。
相关参数
| 参数名 | 说明 |
| --- | --- |
| rt_threshold_ms | 设置代理慢日志的阈值，默认为 500 毫秒。建议将该阈值配置为与客户端超时时间近似的值，推荐为 200 毫秒到 500 毫秒。 |
参数设置方法请参见[设置实例参数](modify-the-values-of-parameters-for-an-instance.md)。
## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击日志管理>慢日志。
在慢日志页面，您可以根据查询时间或关键字来过滤慢日志，如果是集群架构或读写分离架构实例，还支持通过节点类型和节点ID来过滤慢日志。
说明
集群架构与读写分离架构实例的连接数据库的主机地址默认为Proxy IP地址，若您希望获取具体的客户端IP地址，可在参数设置中将ptod_enabled参数设置为1，具体操作请参见[设置实例参数](modify-the-values-of-parameters-for-an-instance.md)。
## 特殊慢查询语句说明
说明
此类请求为实例内核逻辑，与您的实际请求执行速率无直接关系，您可以忽略下述慢查询语句。
| 慢查询语句 | 说明 |
| --- | --- |
| latency:eventloop | 实例运行时使用事件驱动模式，一次事件循环包括命令读取、解析、执行和返回结果整个过程。 latency:eventloop 语句的执行时长表示某次事件循环的整体耗时。 |
| latency:pipeline | 实例支持客户端的 pipeline 执行模式，该模式下客户端发送一批命令，待所有命令执行完后批量返回结果。集群版的代理服务器（Proxy）默认采用 Pipeline 模式向后端数据节点发送请求。 latency:pipeline 语句的执行时长表示 pipeline 执行模式下，批量执行一个客户端所有请求的整体耗时。 |
| latency:fork | latency:fork 语句的执行时长表示执行 fork 创建子进程所消耗的时间，用户的数据量越大，fork 消耗的时间越长。 |
## 相关API
| API | 说明 |
| --- | --- |
| [DescribeSlowLogRecords - 查看慢日志明细](../developer-reference/api-r-kvstore-2015-01-01-describeslowlogrecords-redis.md) | 查询实例在指定时间内产生的慢日志。 |
## 相关文档
[使用慢日志排查超时问题](use-slow-logs-to-troubleshoot-timeout-issues.md)
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
