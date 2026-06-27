# 创建Tair及Redis开源版实例-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/getting-started/step-1-create-an-apsaradb-for-redis-instance

# 步骤1：创建实例
本文指导您如何快速创建云数据库 Tair（兼容 Redis）实例。
如需创建用于生产环境的实例，您可以在[选型必读文档](../product-overview/select-an-apsaradb-for-redis-instance.md)中选择、评估满足业务需求的实例规格。本示例旨在帮助您快速入门，仅需设置关键参数即可完成创建。
## 前提条件
已注册阿里云账号，更多信息，请参见[注册阿里云账号](https://help.aliyun.com/zh/account/ali-cloud-account-registration-process)。
## 快速创建
单击下表的创建链接，您仅需配置地域、网络等选项即可创建出对应规格实例。
| 关注项 | 推荐规格 | 推荐原因 |
| --- | --- | --- |
| 性能优先 | [Tair（企业版）内存型（兼容](https://common-buy.aliyun.com/?commodityCode=kvstore&request=%7B%22ord_time%22:%221:Month%22,%22order_num%22:1,%22enginetype%22:%22Tair%22,%22paymode%22:%22Prepaid%22,%22cloudarchitecture%22:%22CloudNative%22,%22kvstore_series_type%22:%22tair_rdb%22,%22region%22:%22cn-hangzhou%22,%22kvstore_zonetype%22:%22singlezone%22,%22kvstore_iz%22:%22cn-hangzhou-g%22,%22kvstore_web_type%22:%221%22,%22instance_type%22:%22standard_type%22,%22kvstore_engineversion_type%22:%22rdb6.0%22,%22kvstore_architecture_type%22:%22cluster%22,%22connection_mode%22:%22proxy_on%22,%22shard_type%22:%22share%22,%22shard_class%22:%22tair.rdb.with.proxy.2g%22,%22shard_quantity%22:4,%22rwsplit_switch%22:%22false%22,%22replica_quantity%22:%222%22,%22ro_quantity%22:%220%22,%22kvstore_password%22:%22later%22%7D&regionId=cn-hangzhou) [Redis 6.0）、高可用、启用集群](https://common-buy.aliyun.com/?commodityCode=kvstore&request=%7B%22ord_time%22:%221:Month%22,%22order_num%22:1,%22enginetype%22:%22Tair%22,%22paymode%22:%22Prepaid%22,%22cloudarchitecture%22:%22CloudNative%22,%22kvstore_series_type%22:%22tair_rdb%22,%22region%22:%22cn-hangzhou%22,%22kvstore_zonetype%22:%22singlezone%22,%22kvstore_iz%22:%22cn-hangzhou-g%22,%22kvstore_web_type%22:%221%22,%22instance_type%22:%22standard_type%22,%22kvstore_engineversion_type%22:%22rdb6.0%22,%22kvstore_architecture_type%22:%22cluster%22,%22connection_mode%22:%22proxy_on%22,%22shard_type%22:%22share%22,%22shard_class%22:%22tair.rdb.with.proxy.2g%22,%22shard_quantity%22:4,%22rwsplit_switch%22:%22false%22,%22replica_quantity%22:%222%22,%22ro_quantity%22:%220%22,%22kvstore_password%22:%22later%22%7D&regionId=cn-hangzhou) | 在 Redis 开源版 能力的基础上提供： 更强的性能 ，采用多线程模型在流量突增场景中能够更好的保证响应时延与性能稳定性。 更高的数据可靠性 ，支持 [半同步](../user-guide/modify-the-synchronization-mode-of-a-persistent-memory-optimized-instance.md) 、 [按时间点恢复数据](../user-guide/use-data-flashback-to-restore-data-by-point-in-time.md) 。 更丰富的数据结构 ， [Tair](../developer-reference/extended-data-structures-of-apsaradb-for-redis-enhanced-edition.md) [扩展数据结构](../developer-reference/extended-data-structures-of-apsaradb-for-redis-enhanced-edition.md) 可简化业务代码逻辑。 |
| 性能和成本均衡 | [Redis](https://common-buy.aliyun.com/?&commodityCode=kvstore_prepaid_public_cn&request={%22instance_scene%22:%22professional%22,%22region%22:%22cn-beijing%22,%22kvstore_iz%22:%22cn-beijing-l%22,%22kvstore_engineversion_type%22:%226.0%22,%22kvstore_architecture_type%22:%22cluster%22,%22shard_class%22:%22redis.shard.mid.ce%22,%22shard_quantity%22:%224%22,%22shard_class%22:%22redis.shard.with.proxy.mid.ce%22}) [开源版](https://common-buy.aliyun.com/?&commodityCode=kvstore_prepaid_public_cn&request={%22instance_scene%22:%22professional%22,%22region%22:%22cn-beijing%22,%22kvstore_iz%22:%22cn-beijing-l%22,%22kvstore_engineversion_type%22:%226.0%22,%22kvstore_architecture_type%22:%22cluster%22,%22shard_class%22:%22redis.shard.mid.ce%22,%22shard_quantity%22:%224%22,%22shard_class%22:%22redis.shard.with.proxy.mid.ce%22}) [6.0、高可用、启用集群](https://common-buy.aliyun.com/?&commodityCode=kvstore_prepaid_public_cn&request={%22instance_scene%22:%22professional%22,%22region%22:%22cn-beijing%22,%22kvstore_iz%22:%22cn-beijing-l%22,%22kvstore_engineversion_type%22:%226.0%22,%22kvstore_architecture_type%22:%22cluster%22,%22shard_class%22:%22redis.shard.mid.ce%22,%22shard_quantity%22:%224%22,%22shard_class%22:%22redis.shard.with.proxy.mid.ce%22}) | 高可用性 ：通过主备复制和故障自动转移机制，确保数据的高可用性。 高扩展性 ：可通过增加分片数或增加分片中节点数提升容量和性能。 |
| 成本优先 | [Redis](https://common-buy.aliyun.com/?&commodityCode=kvstore_prepaid_public_cn&request={%22instance_scene%22:%22professional%22,%22region%22:%22cn-beijing%22,%22kvstore_iz%22:%22cn-beijing-l%22,%22kvstore_engineversion_type%22:%226.0%22,%22shard_class%22:%22redis.shard.large.ce%22}) [开源版](https://common-buy.aliyun.com/?&commodityCode=kvstore_prepaid_public_cn&request={%22instance_scene%22:%22professional%22,%22region%22:%22cn-beijing%22,%22kvstore_iz%22:%22cn-beijing-l%22,%22kvstore_engineversion_type%22:%226.0%22,%22shard_class%22:%22redis.shard.large.ce%22}) [6.0、高可用、不启用集群](https://common-buy.aliyun.com/?&commodityCode=kvstore_prepaid_public_cn&request={%22instance_scene%22:%22professional%22,%22region%22:%22cn-beijing%22,%22kvstore_iz%22:%22cn-beijing-l%22,%22kvstore_engineversion_type%22:%226.0%22,%22shard_class%22:%22redis.shard.large.ce%22}) | 高可用性 ：通过主备复制和故障自动转移机制，确保数据的高可用性。 低成本 ：支持最小容量 256 MB，适合用于业务起步阶段。 |
## 操作步骤
## Tair（企业版）
本示例将创建Tair内存型（兼容Redis 6.0）1 GB实例规格、不启用集群的标准架构（1主节点、1备节点）实例。
说明
本示例仅介绍重点参数，其余参数可保持默认。
访问[Tair](https://common-buy.aliyun.com/?commodityCode=kvstore_pretair_public_cn&regionId=cn-hangzhou)[售卖页](https://common-buy.aliyun.com/?commodityCode=kvstore_pretair_public_cn&regionId=cn-hangzhou)，选择产品为Tair（企业版）。
选择付费方式。
包年包月：在新建实例时支付费用。适合长期使用，价格比按量付费更实惠，且购买时长越长，折扣越多。
按量付费：先使用后付费，按小时扣费。适合短期使用，用完可立即释放实例，节省费用。
您可以在页面右下角查看价格。在配置完成后，才能最终确定价格。
选择存储介质为内存。
选择地域与可用区。
若您已创建[云服务器](../../../ecs/documents/user-guide/what-is-ecs.md)[ECS](../../../ecs/documents/user-guide/what-is-ecs.md)，推荐选择ECS所在地域与可用区。
若您需要通过本地设备连接实例，请选择就近地域。
说明
建议您选择标有“荐”字的可用区，该区域为当前地域的主售区，意味着在未来较长时间内，该可用区的资源将保持充足供应。
当选择双可用区、且备可用区为自动选择时，系统将自动分配至资源充足的可用区。
选择专有网络（VPC）与虚拟交换机。
若需使用ECS连接，请选择与ECS相同的VPC，否则无法通过内网互通。但VPC相同，交换机不同，仍然可以实现内网互通。
选择版本兼容性为Redis 6.0。
选择密码设置为立即设置，并输入密码。
（可选）若您选择包年包月方式，您还需配置实例的购买时长。
选择购买数量，默认1个。
单击立即购买。
在确认订单页面阅读服务协议，根据提示完成支付流程。
支付成功后，请等待1~5分钟。您可以在[控制台](https://kvstore.console.aliyun.com/)中，选择实例所属的地域，即可看到新购买的实例。
## Redis开源版
本示例将创建Redis开源版6.0版本1 GB实例规格、不启用集群的标准架构（1主节点、1备节点）实例。
说明
本示例仅介绍重点参数，其余参数可保持默认。
访问[Redis](https://common-buy.aliyun.com/?enginetype=Redis&commodityCode=kvstore_prepaid_public_cn)[售卖页](https://common-buy.aliyun.com/?enginetype=Redis&commodityCode=kvstore_prepaid_public_cn)，选择产品为Redis开源版。
选择付费方式。
包年包月：在新建实例时支付费用。适合长期使用，价格比按量付费更实惠，且购买时长越长，折扣越多。
按量付费：先使用后付费，按小时扣费。适合短期使用，用完可立即释放实例，节省费用。
您可以在页面右下角查看价格。在配置完成后，才能最终确定价格。
选择地域与可用区。
若您已创建[云服务器](../../../ecs/documents/user-guide/what-is-ecs.md)[ECS](../../../ecs/documents/user-guide/what-is-ecs.md)，推荐选择ECS所在地域与可用区。
若您需要通过本地设备连接实例，请选择就近地域。
说明
当选择双可用区、且备可用区为自动选择时，系统将自动分配至资源充足的可用区。
选择专有网络（VPC）与虚拟交换机。
若需使用ECS连接，请选择与ECS相同的VPC，否则无法通过内网互通。但VPC相同，交换机不同，仍然可以实现内网互通。
选择大版本为Redis 6.0。
选择密码设置为立即设置，并输入密码。
后续，您可以在控制台中重置或修改密码。
（可选）若您选择包年包月方式，您还需配置实例的购买时长。
选择购买数量，默认1个。
单击立即购买。
在确认订单页面阅读服务协议，根据提示完成支付流程。
支付成功后，请等待1~5分钟。您可以在[管理控制台](https://kvstore.console.aliyun.com/)中，选择实例所属的地域，即可看到新购买的实例。
下一步，请设置实例的IP白名单，更多信息请参见[步骤](step-2-configure-whitelists.md)[2：设置白名单](step-2-configure-whitelists.md)。
## 相关文档
若您希望创建其他架构、规格实例，您可根据控制台界面提示进行配置，更多参数介绍请参见[基本概念](../product-overview/terms.md)。
## 常见问题
创建前
Q：Tair实例创建后可以更改规格（扩容/缩容）吗？
A：可以，Tair实例支持升级、降级配置，同时也支持变更实例架构，例如从标准架构变更为集群架构。更多信息请参见[变更实例配置](../user-guide/change-the-configurations-of-an-instance.md)。
Q：创建实例需要多长时间？
A：创建实例消耗的时间与实例的分片数成正相关。实例的分片数越多，需要调配的资源越多，创建需要的时间则越长。例如，创建一个标准架构（主备节点）实例需要2~3分钟，创建一个128分片的集群架构（高可用）实例需要10~15分钟，创建一个256分片的集群架构（高可用）实例需要20~40分钟。
创建后
Q：找不到创建的实例？
A：可能原因及解决方法见下表。
| 可能原因 | 解决方法 |
| --- | --- |
| 选择了错误的地域 | 登录 [管理控制台](https://kvstore.console.aliyun.com/) ，重新选择实例所属的地域。 |
| 未刷新或过早刷新控制台 | 您可以等待一段时间（通常为几分钟）后刷新控制台，再查看实例列表中是否会出现实例。 |
Q：为什么购买实例后会自动退款，无法正常创建实例？
A：新创建的实例可能会因为资源不足而退款，您可以在[订单管理](https://usercenter2.aliyun.com/order/list)中查看到退款。在您确认退款后，您可以更换可用区再次尝试购买。
Q：如何查看实例的创建时间？
A：在[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)页，单击图标，在弹出的自定义列表中，勾选创建时间并单击确认。您可以在实例列表中查看对应实例的创建时间。
## 相关API
| API | 说明 |
| --- | --- |
| [CreateInstance](../developer-reference/api-r-kvstore-2015-01-01-createinstance-redis.md) | 创建一个 Redis 开源版 或 Tair 内存型经典版实例。 |
| [CreateTairInstance](../developer-reference/api-r-kvstore-2015-01-01-createtairinstance-redis.md) | 创建 Tair 云原生 版实例。 |
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
