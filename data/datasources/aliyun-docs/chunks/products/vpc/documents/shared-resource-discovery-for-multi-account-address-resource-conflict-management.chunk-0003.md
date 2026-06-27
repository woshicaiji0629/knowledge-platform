### API
结合 IPAM 创建 VPC
分配IPv4网段：调用[CreateVpc](developer-reference/api-vpc-2016-04-28-createvpc.md)时传入Ipv4IpamPoolId来指定IPAM地址池，同时传入Ipv4CidrMask来指定掩码从IPAM地址池中分配地址作为新建VPC的IPv4网段。也可以传入CidrBlock来指定VPC使用的网段，而不是通过指定掩码自动分配网段。
分配IPv6网段：在分配IPv4网段的同时，传入Ipv6IpamPoolId和Ipv6CidrMask，将从指定的IPv6地址池中为VPC分配IPv6网段。
为已有 VPC 添加附加网段
添加IPv4网段：调用[AssociateVpcCidrBlock](developer-reference/api-vpc-2016-04-28-associatevpccidrblock.md)，传入IpamPoolId指定IPAM地址池，同时传入SecondaryCidrMask或SecondaryCidrBlock。
添加IPv6网段：调用[AssociateVpcCidrBlock](developer-reference/api-vpc-2016-04-28-associatevpccidrblock.md)，传入IpamPoolId指定IPAM地址池，同时传入Ipv6CidrMask或IPv6CidrBlock。
创建自定义分配
调用[CreateIpamPoolAllocation](developer-reference/api-vpcipam-2023-02-28-createipampoolallocation.md)从IPAM地址池创建自定义分配，预留指定地址段。
释放分配
调用[DeleteIpamPoolAllocation](developer-reference/api-vpcipam-2023-02-28-deleteipampoolallocation.md)释放IPAM地址池的地址分配。
