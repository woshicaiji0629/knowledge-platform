### GWLB高可用架构
单点架构下，安全设备一旦发生故障，将会影响业务系统的可用性。[使用网关型负载均衡](../../slb/documents/gateway-based-load-balancing-gwlb/getting-started/gwlb-quickly-implements-load-balancing-for-ipv4-services.md)[GWLB](../../slb/documents/gateway-based-load-balancing-gwlb/getting-started/gwlb-quickly-implements-load-balancing-for-ipv4-services.md)，将安全设备进行高可用部署，可以消除单点故障。

| IPv4 公网流量入方向路径 | IPv4 公网流量出方向路径 |
| --- | --- |
| 1. IPv4 流量通过 IPv4 网关进入业务 VPC。 2. 根据网关路由表，将流量发送到 GWLBe。 3. GWLBe 将流量转发至 GWLB，由 GWLB 将流量转发到安全设备。 4. 安全设备完成安全检查后，将流量转回到 GWLB，通过私网连接将流量转到 GWLBe。 5. 根据 GWLBe 子网配置的路由表，将流量发送到业务服务器。 | 1. 根据业务服务器子网配置的路由表，将流量发送到 GWLBe。 2. GWLBe 将流量发往 GWLB，GWLB 将流量转发到安全设备。 3. 安全设备完成安全检查后，将流量转回到 GWLB，通过私网连接将流量转到 GWLBe。 4. 根据 GWLBe 子网配置的路由表，将流量发送到 IPv4 网关。 5. IPv4 网关将流量路由至公网。 |

配置网关路由表时，单击目标交换机网段系统路由操作列的编辑，修改下一跳为网关负载均衡终端节点，修改后，路由条目将出现在自定义路由条目页签下。
