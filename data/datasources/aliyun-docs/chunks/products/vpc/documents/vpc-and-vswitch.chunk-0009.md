## 修改网段
创建专有网络时，为其指定的IPv4网段是专有网络的主网段。控制台不支持修改专有网络的主网段，但可以调整[ModifyVpcAttribute](developer-reference/api-vpc-2016-04-28-modifyvpcattribute.md)接口的CidrBlock参数，在主网段内放大或缩小网段。需确保缩小后的网段包含已经使用的IP地址。
专有网络的IPv6网段、交换机的IPv4/IPv6网段，均不支持修改。
