# 通过自定义方式购买云服务器ECS-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/create-an-instance-by-using-the-wizard

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

# 通过购买页自定义购买ECS

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

与快速购买实例相比，自定义购买可根据业务场景灵活地选择配置，如镜像类型、实例规格、存储、带宽、安全组等。本文介绍如何自定义购买实例。

重要

如果您刚接触ECS不久，想要快速上手购买并使用ECS实例，我们为您准备了一个较简单的示例，请参见[控制台自定义购买并使用](products/ecs/documents/user-guide/use-the-ecs-instance-in-the-console.md)[ECS](products/ecs/documents/user-guide/use-the-ecs-instance-in-the-console.md)[实例](products/ecs/documents/user-guide/use-the-ecs-instance-in-the-console.md)，它将帮助您更直观地理解整个流程。在初步了解ECS后，您可以通过阅读本文，了解自定义购买实例时更加详细的配置说明。

## 前提条件

- 

注册中国站阿里云账号，并完成实名认证。具体操作，请参见[阿里云账号注册流程](https://help.aliyun.com/zh/account/ali-cloud-account-registration-process)。

- 

开通按量付费ECS资源时，您的阿里云账户余额（即现金余额）和代金券的总值不得小于100.00元人民币。具体充值操作，请参见[在线充值](https://help.aliyun.com/zh/user-center/use-alipay-online-banking-to-recharge-online)。

## 操作步骤

- 

前往[实例购买页](https://ecs-buy.aliyun.com/wizard/#/)。

- 

选择自定义购买页签。

- 

选择付费类型、地域、实例规格、镜像等配置。

各配置项详细说明，请参考[配置项说明](products/ecs/documents/user-guide/create-an-instance-by-using-the-wizard.md)。

- 

在最终创建实例前，请在页面右侧检查实例的整体配置并配置使用时长等选项，确保符合您的要求。

- 

阅读并签署《云服务器ECS服务条款》等服务协议（若已签署，则无需重复签署，请以页面提示为准），然后单击确认下单。

创建实例一般需要3~5分钟，请您耐心等待。您可前往控制台的实例列表页面查看实例的状态，当实例状态变为运行中时，表示实例创建完成。

## 配置项说明

### 付费类型

付费类型影响实例的计费和收费规则，不同付费类型的实例遵循的资源状态变化规则也存在差异。

- 

- 

- 

| 付费模式 | 说明 | 相关文档 |
| --- | --- | --- |
| 包年包月 | 先付费后使用 ，最短可以按周购买 。适用于长期稳定的业务，如 7*24 的 Web 服务、数据库服务等。 | [包年包月](products/ecs/documents/subscription.md) |
| 按量付费 | 先使用后付费，计费周期精确到秒，方便您按需购买和释放资源。适用于有大幅波动的场景，如临时扩展、测试、电商抢购等。 说明 推荐搭配使用 节省计划、 预留实例券优化成本。 | [按量付费](products/ecs/documents/pay-as-you-go-1.md) [什么是节省计划](products/ecs/documents/savings-plans.md) [什么是预留实例券](products/ecs/documents/reserved-instances.md) |
| 抢占式实例 | 先使用后付费，相对于按量付费实例能最高节约 90%的实例成本，但可能因市场价格变化或实例规格库存不足而自动释放实例。适用于无状态、容错能力强、中断容忍度高的业务场景，如测试、实时分析等。 | [抢占式实例](products/ecs/documents/spot-instance.md) |


### 地域

地域指数据中心所在的地理区域，选择距离近的地域可以降低网络时延，实例创建完成后不支持更改地域。更多信息，请参见[地域和可用区](https://help.aliyun.com/zh/document_detail/40654.html#concept-2459516)。

### 网络及可用区

推荐您使用专有网络，专有网络之间逻辑上彻底隔离，安全性更高，且支持弹性公网IP（EIP）、弹性网卡、IPv6等功能。

可用区是指在同一地域内，电力和网络互相独立的物理区域。同一可用区内实例之间的网络延时更小，其用户访问速度更快。

- 

- 

- 

- 

- 

| 网络类型 | 说明 | 相关文档 |
| --- | --- | --- |
| 专有网络 | 专有网络是您在阿里云自己定义的一个隔离网络环境，您可以完全掌控自己的专有网络，例如选择 IP 地址范围、配置路由表和网关等。 如果在创建实例时不需要自定义专有网络配置，您可以跳过本步骤，系统会自动创建默认专有网络和交换机。 选择已有的专有网络和交换机，或者单击 创建专有网络 、 创建交换机 前往专有网络控制台即时创建专有网络和交换机。创建完成后，返回 ECS 实例创建向导并单击 图标，查看专有网络和交换机列表。 说明 如果您需要为实例分配 IPv6 地址，请选择已开通 IPv6 网段的专有网络和交换机。 | [什么是专有网络](products/vpc/documents/what-is-vpc.md) [VPC](products/vpc/documents/what-is-vpc.md) [创建专有网络和交换机](products/vpc/documents/user-guide/create-and-manage-a-vpc.md) [创建交换机](products/vpc/documents/user-guide/create-and-manage-vswitch.md) [为](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#section-ucc-t6j-xv6) [VPC](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#section-ucc-t6j-xv6) [开启](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#section-ucc-t6j-xv6) [IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#section-ucc-t6j-xv6) [为已有交换机开通](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vswitch-1#section-xz0-9p6-jlk) [IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vswitch-1#section-xz0-9p6-jlk) [网段](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vswitch-1#section-xz0-9p6-jlk) |


### 实例和镜像

实例规格和镜像定义了一台实例的基本属性：vCPU、内存和操作系统等基础资源。

实例规格

可选的实例规格和地域等因素有关，您可以前往[ECS](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)[实例可购买地域](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)查看实例的可购情况。

如果您有特定的配置需求，例如需要挂载多张弹性网卡、使用ESSD云盘、使用本地盘等，请确认实例规格是否支持。关于实例规格的特点、适用场景、指标数据等信息，请参见[实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)。

如果选择付费类型为抢占式实例，配置使用时长和上限价格。

- 

实例使用时长：使用时长指抢占式实例的保护期，超出保护期后可能因市场价格变化或实例规格库存不足而自动释放实例。

| 实例使用时长 | 说明 |
| --- | --- |
| 设定实例使用 1 小时 | 抢占式实例创建后有 1 小时保护期，在保护期内不会被自动释放。 |
| 无确定使用时长 | 抢占式实例创建后没有保护期，但比有保护期的抢占式实例更优惠。 |


- 

单台实例上限价格：

| 单台实例上限价格 | 说明 |
| --- | --- |
| 使用自动出价 | 始终使用实例规格的实时市场价格，该市场价格不会超过对应按量付费实例的价格。使用自动出价可以避免抢占式实例因实时市场价格超过上限被自动释放，但不能避免因实例规格的库存不足被自动释放。 |
| 设置单台上限价 | 自行输入明确的价格上限，实例规格的实时市场价格超出该上限或者库存不足时，抢占式实例都会被自动释放。 |


镜像

镜像提供了运行实例所需的信息，阿里云提供多种镜像来源供您方便地获取镜像，如下表所示。

| 镜像来源 | 说明 | 相关文档 |
| --- | --- | --- |
| 公共镜像 | 阿里云官方提供的基础镜像，均已获得正版授权，涵盖 Windows Server 系统镜像和主流的 Linux 系统镜像。 说明 当您选择倚天实例规格族 g8y/c8y/r8y 以及 Alibaba Cloud Linux 镜像时，即可为实例配置应用加速功能，实现不同程度的性能提升。更多信息，请参见 [应用性能加速](products/ecs/documents/user-guide/booster-extensions.md) 。 | [公共镜像](products/ecs/documents/user-guide/public-mirroring-overview.md) |
| 自定义镜像 | 您自行创建或导入的镜像，包含了初始系统环境、应用环境、软件配置等信息，可以节省重复配置的时间。 | [自定义镜像](products/ecs/documents/user-guide/overview-36.md) |
| 共享镜像 | 其他阿里云账号共享的自定义镜像，方便跨账号使用同一镜像创建实例。 | [共享自定义镜像](products/ecs/documents/user-guide/share-a-custom-image.md) |
| 云市场镜像 | 云市场镜像中的镜像均经过严格审核，种类丰富，方便您一键部署用于建站、应用开发等场景的云服务器。 | [云市场镜像](products/ecs/documents/user-guide/alibaba-cloud-market-mirror-images.md) |
| 社区镜像 | 社区镜像是一种完全公开的镜像。您可以将制作好的自定义镜像发布为社区镜像供他人使用，也可以获取并使用他人发布的社区镜像。 | [社区镜像](products/ecs/documents/user-guide/overview-12.md) |


您也可以通过镜像全局搜索更精细地查找和筛选目标镜像，单击时会弹出镜像目录对话框，在镜像目录中查找所需镜像来创建ECS实例。更多信息，请参见[镜像目录](products/ecs/documents/user-guide/image-catalog.md)。

说明

创建ECS实例时可能因为镜像与实例规格的特性不匹配、镜像与实例规格处理器不兼容等问题看不到某些镜像（包括自定义镜像），处理建议请参见[为什么创建](products/ecs/documents/why-am-i-unable-to-see-my-custom-images-when-i-create-ecs-instances.md)[ECS](products/ecs/documents/why-am-i-unable-to-see-my-custom-images-when-i-create-ecs-instances.md)[实例时看不到某些镜像？](products/ecs/documents/why-am-i-unable-to-see-my-custom-images-when-i-create-ecs-instances.md)

### 存储

实例通过添加系统盘、数据盘、弹性临时盘和文件存储NAS获得存储能力，云服务器ECS提供了云盘和本地盘，以满足不同场景的需求。

- 

云盘可以用作系统盘和数据盘，包括ESSD云盘、SSD云盘、高效云盘等类型。更多信息，请参见[云盘概述](products/ecs/documents/user-guide/disks-2.md)。

说明

随实例一起创建的云盘和实例的付费模式相同。

- 

本地盘只能用作数据盘，如果实例规格配备了本地盘（例如本地SSD型、大数据型等），页面中会显示本地盘的信息。更多信息，请参见[本地盘](products/ecs/documents/user-guide/local-disks.md)。

说明

不支持自行为实例挂载本地盘。

系统盘

系统盘用于安装操作系统，默认容量为40 GiB，但实际可设置的最低容量和镜像类型有关，如下表所示。

| 镜像 | 系统盘容量范围（GiB） |
| --- | --- |
| Linux（不包括 FreeBSD 和 Red Hat） | [max{20, 镜像文件大小}, 2048] |
| FreeBSD | [max{30, 镜像文件大小}, 2048] |
| Red Hat | [max{40, 镜像文件大小}, 2048] |
| Windows | [max{40, 镜像文件大小}, 2048] |


（可选）数据盘

数据盘用于存储应用数据，选择数据盘时，您还可以加密云盘满足数据安全或法规合规等场景的要求。关于数据加密的介绍，请参见[加密云盘](products/ecs/documents/user-guide/encryption-overview.md)。

说明

单台实例支持挂载的数据盘存在数量限制。更多信息，请参见[块存储使用限制](products/ecs/documents/user-guide/limitations.md)。

（可选）快照服务

快照是云盘在某一时间点数据状态的备份文件，用快照创建云盘便于快速导入数据。创建实例时即可为云盘开启自动备份，有效应对数据误删等风险。

选择已有的自动快照策略，或者单击创建自动快照策略前往快照页面即时创建自动快照策略。具体操作，请参见[创建自动快照策略](products/ecs/documents/user-guide/create-an-automatic-snapshot-policy-1.md)。创建完成后，返回ECS实例创建向导并单击图标，查看自动快照策略列表。

重要

使用快照会产生费用，更多详情，请参见[快照计费](products/ecs/documents/snapshots-1.md)。

（可选）弹性临时盘

弹性临时盘是一款可灵活随实例创建或单独创建的、您可以自定义选择容量大小的块存储设备，作为临时数据存储使用，为ECS实例提供临时数据存储，具备高性能、高性价比等特点。更多信息，请参见[弹性临时盘](products/ecs/documents/user-guide/elastic-ephemeral-disks.md)。

（可选）文件存储NAS

如果您有较多数据需要供多台实例共享访问，推荐使用NAS文件系统，可以节约大量拷贝与同步成本。

选择已有的NAS文件系统，或者单击创建文件系统前往NAS文件系统控制台即时创建NAS文件系统。具体操作，请参见[通过控制台创建通用型](https://help.aliyun.com/zh/nas/user-guide/create-a-file-system#section-5jo-0kj-jn5)[NAS](https://help.aliyun.com/zh/nas/user-guide/create-a-file-system#section-5jo-0kj-jn5)[文件系统](https://help.aliyun.com/zh/nas/user-guide/create-a-file-system#section-5jo-0kj-jn5)。创建完成后，返回ECS实例创建向导并单击图标，查看NAS文件系统列表。关于挂载NAS文件系统时的注意事项，请参见[新购](https://help.aliyun.com/zh/nas/use-cases/mount-nas-file-systems-when-you-purchase-an-ecs-instance#task-2480876)[ECS](https://help.aliyun.com/zh/nas/use-cases/mount-nas-file-systems-when-you-purchase-an-ecs-instance#task-2480876)[时挂载](https://help.aliyun.com/zh/nas/use-cases/mount-nas-file-systems-when-you-purchase-an-ecs-instance#task-2480876)[NAS](https://help.aliyun.com/zh/nas/use-cases/mount-nas-file-systems-when-you-purchase-an-ecs-instance#task-2480876)[文件系统](https://help.aliyun.com/zh/nas/use-cases/mount-nas-file-systems-when-you-purchase-an-ecs-instance#task-2480876)。

### 带宽和安全组

网络和安全组配置提供了公网以及与其他阿里云资源通信的能力，并保障实例在网络中的安全。

（可选）公网IP

如果实例需要进行公网通信，必须分配公网IP。您可以在创建实例时选择自动分配一个固定公网IP，或者在创建实例后自行配置，通过EIP、NAT网关等方式进行公网通信。EIP、NAT网关需要自行购买，更多信息，请参见[什么是弹性公网](https://help.aliyun.com/zh/eip/product-overview/what-is-eip#concept-zmv-hd3-vdb)[IP](https://help.aliyun.com/zh/eip/product-overview/what-is-eip#concept-zmv-hd3-vdb)和[什么是 NAT 网关](https://help.aliyun.com/zh/nat-gateway/product-overview/what-is-nat-gateway#concept-wpm-kfy-ydb)。

选中分配公网 IPv4 地址，设置带宽计费模式和带宽值或带宽峰值。

关于公网带宽计费的详细规则，请参见[公网带宽计费](products/ecs/documents/public-bandwidth.md)。

- 

- 

- 

- 

- 

- 

- 

| 带宽计费模式 | 说明 |
| --- | --- |
| 按固定带宽 | 按指定的带宽值收费 ，实际的出网带宽不会高于指定的带宽值。 适用于对网络带宽要求比较稳定的业务场景。 如果云服务器使用率较高，需长时间使用带宽，或带宽利用率高于 10%，建议选择按固定带宽计费。 |
| 按使用流量 | 按实际产生的网络带宽流量收费 。为避免产生高额的带宽流量费，可先设置出网带宽峰值。 适用于对网络带宽需求变化较大的业务场景。 如果公网带宽利用率不高于 10%，平时没什么流量，在某个高峰时段流量波动较大，建议选择按使用流量计费。 （可选）： 选中 升级至 CDT 计费 。CDT 以灵活计费、提供免费流量、阶梯价格优惠及多产品统一计费等优势，为公网带宽费用管理提供高效经济的解决方案。相对于按量付费，有一定的折扣优惠。更多信息，请参见 [什么是云数据传输](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt) [CDT](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt) 。 重要 自 2024 年 12 月 12 日 0 时起，您无需额外操作即可直接使用云数据传输（CDT），享受高效服务。 升级为 CDT 计费后，所有存量和新增的按流量计费实例将通过 CDT 统一计费和出账，按带宽计费的实例继续在原来的云产品上统计费用和出账。您可以前往费用与成本，在账单详情页面查看 CDT 的账单情况。 开通 CDT 即可获得 220 GB/月公网流量免费额度， 其中 20 GB/月可用于 中国内地地域 ，200 GB/月可用于 非中国内地地域 。 |


安全组

安全组是一种虚拟防火墙，用于控制安全组内实例的入流量和出流量。更多信息，请参见[安全组概述](products/ecs/documents/user-guide/overview-44.md)。

当选择的VPC下没有安全组时，系统会自动创建默认安全组。默认安全组入方向放行22端口、3389端口及ICMP协议，您也可以根据需求，放行80、443端口，或者在创建完成后修改安全组配置。

您也可以根据业务需要，选择已有安全组或新建安全组，新建安全组时，需配置安全组名称、安全组类型、开通IPv4端口/协议。

说明

关于安全组各项配置的详细说明，请参见[创建安全组](products/ecs/documents/user-guide/create-a-security-group-1.md)。

（可选）弹性网卡

弹性网卡分为主网卡和辅助网卡。主网卡不支持从实例解绑，只能随实例一起创建和释放。辅助网卡支持自由绑定至实例和从实例解绑，方便您在实例之间切换网络流量。如需随实例一起创建辅助网卡，请单击图标，然后选择辅助网卡所属的交换机。

说明

创建实例时只能添加1块辅助网卡，您也可以在实例创建完成后单独创建辅助网卡并绑定至实例。关于各实例规格支持绑定的弹性网卡的数量，请参见[实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)。

（可选）配置IPv6

开通了IPv6后，IPv6的地址数量不仅能解决网络地址资源数量的问题，而且也解决了多种接入设备连入互联网的障碍。

选中免费分配 IPv6 地址。分配IPv6地址后，您需要登录实例并在操作系统内部进行IPv6地址相关的配置，才能正常使用IPv6地址。具体操作，请参见[IPv6](products/ecs/documents/user-guide/step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](products/ecs/documents/user-guide/step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。

### 管理设置

管理设置包括登录凭证和标签，用于远程连接实例和方便地检索和管理资源。

登录凭证

登录凭证用于安全地登录实例，关于实例连接方式的介绍，请参见[选择](products/ecs/documents/user-guide/connect-to-instance.md)[ECS](products/ecs/documents/user-guide/connect-to-instance.md)[远程连接方式](products/ecs/documents/user-guide/connect-to-instance.md)。

- 

- 

| 登录凭证 | 说明 |
| --- | --- |
| 密钥对 说明 仅 Linux 实例支持使用密钥对登录认证。 | 选择登录实例的用户名和已有的密钥对，或者单击 创建密钥对 即时创建密钥对。创建完成后，返回 ECS 实例创建向导并单击 图标，查看密钥对列表。具体操作，请参见 [创建](products/ecs/documents/user-guide/create-an-ssh-key-pair.md) [SSH](products/ecs/documents/user-guide/create-an-ssh-key-pair.md) [密钥对](products/ecs/documents/user-guide/create-an-ssh-key-pair.md) 。 用户名支持设置为 root 或 ecs-user 。 警告 root 具有操作系统的最高权限，使用 root 作为用户名可能会导致安全风险，建议您使用普通用户 ecs-user 作为用户名。 |
| 使用镜像预设密码 说明 仅 自定义镜像 和 共享镜像 支持此认证方式。 | 可以直接使用所选镜像的预设密码进行登录认证。为了保证您的正常使用，请确保所选镜像中已经设置了密码。 |
| 自定义密码 | 输入并确认密码。使用登录名和密码登录实例时，用户名信息如下： Linux 实例：支持设置为 root 或 ecs-user 。 警告 root 具有操作系统的最高权限，使用 root 作为用户名可能会导致安全风险，建议您使用普通用户 ecs-user 作为用户名。 Windows 实例：默认为 administrator 。 |
| 创建后设置 | 在实例创建完成后，自行绑定密钥对或者重置实例密码。具体操作，请参见 [绑定](products/ecs/documents/user-guide/bind-an-ssh-key-pair-to-an-instance.md) [SSH](products/ecs/documents/user-guide/bind-an-ssh-key-pair-to-an-instance.md) [密钥对](products/ecs/documents/user-guide/bind-an-ssh-key-pair-to-an-instance.md) 和 [重置实例登录密码](products/ecs/documents/user-guide/reset-the-logon-password-of-an-instance.md) 。 |


（可选）标签

标签由一对键值（Key-Value）组成，用来标识创建的实例、云盘、弹性网卡主网卡，便于检索和管理资源。可选择已有的标签，或者填写标签键和标签值即时创建标签。关于标签的更多信息，请参见[标签](products/ecs/documents/user-guide/label-overview.md)。

### （可选）高级选项

高级选项包括主机名、实例元数据、实例自定义数据等，用于定制实例在控制台和操作系统内显示的信息或使用方式。

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 实例名称 、 描述 、 主机名 、 有序后缀 | 创建多台实例时，设置有序的实例名称和主机名称便于从名称了解实例的批次等信息。关于设置有序名称的规则，请参见 [批量设置有序的实例名称或主机名称](products/ecs/documents/user-guide/batch-configure-sequential-names-or-hostnames-for-multiple-instances.md) 。 |
| 实例 RAM 角色 | 实例通过实例 RAM 角色获得该角色拥有的权限，可以基于临时安全令牌 STS（Security Token Service）访问指定云服务的 API 和操作指定的云资源，安全性更高。 选择已有的实例 RAM 角色，或者单击 创建实例 RAM 角色 前往 RAM 控制台即时创建实例 RAM 角色。创建完成后，返回 ECS 实例创建向导并单击 图标，查看实例 RAM 角色列表。具体操作，请参见 [创建实例](products/ecs/documents/user-guide/attach-an-instance-ram-role-to-an-ecs-instance.md) [RAM](products/ecs/documents/user-guide/attach-an-instance-ram-role-to-an-ecs-instance.md) [角色并为角色授予权限](products/ecs/documents/user-guide/attach-an-instance-ram-role-to-an-ecs-instance.md) 。 |
| 元数据访问模式 | 实例元数据（metadata）包含了实例在阿里云系统中的信息，您可以在运行中的实例内方便地查看实例元数据，并基于实例元数据配置或管理实例。关于如何查看实例元数据，请参见 [实例元数据](products/ecs/documents/user-guide/view-instance-metadata.md) 。 |
| 自定义数据 | 实例自定义数据可以作为实例自定义脚本在启动实例时执行，实现自动化配置实例，或者仅作为普通数据传入实例。更多信息，请参见 [自定义实例初始化配置](products/ecs/documents/user-guide/customize-the-initialization-configuration-for-an-instance.md) 。 在输入框输入您准备的实例自定义数据。如果实例自定义数据已进行 Base64 编码，请选中 输入已采用 Base64 编码 。 |
| 资源组 | 资源组供您从业务角度管理跨地域、跨产品的资源，并支持针对资源组管理权限。更多信息，请参见 [资源组](products/ecs/documents/user-guide/resource-groups.md) 。 选择已有的资源组，或者单击 创建资源组 前往资源管理控制台即时创建资源组。创建完成后，返回 ECS 实例创建向导并单击 图标，查看资源组列表。具体操作，请参见 [创建资源组](https://help.aliyun.com/zh/resource-management/resource-group/user-guide/create-a-resource-group#task-xpl-kjm-4fb) 。 |
| 部署集 | 部署集支持高可用策略，部署集内实例会严格分散在不同的物理服务器上，保证业务的高可用性和底层容灾能力。 选择已有的部署集，或者单击 管理部署集 即时创建部署集。创建完成后，返回 ECS 实例创建向导并单击 图标，查看部署集列表。具体操作，请参见 [部署集](products/ecs/documents/user-guide/overview-43.md) 。 |
| 专有宿主机 | 专有宿主机是一台由单租户独享物理资源的云主机，具有满足严格的安全合规要求、允许自带许可证（BYOL）上云等优势。 选择已有的专有宿主机，或者单击 创建专有宿主机 即时创建专有宿主机。创建完成后，返回 ECS 实例创建向导并单击 图标，查看专有宿主机列表。具体操作，请参见 [创建](https://help.aliyun.com/zh/dedicated-host/getting-started/create-a-dedicated-host#task-fbz-5mn-tdb) [DDH](https://help.aliyun.com/zh/dedicated-host/getting-started/create-a-dedicated-host#task-fbz-5mn-tdb) 。 |
| 私有池类型 | 创建弹性保障或容量预定后，系统会自动生成私有池，预留特定属性特定数量的实例。从关联的私有池中创建这一类实例，可以提供资源确定性保障。更多信息，请参见 [资源管家概述](products/ecs/documents/user-guide/overview-29.md) 。 说明 弹性保障和容量预定仅支持为按量付费实例保障资源供应确定性。 开放 ：优先使用开放类型私有池的容量，如果开放类型私有池无可用容量，则尝试使用公共池的容量。 不使用 ：不使用任何私有池的容量。 指定 ：继续指定一个专用或开放类型私有池的 ID，使用其容量创建实例。如果该私有池没有可用容量，则创建失败。 |


## 后续步骤

- 

连接实例

支持通过多种方式连接实例，包括Workbench、VNC和第三方客户端工具。更多信息，请参见[选择](products/ecs/documents/user-guide/connect-to-instance.md)[ECS](products/ecs/documents/user-guide/connect-to-instance.md)[远程连接方式](products/ecs/documents/user-guide/connect-to-instance.md)。

- 

初始化数据盘

如果您随实例创建了数据盘，必须先对数据盘进行分区格式化才能正常使用。具体操作，请参见[初始化数据盘（Linux）](products/ecs/documents/user-guide/initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)和[初始化数据盘（Windows）](products/ecs/documents/user-guide/initialize-a-data-disk-up-to-2-tib-in-size-on-a-windows-instance.md)。

- 

部署环境、搭建网站、搭建应用

创建实例后，您可以使用ECS实例部署环境、搭建网站和应用等。更多信息，请参见[搭建环境](products/ecs/documents/user-guide/build-a-software-development-environment.md)、[搭建网站](products/ecs/documents/user-guide/build-a-website.md)、[搭建应用](products/ecs/documents/user-guide/build-an-application.md)。

## 相关文档

- 

[RunInstances](products/ecs/documents/api-runinstances.md)：创建一台或多台按量付费或者包年包月ECS实例。

- 

[实例](products/ecs/documents/user-guide/instance-faq.md)[FAQ](products/ecs/documents/user-guide/instance-faq.md)

- 

获取价格折扣信息

您可以调用[DescribePrice](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeprice.md)接口查询云服务器ECS资源的最新价格，例如活动规则、价格、折扣等信息。

CLI命令参考如下。例如，查询在华东1（杭州）地域创建一个实例规格为ecs.c6.xlarge的最新价格信息。

aliyun ecs DescribePrice --region cn-hangzhou --RegionId 'cn-hangzhou' --ResourceType instance --InstanceType 'ecs.c6.xlarge'

[上一篇：快速购买实例](products/ecs/documents/user-guide/create-a-subscription-instance-on-the-quick-launch-tab.md)[下一篇：使用自定义镜像或共享镜像创建实例](products/ecs/documents/user-guide/create-an-ecs-instance-by-using-a-custom-image.md)

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
