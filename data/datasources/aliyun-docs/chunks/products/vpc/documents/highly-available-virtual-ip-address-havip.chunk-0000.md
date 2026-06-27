# 高可用虚拟IP（HaVip）
使用高可用虚拟IP（High-Availability Virtual IP Address，HaVip）功能，在云上可以实现同可用区服务器主备切换过程中服务IP不变。
Keepalived本身就可以支持实现虚拟IP高可用，为什么要配合HaVip来实现？
在传统数据中心中，Keepalived 软件在进行主备切换时，基于 VRRP 协议确定新的主服务器。新的主服务器可以直接将虚拟IP绑定到自身网卡，并主动发送Gratuitous ARP广播，宣告自己接管了虚拟IP。局域网中的各设备收到该 ARP 广播后，会更新本地 ARP 缓存，将虚拟IP指向新的主服务器的MAC地址。
然而，大部分云厂商采用SDN架构和虚拟化技术构建网络环境，虚拟服务器IP地址由云平台底层的虚拟化平台分配和管理。应用无法像传统方式一样修改主机IP地址。且整个虚拟网络是基于三层的隧道技术，ARP在发送端被终结，主机无法声明IP地址。为此，阿里云推出HaVip功能，解决此问题。
HaVip 是一种可以独立创建和释放的私网 IP 资源。在 Keepalived 的配置文件中将虚拟 IP 设置为 HaVip 地址，并将 HaVip 与多个服务器绑定。当 Keepalived 选举出新的主服务器后，系统会更新 HaVip 与主服务器的映射关系，实现类似 Gratuitous ARP 的效果，从而确保主备切换过程中服务 IP 不变。
