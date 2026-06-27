### 控制台
创建 HaVip 并绑定主备实例
前往[专有网络控制台-HaVip](https://vpc.console.aliyun.com/vpc/cn-hangzhou/havips)，在页面上方选择 ECS 实例所在的地域后，单击创建高可用虚拟IP。
选择需绑定的 ECS 实例所属的 VPC 和交换机，可从选定的交换机网段自动分配私网 IP 地址，也可以自行指定未被分配的 IP。
在主备 ECS 实例上安装 Keepalived，并执行systemctl start keepalived启动 Keepalived。
Keepalived 安装示例
本示例以双机主备为例，介绍操作系统为CentOS的ECS实例如何安装Keepalived。推荐使用V1.2.15及以上版本的Keepalived。
如有多台备用 ECS 实例，需在各 ECS 实例的unicast_peer中声明所有对端实例的 IP。可前往[Keepalived GitHub](https://github.com/acassen/keepalived/issues)了解更多信息。
主服务器配置
登录主 ECS 实例。
执行yum install keepalived安装Keepalived。
执行vim /etc/keepalived/keepalived.conf编辑keepalived.conf文件。
本示例仅展示需修改部分，请结合具体实例修改keepalived.conf文件配置。请勿直接复制本示例覆盖已有keepalived.conf文件。
! Configuration File for keepalived vrrp_instance VI_1 { state MASTER # 设置为主实例 interface eth0 # 绑定VIP的网卡，本示例配置为eth0 virtual_router_id 51 # 主备集群的virtual_router_id；同一VPC下的不同主备集群需要配置不同的virtual_router_id nopreempt # 设置非抢占模式 priority 100 # 设置优先级，数字越大，优先级越高；本示例配置优先级为100，将本实例设置为主实例 advert_int 1 # 心跳报文发送间隔，单位为秒。设置过小，易受网络抖动影响，可能发生频繁倒换和暂时双主（即脑裂）。设置过大，可能导致主实例故障后，主备切换时间长。 authentication { auth_type PASS auth_pass 1111 } unicast_src_ip 192.168.0.25 # 本实例的私网IP地址，本示例配置为192.168.0.25 unicast_peer { 192.168.0.26 # 对端实例的私网IP地址，本示例配置为192.168.
