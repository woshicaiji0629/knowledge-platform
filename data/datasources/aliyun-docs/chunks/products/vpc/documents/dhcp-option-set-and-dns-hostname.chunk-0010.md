### 控制台
启用 DNS 主机名
前往[专有网络控制台](https://vpc.console.aliyun.com/vpc/cn-hangzhou/vpcs)，在目标 VPC基本信息页面，单击启用DNS 主机名。
前往[ECS](https://ecs.console.aliyun.com/server/region/cn-hangzhou)[实例管理控制台](https://ecs.console.aliyun.com/server/region/cn-hangzhou)，为 ECS 配置私网域名解析，对应 ECS 可通过主机名被同一 VPC 内的 ECS 访问。
创建实例时，展开高级选项配置私网域名解析，选择IP 格式主机名到实例主私网 IPv4 的 DNS 解析或实例 ID 格式主机名到实例主私网 IPv4的 DNS 解析。
实例 ID 无法修改；实例 IP 变化后，域名解析记录将自动更新为新 IP 格式的主机名到新 IP 的映射。实例分配 IPv6 地址后，可选择实例 ID 格式主机名到实例主私网 IPv6的 DNS 解析。
针对已创建的 ECS，在其操作列选择>实例属性>编辑实例属性，选择对应的私网域名和IP地址的映射关系。
禁用 DNS 主机名
在目标 VPC基本信息页面，单击禁用DNS 主机名，阿里云统一分配的域名将失效，无法将 ECS 私网域名解析为对应的 IP。
系统会自动解除与默认 DHCP 选项集的关联，但不会删除 DHCP 选项集。如需删除，确保已解除与所有 VPC 的关联。
