### 控制台
请确保已[创建](address-planning.md)[IPAM](address-planning.md)[和](address-planning.md)[IPAM](address-planning.md)[地址池](address-planning.md)。
为 VPC 分配网段
结合 IPAM 创建 VPC：
前往专有网络控制台的[创建专有网络](https://vpc.console.aliyun.com/vpc/cn-hangzhou/vpcs/new)页面。
使用IPAM 分配的 IPv4 地址段，选择IPv4地址池并配置掩码，系统会默认分配指定掩码范围内第一个可用的CIDR，可以在地址池预置CIDR内调整分配的IPv4网段。
需开启IPv6时，可以使用IPAM 分配的 IPv6 地址段，选择IPv6地址池并配置地址掩码或指定CIDR。
为已有 VPC 添加附加网段：
添加IPv4网段：在目标VPC详情页的网段管理页签，单击添加附加IPv4网段，使用IPAM 分配的 IPv4 地址段，选择IPv4地址池并配置掩码。系统会默认分配指定掩码范围内第一个可用的CIDR。
添加IPv6网段：VPC未开启IPv6时，单击开通IPv6；已开启时，单击添加IPv6网段。使用IPAM 分配的 IPv6 地址段，选择IPv6地址池并配置地址掩码或指定CIDR。
创建自定义分配
创建自定义分配前，需确保目标地址池已[预置](address-planning.md)[CIDR](address-planning.md)。
前往[IPAM](https://ipam.console.aliyun.com/cn-hangzhou/pool)[控制台 - IPAM](https://ipam.console.aliyun.com/cn-hangzhou/pool)[地址池](https://ipam.console.aliyun.com/cn-hangzhou/pool)，在页面上方选择目标地址池所在的地域。
单击目标地址池实例ID或操作列的管理，在分配页签，单击创建自定义分配，预留的地址段不会分配给云上资源。
输入CIDR或单击已预置CIDR的可分配区域，支持添加多个CIDR。
释放地址分配
前往目标地址池详情页的分配页签，在目标分配的操作列单击释放。
支持释放专有网络、自定义分配类型的分配。
释放专有网络类型的分配时，仅解除VPC与地址池的分配关系，不会删除VPC。
