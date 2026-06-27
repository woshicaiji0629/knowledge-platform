### 限制从IPAM地址池为VPC分配网段
多账号企业中，各业务账号独立创建 VPC 时若随意分配私网网段，VPC互连时易因网段冲突无法连通。使用管理账号创建[管控策略](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/control-policy-overview#DAS)，与资源夹或成员绑定，限制业务账号只能从[共享的](address-planning.md)[IPAM](address-planning.md)[地址池](address-planning.md)中为 VPC 分配网段。IPAM 确保分配的网段不重叠，避免VPC互连时出现地址冲突。
管控策略对所有资源目录成员中的RAM用户和RAM角色生效，但对成员的根用户不生效。同时，资源目录的管理账号位于资源目录外部，不归属于资源目录，所以管控策略对管理账号内的所有身份也不生效。
管控策略一：限定用户从地址池创建VPC和为VPC添加附加网段
{ "Statement": [ { "Action": [ "vpc:CreateVpc", "vpc:AssociateVpcCidrBlock" ], "Resource": "*", "Effect": "Deny", "Condition": { "Null": { "vpc:Ipv4IpamPoolId": "true" } } } ], "Version": "1" }
管控策略二：限定用户从特定地址池创建VPC
用户需要选择与"vpc:Ipv4IpamPoolId"的设定值一致的IPAM地址池，才能够成功创建VPC。
{ "Statement": [ { "Action": [ "vpc:CreateVpc" ], "Resource": "*", "Effect": "Deny", "Condition": { "StringNotEquals": { "vpc:Ipv4IpamPoolId": "ipam-pool-0123456789abcdefg" } } }, { "Action": [ "vpc:CreateVpc" ], "Resource": "*", "Effect": "Deny", "Condition": { "Null": { "vpc:Ipv4IpamPoolId": "true" } } } ], "Version": "1" }
管控策略三：限定用户使用特定地址池创建VPC和为VPC添加附加网段
创建VPC时，选择与"vpc:Ipv4IpamPoolId"的设定值一致的IPAM地址池；
添加附加网段时，选择IPAM 分配的 IPv4 地址段，并使用与"vpc:Ipv4IpamPoolId"的设定值一致的IPA
