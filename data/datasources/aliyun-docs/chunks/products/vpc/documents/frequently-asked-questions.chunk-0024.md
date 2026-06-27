PAM地址池[预置](create-and-manage-address-pools.md)[CIDR](create-and-manage-address-pools.md)时，需要包括这些已经使用的网段。
通过在IPAM地址池[创建自定义分配](create-and-manage-address-pools.md)，保留这些地址段。
后续所有新建VPC的网段都通过IPAM来分配。由于IPAM已经记录了所有已用网段，它分配出的新网段自然就不会与已有网段冲突。
HaVip是否支持IPv6？
不支持。当前仅支持IPv4。
