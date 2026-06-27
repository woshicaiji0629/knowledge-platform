## 预留网段
在交换机中预留网段，可以确保此网段不被其他资源的创建所占用。预留的网段，当前仅用于给弹性网卡的辅助私网IP分配[IP](../../ecs/documents/user-guide/ip-prefix.md)[前缀](../../ecs/documents/user-guide/ip-prefix.md)。
1、预留网段内不能包含交换机的[系统保留地址](vpc-and-vswitch.md)。2、单个 VPC 支持创建的 IPv4、IPv6最大预留网段数目均为100个。3、IPv4预留网段的掩码长度最大不超过28，IPv6网段掩码长度且最大不超过80。
