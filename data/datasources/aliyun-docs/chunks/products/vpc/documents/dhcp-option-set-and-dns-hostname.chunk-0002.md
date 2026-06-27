### 配置域名：使用主机名通信
完整的私网域名包括主机名（host name）和域名（domain name）两部分，例如host01.host.prvz中，主机名为host01，域名为host.prvz。
在 DNS 服务器中配置 ECS 域名解析记录后，ECS 可通过完整的私网域名被访问。如需简化为仅使用主机名通信，您可以使用vim /etc/resolv.conf修改 ECS 的 DNS 配置文件，添加search host.prvz，将host.prvz设置成 DNS 搜索域（search domain）。
但手动配置每个 ECS，可能存在配置效率低下、配置不统一等问题。在关联的 DHCP 选项集中配置域名后，VPC 内的 ECS 实例可以通过 DHCP 获取 DHCP 选项集中配置的域名，写入/etc/resolv.conf，统一设置 DNS 搜索域。使用主机名访问 ECS 时，系统将补全搜索域，向指定的 DNS 服务器查询完整域名与 IP 的映射关系。
