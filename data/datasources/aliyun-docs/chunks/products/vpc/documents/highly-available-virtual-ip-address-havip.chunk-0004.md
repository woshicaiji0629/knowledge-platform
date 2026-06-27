ntication { auth_type PASS auth_pass 1111 } unicast_src_ip 192.168.0.25 # 本实例的私网IP地址，本示例配置为192.168.0.25 unicast_peer { 192.168.0.26 # 对端实例的私网IP地址，本示例配置为192.168.0.26；如有多台备用ECS实例，需声明所有对端实例的IP，每个地址单独占一行，无需逗号或其他分隔符。 } virtual_ipaddress { 192.168.0.24 # 虚拟IP地址，配置为HaVip的IP地址，本示例为192.168.0.24 } garp_master_delay 1 # 当切为主实例后多久更新ARP缓存，单位为秒 garp_master_refresh 5 # 发送ARP报文的时间间隔，单位为秒 track_interface { eth0 # 绑定VIP的网卡，本示例配置为eth0 } }
执行systemctl start keepalived启动 Keepalived。
备服务器配置
登录备 ECS 实例。
执行yum install keepalived安装Keepalived。
执行vim /etc/keepalived/keepalived.conf编辑keepalived.conf文件。
本示例仅展示需修改部分，请结合具体实例修改keepalived.conf文件配置。请勿直接复制本示例覆盖已有keepalived.conf文件。
! Configuration File for keepalived vrrp_instance VI_1 { state BACKUP # 设置为备实例 interface eth0 # 绑定VIP的网卡，本示例配置为eth0 virtual_router_id 51 # 主备集群的virtual_router_id；同一VPC下的不同主备集群需要配置不同的virtual_router_id nopreempt # 设置非抢占模式 priority 10 # 设置优先级，数字越大，优先级越高；本示例配置优先级为10，将本实例设置为备实例 advert_int 1 # 心跳报文发送间隔，单位为秒。设置过小，易受网络抖动影响，可能发生频繁倒换和暂时双主（即脑裂）。设置过大，可能导致主实例故障后，主备切换时间长。 authentication { auth_type PASS auth_pass 1111 } unicast_src_ip 192.168.0.26 # 本实例的私网IP地址，本示例配置为192.168.0.26 unicast_peer { 192.168.0.25 # 对端实例的私网IP地址，本示例配置为192.168.0.25。需声明所有对端实例的IP，每
