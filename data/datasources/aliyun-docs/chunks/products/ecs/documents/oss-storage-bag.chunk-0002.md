## 购买资源包
说明
以下操作以在ECS控制台入口购买OSS资源包为例，关于在OSS控制台购买资源包的具体操作请参见[资源包购买指南](../../oss/documents/purchase-resource-plans.md)。
购买OSS资源包前，建议您先评估以下内容以便购买合适的资源包。
确认您快照所在的地域，快照和OSS资源包必须位于同一地域才能抵扣。
预估您的快照容量，确定购买的OSS资源包规格。
如何根据快照容量评估购买的OSS资源包规格？
示例1：假设您在华北2（北京）地域已经有100 GB的标准快照，则购买多大容量的OSS资源包合适？
您可以在华北2（北京）地域购买100 GB的OSS资源包，购买后每小时开始抵扣100 GB快照的存储费用。
示例2：假设您在华北2（北京）地域计划为容量为100 GB的云盘周期性创建云盘快照备份数据，则购买多大容量的OSS资源包合适？
建议您根据云盘后续的备份情况（多久备份一次、快照保留多长时间等因素）来预估可能产生的快照容量，然后再评估需要购买多大容量的OSS资源包，避免产生资源浪费。例如您计划每天凌晨对云盘创建一份快照（容量为0.5 GB），快照保留时间6个月，则6个月内产生的快照容量为90 GB。因此，您可以在创建快照前购买容量为100 GB、时长为6个月的OSS资源包，这样可以完全抵扣快照的存储费用。
进入[ECS](https://ecs.console.aliyun.com/snapshot/region/cn-hangzhou)[控制台](https://ecs.console.aliyun.com/snapshot/region/cn-hangzhou)[OSS](https://ecs.console.aliyun.com/snapshot/region/cn-hangzhou)[资源包购买入口](https://ecs.console.aliyun.com/snapshot/region/cn-hangzhou)，单击立即购买。
跳转至OSS控制台资源包购买页，选择购买参数，并按照页面指引完成购买。
商品类型选择OSS资源包。
资源包类型选择标准 - 本地冗余存储。
选择OSS资源包的地域。
说明
指定地域的资源包只能抵扣指定地域的费用，中国内地通用的资源包可以跨地域抵扣中国内地各地域的存储费用，请您根据业务需求合理选择。关于中国内地通用资源包支持抵扣的中国内地地域，请参见[资源包](../../oss/documents/resource-plan.md)。
选择OSS资源包的规格和购买时长。
OSS资源包根据规格和购买时长进行计费。您可以访问[资源包定价详情](https://www.aliyun.com/price/product?spm=5176.8064714.694085.p
