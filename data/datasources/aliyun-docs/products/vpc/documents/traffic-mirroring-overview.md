# 流量镜像-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/traffic-mirroring-overview

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/vpc/documents/vpc-user-guide.md)

- [开发参考](products/vpc/documents/developer-reference.md)

- [产品计费](products/vpc/documents/product-billing.md)

- [常见问题](products/vpc/documents/troubleshooting.md)

- [动态与公告](products/vpc/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 流量镜像

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/vpc)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当您需要监控网络流量时，传统方式为登录实例抓包或在实例部署监控Agent，占用实例的系统资源，影响业务性能。VPC流量镜像提供旁路监控方案，在不影响业务流量的前提下，将符合筛选条件的出入指定弹性网卡的流量复制并转发到安全分析设备，实现实时检测。

流量镜像常见的使用场景：

- 

安全场景：网络入侵检测

使用流量镜像获取特定流的全部数据包，通过自主研发或者第三方安全软件进行全面检查，实时捕获所有可能存在的安全漏洞和入侵威胁，更快速地检查和响应攻击。

- 

审计场景：金融或政府

对于金融或安全性合规性比较高的业务场景，通过流量镜像透明地将实例流量镜像到统一审计平台进行分析，满足审计需求。

- 

网络运维场景：网络问题定位

通过流量镜像来检查网络问题，运维人员可以直接查看传输的内容（例如：分析TCP的重传）来排查问题，无需登录ECS实例内部抓取报文。

## 工作原理

### 工作流程

流量镜像会话在指定的镜像源和镜像目的建立转发路径。启动镜像会话后，流量镜像将执行以下操作：

- 

复制符合筛选条件的镜像源业务报文。

镜像源当前仅支持弹性网卡。

筛选条件中包含入方向规则和出方向规则，采用源网段、源端口、目的网段、目的端口和协议类型组成的五元组，按照优先级分别筛选弹性网卡实例接收/发出的流量。

- 

