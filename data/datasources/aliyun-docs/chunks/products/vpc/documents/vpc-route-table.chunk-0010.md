## 控制台
绑定路由表
前往VPC控制台[路由表](https://vpc.console.aliyun.com/vpc/cn-hangzhou/route-tables)页面，在目标路由表的绑定资源列，单击立即绑定：
路由表绑定对象类型为交换机：单击绑定交换机，在打开的对话框中选择目标交换机。
交换机绑定自定义路由表后，会自动解绑系统路由表。
路由表绑定对象类型为边界网关：单击绑定边界网关，在打开的对话框中选择目标IPv4网关或IPv6网关。
关于绑定边界网关的路由表的使用教程，请查看[使用网关路由表控制进入](use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md)[VPC](use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md)[的流量](use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md)。
解绑路由表
前往目标路由表的详情页面：
路由表绑定对象类型为交换机：在已绑定交换机页签下，勾选要解绑的交换机，然后单击解绑。解绑后交换机会绑回系统路由表。
路由表绑定对象类型为边界网关：在已绑定的边界网关页签下，在目标IPv4/IPv6网关的操作列单击解绑。
警告
解绑路由表前，请充分评估路由条目变化带来的相关业务影响，避免导致业务受损。
