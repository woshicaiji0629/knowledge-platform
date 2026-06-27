### CROSSSLOT Keys in request don't hash to the same slot
可能原因：Tair集群架构直连模式不支持跨Slot执行涉及多Key的命令，例如DEL、MSET、MGET等。
解决方法：
在执行操作命令前增加确认Key Slot的逻辑（例如通过CLUSTER KEYSLOT命令），确保单个命令执行的所有Key在一个Slot中。
通过改造Key名称，增加Hash tags使其保证在同一个Slot，该方案在使用过程中需避免数据倾斜。
改造实例为集群架构代理（Proxy）模式，Proxy模式支持跨Slot执行DEL、MGET、MSET等涉及多Key的命令，更多信息请参见[Tair Proxy](../product-overview/features-of-proxy-nodes.md)[特性说明](../product-overview/features-of-proxy-nodes.md)。
