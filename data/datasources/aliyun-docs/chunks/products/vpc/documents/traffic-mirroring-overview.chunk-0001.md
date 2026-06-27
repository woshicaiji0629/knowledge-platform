### 工作流程
流量镜像会话在指定的镜像源和镜像目的建立转发路径。启动镜像会话后，流量镜像将执行以下操作：
复制符合筛选条件的镜像源业务报文。
镜像源当前仅支持弹性网卡。
筛选条件中包含入方向规则和出方向规则，采用源网段、源端口、目的网段、目的端口和协议类型组成的五元组，按照优先级分别筛选弹性网卡实例接收/发出的流量。
使用[标准的](https://datatracker.ietf.org/doc/html/rfc7348)[VXLAN](https://datatracker.ietf.org/doc/html/rfc7348)[报文格式](https://datatracker.ietf.org/doc/html/rfc7348)封装后作为镜像报文。
VNI（VXLAN Network Identifier，VXLAN ID）：分配给镜像会话的虚拟网络 ID，用于区分不同会话的镜像流量。创建镜像会话时，如未指定VNI，将由系统随机分配。
源 IP：镜像源的主IP地址。
源端口：由业务报文的五元组哈希值确定。
目的IP：镜像目的的主IP地址。
目的端口：默认使用4789端口，不支持修改。
将镜像报文转发至路由可达的镜像目的。如果镜像目的和镜像源不属于同一个VPC，您需要[配置](cross-vpc-interconnection-overview.md)[VPC](cross-vpc-interconnection-overview.md)[互连](cross-vpc-interconnection-overview.md)，确保镜像源和镜像目的之间路由可达。
镜像目的当前支持弹性网卡、专有网络类型的私网CLB或网关型负载均衡终端节点GWLBe。
当前，支持将流量转发至网关型负载均衡终端节点GWLBe的地域，有华东1（杭州）、华东2（上海）、华北1（青岛）、华北2（北京）、华北5（呼和浩特）、华南1（深圳）、新加坡、美国（硅谷）、美国（弗吉尼亚）。
从镜像源复制报文时不受安全组和网络ACL策略的限制，但镜像报文转发至镜像目的时，需确保在镜像目的所在的安全组和网络ACL中配置入方向规则，允许来自镜像源的UDP协议报文访问镜像目的的4789端口。
使用专有网络类型的私网CLB作为镜像目的时，需确保在4789端口[配置](../../slb/documents/classic-load-balancer/user-guide/add-a-udp-listener.md)[UDP](../../slb/documents/classic-load-balancer/user-guide/add-a-udp-listener.md)[监听](../../slb/documents/classic-load-balancer/user-guide/add-a-ud
