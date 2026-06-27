## API
如已创建过IPAM地址池：
分配IPv4网段：可在调用[CreateVpc](developer-reference/api-vpc-2016-04-28-createvpc.md)时传入Ipv4IpamPoolId来指定IPAM地址池，同时传入Ipv4CidrMask来指定掩码从IPAM地址池中分配地址作为新建VPC的IPv4网段。也可以传入CidrBlock来指定VPC使用的网段，而不是通过指定掩码自动分配网段。
分配IPv6网段：同时传入Ipv6IpamPoolId和Ipv6CidrMask，将从指定的IPv6地址池中为VPC分配IPv6网段。
如未创建过IPAM地址池，可依次调用如下API来创建IPAM地址池，然后参考上述逻辑创建专有网络。
[OpenVpcIpamService-开通](developer-reference/api-vpcipam-2023-02-28-openvpcipamservice.md)[IPAM](developer-reference/api-vpcipam-2023-02-28-openvpcipamservice.md)[功能](developer-reference/api-vpcipam-2023-02-28-openvpcipamservice.md)
[CreateIpam-创建一个](developer-reference/api-vpcipam-2023-02-28-createipam.md)[IPAM](developer-reference/api-vpcipam-2023-02-28-createipam.md)[实例](developer-reference/api-vpcipam-2023-02-28-createipam.md)
[CreateIpamPool-创建](developer-reference/api-vpcipam-2023-02-28-createipampool.md)[IPAM](developer-reference/api-vpcipam-2023-02-28-createipampool.md)[地址池](developer-reference/api-vpcipam-2023-02-28-createipampool.md)
[AddIpamPoolCidr-为](developer-reference/api-vpcipam-2023-02-28-addipampoolcidr.md)[IPAM](developer-reference/api-vpcipam-2023-02-28-addipampoolcidr.md)[地址池预置](developer-reference/api-vpcipam-2023-02-28-addipampool
