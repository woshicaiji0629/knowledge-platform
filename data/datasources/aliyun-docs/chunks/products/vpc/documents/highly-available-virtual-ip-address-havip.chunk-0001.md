## 工作原理
通过1个HaVip和2个ECS实例实现高可用主备集群的架构如下图所示。工作原理如下：
Keepalived配置：HaVip 绑定 ECS1 和 ECS2，二者均安装 Keepalived软件。在 Keepalived 的配置文件中，virtual_ipaddress（虚拟 IP）均设置为 HaVip 地址。同时，需要在配置文件中设置优先级priority，值越大，该服务器作为主服务器的优先级越高。
主服务器选举：Keepalived 软件基于 VRRP 协议，通过比较 ECS1 和 ECS2 的priority值大小，自动选举优先级更高的 ECS1 为主服务器，系统会自动更新 HaVip 与主服务器的映射关系，所有访问 HaVip 的流量将被转发至 ECS1。
主备切换：主服务器 ECS1 会周期性发送心跳消息到备服务器 ECS2（心跳间隔由配置文件中的advert_int决定）。如果 ECS2 在指定时间内未收到心跳消息，Keepalived 软件会自动将主服务器切换为 ECS2。系统检测到主服务器变更后，会自动更新 HaVip 与新主服务器的映射关系，所有访问 HaVip 的流量将被转发至 ECS2，从而实现主备切换过程中服务IP不变。
如果需要公网访问，可为HaVip绑定EIP，绑定后该HaVip可以通过EIP面向公网提供高可用服务。
