### API
每个地域首次为 VPC 启用 DNS 主机名时，自动创建默认 DHCP 选项集并关联至 VPC。修改 DHCP 选项集配置或变更关联关系后，新建 ECS 会自动使用最新配置，存量 ECS 需重启实例、重启实例中 DHCP 进程或重启网络服务，才能使用最新配置。
调用[CreateDhcpOptionsSet](developer-reference/api-vpc-2016-04-28-createdhcpoptionsset.md)创建 DHCP 选项集。
调用[AttachDhcpOptionsSetToVpc](developer-reference/api-vpc-2016-04-28-attachdhcpoptionssettovpc.md)将 DHCP 选项集关联到目标 VPC。
调用[DetachDhcpOptionsSetFromVpc](developer-reference/api-vpc-2016-04-28-detachdhcpoptionssetfromvpc.md)取消 DHCP 选项集与目标 VPC 的关联。
调用[ReplaceVpcDhcpOptionsSet](developer-reference/api-vpc-2016-04-28-replacevpcdhcpoptionsset.md)更改 DHCP 选项集关联的 VPC。
调用[UpdateDhcpOptionsSetAttribute](developer-reference/api-vpc-2016-04-28-updatedhcpoptionssetattribute.md)修改 DHCP 选项集配置信息。
调用[DeleteDhcpOptionsSet](developer-reference/api-vpc-2016-04-28-deletedhcpoptionsset.md)删除 DHCP 选项集。
