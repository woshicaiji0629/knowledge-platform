01.example.com. 3 PTR Web02.example.com.
执行systemctl restart named重启 BIND 服务。
如果您在使用自建 DNS 服务的同时希望使用阿里云 DNS 服务，需要为自建 DNS 服务器配置转发规则，将自定义域名以外的查询请求转发至阿里云默认DNS服务器。
为自建 DNS 服务器配置转发规则
执行vim /etc/named.conf命令，修改配置文件。
// 默认转发：其他请求转发到默认 DNS 服务器 options { forwarders { 100.100.2.136; 100.100.2.138; }; # 阿里云VPC默认DNS forward only; }; // 配置自建 DNS 权威解析，"example.com"需替换为自定义域名 zone "example.com" { type master; file "example.com.zone"; # 域名解析配置文件 };
在自定义 DHCP 选项集中指定 DNS 服务器 IP 时，需注意：1、控制台会自动填入阿里云的默认 DNS 服务器 IP（100.100.2.136 和 100.100.2.138），如果您删除该 IP，可能会导致您无法访问阿里云基础云上服务，请谨慎操作。调用 API 时，确保填入上述 IP。2、确保将自建 DNS 服务器 IP 填写在首位，否则将优先向阿里云默认 DNS 服务器发起查询请求。由于默认 DNS 服务器无法解析自定义域名，将直接返回NXDOMAIN，系统将认为无需继续查询后续服务器，从而无法将私网域名解析为 IP 。3、您需要在关联 VPC 的[安全组](../../ecs/documents/user-guide/manage-security-group-rules.md)和[网络](work-with-network-acls.md)[ACL](work-with-network-acls.md)（如有）中添加允许访问自建 DNS 服务器 IP 的规则，否则可能导致域名无法解析。4、自定义服务器 IP 不支持使用 IPv6 地址。
控制台
前往[专有网络控制台 - DHCP 选项集](https://vpc.console.aliyun.com/dhcp/cn-hangzhou/dhcps)，创建DHCP选项集，配置域名为自建 DNS 服务中使用的域名，单击自定义服务器IP，将自建 DNS 服务器 IP 填写在首位。
在目标 DHCP 选项集的操作列选择关联专有网络，已配置域名解析记录的 ECS 可通过主机名被关联 VPC 内的 ECS 访问。
API
依次调用如下 API，创建自定义 DHCP 选项集指定域名与自建 DNS 服务器 IP，与 VPC 关联。
[CreateDhcp
