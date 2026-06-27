com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth#section-dvo-wjp-zcb)。详细操作可参考[开启/关闭](vpc-and-vswitch.md)[IPv6](vpc-and-vswitch.md)。
VPC是否可以只分配IPv6网段（即IPv6 only）？
不可以。VPC当前支持仅IPv4和双栈（IPv4+IPv6），不支持IPv6 only。
如何为已有ECS实例分配指定私网IP？
您可参考：[修改已有实例主网卡的主私网](../../ecs/documents/user-guide/modify-a-private-ip-address.md)[IPv4](../../ecs/documents/user-guide/modify-a-private-ip-address.md)[地址](../../ecs/documents/user-guide/modify-a-private-ip-address.md)。
为什么docker网络与VPC网段冲突时无法互通？
这是云上网络规划中一个非常典型的问题。当部署在ECS上的Docker（或K8s Pod）网络与您VPC内的其他交换机网段或对等连接对端的VPC网段发生重叠时，会导致路由冲突，无法正常通信。
原因：假设Docker默认网段为172.17.0.0/16，而VPC中有一个交换机B的网段是172.17.0.0/24。当Docker容器内的应用尝试访问交换机B中的IP时，ECS的操作系统会根据自身的路由表，将这个流量错误地路由到了本地的docker0网桥，而不是通过VPC的路由转发出去，导致通信失败。
解决方案：
修改Docker/K8s的网络配置：修改Docker守护进程的配置文件（如/etc/docker/daemon.json），为其指定一个与您整体云上网络环境（包括所有互联的VPC和线下IDC）不冲突的私网网段。这是最根本的解决方法。
规划VPC网段时避坑：在规划VPC和交换机网段时，主动避开172.17.0.0/16、10.0.0.0/8中部分被K8s常用的网段。
如何设置IPAM地址池网段，避免新建的VPC与线下IDC或其他云的已有网段冲突？
在启用IPAM前，全面梳理您所有需要互联的网络环境，包括线下数据中心、办公网络、其他云等，将所有已使用的网段记录下来。
在IPAM地址池[预置](create-and-manage-address-pools.md)[CIDR](create-and-manage-address-pools.md)时，需要包括这些已经使用的网段。
通过在IPAM地址池[创建自定义分配](create-and-manage-address-pools.md)
