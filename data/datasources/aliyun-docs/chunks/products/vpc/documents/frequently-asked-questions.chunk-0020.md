(../../ecs/documents/user-guide/change-the-vpc-of-an-ecs-instance.md)[ECS](../../ecs/documents/user-guide/change-the-vpc-of-an-ecs-instance.md)[实例的](../../ecs/documents/user-guide/change-the-vpc-of-an-ecs-instance.md)[VPC](../../ecs/documents/user-guide/change-the-vpc-of-an-ecs-instance.md)。
VPC内能否自定义DNS服务器？
可以。通过DHCP选项集功能，您可以将VPC的默认DNS服务器配置，修改为您的自建在ECS上的DNS服务器、本地数据中心的DNS服务器、第三方的公共DNS服务（注意需要网络打通）。您可参考：[使用自建 DNS 服务](dhcp-option-set-and-dns-hostname.md)。
VPC对等连接能否连通中国站点和国际站点账号下的VPC？
不能。
根据跨账号合规要求，对等连接不支持中国站账号与国际站账号下VPC的私网互通。
VPC对等连接是否支持跨境私网互通？
支持。
跨境对等连接统一由[云数据传输](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt)[CDT](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt)按出向流量收取流量传输费。使用CDT跨境功能，需先完成跨境合规认证。请在[联通跨境云专线在线申请](https://ecommerce.ictsoft.cn/apply/)页面提交资料，申请联通跨境业务资质。
VPC对等连接的网络时延如何？
同地域对等连接：网络延迟较低，通常可以达到较低的毫秒级延迟。
跨地域对等连接：由于涉及不同地域之间的数据传输，网络延迟相对较高，具体延迟取决于两地之间的物理距离和网络状况。 您可以使用[云网络互访性能观测工具](https://help.aliyun.com/zh/nis/user-guide/cloud-network-mutual-access-performance-observation)，查看地域间的网络平均时延作为参考，选择更适合您业务的链路类型。
