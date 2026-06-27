pe PASS auth_pass 1111 } unicast_src_ip 192.168.0.26 # 本实例的私网IP地址，本示例配置为192.168.0.26 unicast_peer { 192.168.0.25 # 对端实例的私网IP地址，本示例配置为192.168.0.25。需声明所有对端实例的IP，每个地址单独占一行，无需逗号或其他分隔符。 } virtual_ipaddress { 192.168.0.24 # 虚拟IP地址，配置为HaVip的IP地址，本示例为192.168.0.24 } garp_master_delay 1 # 当切为主实例后多久更新ARP缓存，单位为秒 garp_master_refresh 5 # 发送ARP报文的时间间隔，单位为秒 track_interface { eth0 # 绑定VIP的网卡，本示例配置为eth0 } }
执行systemctl start keepalived启动 Keepalived。
单击目标 HaVip ID，在绑定资源区域，单击ECS实例右侧的立即绑定，选择要绑定的 ECS 实例或弹性网卡。
绑定完成后，可以在目标 HaVip 的绑定实例列或详情页的绑定资源区域，查看当前的主备关系。
效果验证：
在主备实例分别执行以下命令，创建Web测试服务，返回不同结果。
通过netstat -an | grep 8000查看端口占用情况，如果8000端口被占用，需要选择其他端口。
主实例：
echo "ECS 1" > index.html # 主实例返回"ECS 1" python3 -m http.server 8000
备实例：
echo "ECS 2" > index.html # 备实例返回"ECS 2" python3 -m http.server 8000
在同 VPC 内的其他 ECS 实例中，执行curl <havip_private_ip>:8000，将返回ECS 1；当主服务器停机后，将返回ECS 2。
请确保主备实例的安全组已允许同 VPC 内的 HTTP 流量访问 8000 端口。
解绑资源
单击目标 HaVip ID，在绑定资源区域已绑定资源处找到目标 ECS 实例或弹性网卡，单击解除关联。
删除 HaVip
需先确保 HaVip 未绑定 ECS实例、弹性网卡或 EIP，在目标 HaVip 的操作列或详情页单击删除。
