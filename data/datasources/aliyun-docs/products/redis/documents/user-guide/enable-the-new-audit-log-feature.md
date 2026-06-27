# 开通审计日志-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/user-guide/enable-the-new-audit-log-feature

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/redis/documents/product-overview.md)

- [快速入门](products/redis/documents/getting-started.md)

- [Tair AI能力](products/redis/documents/tair-ai-ability.md)

- [操作指南](products/redis/documents/user-guide.md)

- [实践教程](products/redis/documents/use-cases.md)

- [安全合规](products/redis/documents/security-compliance.md)

- [开发参考](products/redis/documents/developer-reference.md)

- [服务支持](products/redis/documents/support.md)

- [视频专区](products/redis/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# 审计日志

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

审计日志功能基于阿里云日志服务SLS（Log Service），支持记录云数据库 Tair（兼容 Redis）实例的所有写操作。为您提供审计日志的查询、在线分析、导出等功能，既可以帮助安全审计人员及时发现数据异常操作的行为，快速定位修改数据的用户身份与时间点，又可以助力业务系统满足安全性与合规性的要求，还能帮助开发运维人员定位性能问题。

## 功能概述

开通审计日志后，系统将记录写操作的审计信息，不会记录读操作的审计信息。

重要

在写入负载高的场景（如频繁使用INCR计数）下，该功能可能会带来5%～15%的性能损失及一定延时抖动。建议在故障排查或安全审计时开通该功能。

当命令参数过多、过长或总长度超限时，审计日志中的命令将截断显示，格式类似于SLOWLOG命令。

典型场景

云数据库 Tair（兼容 Redis）将[阿里云日志服务](products/sls/documents/what-is-log-service.md)的部分功能融合到审计日志中，为您带来更加稳定、易用、灵活且高效的审计日志服务，典型使用场景如下：

| 典型场景 | 说明 |
| --- | --- |
| 操作审查 | 帮助安全审计人员定位数据修改的操作者身份或时间点等信息，帮助识别是否存在滥用权限、执行非合规命令等内部风险。 |
| 安全合规 | 助力业务系统通过安全规范中关于审计部分的要求。 |


费用说明

根据审计日志的存储空间和保存时长按量收取费用，不同地域的收费标准有所区别，更多信息请参见[计费项](products/redis/documents/product-overview/billable-items.md)。

说明

关闭审计日志功能后，审计日志仍会按之前的日志保留时长存储日志，直到所有的日志过期，因此在关闭后仍会产生审计日志费用。

## RAM用户权限限制

如使用阿里云账号（主账号），则可以忽略此说明。若RAM用户开通审计日志，需要具备日志服务的管理权限。

- 

您可以为RAM用户授予系统权限策略AliyunLogFullAccess。授权后，RAM用户可以管理所有日志库（Logstore）。具体操作，请参见[授予权限](products/ram/documents/grant-permissions-to-a-ram-user.md)。

- 

您也可以自定义权限策略，限定RAM用户只能管理云数据库 Tair（兼容 Redis）实例的审计日志。

自定义权限策略示例

{ "Version": "1", "Statement": [ { "Action": "log:*", "Resource": "acs:log:*:*:project/nosql-*", "Effect": "Allow" } ] }

## 操作步骤

- 

访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。

- 

在左侧导航栏，选择日志管理>审计日志。

- 

设置审计日志的保留时长。

说明

该设置会应用至当前地域下所有已开通审计日志的实例，审计日志按照存储容量及保留时长收费，日志保留时长支持的范围为1~365天。

- 

单击费用估算并开通。

- 

在弹出的对话框中进行费用估算并阅读相关提示，确认后单击开通。

说明

如果未开通阿里云日志服务，您需要根据弹出的对话框提示开通日志服务。

## 常见问题

- 

Q：如何关闭某个实例的审计功能？

A：您可以在审计日志页面，单击右上角的服务设置，关闭所有节点的审计开关。

- 

Q：如何下载完整的审计日志？

A：具体操作，请参见[下载日志](products/sls/documents/download-logs.md)。在操作时，您需要注意以下内容：

- 

在执行下载日志的操作时，选择的目标Project的命名格式为nosql-{用户UID}-{Region}，例如nosql-176498472******-cn-hangzhou；然后选择目标Logstore为redis_audit_log_standard。

- 

下载方式选择为通过Cloud Shell下载或通过命令行工具下载即可下载全部日志，如果选择为直接下载，仅会下载本页面展示的日志。

- 

Q：为什么仅支持写操作的审计功能，不开放读操作的审计功能？

A：绝大多数场景下读操作占比较高，读操作的审计将带来较多的性能损失，且由于要存储的数据过大，如果保持稳定的策略有可能会丢失部分审计日志，所以未开放读操作的审计功能。

- 

Q：正式版的审计日志保存时长是当前地域生效，如果第一个实例设置为7天，第二个实例设置为14天，最终以哪个为准？

A：以最近一次设置的为准。

- 

Q：为什么某些审计日志对应的客户端IP不是业务所属的客户端？

A：因为审计日志包含了管控类的写操作日志，您可以过滤相关信息。

- 

Q：为什么实例版本为兼容Redis 4.0及以上仍无法开通审计日志？

A：部分实例由于小版本过旧无法开通审计日志，请[升级小版本与代理版本](products/redis/documents/user-guide/update-the-minor-version.md)后重试。

- 

Q：为什么有一些审计日志的写入IP是127.0.0.1？

A：IP为127.0.0.1的日志来源有以下两种情况：

- 

大版本7.0且小版本低于7.0.1.17的实例使用LUA脚本，[升级至最新小版本](products/redis/documents/user-guide/update-the-minor-version.md)后记录为客户端IP。

- 

实例的内部管理操作。常见的内部操作日志如下表所示：

| 日志类型 | 说明 |
| --- | --- |
| 主节点驱逐 | 节点发生数据逐出。 |
| 主节点审计日志丢弃事件 | 审计日志丢弃事件（drop start）。 |
| 主节点审计日志丢弃事件 | 审计日志丢弃事件（drop end）。 |
| 主节点热点 Key 日志 | 节点内部当前正在访问的热 Key（按 QPS 或流量统计）信息。 |
| 主节点大 Key 日志 | 节点内部当前存储的大 Key（子元素数目）信息。 |


## 相关API

| API | 说明 |
| --- | --- |
| [修改审计日志设置](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-modifyauditlogconfig-redis.md) | 设置实例的审计日志开关与保留时长。 |
| [查询审计日志配置](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-describeauditlogconfig-redis.md) | 查询实例审计日志是否已开通、日志保存时间等配置信息。 |
| [查询实例的审计日志](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-describeauditrecords-redis.md) | 查询实例的审计日志。 |


## 相关文档

- 

[查询审计日志](products/redis/documents/user-guide/view-audit-logs.md)

- 

[下载审计日志](products/redis/documents/user-guide/download-audit-logs.md)

- 

[订阅审计日志报表](products/redis/documents/user-guide/subscribe-to-audit-log-reports.md)

- 

[通过日志服务实现日志的实时消费](products/sls/documents/overview-of-real-time-consumption.md)

[上一篇：实时追踪日志](products/redis/documents/user-guide/real-time-tracking-log.md)[下一篇：查询审计日志](products/redis/documents/user-guide/view-audit-logs.md)

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
