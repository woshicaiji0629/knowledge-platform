### API
与控制台逻辑不同的是，调用API为专有网络和交换机开启IPv6后，将不会自动创建IPv6网关，需调用[CreateIpv6Gateway](https://help.aliyun.com/zh/ipv6-gateway/developer-reference/api-vpc-2016-04-28-createipv6gateway-ipv6s)自行创建。
创建专有网络和交换机时，调整[CreateVpc](developer-reference/api-vpc-2016-04-28-createvpc.md)和[CreateVSwitch](developer-reference/api-vpc-2016-04-28-createvswitch.md)的EnableIPv6参数开启/关闭IPv6。创建专有网络时，传入Ipv6IpamPoolId和Ipv6CidrMask将从指定的IPv6地址池中为VPC分配IPv6网段。
针对已创建的专有网络和交换机，调整[ModifyVpcAttribute](developer-reference/api-vpc-2016-04-28-modifyvpcattribute.md)与[ModifyVSwitchAttribute](developer-reference/api-vpc-2016-04-28-modifyvswitchattribute.md)的EnableIPv6参数开启/关闭IPv6。如需从指定IPv6地址池中为VPC分配IPv6网段，调用[AssociateVpcCidrBlock](developer-reference/api-vpc-2016-04-28-associatevpccidrblock.md)添加。
