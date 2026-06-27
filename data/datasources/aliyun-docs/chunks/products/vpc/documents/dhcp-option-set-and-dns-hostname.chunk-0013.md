### 使用内网 DNS 解析
为统一添加 ECS 的域名解析记录，您可以使用[内网 DNS 解析](https://help.aliyun.com/zh/dns/form-filling-mode)。该服务将结合添加的域名数量、解析请求量[收取费用](https://help.aliyun.com/zh/dns/product-billing)。
控制台
前往[内网 DNS 解析控制台](https://dnsnext.console.aliyun.com/privateDNS/zones)，单击添加域名 (Zone)，配置自定义的内网权威域名 (Zone)，并设置域名生效范围为目标 VPC。
单击目标域名 ID，您可以在ECS主机名页签，单击添加ECS主机名，系统将自动添加所选地域中 ECS 主机名与 IP 的域名解析记录，但主机名修改后，无法同步更新。您可以开启自动同步配置，系统将自动添加所选地域内的域名解析记录，且1分钟同步1次。如需使用自定义域名前缀，您可以选择解析记录页签，添加自定义主机记录。
前往[专有网络控制台 - DHCP 选项集](https://vpc.console.aliyun.com/dhcp/cn-hangzhou/dhcps)，创建DHCP选项集，配置域名为对应的内置权威域名。
在目标 DHCP 选项集的操作列选择关联专有网络，已配置域名解析记录的 ECS 可通过主机名/主机记录被关联 VPC 内的 ECS 访问。
API
依次调用如下 API，使用阿里云的内网 DNS 解析服务：
[AddZone - 添加内置权威域名](https://help.aliyun.com/zh/dns/api-pvtz-2018-01-01-addzone)
[添加解析记录](https://help.aliyun.com/zh/dns/api-pvtz-2018-01-01-addzonerecord)或[UpdateSyncEcsHostTask - 主机名同步](https://help.aliyun.com/zh/dns/api-pvtz-2018-01-01-updatesyncecshosttask)
[CreateDhcpOptionsSet - 创建 DHCP 选项集](developer-reference/api-vpc-2016-04-28-createdhcpoptionsset.md)
[AttachDhcpOptionsSetToVpc - 将 DHCP 选项集关联到 VPC](developer-reference/api-vpc-2016-04-28-attachdhcpoptionssettovpc.md)
Terraform当前不支持自动添加 ECS 主机名解析记录，您需要逐条添加自定义域名解析记录。Reso
