## 创建/删除 DHCP 选项集
为降低对固定 IP 的依赖、使用主机名/完整域名互访，您可以使用 DHCP 选项集为关联 VPC 内的 ECS 统一配置 DNS 服务器 IP 和搜索域。ECS 执行ping <hostname>时，系统将补全搜索域（例如hostname.example.com），向指定的 DNS 服务器查询域名与 IP 的映射关系。
一个DHCP选项集可以关联多个同地域VPC，但一个VPC只能关联一个同地域DHCP选项集。
