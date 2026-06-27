### 使用限制
一个VPC下只支持创建一个IPv4网关，且一个IPv4网关仅能关联一个VPC。
VPC内存在[EIP](../../eip/documents/associate-an-eip-with-a-secondary-eni-1.md)[网卡可见模式](../../eip/documents/associate-an-eip-with-a-secondary-eni-1.md)的资源时，不支持创建IPv4网关。
例如，VPC中的公网NAT网关的EIP绑定模式为多 EIP 网卡可见模式时，不兼容IPv4网关。需要调用[ModifyNatGatewayAttribute](../../nat-gateway/documents/developer-reference/api-vpc-2016-04-28-modifynatgatewayattribute-natgws.md)，修改EipBindMode为NAT模式，使其兼容IPv4网关。
多账号共享VPC场景下，资源所有者可以创建IPv4网关或对已创建的IPv4网关进行修改或删除，而资源使用者对IPv4网关没有操作权限。
通过EIP或者任播弹性公网IP绑定私网传统型负载均衡CLB时：
在英国（伦敦）、日本（东京）、沙特（利雅得）- 合作伙伴运营、马来西亚（吉隆坡）、华北5（呼和浩特）、美国（弗吉尼亚），公网访问流量同样受 IPv4 网关的限制。
支持的地域持续变更中。
部署在公有交换机的私网 CLB，绑定公网 IP 即可实现公网访问。
部署在私有交换机的私网 CLB，即使绑定公网 IP 也无法实现公网访问。可配置路由指向公网 NAT 网关，将访问公网的流量路由至公网 NAT 网关，使用公网NAT网关绑定的公网 IP 实现公网访问。
其他地域，公网访问流量不受 IPv4 网关的限制。
