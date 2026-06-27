"Version": "1" }
管控策略三：限定用户使用特定地址池创建VPC和为VPC添加附加网段
创建VPC时，选择与"vpc:Ipv4IpamPoolId"的设定值一致的IPAM地址池；
添加附加网段时，选择IPAM 分配的 IPv4 地址段，并使用与"vpc:Ipv4IpamPoolId"的设定值一致的IPAM地址池。
{ "Statement": [ { "Action": [ "vpc:CreateVpc", "vpc:AssociateVpcCidrBlock" ], "Resource": "*", "Effect": "Deny", "Condition": { "ForAllValues:StringNotLikeIfExists": { "vpc:Ipv4IpamPoolId": "ipam-pool-0123456789abcdefg" } } } ], "Version": "1" }
