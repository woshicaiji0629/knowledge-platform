### 调整公网入方向路由
您可以通过调整网关路由表的系统路由条目，调整公网入方向路由。
IPv4/IPv6路由的下一跳支持修改为ECS实例、弹性网卡、网关型负载均衡终端节点和路由目标组。
网关路由表仅允许修改系统路由，不支持创建自定义路由条目。
网关路由表编辑系统路由信息并成功保存后，将会转化为自定义路由条目；删除后可转化为系统路由条目。
编辑网关路由表的系统路由条目时，下一跳类型的说明与建议如下：
ECS实例/弹性网卡：交换机内部指定实例或网卡可被访问。常用于公网流量安全引流到特定ECS实例或弹性网卡。如果需要更换ECS实例或弹性网卡，需要先删除路由条目再重新编辑系统路由信息，无法直接替换。
[网关型负载均衡终端节点](../../slb/documents/gateway-based-load-balancing-gwlb/getting-started/gwlb-quickly-implements-load-balancing-for-ipv4-services.md)：交换机内部指定终端节点可被访问。用于网关型负载均衡GWLB场景的第三方安全设备公网流量引流。
支持修改下一跳为网关型负载均衡终端节点的地域，请参见[网关型负载均衡](../../slb/documents/gateway-based-load-balancing-gwlb/product-overview/regions-and-zones-supported-by-gwlb.md)[GWLB](../../slb/documents/gateway-based-load-balancing-gwlb/product-overview/regions-and-zones-supported-by-gwlb.md)[支持的地域](../../slb/documents/gateway-based-load-balancing-gwlb/product-overview/regions-and-zones-supported-by-gwlb.md)。
[路由目标组](route-target-group.md)：支持通过主备模式配置两个下一跳实例，系统将自动检测实例的健康状态，当实例异常时，自动实现可用区级别的容灾切换，缩短故障恢复时间（RTO）。
