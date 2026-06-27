### 控制台
创建专有网络前，请确保已通过[IPAM](https://ipam.console.aliyun.com/cn-hangzhou/ipam)[控制台](https://ipam.console.aliyun.com/cn-hangzhou/ipam)创建IPAM和IPAM地址池。
前往专有网络控制台的[创建专有网络](https://vpc.console.aliyun.com/vpc/cn-hangzhou/vpcs/new)页面。
分配IPv4网段：使用IPAM 分配的 IPv4 地址段，选择IPAM地址池并配置掩码，系统会默认分配指定掩码范围内第一个可用的CIDR，也可以在地址池预置CIDR内，调整IPv4网段。
需开启IPv6时：可以选择IPAM 分配的 IPv6 地址段，首先选择IPv6地址池，再配置地址掩码或指定CIDR。
