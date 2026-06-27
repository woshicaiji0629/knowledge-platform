### 步骤一：创建ALB服务器组
创建IP类型的服务器组，挂载ECS01和跨地域VPC内的ECS02。
- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏，选择ALB所属的地域。本文选择西南1（成都）。
在左侧导航栏，选择应用型负载均衡ALB>服务器组。
在服务器组页面，单击创建服务器组，完成以下配置，然后单击创建。
此处仅列出和本文强相关的配置项，其余参数的配置可保持默认值。更多信息，请参见[NLB](../../network-load-balancer/user-guide/create-and-manage-a-server-group.md)[服务器组](../../network-load-balancer/user-guide/create-and-manage-a-server-group.md)。

| 配置 | 说明 |
| --- | --- |
| 服务器组类型 | 需选择 IP 类型 ，后续可通过添加 IP 地址挂载非 VPC 网段内的服务器。 |
| VPC | 选择 VPC1。 |
| 选择后端协议 | 选择 HTTP 。 说明 基础版 ALB 实例的 HTTPS 监听只能选择后端协议是 HTTP 的服务器组。 |
| 选择调度算法 | 使用默认值 加权轮询 ，更多调度算法参考 [负载均衡调度算法介绍](../../product-overview/introduction-to-load-balancing-scheduling-algorithm.md) 。 |

在服务器组创建成功对话框，单击添加后端服务器。
在添加后端服务器面板，添加ECS01的私网IP地址，单击下一步，设置添加的IP地址的端口和权重，然后单击确定。
端口设置需要与后端服务的端口保持一致。本文端口输入80，权重使用默认值。
单击添加IP，添加ECS02的私网IP地址，ECS02的IP地址不在服务器组关联的VPC网段内，需打开远端IP，然后单击下一步，设置添加的IP地址的端口和权重，然后单击确定。本文端口输入80，权重使用默认值。
未开启远端IP时，仅支持输入当前服务器组所在VPC网段内的IP地址。开启远端IP后，支持输入以下网段内的IP地址。
10.0.0.0/8
100.64.0.0/10
172.16.0.0/12
192.168.0.0/16
