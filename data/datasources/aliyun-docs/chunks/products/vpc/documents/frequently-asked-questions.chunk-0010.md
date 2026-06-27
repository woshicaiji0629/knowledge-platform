”，而不是“公网模式”。选择私网模式删除后，VPC内部所有资源将全部无法与公网互通。
如果VPC需要恢复到没有IPv4网关且可以公网访问的状态，您可以重新创建IPv4网关，然后删除IPv4网关并选择“公网模式”。详细逻辑可参考[IPv4](ipv4-gateway-overview.md)[网关](ipv4-gateway-overview.md)。
同VPC下主网段内的ECS实例与附加网段内的ECS实例是否可以互通？
主网段与附加网段的ECS实例均属于VPC内的实例。如果安全组和网络ACL规则允许通行，则可以互通。
VPC开启ClassicLink功能后，经典网络ECS实例是否可以与VPC附加网段内的云资源互通？
不支持，附加网段不兼容ClassicLink功能。
为什么绑定HaVip后VIP无法漂移？
当主节点故障后，Vip无法自动漂移到备用节点，是HaVip配置中最常见的问题。原因通常有以下几点：
Keepalived服务未启动：以CentOS 7.9为例，执行systemctl status keepalived检查服务启动情况。如果未启动，可以执行systemctl start keepalived启动Keepalived。
Keepalived配置错误：检查keepalived.conf配置文件是否配置错误，例如：
主备节点的virtual_router_id不一致。
主备节点的authentication不一致。
unicast_peer中指定的对端IP地址不正确。
virtual_ipaddress中指定的虚拟IP地址不是HaVip地址。
安全组或网络ACL拦截：检查安全组或网络ACL规则是否拦截了请求源IP的相关流量。
实例内防火墙：检查ECS实例内部的防火墙（如firewalld, iptables）是否拦截了请求源IP的相关流量。
为什么添加路由后网络还是不通？
添加了正确的路由只是网络连通的前提之一。如果不通，请按以下步骤系统排查：
路由双向检查：确保请求方向和响应方向的路由都已正确配置。例如，VPC对等连接必须在两端都配置路由。
安全组规则：检查源端和目的端ECS实例所属的安全组，是否放行了相应协议和端口的流量（例如ping需要放行ICMP协议）。
网络ACL规则：如果您配置了网络ACL，请检查其出站和入站规则是否允许相关流量通过。
ECS内部防火墙：检查ECS实例操作系统内部的防火墙（如Linux的iptables/firewalld，Windows的防火墙）是否拦截了流量。
网段冲突：检查是否存在网络地址冲突，例如ECS上的Docker网段与对端VPC网段冲突。
使用路径分析工具：在控制台使用[网络智能服务-路径分析](https://nis.console.aliyun.com/diagnosis/pathAnalysis)工
