### 控制台
开启IPv6
创建专有网络和交换机时，可以选择以下方式开启IPv6：
使用系统分配的 IPv6 地址段，并下拉选择分配BGP(多线)，系统将自动创建[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)[网关](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)并分配IPv6网段。
为了统一管理地址资源，可以使用IPAM 分配的 IPv6 地址段，选择预置了IPv6 CIDR的地址池并配置地址掩码或指定CIDR，从地址池中分配IPv6网段。
针对已创建的专有网络，可以在目标专有网络的IPv6网段列单击开通IPv6：
选择系统分配的 IPv6 地址段或IPAM 分配的 IPv6 地址段。
由系统分配时，可以勾选自动开启专有网络内所有交换机IPv6功能。未勾选或由IPAM分配时，需要在目标交换机的IPv6网段列单击开通IPv6，为交换机开启IPv6。
关闭IPv6
在目标专有网络/交换机的IPv6网段列单击关闭IPv6，但关闭专有网络的IPv6，需要所有交换机关闭IPv6，并删除该专有网络下的IPv6网关。
