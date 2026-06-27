## 注意事项
在Alibaba Cloud Linux 3中，iptables和nftables不兼容。使用iptables的组件，网络能力可能会受到影响。
Alibaba Cloud Linux 3可能会将部分Hostname作为DNS搜索域，可能导致DNS解析的次数增加。
使用Alibaba Cloud Linux 3时，请确保已安装组件及集群满足以下最低版本要求。

| 组件或集群 | 最低版本 |
| --- | --- |
| 集群 | 1.20.4 |
| ACK NodeLocal DNSCache | 1.5.0 |
| Flannel | v0.13.0.1-466064b-aliyun |
| Terway | v1.0.10.390-g5f3c461-aliyun |
