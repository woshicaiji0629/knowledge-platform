## 启用 DNS 主机名
为实现同一VPC内通过私网域名进行通信，您可以为 VPC 启用 DNS 主机名，并在 ECS 中配置私网域名解析，由阿里云的内网 DNS 解析自动维护域名解析记录，降低域名解析记录的维护时间与成本。VPC 会关联默认 DHCP 选项集，为 ECS 指定统一的[ECS 云产品内置权威域名 [regionID].ecs.internal](../../ecs/documents/user-guide/ecs-private-domain-resolution.md)。
1、每个地域首次启用 DNS 主机名时，自动创建默认 DHCP 选项集并关联至 VPC。该地域其他 VPC 启用 DNS 主机名时，系统自动将该默认 DHCP 选项集与对应 VPC 关联。2、如果 VPC 已关联其他 DHCP 选项集，VPC 启用 DNS 主机名后，将不会关联默认 DHCP 选项集，您需要自行修改关联关系。3、暂不支持跨 VPC、混合云场景下，使用私网域名通信。
