# 为ECS实例实现IPv6通信-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 为ECS实例实现IPv6通信

更新时间：

复制 MD 格式

一键部署

我的部署

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

如果您需要在VPC中进行IPv6公私网通信，您可以在开通了IPv6网段的VPC和交换机下创建带有IPv6地址的ECS实例。本文介绍ECS实例如何通过IPv6地址通信、如何为ECS实例分配IPv6地址、配置IPv6地址等。

说明

由于IPv4网络地址资源的有限性，在IPv4环境中，网络工程师经常需要花费大量时间和精力去解决地址冲突等问题。相比之下，引入IPv6网段后，不仅因其庞大的地址空间解决了网络地址资源的限制问题，还消除了众多接入设备连接互联网时所面临的障碍。

## 使用限制

IPv6网关支持的地域

说明

IPv6 网关（IPv6 Gateway）是VPC的一个IPv6流量网关。默认申请的IPv6地址只具备IPv6私网通信能力，您可以通过在IPv6网关中为IPv6地址开通IPv6公网带宽，使其具备公网通信能力。详细信息，请参见[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)[网关](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)。

| 区域 | 地域 |
| --- | --- |
| 中国 | 华北 1（青岛）、华北 2（北京）、华北 3（张家口）、华北 5（呼和浩特）、华北 6（乌兰察布）、华东 1（杭州）、华东 2（上海）、华东 6（福州-本地地域）、华南 1（深圳）、华南 2（河源）、华南 3（广州）、西南 1（成都）、中国香港 、华东 5（南京-本地地域）、华中 1（武汉-本地地域） |
| 亚太 | 菲律宾（马尼拉）、新加坡、日本（东京）、韩国（首尔）、印度尼西亚（雅加达）、马来西亚（吉隆坡）、泰国（曼谷） |
| 欧洲与美洲 | 美国（弗吉尼亚）、美国（硅谷）、德国（法兰克福）、英国（伦敦） |


不支持IPv6的ECS实例规格族

- 

密集计算型实例规格族ic5

- 

内存型实例规格族se1

- 

大数据型实例规格族d1

- 

本地SSD型实例规格族i2g，本地SSD型实例规格族i1

- 

高主频计算型实例规格族hfc5，高主频通用型实例规格族hfg5

- 

通用型弹性裸金属服务器实例规格族ebmg5，内存网络增强型弹性裸金属服务器实例规格族ebmr5s

- 

上一代共享型实例规格族xn4、n4、mn4、e4

- 

高主频型超级计算集群实例规格族scch5

- 

GPU计算型实例规格族gn5

ECS实例可分配的IPv6地址数量限制

单台ECS实例可分配的IPv6地址数量取决于实例可绑定的弹性网卡和单张网卡可分配的IPv6地址数量：

- 

单张网卡支持可分配的IPv6地址数量和实例规格有关，详见[实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)中的单网卡IPv6地址数。

- 

单个实例可以绑定的网卡数量由实例规格决定，详见[实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)中的弹性网卡。

## 配置步骤

说明

您可以通过一键部署快速完成以下操作。

### 步骤一： VPC与交换机开通IPv6

首先，您需要确保ECS实例所在的VPC与交换机开通了IPv6，具体操作步骤，请参见[为](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc)[VPC](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc)[开启](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc)与[交换机开通](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vswitch-1)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vswitch-1)。

### 步骤二：分配IPv6地址

为ECS实例分配IPv6地址，以使其能够通过IPv6协议与其他实例或外部网络进行通信。

为已有实例分配IPv6地址

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。

- 

在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

找到目标ECS实例，点击进入实例详情页。在全部操作中选择网络和安全组>管理IPv6。

- 

在管理辅助私网IP对话框中，在IPv6区域下方，单击增加。

若无指定 IPv6 地址，设置IPv6地址的输入框留空即可，系统将自动生成。

- 

单击确定。

新建实例时分配IPv6地址

创建实例时，需要注意以下信息（其他配置说明，请参见[自定义购买实例](products/ecs/documents/user-guide/create-an-instance-by-using-the-wizard.md)）：

