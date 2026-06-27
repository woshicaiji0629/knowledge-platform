h/ipv6-gateway/getting-started/allow-an-ecs-instance-in-a-vpc-to-communicate-with-external-ipv6-clients-over-the-internet#section-hh0-5ut-dru)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/getting-started/allow-an-ecs-instance-in-a-vpc-to-communicate-with-external-ipv6-clients-over-the-internet#section-hh0-5ut-dru)[互联网互通](https://help.aliyun.com/zh/ipv6-gateway/getting-started/allow-an-ecs-instance-in-a-vpc-to-communicate-with-external-ipv6-clients-over-the-internet#section-hh0-5ut-dru)。
创建网关路由表并与IPv6网关绑定。
登录[路由表控制台](https://vpc.console.aliyun.com/vpc/cn-hangzhou/route-tables)，顶部菜单栏选择IPv6网关所在地域。
单击创建路由表，选择对应的VPC，绑定对象类型选择边界网关，配置路由表名称并单击确定。
在网关路由表详情页，单击已绑定的边界网关>绑定边界网关，选择IPv6网关并绑定。
配置网关路由表，路由入方向流量。
进入路由条目列表>系统路由条目页签，可以查看到系统路由条目。系统默认添加以交换机网段为目标网段的系统路由。
编辑目标网段指向交换机2的IPv6路由条目，将下一跳设置为ECS-A（安全设备）。
