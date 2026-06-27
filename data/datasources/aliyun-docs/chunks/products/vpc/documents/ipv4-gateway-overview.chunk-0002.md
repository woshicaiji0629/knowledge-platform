### IPv4网关与NAT网关的区别
IPv4 网关和公网 NAT 网关可结合使用。参考[公网访问](public-network-access.md)，详细了解相关网络组件之间的关系。

| 网络组件 | IPv4 网关 | 公网 NAT 网关 |
| --- | --- | --- |
| 功能定位 | VPC 边界上的公网 IPv4 流量控制组件 | VPC 内部的网络地址转换设备 |
| 使用场景 | 集中控制公网访问流量 | 统一公网流量出口 |
| 是否提供公网访问能力 | 不提供，仅控制公网流量 | 通过绑定 EIP 提供公网访问能力 （公网访问能力是由 EIP 提供的，NAT 网关本身不提供公网访问能力） |

创建 IPv4 网关后，交换机可区分为：
公有交换机：绑定的路由表中存在目标网段为0.0.0.0/0，下一跳为IPv4网关的路由，其中的资源绑定公网IP即可访问公网。
私有交换机：绑定的路由表中不存在指向IPv4网关的路由，其中的资源绑定公网IP后无法直接访问公网。
结合公网NAT网关使用时，需要将公网NAT网关部署在公有交换机，部署在私有交换机的ECS实例配置路由指向公网NAT网关，将访问公网的流量路由至公网NAT网关，再使用公网NAT网关绑定的公网IP访问公网。需注意：
确保公网NAT网关的EipBindMode为NAT模式，兼容IPv4网关。
控制台创建的公网NAT网关默认为NAT模式，调用[CreateNatGateway](../../nat-gateway/documents/developer-reference/api-vpc-2016-04-28-createnatgateway-natgws.md)创建时，EipBindMode需传入NAT。创建完成后，可以调用[ModifyNatGatewayAttribute](../../nat-gateway/documents/developer-reference/api-vpc-2016-04-28-modifynatgatewayattribute-natgws.md)调整EipBindMode。
如果已创建EipBindMode为MULTI_BINDED模式的公网NAT网关，由于不兼容IPv4网关，将无法创建IPv4网关。
如果已创建IPv4网关，调用[CreateNatGateway](../../nat-gateway/documents/developer-reference/api-vpc-2016-04-28-createnatgateway-natgws.md)创建EipBindMode为MULTI_BINDED模式的公网NAT网关，将无法绑定EIP。
为避免激活IPv4网关后私有交换机中的资源无法访问公网，确保在激活IPv4网关前完成路由配置。
