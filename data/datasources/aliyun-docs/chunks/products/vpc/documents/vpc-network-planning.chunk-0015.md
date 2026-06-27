## 跨VPC互联
您可以选择以下产品服务实现不同VPC之间的网络连通：
当您规划的VPC数量较少时（一般不超过5个），您可以在两个VPC之间建立[VPC](vpc-peer-to-peer-connection.md)[对等连接](vpc-peer-to-peer-connection.md)实现跨VPC互联。
如果您的业务规模较大且网络架构复杂，根据业务需求规划了较多VPC时，您可以使用[云企业网](../../cen/documents/product-overview/what-is-cen.md)集中且高效地管理分散的网络资源，降低运维难度，并确保数据的安全传输。
通过公网访问阿里云服务（例如对象存储OSS）可能导致敏感信息泄露，威胁数据安全，您可以使用[私网连接](https://help.aliyun.com/zh/privatelink/what-is-a-private-network-connection)将终端节点所在VPC（服务使用方）与终端节点服务所在VPC（服务提供方）通过终端节点建立连接，避免通过公网访问服务带来的潜在安全风险。
[VPN](https://help.aliyun.com/zh/vpn/product-overview/what-is-vpn-gateway)[网关](https://help.aliyun.com/zh/vpn/product-overview/what-is-vpn-gateway)通过建立加密隧道的方式在两个VPC之间建立安全连接，但网络延迟高。