使用[标准的](https://datatracker.ietf.org/doc/html/rfc7348)[VXLAN](https://datatracker.ietf.org/doc/html/rfc7348)[报文格式](https://datatracker.ietf.org/doc/html/rfc7348)封装后作为镜像报文。

- 

VNI（VXLAN Network Identifier，VXLAN ID）：分配给镜像会话的虚拟网络 ID，用于区分不同会话的镜像流量。创建镜像会话时，如未指定VNI，将由系统随机分配。

- 

源 IP：镜像源的主IP地址。

- 

源端口：由业务报文的五元组哈希值确定。

- 

目的IP：镜像目的的主IP地址。

- 

目的端口：默认使用4789端口，不支持修改。

- 

将镜像报文转发至路由可达的镜像目的。如果镜像目的和镜像源不属于同一个VPC，您需要[配置](products/vpc/documents/cross-vpc-interconnection-overview.md)[VPC](products/vpc/documents/cross-vpc-interconnection-overview.md)[互连](products/vpc/documents/cross-vpc-interconnection-overview.md)，确保镜像源和镜像目的之间路由可达。

镜像目的当前支持弹性网卡、专有网络类型的私网CLB或网关型负载均衡终端节点GWLBe。

当前，支持将流量转发至网关型负载均衡终端节点GWLBe的地域，有华东1（杭州）、华东2（上海）、华北1（青岛）、华北2（北京）、华北5（呼和浩特）、华南1（深圳）、新加坡、美国（硅谷）、美国（弗吉尼亚）。

从镜像源复制报文时不受安全组和网络ACL策略的限制，但镜像报文转发至镜像目的时，需确保在镜像目的所在的安全组和网络ACL中配置入方向规则，允许来自镜像源的UDP协议报文访问镜像目的的4789端口。

使用专有网络类型的私网CLB作为镜像目的时，需确保在4789端口[配置](products/slb/documents/classic-load-balancer/user-guide/add-a-udp-listener.md)[UDP](products/slb/documents/classic-load-balancer/user-guide/add-a-udp-listener.md)[监听](products/slb/documents/classic-load-balancer/user-guide/add-a-udp-listener.md)。而网关型负载均衡配置会监听所有端口的所有数据包。

### 匹配规则

同一个镜像源的同一个报文只能被镜像一次。

以镜像源的入方向流量为例：

- 

当镜像源仅加入一个镜像会话时，与镜像会话关联的筛选条件的入方向规则匹配。每条规则有优先级，根据规则的五元组依次判断是否与流量匹配。匹配到首条规则后，执行指定的镜像策略。无法匹配时，不镜像对应的流量。

- 

当镜像源加入多个镜像会话时，将按照镜像会话的优先级，依次与镜像会话关联的筛选条件的入方向规则匹配。当前镜像会话无法匹配时，将与下一优先级的镜像会话匹配，直到匹配到首条入方向规则，将执行指定的镜像策略。若所有镜像会话关联的入方向规则均无法匹配，则不镜像对应的流量。

### 镜像目的接收的报文长度

- 

分片业务报文的镜像行为

- 

当原始业务报文长度超过链路 MTU 时，会被切割为多个分片传输。

例如，业务报文长度为 2000 字节，而链路 MTU 为 1500 字节，报文将被切割为 1500、500 字节的两个分片。

在阿里云网络内，链路默认支持的MTU为 1500，但部分网络组件例如 VPN 网关等自身的MTU限制小于1500。

- 

当镜像源绑定的 ECS 实例开启 TSO 或 UFO 功能时，分片业务报文的镜像行为可能会有所不同。如需镜像目的接收到所有分片业务报文的镜像报文，建议您关闭 TSO 和 UFO 功能（关闭后可能会对实例性能有影响）或使用 7 代及以上的[实例规格族](products/ecs/documents/user-guide/best-practices-for-instance-type-selection.md)。

您可以根据实例规格族主体中的数字来判断实例规格是否为7代，例如ecs.g7se.xlarge。

不同实例规格的业务报文镜像行为

| 源 ECS 实例规格（自身 MTU 值 = 1500） | - 7 代及以上的实例 - 7 代以下且关闭 TSO 和 UFO 功能的实例 | 7 代以下且开启 TSO 或 UFO 功能的实例 |
| --- | --- | --- |
| 业务报文长度 | 2000 |  |
| 链路 MTU | 1500 |  |
| 镜像行为 | 先对完整业务报文分片，再分别对每个分片报文做镜像。 - 被镜像的分片报文 1：1500 字节 - 被镜像的分片报文 2：500 字节 | 先对完整业务报文做镜像，再对业务报文分片。 被镜像的报文：2000 字节 |


- 

镜像报文截断：当被镜像的分片报文或完整业务报文的长度加上 VXLAN 头的长度（固定值50字节），大于能够完全转发的镜像报文长度时，系统会对镜像报文进行截断。

- 

在华东1（杭州）、华东2（上海）、华北1（青岛）、华北2（北京）、华北5（呼和浩特）、华南1（深圳）、新加坡、美国（硅谷）、美国（弗吉尼亚）地域，镜像目的收到的被镜像的报文长度受限于镜像目的 MTU。目前，阿里云的 8 代主售实例规格族支持 8500 MTU 的巨型帧。建议您为镜像目的开启巨型帧，避免镜像报文被截断。

镜像报文截断行为

如果业务报文长度为1500字节，当镜像目的MTU为1500字节时，系统会对镜像报文进行截断；而镜像目的开启巨型帧（支持8500字节的MTU）时，能够完全转发镜像报文。

| 业务报文长度 | 500 | 1500 | 1500 |
| --- | --- | --- | --- |
| 镜像目的 MTU | 1500 | 1500 | 8500 |
| 镜像目的接收到的镜像报文大小 | 550=500（实际被镜像的业务报文长度）+50（VXLAN 头的长度） | 1500=1450（实际被镜像的业务报文长度）+50（VXLAN 头的长度） | 1550=1500（实际被镜像的业务报文长度）+50（VXLAN 头的长度） |


- 

其他地域，镜像目的收到的被镜像的报文长度受限于链路默认 MTU（1500字节）。

镜像报文截断行为

如果链路 MTU 大于 1500字节，例如 8500字节，系统将按照链路默认 MTU = 1500字节进行截断。

| 业务报文长度 | 500 | 1500 | 1500 |
| --- | --- | --- | --- |
| 链路 MTU | 1500 | 1500 | 8500 |
| 镜像目的接收到的镜像报文大小 | 550=500（实际被镜像的业务报文长度）+50（VXLAN 头的长度） | 1500=1450（实际被镜像的业务报文长度）+50（VXLAN 头的长度） | 1500=1450（实际被镜像的业务报文长度）+50（VXLAN 头的长度） |


- 

如果仅需要查看特定长度的镜像报文头，您可以设置镜像报文长度，系统将对镜像源业务报文中超过该值的部分进行截断，再转发到镜像目的。

镜像特定长度的报文

## 使用限制

- 

镜像源和镜像目的：同一个弹性网卡不能既作为镜像源又作为镜像目的。镜像源和镜像目的，不支持选择[托管弹性网卡](products/ecs/documents/user-guide/managed-enis.md)。

- 

账号与地域：支持在同账号、同地域的单VPC或跨VPC下配置镜像源和镜像目的，暂不支持跨地域或跨账号的场景。

- 

IP版本：支持镜像IPv4的网络流量，暂不支持IPv6。

- 

带宽：流量镜像会占用实例的带宽，且不会作额外限速。当实例带宽达到最大容量时，会丢弃流量镜像报文，保障优先转发业务流量。

- 

流量类型：不支持镜像网络ACL丢弃流量、安全组丢弃流量、流日志流量、ARP及DHCP流量。

## 创建/删除流量镜像

出入镜像源的业务流量，按照优先级，基于协议类型、IP版本、源网段、目的网段、源端口、目的端口匹配到筛选条件中的特定规则后，系统将对流量执行指定策略，镜像/不镜像对应的流量。镜像流量将被复制并转发到镜像目的。

- 

优先级决定规则的生效顺序，取值范围为1~16777216。数字越小，优先级越高，同一个筛选条件的每条入方向规则或出方向规则优先级不能重复。

- 

协议类型为TCP(6)/UDP(17)时，可以调整端口范围。取值范围为0~65535，设置格式为起始端口/终止端口。选择其他协议类型时，端口范围无法设置，默认为-1/-1，表示不限制端口。

### 控制台

初次使用时，请登录[流量镜像开通页面](https://common-buy.aliyun.com/?commodityCode=vpc_trafficmirror_public_cn#/buy)，根据提示开通流量镜像功能。

创建流量镜像

- 

创建筛选条件

如果已创建了符合镜像流量需求的筛选条件，您可以直接创建镜像会话。

- 

前往[专有网络控制台 - 筛选条件](https://vpc.console.aliyun.com/traffic-mirror/cn-hangzhou/filters)，在顶部菜单栏选择要创建流量镜像的地域。单击创建筛选条件。

- 

配置入方向规则和出方向规则，确定哪些流量从镜像源复制并转发到镜像目的。当筛选条件中不包含任何规则时，不镜像任何流量。

创建筛选条件时，出入方向规则分别最多可配置10条，创建完成后，您可以添加/编辑/删除出入方向规则。

如需删除筛选条件，请确保筛选条件没有关联镜像会话。如有关联，需先变更镜像会话关联的筛选条件，再在目标筛选条件的操作列单击删除。

- 

创建镜像会话

- 

前往[专有网络控制台 - 镜像会话](https://vpc.console.aliyun.com/traffic-mirror/cn-hangzhou/sessions)，在顶部菜单栏选择要创建流量镜像的地域。单击创建镜像会话。

- 

配置镜像会话：

- 

指定VNI：分配给镜像会话的虚拟网络ID，用于区分不同会话的镜像流量，取值范围为0~16777215。如未指定VNI，将由系统随机分配。

- 

配置优先级：当镜像源加入多个镜像会话时，将按照镜像会话的优先级来确定镜像到哪个目的。取值范围为1~32766。 数字越小，优先级越高。同一账号在同一个地域创建的镜像会话优先级不能重复。

- 

如果仅需要查看特定长度的镜像报文头，您可以设置镜像报文长度，系统将对镜像源业务报文中超过该值的部分进行截断，再转发到镜像目的。

- 

配置关联的筛选条件、镜像源、镜像目的。

- 

启动镜像会话

- 

创建完成后启用镜像会话，或返回列表，在目标镜像会话的操作列单击启动。

- 

当镜像源有符合筛选条件的流量时，您可以在镜像目的执行tcpdump -i 镜像目的对应的网卡名称 udp port 4789 -nne，查看镜像目的接收的镜像报文。

变更流量镜像

在目标镜像会话的详情页，您可以变更镜像目的、筛选条件，添加或删除镜像源，或修改镜像会话的VNI、优先级与镜像报文长度。

停止/删除镜像会话

在目标镜像会话的操作列单击停止/删除。

### API

创建流量镜像初次使用时，需调用[OpenTrafficMirrorService](products/vpc/documents/developer-reference/api-vpc-2016-04-28-opentrafficmirrorservice.md)开通流量镜像功能。

- 

调用[CreateTrafficMirrorFilter](products/vpc/documents/developer-reference/api-vpc-2016-04-28-createtrafficmirrorfilter.md)创建流量镜像筛选条件。

- 

调用[CreateTrafficMirrorFilterRules](products/vpc/documents/developer-reference/api-vpc-2016-04-28-createtrafficmirrorfilterrules.md)创建筛选条件的入方向或出方向规则。

- 

调用[CreateTrafficMirrorSession](products/vpc/documents/developer-reference/api-vpc-2016-04-28-createtrafficmirrorsession.md)创建镜像会话。

- 

调用[UpdateTrafficMirrorSessionAttribute](products/vpc/documents/developer-reference/api-vpc-2016-04-28-updatetrafficmirrorsessionattribute.md)调整Enabled为true，启动镜像会话。

变更流量镜像

- 

调用[AddSourcesToTrafficMirrorSession](products/vpc/documents/developer-reference/api-vpc-2016-04-28-addsourcestotrafficmirrorsession.md)/[RemoveSourcesFromTrafficMirrorSession](products/vpc/documents/developer-reference/api-vpc-2016-04-28-removesourcesfromtrafficmirrorsession.md)为镜像会话增加/删除镜像源。

- 

调用[UpdateTrafficMirrorSessionAttribute](products/vpc/documents/developer-reference/api-vpc-2016-04-28-updatetrafficmirrorsessionattribute.md)修改镜像会话的配置或变更镜像目的、筛选条件。

修改/删除筛选条件

- 

调用[CreateTrafficMirrorFilterRules](products/vpc/documents/developer-reference/api-vpc-2016-04-28-createtrafficmirrorfilterrules.md)创建筛选条件的入方向或出方向规则。

- 

调用[DeleteTrafficMirrorFilterRules](products/vpc/documents/developer-reference/api-vpc-2016-04-28-deletetrafficmirrorfilterrules.md)删除筛选条件的入方向或出方向规则。

- 

调用[DeleteTrafficMirrorFilter](products/vpc/documents/developer-reference/api-vpc-2016-04-28-deletetrafficmirrorfilter.md)删除筛选条件。

停止/删除流量镜像

- 

调用[UpdateTrafficMirrorSessionAttribute](products/vpc/documents/developer-reference/api-vpc-2016-04-28-updatetrafficmirrorsessionattribute.md)调整Enabled为false，停止镜像会话。

- 

调用[DeleteTrafficMirrorSession](products/vpc/documents/developer-reference/api-vpc-2016-04-28-deletetrafficmirrorsession.md)删除镜像会话。

### Terraform

本示例仅镜像进出镜像源的TCP流量，您应根据需镜像的流量配置筛选条件的出入方向规则。

Resources：[alicloud_vpc_traffic_mirror_filter](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_traffic_mirror_filter)、[alicloud_vpc_traffic_mirror_session](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_traffic_mirror_session)# 指定创建流量镜像的地域 provider "alicloud" { region = "cn-hangzhou" } # 指定镜像源的ID variable "traffic_mirror_source_id" { default = "eni-hp3e******" # 修改为弹性网卡的实际ID } # 指定镜像目的的ID variable "traffic_mirror_target_id" { default = "eni-hp3h******" # 修改为弹性网卡的实际ID } # 创建筛选条件并配置出入方向规则：采集进出镜像源的所有TCP流量 resource "alicloud_vpc_traffic_mirror_filter" "example_vpc_traffic_mirror_filter" { traffic_mirror_filter_name = "example_vpc_traffic_mirror_filter_name" egress_rules { priority = 1 protocol = "TCP" action = "accept" destination_cidr_block = "0.0.0.0/0" destination_port_range = "-1/-1" source_cidr_block = "0.0.0.0/0" source_port_range = "-1/-1" } ingress_rules { priority = 1 protocol = "TCP" action = "accept" destination_cidr_block = "0.0.0.0/0" destination_port_range = "-1/-1" source_cidr_block = "0.0.0.0/0" source_port_range = "-1/-1" } } # 创建流量镜像会话 resource "alicloud_vpc_traffic_mirror_session" "example_vpc_traffic_mirror_session" { traffic_mirror_session_name = "example_vpc_traffic_mirror_session" priority = 1 # 指定镜像会话的优先级,当镜像源加入多个镜像会话时，将按照镜像会话的优先级来确定镜像到哪个目的。取值范围为1~32766。 数字越小，优先级越高。同一账号在同一个地域创建的镜像会话优先级不能重复。 virtual_network_id = 10 # 指定镜像会话的VNI,用于区分不同会话的镜像流量，取值范围为0~16777215。如未指定VNI，将由系统随机分配。 traffic_mirror_filter_id = alicloud_vpc_traffic_mirror_filter.example_vpc_traffic_mirror_filter.id # 指定关联的筛选条件 traffic_mirror_source_ids = [var.traffic_mirror_source_id] # 指定流量镜像源 traffic_mirror_target_type = "NetworkInterface" # 指定流量镜像目的类型 traffic_mirror_target_id = var.traffic_mirror_target_id # 指定流量镜像目的 #packet_length = 1500 # 如果仅需要查看特定长度的镜像报文头，您可以设置镜像报文长度，系统将对镜像源业务报文中超过该值的部分进行截断，再转发到镜像目的。 }

## 流量镜像配置示例

### 将入方向TCP流量镜像到弹性网卡

### 将入方向TCP/UDP流量镜像到不同的镜像目的

### 将非VPC内部流量镜像到跨VPC的镜像目的

配置以下筛选条件，可以监控来自VPC外部的流量和流出VPC的流量。

例如，按照入方向规则的优先级，所有源IP在VPC CIDR地址段内的入方向流量就不采集，但会采集其他所有流量。

由于镜像目的与镜像源位于不同VPC，默认网络隔离。需要使用[VPC](products/vpc/documents/vpc-peer-to-peer-connection.md)[对等连接](products/vpc/documents/vpc-peer-to-peer-connection.md)并在两端VPC配置路由，确保镜像目的路由可达。

## 更多信息

### 计费说明

计费项

流量镜像费用 = 实例费 + 流量处理费

- 

实例费 = 启动镜像会话的镜像源个数（个） × 镜像会话活跃时长（小时） × 实例费单价（元/个/小时）

- 

流量处理费 = 镜像流量总量（GB） × 流量处理费单价（元/GB）

| 计费项 | 单价 |
| --- | --- |
| 实例费 | 0.1（元/个/小时） |
| 流量处理费 | 0.05（元/GB） |


计费规则

- 

2027年03月31日前，免收流量处理费。

- 

镜像源启动镜像会话后，每个启用了镜像会话的镜像源按小时付费，不足1小时按1小时计费。

- 

单个镜像源创建了多个镜像会话，实例费仅收取一次。镜像会话活跃时长按照镜像源在每个镜像会话中累计的活跃时长计算。例如，镜像源在镜像会话1中活跃时长为5小时，在镜像会话2中活跃时长为4小时，计费时镜像会话活跃时长为9小时。

计费示例

例如，一个VPC中有5个弹性网卡实例启用了镜像会话，镜像会话的活跃时间为30天，每天24小时，镜像流量总量为20 GB。详细费用计算如下：

- 

实例费 =5 × 30 × 24 × 0.1 = 360 元

- 

流量处理费 =20 × 0.05 = 1 元

- 

流量镜像总费用 =360 + 1 = 361 元

欠费与充值

欠费和续费说明

- 

欠费后如果在延停权益额度内，流量镜像功能不会受到停服影响。

阿里云提供[延期免停权益](https://help.aliyun.com/zh/user-center/exemption-of-suspension-after-delinquency)，即当按量付费的资源发生欠费后，提供一定额度或时长继续使用云服务的权益，延停期间正常计费。

- 

欠费后如果超出了延停权益额度，流量镜像功能停止工作，已开启的镜像会话自动关闭。

- 

如果在流量镜像功能停止15天内[充值](https://help.aliyun.com/zh/document_detail/37107.html)并补足欠费后，服务会自动开启，您可以继续使用流量镜像服务，被停止的镜像会话会自动恢复。

- 

如果流量镜像功能停止15天仍未及时充值，镜像会话实例会被删除。实例被删除后相关配置和数据将被删除，不可恢复。

### 支持的地域

公有云支持的地域

| 区域 | 支持流量镜像的地域 |
| --- | --- |
| 亚太-中国 | 华东 1（杭州） 、 华东 2（上海） 、 华东 5 （南京-本地地域-关停中） 、 华北 1（青岛） 、 华北 2（北京） 、 华北 3（张家口） 、 华北 5（呼和浩特） 、 华北 6（乌兰察布） 、 华南 1（深圳） 、 华南 2（河源） 、 华南 3（广州） 、 西南 1（成都） 、 中国香港 、 华东 6（福州-本地地域-关停中） |
| 亚太-其他 | 日本（东京） 、 韩国（首尔） 、 新加坡 、 马来西亚（吉隆坡） 、 印度尼西亚（雅加达） 、 泰国（曼谷） 、 菲律宾（马尼拉） |
| 欧洲与美洲 | 德国（法兰克福） 、 英国（伦敦） 、 美国（硅谷） 、 美国（弗吉尼亚） 、 墨西哥 |
| 中东 | 沙特（利雅得）- 合作伙伴运营 |


金融云支持的地域

| 区域 | 支持流量镜像的地域 |
| --- | --- |
| 亚太 | 华北 2 金融云（邀测） 、 华东 1 金融云 、 华东 2 金融云 |


政务云支持的地域

| 区域 | 支持流量镜像的地域 |
| --- | --- |
| 亚太 | 华北 2 阿里政务云 1 |


### 配额

| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| trafficmirror_quota_source_num_per_session | 单个镜像会话支持加入的镜像源个数 | 10 个 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
| vpc_quota_traffic_mirror_source_num_per_large_ecs_target | 镜像目的为弹性网卡，且弹性网卡绑定的是以下规格的 ECS 实例时，单个镜像目的支持的镜像源个数 ECS 实例规格 ecs.ebmc7.32xlarge、ecs.ebmg7.32xlarge、ecs.ebmr7.32xlarge、ecs.ebmhfg7.48xlarge、ecs.ebmhfc7.48xlarge、ecs.ebmhfr7.48xlarge、ecs.ebmc7a.64xlarge、ecs.ebmg7a.64xlarge、ecs.ebmg7se.32xlarge、ecs.ebmg6a.64xlarge、ecs.ebmg6e.26xlarge、ecs.ebmc6a.64xlarge、ecs.ebmc6e.26xlarge、ecs.ebmr7a.64xlarge、ecs.ebmr6a.64xlarge、ecs.ebmr6e.26xlarge、ecs.c8i.48xlarge、ecs.g8i.48xlarge、ecs.c7nex.32xlarge、ecs.g7nex.32xlarge、 ecs.g7ne.24xlarge、ecs.c7.32xlarge、ecs.g7.32xlarge、ecs.r7.32xlarge、ecs.r6e.26xlarge、 ecs.g7t.32xlarge、ecs.g6t.26xlarge、ecs.g6e.26xlarge、ecs.c7t.32xlarge、ecs.c6t.26xlarge、ecs.c6e.26xlarge、ecs.g5ne.18xlarge、ecs.r7t.32xlarge | 200 个 |  |
| vpc_quota_traffic_mirror_source_num_per_small_ecs_target | 镜像目的为弹性网卡，且弹性网卡绑定的不是以下规格的 ECS 实例，单个镜像目的支持的镜像源个数 ECS 实例规格 ecs.ebmc7.32xlarge、ecs.ebmg7.32xlarge、ecs.ebmr7.32xlarge、ecs.ebmhfg7.48xlarge、ecs.ebmhfc7.48xlarge、ecs.ebmhfr7.48xlarge、ecs.ebmc7a.64xlarge、ecs.ebmg7a.64xlarge、ecs.ebmg7se.32xlarge、ecs.ebmg6a.64xlarge、ecs.ebmg6e.26xlarge、ecs.ebmc6a.64xlarge、ecs.ebmc6e.26xlarge、ecs.ebmr7a.64xlarge、ecs.ebmr6a.64xlarge、ecs.ebmr6e.26xlarge、ecs.c8i.48xlarge、ecs.g8i.48xlarge、ecs.c7nex.32xlarge、ecs.g7nex.32xlarge、 ecs.g7ne.24xlarge、ecs.c7.32xlarge、ecs.g7.32xlarge、ecs.r7.32xlarge、ecs.r6e.26xlarge、 ecs.g7t.32xlarge、ecs.g6t.26xlarge、ecs.g6e.26xlarge、ecs.c7t.32xlarge、ecs.c6t.26xlarge、ecs.c6e.26xlarge、ecs.g5ne.18xlarge、ecs.r7t.32xlarge | 20 个 |  |
| vpc_quota_traffic_mirror_rules_num_per_filter | 单个筛选条件支持的筛选规则数 | 20 个 |  |
| 无 | 单账号单地域支持的最大镜像会话数 | 20000 个 | 无法提升 |
| 单个镜像源支持创建的最大镜像会话数 | 3 个 |  |  |
| 镜像目的为私网传统型负载均衡 CLB 时，单个镜像目的支持的镜像源个数 | 500 个 |  |  |
| 镜像目的为网关型负载均衡终端节点 GWLBe 时，单个镜像目的支持的镜像源个数 | 500 个 |  |  |
| 单账号单地域支持的最大筛选条件数 | 100 个 |  |  |
| 单个筛选条件支持关联的镜像会话数 | 2000 个 |  |  |


[上一篇：流日志](products/vpc/documents/vpc-flow-logs.md)[下一篇：使用流量镜像对VPC流量进行安全审查](products/vpc/documents/use-traffic-mirroring-to-perform-security-audit-on-vpc-traffic.md)

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
