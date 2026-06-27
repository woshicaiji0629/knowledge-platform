# 高可用虚拟IP（HaVip）-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/highly-available-virtual-ip-address-havip

# 高可用虚拟IP（HaVip）
使用高可用虚拟IP（High-Availability Virtual IP Address，HaVip）功能，在云上可以实现同可用区服务器主备切换过程中服务IP不变。
Keepalived本身就可以支持实现虚拟IP高可用，为什么要配合HaVip来实现？
在传统数据中心中，Keepalived 软件在进行主备切换时，基于 VRRP 协议确定新的主服务器。新的主服务器可以直接将虚拟IP绑定到自身网卡，并主动发送Gratuitous ARP广播，宣告自己接管了虚拟IP。局域网中的各设备收到该 ARP 广播后，会更新本地 ARP 缓存，将虚拟IP指向新的主服务器的MAC地址。
然而，大部分云厂商采用SDN架构和虚拟化技术构建网络环境，虚拟服务器IP地址由云平台底层的虚拟化平台分配和管理。应用无法像传统方式一样修改主机IP地址。且整个虚拟网络是基于三层的隧道技术，ARP在发送端被终结，主机无法声明IP地址。为此，阿里云推出HaVip功能，解决此问题。
HaVip 是一种可以独立创建和释放的私网 IP 资源。在 Keepalived 的配置文件中将虚拟 IP 设置为 HaVip 地址，并将 HaVip 与多个服务器绑定。当 Keepalived 选举出新的主服务器后，系统会更新 HaVip 与主服务器的映射关系，实现类似 Gratuitous ARP 的效果，从而确保主备切换过程中服务 IP 不变。
## 工作原理
通过1个HaVip和2个ECS实例实现高可用主备集群的架构如下图所示。工作原理如下：
Keepalived配置：HaVip 绑定 ECS1 和 ECS2，二者均安装 Keepalived软件。在 Keepalived 的配置文件中，virtual_ipaddress（虚拟 IP）均设置为 HaVip 地址。同时，需要在配置文件中设置优先级priority，值越大，该服务器作为主服务器的优先级越高。
主服务器选举：Keepalived 软件基于 VRRP 协议，通过比较 ECS1 和 ECS2 的priority值大小，自动选举优先级更高的 ECS1 为主服务器，系统会自动更新 HaVip 与主服务器的映射关系，所有访问 HaVip 的流量将被转发至 ECS1。
主备切换：主服务器 ECS1 会周期性发送心跳消息到备服务器 ECS2（心跳间隔由配置文件中的advert_int决定）。如果 ECS2 在指定时间内未收到心跳消息，Keepalived 软件会自动将主服务器切换为 ECS2。系统检测到主服务器变更后，会自动更新 HaVip 与新主服务器的映射关系，所有访问 HaVip 的流量将被转发至 ECS2，从而实现主备切换过程中服务IP不变。
如果需要公网访问，可为HaVip绑定EIP，绑定后该HaVip可以通过EIP面向公网提供高可用服务。
## 使用 HaVip 实现主备切换
HaVip 支持绑定同一交换机内的ECS实例或弹性网卡，结合Keepalived等软件实现主备切换时的服务 IP 不变。
配额：使用前，需登录[配额中心控制台](https://quotas.console.aliyun.com/products/vpc/quotas?spm=a2c4g.11186623.0.0.610ecda16wO953&query=vpc_privilege_allow_buy_havip_instance&keyword=buy_havip_instance)申请创建 HaVip 的权限。配额为1，代表可创建 HaVip，而单账号支持创建 HaVip 的数量为 50 个。
IP 版本：HaVip 仅支持 IPv4。
绑定资源：
HaVip 只能同时绑定同一类型资源。如需绑定其他类型资源，需先解绑已经绑定的资源。
HaVip 绑定弹性网卡时，需确保弹性网卡绑定在ECS实例上。
如果已绑定的 ECS 实例或弹性网卡被删除，系统会自动解除 HaVip 和对应 ECS 实例或弹性网卡的绑定关系。
如果从 ECS 实例上解绑已绑定 HaVip 的辅助弹性网卡，不会影响 HaVip 和该辅助弹性网卡的绑定关系。
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
! Configuration File for keepalived vrrp_instance VI_1 { state MASTER # 设置为主实例 interface eth0 # 绑定VIP的网卡，本示例配置为eth0 virtual_router_id 51 # 主备集群的virtual_router_id；同一VPC下的不同主备集群需要配置不同的virtual_router_id nopreempt # 设置非抢占模式 priority 100 # 设置优先级，数字越大，优先级越高；本示例配置优先级为100，将本实例设置为主实例 advert_int 1 # 心跳报文发送间隔，单位为秒。设置过小，易受网络抖动影响，可能发生频繁倒换和暂时双主（即脑裂）。设置过大，可能导致主实例故障后，主备切换时间长。 authentication { auth_type PASS auth_pass 1111 } unicast_src_ip 192.168.0.25 # 本实例的私网IP地址，本示例配置为192.168.0.25 unicast_peer { 192.168.0.26 # 对端实例的私网IP地址，本示例配置为192.168.0.26；如有多台备用ECS实例，需声明所有对端实例的IP，每个地址单独占一行，无需逗号或其他分隔符。 } virtual_ipaddress { 192.168.0.24 # 虚拟IP地址，配置为HaVip的IP地址，本示例为192.168.0.24 } garp_master_delay 1 # 当切为主实例后多久更新ARP缓存，单位为秒 garp_master_refresh 5 # 发送ARP报文的时间间隔，单位为秒 track_interface { eth0 # 绑定VIP的网卡，本示例配置为eth0 } }
执行systemctl start keepalived启动 Keepalived。
备服务器配置
登录备 ECS 实例。
执行yum install keepalived安装Keepalived。
执行vim /etc/keepalived/keepalived.conf编辑keepalived.conf文件。
本示例仅展示需修改部分，请结合具体实例修改keepalived.conf文件配置。请勿直接复制本示例覆盖已有keepalived.conf文件。
! Configuration File for keepalived vrrp_instance VI_1 { state BACKUP # 设置为备实例 interface eth0 # 绑定VIP的网卡，本示例配置为eth0 virtual_router_id 51 # 主备集群的virtual_router_id；同一VPC下的不同主备集群需要配置不同的virtual_router_id nopreempt # 设置非抢占模式 priority 10 # 设置优先级，数字越大，优先级越高；本示例配置优先级为10，将本实例设置为备实例 advert_int 1 # 心跳报文发送间隔，单位为秒。设置过小，易受网络抖动影响，可能发生频繁倒换和暂时双主（即脑裂）。设置过大，可能导致主实例故障后，主备切换时间长。 authentication { auth_type PASS auth_pass 1111 } unicast_src_ip 192.168.0.26 # 本实例的私网IP地址，本示例配置为192.168.0.26 unicast_peer { 192.168.0.25 # 对端实例的私网IP地址，本示例配置为192.168.0.25。需声明所有对端实例的IP，每个地址单独占一行，无需逗号或其他分隔符。 } virtual_ipaddress { 192.168.0.24 # 虚拟IP地址，配置为HaVip的IP地址，本示例为192.168.0.24 } garp_master_delay 1 # 当切为主实例后多久更新ARP缓存，单位为秒 garp_master_refresh 5 # 发送ARP报文的时间间隔，单位为秒 track_interface { eth0 # 绑定VIP的网卡，本示例配置为eth0 } }
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
### API
调用[CreateHaVip](developer-reference/api-vpc-2016-04-28-createhavip.md)创建 HaVip。
调用[AssociateHaVip](developer-reference/api-vpc-2016-04-28-associatehavip.md)绑定 HaVip 和 ECS 实例或弹性网卡。
调用[UnassociateHaVip](developer-reference/api-vpc-2016-04-28-unassociatehavip.md)解绑 HaVip 和 ECS 实例或弹性网卡。
调用[DeleteHaVip](developer-reference/api-vpc-2016-04-28-deletehavip.md)删除 HaVip。
### Terraform
Resource：[alicloud_havip](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/havip)、[alicloud_havip_attachment](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/havip_attachment)、[alicloud_instance](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/instance)、[alicloud_security_group](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/security_group)、[alicloud_security_group_rule](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/security_group_rule)# 指定创建HaVip的地域 provider "alicloud" { region = "cn-hangzhou" } # 指定VPC的ID variable "vpc_id" { default = "vpc-bp1k******" # 修改为VPC的实际ID } # 指定交换机ID variable "vswitch_id" { default = "vsw-bp1y******" # 修改为交换机的实际ID } # 指定实例规格 variable "instance_type" { default = "ecs.e-c1m1.large" } # 指定镜像ID variable "image_id" { default = "aliyun_3_x64_20G_alibase_20221102.vhd" } # 创建HaVip resource "alicloud_havip" "test_havip" { ha_vip_name = "test_havip_name" vswitch_id = var.vswitch_id ip_address = "192.168.0.24" # 从交换机网段内，指定HaVip的IP地址；若不指定，将由系统分配 } # 创建安全组 resource "alicloud_security_group" "test_security_group" { security_group_name = "test_security_group_name" vpc_id = var.vpc_id } # 创建安全组规则，需根据实际流量调整协议、访问来源与端口。 resource "alicloud_security_group_rule" "allow_vpc_tcp" { type = "ingress" ip_protocol = "tcp" nic_type = "intranet" policy = "accept" port_range = "8000/8000" priority = 1 security_group_id = alicloud_security_group.test_security_group.id cidr_ip = "192.168.0.0/24" } # 创建主服务器 resource "alicloud_instance" "test_master_instance" { instance_name = "test_master_instance_name" vswitch_id = var.vswitch_id instance_type = var.instance_type image_id = var.image_id system_disk_category = "cloud_essd" security_groups = [alicloud_security_group.test_security_group.id] user_data = base64encode(<<-EOT #!/bin/sh yum install keepalived -y printf '! Configuration File for keepalived vrrp_instance VI_1 { state MASTER # 设置为主实例 interface eth0 # 绑定VIP的网卡，本示例配置为eth0 virtual_router_id 51 # 主备集群的virtual_router_id；同一VPC下的不同主备集群需要配置不同的virtual_router_id nopreempt # 设置非抢占模式 priority 100 # 设置优先级，数字越大，优先级越高；本示例配置优先级为100，将本实例设置为主实例 advert_int 1 # 心跳报文发送间隔，单位为秒。设置过小，易受网络抖动影响，可能发生频繁倒换和暂时双主（即脑裂）。设置过大，可能导致主实例故障后，主备切换时间长。 authentication { auth_type PASS auth_pass 1111 } unicast_src_ip 192.168.0.25 # 本实例的私网IP地址，本示例配置为192.168.0.25 unicast_peer { 192.168.0.26 # 对端实例的私网IP地址，本示例配置为192.168.0.26；如有多台备用ECS实例，需声明所有对端实例的IP。每个地址单独占一行，无需逗号或其他分隔符。 } virtual_ipaddress { 192.168.0.24 # 虚拟IP地址，配置为HaVip的IP地址，本示例为192.168.0.24 } garp_master_delay 1 # 当切为主实例后多久更新ARP缓存，单位为秒 garp_master_refresh 5 # 发送ARP报文的时间间隔，单位为秒 track_interface { eth0 # 绑定VIP的网卡，本示例配置为eth0 } }' > /etc/keepalived/keepalived.conf systemctl start keepalived EOT ) # 指定主服务器的初始化脚本，为主服务器安装keepalived private_ip = "192.168.0.25" # 指定主服务器的私网IP instance_charge_type = "PostPaid" # 指定付费类型为按量付费 spot_strategy = "SpotWithPriceLimit" # 设置上限价格的抢占式实例 } # 创建备服务器 resource "alicloud_instance" "test_backup_instance" { instance_name = "test_backup_instance_name" vswitch_id = var.vswitch_id instance_type = var.instance_type image_id = var.image_id system_disk_category = "cloud_essd" security_groups = [alicloud_security_group.test_security_group.id] user_data = base64encode(<<-EOT #!/bin/sh yum install keepalived -y printf '! Configuration File for keepalived vrrp_instance VI_1 { state BACKUP # 设置为备实例 interface eth0 # 绑定VIP的网卡，本示例配置为eth0 virtual_router_id 51 # 主备集群的virtual_router_id；同一VPC下的不同主备集群需要配置不同的virtual_router_id nopreempt # 设置非抢占模式 priority 10 # 设置优先级，数字越大，优先级越高；本示例配置优先级为10，将本实例设置为备实例 advert_int 1 # 心跳报文发送间隔，单位为秒。设置过小，易受网络抖动影响，可能发生频繁倒换和暂时双主（即脑裂）。设置过大，可能导致主实例故障后，主备切换时间长 authentication { auth_type PASS auth_pass 1111 } unicast_src_ip 192.168.0.26 # 本实例的私网IP地址，本示例配置为192.168.0.26 unicast_peer { 192.168.0.25 # 对端实例的私网IP地址，本示例配置为192.168.0.25。需声明所有对端实例的IP。每个地址单独占一行，无需逗号或其他分隔符。 } virtual_ipaddress { 192.168.0.24 # 虚拟IP地址，配置为HaVip的IP地址，本示例为192.168.0.24 } garp_master_delay 1 # 当切为主实例后多久更新ARP缓存，单位为秒 garp_master_refresh 5 # 发送ARP报文的时间间隔，单位为秒 track_interface { eth0 # 绑定VIP的网卡，本示例配置为eth0 } }' > /etc/keepalived/keepalived.conf systemctl start keepalived EOT ) # 指定备服务器的初始化脚本，为备服务器安装keepalived private_ip = "192.168.0.26" # 指定备服务器的私网IP instance_charge_type = "PostPaid" # 指定付费类型为按量付费 spot_strategy = "SpotWithPriceLimit" # 设置上限价格的抢占式实例 } # 绑定主服务器 resource "alicloud_havip_attachment" "test_havip_attachment" { ha_vip_id = alicloud_havip.test_havip.id instance_id = alicloud_instance.test_master_instance.id # 指定HaVip关联的实例ID } # 绑定备服务器 resource "alicloud_havip_attachment" "test_havip_attachment_new" { ha_vip_id = alicloud_havip.test_havip.id instance_id = alicloud_instance.test_backup_instance.id # 指定HaVip关联的实例ID }
## 绑定 EIP 实现公网访问
HaVip 是交换机内的私网 IP 资源，如需公网访问，可以将 HaVip 与弹性公网IP（EIP）绑定。EIP 的使用会[产生费用](../../eip/documents/billing-overview.md)。
1、绑定的 EIP 地域需和 HaVip 的地域相同，且处于可用状态。2、ECS 实例借助 HaVip 绑定的 EIP 访问公网时，数据包的源 IP 为 HaVip 的私网IP，而非 ECS 实例的私网 IP。
### 控制台
绑定/解绑 EIP绑定 EIP 前，确保已创建 EIP。可通过[EIP 控制台](https://vpc.console.aliyun.com/eip/cn-hangzhou/eips)创建 EIP，也可在绑定页面，单击创建弹性公网IP。
在目标 HaVip 的操作列，单击绑定EIP或解绑EIP，完成相应操作。
### API
绑定 EIP 前，确保已调用[AllocateEipAddress](../../eip/documents/developer-reference/api-vpc-2016-04-28-allocateeipaddress-eips.md)创建 EIP。
调用[AssociateEipAddress](../../eip/documents/developer-reference/api-vpc-2016-04-28-associateeipaddress-eips.md)绑定 HaVip 和 EIP。
调用[UnassociateEipAddress](../../eip/documents/developer-reference/api-vpc-2016-04-28-unassociateeipaddress-eips.md)解绑 HaVip 和 EIP。
### Terraform
Resource：[alicloud_eip_address](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/eip_address)、[alicloud_eip_association](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/eip_association)# 指定HaVip所在地域 provider "alicloud" { region = "cn-hangzhou" } # 指定HaVip的ID variable "havip_id" { default = "havip-8vb0******" # 修改为HaVip的实际ID } # 创建EIP resource "alicloud_eip_address" "test_eip" { address_name = "test_eip_name" isp = "BGP" netmode = "public" bandwidth = "1" payment_type = "PayAsYouGo" } # 绑定EIP resource "alicloud_eip_association" "test_eip_havip_association" { allocation_id = alicloud_eip_address.test_eip.id instance_type = "HAVIP" instance_id = var.havip_id # 指定HaVip的ID }
## 更多信息
### 计费说明
HaVip 功能正在公测，可免费使用，但不承诺任何服务等级协议（SLA）相关的保障条款。
HaVip 绑定的云资源，如[ECS 实例](../../ecs/documents/billing-overview.md)、[EIP](../../eip/documents/billing-overview.md)，将按其各自的计费规则独立计费。
### 支持的地域
公有云支持的地域
| 区域 | 支持高可用虚拟 IP 的地域 |
| --- | --- |
| 亚太-中国 | 华东 1（杭州） 、 华东 2（上海） 、 华东 5 （南京-本地地域-关停中） 、 华北 1（青岛） 、 华北 2（北京） 、 华北 3（张家口） 、 华北 5（呼和浩特） 、 华北 6（乌兰察布） 、 华南 1（深圳） 、 华南 2（河源） 、 华南 3（广州） 、 西南 1（成都） 、 西北 2（中卫） 、 中国香港 、 华中 1（武汉-本地地域） 、 华东 6（福州-本地地域-关停中） |
| 亚太-其他 | 日本（东京） 、 韩国（首尔） 、 新加坡 、 马来西亚（吉隆坡） 、 印度尼西亚（雅加达） 、 菲律宾（马尼拉） 、 泰国（曼谷） 、 马来西亚（柔佛州） |
| 欧洲与美洲 | 德国（法兰克福） 、 英国（伦敦） 、 法国（巴黎） 、 美国（硅谷） 、 美国（弗吉尼亚） 、 墨西哥 |
| 中东 | 阿联酋（迪拜） 、 沙特（利雅得）- 合作伙伴运营 |
金融云支持的地域
| 区域 | 支持高可用虚拟 IP 的地域 |
| --- | --- |
| 亚太 | 华南 1 金融云 、 华东 2 金融云 、 华北 2 金融云（邀测） |
政务云支持的地域
| 区域 | 支持高可用虚拟 IP 的地域 |
| --- | --- |
| 亚太 | 华北 2 阿里政务云 1 |
### 配额
HaVip 功能正在公测，需登录阿里云[配额中心控制台](https://quotas.console.aliyun.com/products/vpc/quotas?spm=a2c4g.11186623.0.0.610ecda16wO953&query=vpc_privilege_allow_buy_havip_instance&keyword=havip)进行自助申请。
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| 无 | 支持创建高可用虚拟 IP（HaVip）的网络类型 | VPC 类型 | 无法提升 |
| 单个 ECS 实例支持同时绑定的 HaVip 数量 | 5 个 |  |  |
| 单个 HaVip 支持同时绑定的 EIP 数量 | 1 个 |  |  |
| 单个 HaVip 支持同时绑定的 ECS 实例或弹性网卡的数量 | 10 个 1、1 个 HaVip 支持同时绑定 10 个 ECS 实例或同时绑定 10 个弹性网卡，但 1 个 HaVip 不能同时绑定 ECS 实例和弹性网卡。 2、HaVip 具有子网属性，仅支持绑定到同一交换机下的 ECS 实例或弹性网卡上。 |  |  |
| HaVip 是否支持广播和组播通信 | 不支持 HaVip 只支持单播，如果您使用 Keepalived 等第三方软件实现高可用，需要修改配置文件中的通信方式为单播通信。 |  |  |
| 单个账号支持创建的 HaVip 的数量 | 50 个 |  |  |
| 单个 VPC 支持创建的 HaVip 的数量 | 50 个 |  |  |
| vpc_quota_havip_custom_route_entry | 单个路由表内，目的地址指向 HaVip 的路由条目的数量 | 5 条 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
