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
