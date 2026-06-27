| 字段 | 说明 |
| --- | --- |
| version | 流日志版本，当前所有的日志条目版本为 1 。 |
| account-id | 阿里云账号 ID。 |
| eni-id | 弹性网卡 ID。 |
| vm-id | 弹性网卡绑定的 ECS 云服务器 ID。 |
| vswitch-id | 弹性网卡所在交换机 ID。 |
| vpc-id | 弹性网卡所在专有网络 ID。 |
| type | 流量类型，取值为 IPv4 或 IPv6。 支持采集 IPv4/IPv6 双栈 流量的地域有： 华东 1（杭州） 、 华东 2（上海） 、 华北 1（青岛） 、 华北 2（北京） 、 华北 5（呼和浩特） 、 华南 1（深圳） 、 新加坡 、 美国（硅谷） 、 美国（弗吉尼亚） 。 |
| protocol | 流量的 [IANA](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) [协议编号](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) 。 常见协议号举例：ICMP 为 1，TCP 为 6，UDP 为 17。 |
| srcaddr | 源 IP 地址。 |
| srcport | 源端口。 |
| dstaddr | 目的 IP 地址。 |
| dstport | 目的端口。 |
| direction | 流量方向： in：流入弹性网卡的流量。 out：流出弹性网卡流量。 |
| action | 安全组或网络 ACL 是否允许该访问： ACCEPT：允许。 REJECT：拒绝。 |
| packets | 数据包个数。 |
| bytes | 字节数。 |
| start | 在采集窗口内，收到第 1 个包的时间。格式为 Unix 时间戳。 |
| end | 对于长连接，是采集窗口结束的时间；对于短连接，是连接关闭的时间。格式为 Unix 时间戳。 |
| tcp-flags | TCP 标志位，以十进制表示，反映了 TCP 协议中的 SYN、ACK、FIN 等标志的组合。 采集窗口内 1 个流日志条目可能会对应多个 TCP 数据包，该值是所有相关数据包的标志位字段进行 按位或（bitwise OR） 运算后的结果。 例如，1 个 TCP 会话在某采集窗口内有两个数据包，分别带有 SYN（2）和 SYN-ACK（18）标志，则日志中记录的 TCP 标志位字段为 18（2 | 18 = 18）。 部分 TCP 标志位对应的十进制： FIN: 1 SYN: 2 RST: 4 PSH: 8 SYN-ACK: 18 URG: 32 关于 T