- 

网络及可用区：选择已开通IPv6的专有网络和交换机。

- 

实例：点击查看更多规格参数，筛选出支持IPv6的实例规格，并选择一个实例规格。

- 

带宽和安全组：单击弹性网卡｜IPv6（选填），然后选中免费分配 IPv6 地址。

分配完成后，您可以通过ECS管理控制台查看IP地址详情。具体操作，请参见[IP](products/ecs/documents/user-guide/ip-address.md)[地址](products/ecs/documents/user-guide/ip-address.md)。

### 步骤三： 配置IPv6地址

将IPv6地址配置到云服务器的网卡上，以使镜像操作系统内部识别并生效IPv6。

- 

部分镜像支持自动配置并识别IPv6地址，通过以下步骤确认您的ECS实例操作系统是否已经识别了IPv6地址。

## Linux实例

- 

远程连接Linux实例。

具体操作，请参见[使用](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[登录](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Linux](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[实例](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)。

- 

执行ip -6 addr show或者ifconfig命令。

- 

如果返回信息如下图所示（一个全局单播地址和一个链路本地地址），则表示已成功识别IPv6地址，可以跳过此配置IPv6的步骤，如果没有，请继续执行以下操作。

## Windows实例

- 

远程连接Windows实例。

具体操作，请参见[使用](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)[Workbench](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)[登录](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)[Windows](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)[实例](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)。

- 

打开命令行工具，执行ipconfig命令

- 

如果返回信息如下图所示（一个全局单播地址和一个链路本地地址），则表示已成功识别IPv6地址，可以跳过此配置IPv6的步骤，如果没有，请继续执行以下操作。

- 

配置IPv6地址。

重要

自动配置IPv6地址方式需安装云助手；若您的实例不支持或不方便安装云助手，请通过手动方式配置IPv6地址。

（推荐）自动配置IPv6地址前提条件

- 

实例已安装云助手。若未安装，请参见[安装云助手](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md)[Agent](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md)。

- 

仅适用于以下操作系统：Alibaba Cloud Linux 2/3、CentOS 6/7/8、Red Hat 6/7、Anolis OS、Fedora、Ubuntu 14/16/18/20、Debian 8/9/10/11、SUSE 11/12/15、OpenSUSE 15/42、FreeBSD 11。

重要

配置过程需使用到云助手，可能会自动重启网卡、网络服务，短时间内网络可能会不可用，请慎重执行。

操作步骤

- 

远程连接Linux实例。

具体操作，请参见[使用](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[登录](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Linux](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[实例](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)。

- 

执行以下命令配置IPv6地址。

说明

在默认情况下，执行以下命令时会自动校验ecs-utils-ipv6插件是否已在本地安装，或本地版本是否为最新。若未安装或版本较旧，插件将自动下载最新版本并执行安装。

sudo acs-plugin-manager --exec --plugin=ecs-utils-ipv6

手动配置（Linux）

- 

远程连接Linux实例。

具体操作，请参见[使用](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[登录](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Linux](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[实例](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)。

- 

执行ip addr | grep inet6或者ifconfig | grep inet6命令，检查实例是否已开启IPv6服务。

- 

如果未返回inet6相关内容：表示实例未开启IPv6服务，请开启IPv6服务。

如何开启IPv6服务？

Alibaba Cloud Linux 2/3

- 

执行以下命令，修改/etc/sysctl.conf配置文件。

vi /etc/sysctl.conf

- 

按i键进入编辑模式，找到如下内容，将内容末尾数值1替换为0。

net.ipv6.conf.all.disable_ipv6 = 1 net.ipv6.conf.default.disable_ipv6 = 1 net.ipv6.conf.lo.disable_ipv6 = 1

- 

如果需要开启指定网络接口，修改信息示例如下。

net.ipv6.conf.eth0.disable_ipv6 = 0

- 

修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。

- 

执行以下命令，验证/etc/sysctl.conf配置信息是否与initramfs中的/etc/sysctl.conf存在差异。

diff -u /etc/sysctl.conf <(lsinitrd -f /etc/sysctl.conf)

说明

Alibaba Cloud Linux 2配置了initramfs（initram file system）。如果initramfs中的/etc/sysctl.conf文件与IPv6的配置文件/etc/sysctl.conf存在差异，系统可能会生效新的配置，与您需求的配置混淆。

- 

若两个配置文件存在差异，执行以下命令，重新生成initramfs。

sudo dracut -v -f

- 

重启ECS实例使配置生效。具体操作，请参见[重启实例](products/ecs/documents/user-guide/restart-instances.md)。

- 

执行ip addr | grep inet6或者ifconfig | grep inet6命令，验证是否已成功开启IPv6。

若系统返回inet6相关内容，则表示IPv6服务已成功开启。

Alibaba Cloud Linux 4

- 

执行以下命令，修改/etc/sysctl.conf配置文件。

vi /etc/sysctl.conf

- 

按i键进入编辑模式，添加或修改以下内容：

net.ipv6.conf.all.disable_ipv6 = 0 net.ipv6.conf.default.disable_ipv6 = 0

- 

修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。

- 

执行以下命令使配置生效。

sysctl -p

- 

执行ip -6 addr show命令，验证是否已成功开启IPv6。

若系统返回inet6相关内容，则表示IPv6服务已成功开启。

CentOS 6/7

- 

执行以下命令，修改/etc/modprobe.d/disable_ipv6.conf配置文件。

vi /etc/modprobe.d/disable_ipv6.conf

- 

按i键进入编辑模式，将options ipv6 disable=1修改为options ipv6 disable=0。

- 

修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。

- 

执行以下命令，修改/etc/sysconfig/network配置文件。

vi /etc/sysconfig/network

- 

按i键进入编辑模式，将NETWORKING_IPV6=no修改为NETWORKING_IPV6=yes。

- 

修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。

- 

（可选）依次执行以下命令，重新加载IPv6模块。

说明

若您的操作系统为CentOS 6，则需要执行该步骤。否则，跳过该步骤。

modprobe ipv6 -r modprobe ipv6 lsmod | grep ipv6

若系统返回以下内容，表明IPv6模块已经成功加载。

ipv6 xxxxx 8

说明

返回内容第三列参数值不能为 0，否则您需要重新设置IPv6服务。

- 

执行以下命令，修改/etc/sysctl.conf配置文件。

vi /etc/sysctl.conf

- 

按i键进入编辑模式，找到如下内容，替换内容末尾数值1为0。

net.ipv6.conf.all.disable_ipv6 = 1 net.ipv6.conf.default.disable_ipv6 = 1 net.ipv6.conf.lo.disable_ipv6 = 1

- 

修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。

- 

执行以下命令，使配置生效。

sudo sysctl -p

Debian 8/9

- 

执行以下命令，修改/etc/default/grub配置文件。

vi /etc/default/grub

- 

按i键进入编辑模式，删除ipv6.disable=1内容。

- 

修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。

- 

执行以下命令，修改/boot/grub/grub.cfg配置文件。

vi /boot/grub/grub.cfg

- 

按i键进入编辑模式，删除ipv6.disable=1内容。

- 

修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。

- 

重启Linux实例。具体操作，请参见[重启实例](products/ecs/documents/user-guide/restart-instances.md)。

- 

执行以下命令，修改/etc/sysctl.conf配置文件。

vi /etc/sysctl.conf

- 

按i键进入编辑模式，找到如下内容，替换内容末尾数值1为0。

net.ipv6.conf.all.disable_ipv6 = 0 net.ipv6.conf.default.disable_ipv6 = 0 net.ipv6.conf.lo.disable_ipv6 = 0

- 

修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。

- 

执行以下命令，使配置生效。

sudo sysctl -p

Ubuntu 14/16、OpenSUSE 42

- 

执行以下命令。修改vi /etc/sysctl.conf配置文件。

vi /etc/sysctl.conf

- 

按i键进入编辑模式，找到如下内容，替换内容末尾数值1为0。

net.ipv6.conf.all.disable_ipv6 = 0 net.ipv6.conf.default.disable_ipv6 = 0 net.ipv6.conf.lo.disable_ipv6 = 0

- 

修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。

- 

执行以下命令，使配置生效。

sysctl -p

FreeBSD 11

- 

执行以下命令，修改/etc/rc.conf配置文件。

vi /etc/rc.conf

- 

按i键进入编辑模式，添加ipv6_activate_all_interfaces="YES"内容。

- 

修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。

- 

执行以下命令，重启网络使配置生效。

/etc/netstart restart

SUSE 11/12

- 

执行以下命令，修改/etc/modprobe.d/50-ipv6.conf配置文件。

vi /etc/modprobe.d/50-ipv6.conf

- 

按i键进入编辑模式，删除install ipv6 /bin/true内容。

- 

修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。

- 

执行以下命令。修改vi /etc/sysctl.conf配置文件。

vi /etc/sysctl.conf

- 

按i键进入编辑模式，找到如下内容，替换内容末尾数值1为0。

net.ipv6.conf.all.disable_ipv6 = 0 net.ipv6.conf.default.disable_ipv6 = 0 net.ipv6.conf.lo.disable_ipv6 = 0

- 

修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。

- 

执行以下命令，使配置生效。

sysctl -p

- 

如果返回inet6相关内容：表示实例已开启IPv6服务，请配置IPv6地址。

- 

配置IPv6地址。

Alibaba Cloud Linux 2/3、CentOS 6/7、Red Hat 6/7

- 

执行以下命令，修改网卡配置文件。

vi /etc/sysconfig/network-scripts/ifcfg-eth0

eth0：需要替换为实际网卡接口名称。修改完成后，保存并退出。

- 

按i键进入编辑模式，在文件中根据实际信息添加以下配置。

DHCPV6C=yes IPV6INIT=yes

- 

修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。

- 

重启ECS实例使配置生效。具体操作，请参见[重启实例](products/ecs/documents/user-guide/restart-instances.md)。

Alibaba Cloud Linux 4

说明

Alibaba Cloud Linux 4使用NetworkManager管理网络，网卡配置文件位于/etc/NetworkManager/system-connections/目录下，而非传统的/etc/sysconfig/network-scripts/。

- 

执行以下命令，查看网络连接名称。

nmcli connection show

记录连接名称（通常为cloud-init eth0）。

- 

执行以下命令，将IPv6配置为自动获取地址。

nmcli connection modify "cloud-init eth0" ipv6.method auto

cloud-init eth0：需要替换为实际的连接名称。若连接名称包含空格，请使用引号。

- 

执行以下命令，重载网络配置并使其生效。

nmcli connection reload nmcli connection up "cloud-init eth0"

- 

重启ECS实例使配置生效。具体操作，请参见[重启实例](products/ecs/documents/user-guide/restart-instances.md)。

CentOS 8

- 

确认网卡配置文件是否包含IPV6INIT=yes和DHCPV6C=yes两项内容。如果包含直接进行下一步操作，如果未包含需先手动添加。

vi /etc/sysconfig/network-scripts/ifcfg-eth0

eth0为网卡标识符，您需要修改成实际的标识符。修改完成后，保存并退出。

- 

禁用cloud-init修改/etc/sysconfig/network-scripts/目录下网卡文件的能力。

说明

分配IPv6地址后无需手动配置，但重启之后可能丢失，因此需要禁用cloud-init修改网卡文件的能力。

- 

执行vi /etc/cloud/cloud.cfg打开网卡配置文件。

vi /etc/cloud/cloud.cfg

- 

在Example datasource config内容前添加以下信息：

network: config: disabled

修改完成后，保存并退出。

- 

重启ECS实例使配置生效。具体操作，请参见[重启实例](products/ecs/documents/user-guide/restart-instances.md)。

Debian 8/9/10/11、Ubuntu 16

- 

执行vi /etc/network/interfaces打开网卡配置文件，在文件中根据实际信息添加以下内容：

iface eth0 inet6 dhcp

eth0：需要替换为实际网卡接口名称。修改完成后，保存并退出。

- 

重启ECS实例使配置生效。具体操作，请参见[重启实例](products/ecs/documents/user-guide/restart-instances.md)。

Ubuntu 18/20

- 

禁用cloud-init修改/etc/sysconfig/network-scripts/目录下网卡文件的能力。

说明

分配IPv6地址后无需手动配置，但重启之后可能丢失，因此需要禁用cloud-init修改网卡文件的能力。

- 

执行vi /etc/cloud/cloud.cfg打开网卡配置文件。

vi /etc/cloud/cloud.cfg

- 

在Example datasource config内容前添加以下信息：

network: config: disabled

修改完成后，保存并退出。

- 

重启ECS实例使配置生效。具体操作，请参见[重启实例](products/ecs/documents/user-guide/restart-instances.md)。

Ubuntu 14

- 

执行vi /etc/network/interfaces打开网卡配置文件，在文件中根据实际信息添加以下内容：

iface eth0 inet6 dhcp

eth0：需要替换为实际网卡接口名称。修改完成后，保存并退出。

- 

重启ECS实例使配置生效。具体操作，请参见[重启实例](products/ecs/documents/user-guide/restart-instances.md)。

FreeBSD 11

- 

执行vi /etc/rc.conf命令，打开网卡配置文件，在文件中根据实际信息添加以下内容：

ipv6_enable="YES" ipv6_ifconfig_vtnet0="<IPv6地址> <子网前缀长度>"

vtnet0：需要替换为实际网卡接口名称。修改完成后，保存并退出。

- 

继续在文件中修改以下信息，修改完成后，保存并退出。

ip6addrctl_enable="YES" ipv6_activate_all_interfaces="YES" ipv6_network_interfaces="auto"

修改完成后，配置文件内容示例如下：

hostname="Aliyun" sshd_enable="YES" dumpdev="NO" ipv6_enable="YES" ip6addrctl_enable="YES" ip6addrctl_policy="ipv4_prefer" ipv6_activate_all_interfaces="YES" ipv6_network_interfaces="auto" ifconfig_lo0="inet 127.0.0.1 netmask 255.0.0.0" ifconfig_vtnet0="inet 192.168.XX.XX netmask 255.255.255.0" ipv6_ifconfig_vtnet0="2001:XXXX:4:4:4:4:4:4 prefixlen 64" defaultrouter="192.168.XX.XX" hostname="freebsd"

- 

重启ECS实例使配置生效。具体操作，请参见[重启实例](products/ecs/documents/user-guide/restart-instances.md)。

Anolis OS 7.9/8.4、CentOS Stream、Fedora

- 

确认网卡配置文件是否包含IPV6INIT=yes和DHCPV6C=yes两项内容。如果包含无需再做任何操作，如果未包含需先手动添加。

vi /etc/sysconfig/network-scripts/ifcfg-eth0

eth0：需要替换为实际网卡接口名称。修改完成后，保存并退出。

- 

重启ECS实例使配置生效。具体操作，请参见[重启实例](products/ecs/documents/user-guide/restart-instances.md)。

手动配置（Windows）

- 

远程连接Windows实例。

具体操作，请参见[使用](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)[Workbench](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)[登录](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)[Windows](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)[实例](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)。

- 

打开命令行工具，执行ipconfig命令，检查实例是否已开启IPv6服务。

- 

如果未返回inet6相关内容：表示实例未开启IPv6服务，请开启IPv6服务。

如何开启IPv6服务？

- 

选择控制面板>网络和共享中心>网络连接。

- 

单击当前网络连接名，打开状态界面，再单击属性。

- 

选中Internet 协议版本 6 （TCP/IPv6）。

- 

Windows Server 2008/2012/2016/2019/2022的操作步骤如下：

检查IPv6协议这一行是否被选中。如果没有选中则需要先选中，然后单击确定。

- 

Windows Server 2003的操作步骤如下：

根据IPv6协议是否存在，执行不同操作。

存在IPv6协议：

- 

选中Internet 协议版本 6 （TCP/IPv6），再单击确定。

不存在IPv6协议：

- 

在本地连接属性页面，单击安装，在网络组件类型页面单击协议>添加。

- 

在选择网络协议页面，选择Microsoft TCP/IP 版本 6>确定完成安装。

- 

选中Internet 协议版本 6 （TCP/IPv6），再单击确定。

- 

如果返回inet6相关内容：表示实例已开启IPv6服务，请配置IPv6地址。

- 

配置IPv6地址。

- 

在实例详情页，获取已生成的IPv6地址。

- 

配置IPv6地址。

- 

Windows Server 2008/2012/2016的操作步骤如下：

- 

选择控制面板>网络。

- 

单击当前网络连接名，打开状态界面，再单击属性。

- 

选择IPv6协议>属性。

- 

选中使用以下IPv6地址，并填入IPv6地址、子网前缀长度和IPv6网关，单击确定。

- 

（可选）绑定多个IPv6地址：在Internet 协议版本 6（TCP/IP）属性界面，单击高级打开高级设置界面，单击添加做批量处理。完成后单击确定。

- 

Windows Server 2003的操作步骤如下：

- 

选择控制面板>网络连接，查看当前网络连接名，假设为本地连接 2。

- 

在Windows系统桌面使用Win+R组合键打开运行对话框，并输入cmd命令，然后单击确定，打开命令行工具。

- 

添加IPv6地址。

- 

单个IPv6地址执行以下命令：

netsh interface ipv6 add address "本地连接 2" <IPv6 地址>

- 

多个IPv6地址执行以下命令：

netsh interface ipv6 add address "本地连接 2" <IPv6 地址 1> netsh interface ipv6 add address "本地连接 2" <IPv6 地址 2>

- 

执行以下命令，添加默认路由。

netsh interface ipv6 add route ::/0 "本地连接 2" <IPv6 网关>

- 

（条件必选）如果您的ECS实例运行的是Linux系统，请执行此步骤；否则，可跳过此操作。

执行以下命令，查看实例是否安装了多网卡配置工具。

ls /sbin/eni-ifscan

若返回信息如下图，则表示实例预装了多网卡配置工具，您需要修改多网卡配置工具的eni-function文件。

说明

如果Linux实例预装了多网卡配置工具，由于该工具默认不支持IPv6，将导致Linux系统内的IPv6网卡无法自动识别，实例重启后系统无法获取IPv6地址。

如何修改eni-function文件

- 

执行以下命令，修改eni-function文件。

vim /etc/eni_utils/eni-function

- 

按i键进入编辑模式，将IPV6INIT=no修改为IPV6INIT=yes，并添加DHCPV6C=yes行，修改后保存并退出。

- 

验证，当输入ifconfig或ipconfig命令返回[第一步](products/ecs/documents/user-guide/step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)的结果时即表示配置成功。

此时ECS实例已具备IPv6私网通信的能力，可以按如下步骤测试私网连通性。

测试私网连通性

说明

测试IPv6的网络连通性时，您需要确保服务端与客户端都支持并配置了IPv6。在此示例中，两台ECS实例互相访问的前提是您的ECS01实例与ECS02实例均已配置了IPv6。

在ECS01实例中执行ping6 <ECS02 IPv6私网地址>命令，ping6ECS02实例的IPv6地址，测试私网通信是否正常。

如果能接收到回复报文，表示通信正常。经测试，ECS01实例到ECS02实例的IPv6私网通信正常。

在ECS02实例中执行ping6命令，pingECS01实例的IPv6地址，测试私网通信是否正常。

如果能接收到回复报文，表示通信正常。经测试，ECS02实例到ECS01实例的IPv6私网通信正常。

### 步骤四： 开通IPv6公网带宽

默认云服务器的IPv6地址仅具有私网通信能力，若您想要通过该IPv6地址访问公网或被公网访问，则需参照如下步骤开通IPv6公网带宽。

- 

登录[专有网络管理控制台](https://vpcnext.console.aliyun.com)。

- 

在左侧导航栏，选择公网访问>IPv6网关。

- 在顶部菜单栏处，选择IPv6网关的地域。

- 

在IPv6网关页面，根据实例的专有网络ID找到对应IPv6网关，然后单击IPv6网关ID。

- 

在IPv6网关的详情页面，单击IPv6公网带宽页签，找到目标IPv6地址，然后在操作列单击开通公网带宽。

- 

在IPv6公网带宽（后付费）页面，根据以下信息配置公网带宽，然后单击立即购买并完成支付。

- 

- 

| 参数 | 描述 |
| --- | --- |
| 流量 | 选择公网带宽的计费类型。 公网带宽支持 按固定带宽计费 和 按使用流量计费 两种计费类型。更多信息，请参见 [IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb) [网关计费说明](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb) 。 |
| 带宽 | 根据需要调整公网带宽的带宽峰值。 |
| 计费周期 | 公网带宽的计费周期。有 按天 和 按小时 两种计费周期。 当公网带宽选择 按固定带宽计费 时，计费周期为 按天 。 当公网带宽选择 按使用流量计费 时，计费周期为 按小时 。 |


开通IPv6公网带宽完成后，即可测试IPv6的公网连通性。

说明

测试IPv6的网络连通性时，您需要确保服务端与客户端都支持并配置了IPv6。

ping -6 aliyun.com

系统返回信息如下图所示，表示网络连接正常。

说明

在此示例中，网站aliyun.com已支持IPv6，当您的ECS实例配置完成后，即可通过IPv6访问aliyun.com。

## 其他操作

### 添加IPv6安全组规则

IPv4和IPv6通信彼此独立，如果当前的安全组规则不能满足业务需求，为了增强网络安全性您需要为ECS实例单独配置IPv6安全组规则。

如何添加IPv6安全组规则

- 

访问[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)。

- 

在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

找到目标安全组，在操作列中，单击管理规则。

- 

在安全组详情页，找到访问规则区域，选择入方向或出方向。

- 

添加安全组规则。具体操作，请参见[添加安全组规则](products/ecs/documents/user-guide/start-using-security-groups.md)。

说明

您需要设置访问来源为IPv6地址段，例如：2001:db8:1234:1a00::***。有关安全组规则更多信息，可参见[安全组规则](products/ecs/documents/user-guide/security-group-rules.md)。

### 删除已分配的IPv6地址

如果您的ECS实例不需要IPv6地址，您可以删除实例的IPv6地址。删除IPv6地址后，您仍然可以使用IPv4地址。本章节介绍如何通过ECS管理控制台删除IPv6地址。

重要

请确保实例的状态为运行中或已停止。

操作步骤

- 

访问[ECS](https://ecs.console.aliyun.com/networkInterfaces)[控制台-弹性网卡](https://ecs.console.aliyun.com/networkInterfaces)。

- 

在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

在弹性网卡页面，选择已绑定至目标实例并分配了IPv6地址的弹性网卡，然后在操作列单击管理弹性网卡IP。

- 

在弹出的管理弹性网卡IP对话框中，单击待删除的目标IPv6地址右侧的图标。

- 

单击确定。

## 相关文档

- 

当某个IPv6地址不需要公网通信能力时，您可以删除IPv6地址的公网带宽。具体操作，请参见[删除](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth#section-gev-go2-wyf)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth#section-gev-go2-wyf)[公网带宽](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth#section-gev-go2-wyf)。

- 

您可以通过添加和管理路由表中的IPv6路由，来管理专有网络 VPC（Virtual Private Cloud）内的IPv6流量。具体操作，请参见[添加和管理](https://help.aliyun.com/zh/ipv6-gateway/user-guide/create-and-manage-ipv6-routes)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/create-and-manage-ipv6-routes)[路由](https://help.aliyun.com/zh/ipv6-gateway/user-guide/create-and-manage-ipv6-routes)。

[上一篇：IP前缀](products/ecs/documents/user-guide/ip-prefix.md)[下一篇：ECS实例私网域名解析](products/ecs/documents/user-guide/ecs-private-domain-resolution.md)

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
