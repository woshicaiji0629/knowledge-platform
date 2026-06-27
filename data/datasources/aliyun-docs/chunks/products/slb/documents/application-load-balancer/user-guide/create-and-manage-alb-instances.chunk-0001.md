## 控制台
前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，单击创建应用型负载均衡。
在购买页完成以下配置，点击立即创建。
地域：建议选择最靠近客户端的地域以降低访问延迟。
参考[ALB](../product-overview/supported-regions-and-zones.md)[功能特性支持的地域与可用区](../product-overview/supported-regions-and-zones.md)。
实例网络类型：
私网：仅分配私网IP地址，用于阿里云内部网络访问。
公网：同时分配公网IP和私网IP，支持互联网访问和内网访问。ALB默认由弹性公网IP（EIP）提供公网能力。
选择公网将收取EIP的[配置费和流量费](../../../../eip/documents/billing-overview.md)。双栈公网实例默认使用IPv4地址提供公网服务，无IPv6公网能力。如需IPv6公网能力，请[变更](change-the-network-type-of-an-alb-instance.md)[ALB](change-the-network-type-of-an-alb-instance.md)[实例的网络类型](change-the-network-type-of-an-alb-instance.md)，这将产生[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb)[公网费用](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb)。
VPC：实例和服务器组需位于同一个VPC。ALB实例创建后，所属VPC无法修改。
可用区：
如地域支持多可用区，至少选择2个可用区及对应交换机。
（仅当实例网络类型为公网）可选择绑定已有EIP或自动分配公网IP。如选择后者，系统将创建按量付费（按使用流量计费）的EIP并绑定至ALB实例。
仅支持绑定暂未加入共享带宽的按量付费（按使用流量计费）的已购EIP；同一个ALB实例不同可用区绑定的[EIP](../support/faq-about-alb.md)[类型](../support/faq-about-alb.md)需保持一致。
协议版本：如需支持IPv6访问，选择[双栈](alb-instance-overview.md)；否则选择IPv4。
购买双栈ALB实例前，请为实例所在交换机[开启](../../
