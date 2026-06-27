# 公共镜像类型、公共镜像的操作系统版本以及镜像族系-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/public-mirroring-overview

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

# 公共镜像概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

公共镜像是指阿里云官方提供的镜像，皆已正版授权，旨在为ECS实例上的应用程序提供安全、稳定的运行环境。本文介绍公共镜像类型、公共镜像的操作系统版本以及镜像族系。

## 公共镜像类型

阿里云提供以下两种类型的公共镜像。除了Windows Server（在中国香港及海外地域创建）、Red Hat Enterprise Linux、SUSE Linux Enterprise Server和Alibaba Cloud Linux 3 Pro之外，您可以免费使用其他公共镜像创建ECS实例。费用详情，请参见[镜像计费](products/ecs/documents/images.md)。

- 

- 

- 

- 

| 公共镜像类型 | 描述 | 技术支持 |
| --- | --- | --- |
| [Alibaba Cloud Linux](products/ecs/documents/user-guide/public-mirroring-overview.md) [镜像](products/ecs/documents/user-guide/public-mirroring-overview.md) | 阿里云针对 ECS 实例提供的定制化原生操作系统镜像。Alibaba Cloud Linux 镜像均经过严格测试，确保镜像安全、稳定，保证您能够正常启动和使用镜像。 | 阿里云将为您在使用 Alibaba Cloud Linux 操作系统过程中遇到的问题提供技术支持。 |
| [第三方及开源公共镜像](products/ecs/documents/user-guide/public-mirroring-overview.md) | 由阿里云测试发布，确保镜像安全、稳定。第三方公共镜像包括： Windows 系统：Windows Server Linux 系统：龙蜥（Anolis）OS、Ubuntu、CentOS、CentOS Stream、Redhat Enterprise Linux、Debian、OpenSUSE、SUSE Linux Enterprise Server、FreeBSD、CoreOS、Fedora CoreOS、Fedora、Rocky Linux 和 AlmaLinux 等 | 对于开源操作系统镜像，建议联系开源社区获得技术支持，同时阿里云提供相应的技术协助。 对于商业版镜像，阿里云提供许可证并联合操作系统原厂提供技术支持。 |


说明

- 

以上技术支持的前提条件是镜像在生命周期之内，如果操作系统版本结束了生命周期（EOL），则参照EOL镜像的支持策略。更多信息，请参见[操作系统生命周期概述](products/ecs/documents/user-guide/eol-overview.md)。

- 

针对各个操作系统的新特性、安全补丁等，阿里云会定期更新公共镜像的版本，详情请参见[公共镜像发布记录](products/ecs/documents/user-guide/release-notes-for-2023.md)。您在ECS购买页面选中某个公共镜像时，默认为最近更新的版本。如果您希望购买到较旧的版本，可以通过调用OpenAPI[RunInstances](products/ecs/documents/api-runinstances.md)指定镜像ID来实现。

- 

阿里云会定时从开源社区官方或者操作系统原厂同步至[阿里云镜像站](https://developer.aliyun.com/mirror/)，您可以按需更新新特性、安全补丁等。

- 

安全性是阿里云和客户的共同责任。阿里云负责云平台自身的安全，包括云平台硬件、软件和网络安全。客户负责ECS实例的安全，包括ECS操作系统的管理（包括安装更新和安全补丁）、在ECS上安装的任何应用程序软件或工具，以及阿里云提供的安全组防火墙的配置。更多信息，请参见[云服务器](products/ecs/documents/user-guide/best-security-practices.md)[ECS](products/ecs/documents/user-guide/best-security-practices.md)[安全性](products/ecs/documents/user-guide/best-security-practices.md)。

- 

如果操作系统EOL，阿里云可能会对该操作系统停止技术支持，并可能下线相关的公共镜像。此时无法使用镜像族系查询对应的公共镜像后创建ECS实例。建议您尽快将运行的工作负载迁移到替代的操作系统，以继续获取软件更新和安全补丁。更多信息，请参见[操作系统维护周期和](products/ecs/documents/user-guide/image-eol.md)[EOL](products/ecs/documents/user-guide/image-eol.md)[应对方案](products/ecs/documents/user-guide/image-eol.md)。

## Alibaba Cloud Linux镜像

Alibaba Cloud Linux 3、Alibaba Cloud Linux 3 Pro和Alibaba Cloud Linux 2是阿里云自主研发的Linux系统镜像，属于公共镜像。Alibaba Cloud Linux支持多种ECS实例规格，包括弹性裸金属服务器。Alibaba Cloud Linux中默认搭载了阿里云CLI及其他软件包，方便您使用。关于阿里云CLI的更多信息，请参见[什么是阿里云](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli#concept-rc3-qrc-bhb)[CLI](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli#concept-rc3-qrc-bhb)。如果您要从其他Linux版本更换为Alibaba Cloud Linux，可以通过创建新实例或更换操作系统（系统盘）的方式进行更换。更多信息，请参见[Alibaba Cloud Linux](products/ecs/documents/user-guide/alibaba-cloud-linux.md)。

- 

Alibaba Cloud Linux 3

| 操作系统版本 | 镜像族系 |
| --- | --- |
| Alibaba Cloud Linux 3.2104 LTS 64 位 | acs:alibaba_cloud_linux_3_2104_lts_x64 |
| Alibaba Cloud Linux 3.2104 64 位 | 无 |
| Alibaba Cloud Linux 3.2104 64 位 快速启动版 | 无 |
| Alibaba Cloud Linux 3.2104 LTS 64 位 等保 2.0 三级版 | acs:alibaba_cloud_linux_3_2104_lts_x64_dengbao2.0 |
| Alibaba Cloud Linux 3.2104 64 位 SCC 版 | 无 |
| Alibaba Cloud Linux 3.2104 64 位 ARM 版 | 无 |
| Alibaba Cloud Linux 3.2104 LTS 64 位 ARM 版 | acs:alibaba_cloud_linux_3_2104_lts_arm64 |
| Alibaba Cloud Linux 3.2104 64 位 UEFI 版 | 无 |
| Alibaba Cloud Linux 3.2104 LTS 64 位 UEFI 版 | acs:alibaba_cloud_linux_3_2104_lts_x64_uefi |
| Alibaba Cloud Linux 3.2104 LTS 64 位 SCC 版 | acs:alibaba_cloud_linux_3_2104_lts_x64_scc |
| Alibaba Cloud Linux 3.2104 LTS 64 位 快速启动版 | acs:alibaba_cloud_linux_3_2104_lts_x64_qboot |
| Alibaba Cloud Linux 3.2104 LTS 64 位 ARM 版 等保 2.0 三级版 | acs:alibaba_cloud_linux_3_2104_lts_arm64_dengbao2.0 |


- 

Alibaba Cloud Linux 3 Pro

| 操作系统版本 | 镜像族系 |
| --- | --- |
| Alibaba Cloud Linux 3 Pro 64 位 | acs:alibaba_cloud_linux_3_pro_x64 |


- 

Alibaba Cloud Linux 2

| 操作系统版本 | 镜像族系 |
| --- | --- |
| Alibaba Cloud Linux 2.1903 LTS 64 位 | acs:alibaba_cloud_linux_2_1903_lts_x64 |
| Alibaba Cloud Linux 2.1903 64 位 快速启动版 | 无 |
| Alibaba Cloud Linux 2.1903 LTS 64 位 等保 2.0 三级版 | acs:alibaba_cloud_linux_2_1903_lts_x64_dengbao2.0 |
| Alibaba Cloud Linux 2.1903 LTS 64 位 SCC 版 | acs:alibaba_cloud_linux_2_1903_lts_x64_scc |
| Alibaba Cloud Linux 2.1903 64 位 UEFI 版 | acs:alibaba_cloud_linux_2_1903_x64_uefi |
| Alibaba Cloud Linux 2.1903 64 位 可信版 | acs:alibaba_cloud_linux_2_1903_x64_trust |
| Alibaba Cloud Linux 2.1903 LTS 64 位 快速启动版 | acs:alibaba_cloud_linux_2_1903_lts_x64_qboot |
| Alibaba Cloud Linux 2.1903 LTS 64 位 AMD 版 | acs:alibaba_cloud_linux_2_1903_lts_x64_amd |
| Alibaba Cloud Linux 2.1903 LTS 64 位 UEFI 版 | acs:alibaba_cloud_linux_2_1903_lts_x64_uefi |


说明

Alibaba Cloud Linux 2已于2024年03月31日停止维护（EOL），并为用户提供延保服务至2026年03月31日。延保结束后，Alibaba Cloud Linux将停止对Alibaba Cloud Linux 2的技术支持，建议您尽快将Alibaba Cloud Linux 2上运行的工作负载迁移到替代的操作系统，以继续获取软件更新和安全补丁。更多信息，请参见[Alibaba Cloud Linux](products/ecs/documents/user-guide/solution-for-alibaba-cloud-linux-2-entering-the-els-phase.md)[操作系统](products/ecs/documents/user-guide/solution-for-alibaba-cloud-linux-2-entering-the-els-phase.md)。

## 第三方及开源公共镜像

阿里云会定期发布或更新公共镜像，请前往[公共镜像发布记录](products/ecs/documents/release-notes-2.md)页面查看详情。您也可以在ECS管理控制台相应地域的[公共镜像列表页](https://ecs.console.aliyun.com/#image/region/cn-hangzhou/systemImageList)查看或查找可用的公共镜像。具体操作，请参见[查找镜像](products/ecs/documents/user-guide/find-an-image.md)。

阿里云提供的第三方商业镜像及开源公共镜像，如下表所示。

- 

Windows系统镜像

| 操作系统版本 | 镜像族系 |
| --- | --- |
| Windows Server 2025 数据中心版 64 位中文版 | acs:win_2025_datacenter_x64_zh |
| Windows Server 2025 数据中心版 64 位英文版 | acs:win_2025_datacenter_x64_en |
| Windows Server 2025 数据中心版 64 位中文 UEFI 版 | acs:win_2025_datacenter_x64_zh_uefi |
| Windows Server 2025 数据中心版 64 位英文 UEFI 版 | 无 |
| Windows Server 2025 数据中心版 64 位中文版（不含图形化界面） | 无 |
| Windows Server 2025 数据中心版 64 位英文版（不含图形化界面） | 无 |
| Windows Server 2022 数据中心版 64 位中文版 | acs:win_2022_datacenter_x64_zh |
| Windows Server 2022 数据中心版 64 位英文版 | acs:win_2022_datacenter_x64_en |
| Windows Server 2022 数据中心版 64 位中文版（不含图形化桌面） | acs:win_2022_datacenter_x64_zh_without_ui |
| Windows Server 2022 数据中心版 64 位英文版（不含图形化桌面） | acs:win_2022_datacenter_x64_en_without_ui |
| Windows Server 2022 with Container 数据中心版 64 位英文版 | acs:win_2022_container_datacenter_x64_en |
| Windows Server 2022 with Container 数据中心版 64 位中文版 | acs:win_2022_container_datacenter_x64_zh |
| Windows Server Version 2022 with Container 数据中心版 64 位中文版（不含图形化桌面） | acs:win_2022_container_datacenter_x64_zh_without_ui |
| Windows Server Version 2022 with Container 数据中心版 64 位英文版（不含图形化桌面） | acs:win_2022_container_datacenter_x64_en_without_ui |
| Windows Server 2022 数据中心版 64 位中文 UEFI 版 | acs:win_2022_datacenter_x64_zh_uefi |
| Windows Server 2022 数据中心版 64 位英文 UEFI 版 | acs:win_2022_datacenter_x64_en_uefi |
| Windows Server 2019 with Container 数据中心版 64 位中文版 | acs:win_2019_container_datacenter_x64_zh |
| Windows Server 2019 with Container 数据中心版 64 位英文版 | acs:win_2019_container_datacenter_x64_en |
| Windows Server 2019 数据中心版 64 位中文版 | acs:win_2019_datacenter_x64_zh |
| Windows Server 2019 数据中心版 64 位英文版 | acs:win_2019_datacenter_x64_en |
| Windows Server 2016 数据中心版 64 位中文版 | acs:win_2016_datacenter_x64_zh |
| Windows Server 2016 数据中心版 64 位英文版 | acs:win_2016_datacenter_x64_en |
| Windows Server 2012 R2 数据中心版 64 位中文版 | acs:win_2012_r2_datacenter_x64_zh |
| Windows Server 2012 R2 数据中心版 64 位英文版 | acs:win_2012_r2_datacenter_x64_en |
| Windows Server 2008 R2 企业版 64 位中文版 | acs:win_2008_r2_enterprise_x64_zh |
| Windows Server 2008 R2 企业版 64 位英文版 | acs:win_2008_r2_enterprise_x64_en |
| Windows Server Version 2004 数据中心版 64 位中文版（不含图形化桌面） | acs:win_2004_datacenter_x64_zh_without_ui |
| Windows Server Version 2004 数据中心版 64 位英文版（不含图形化桌面） | acs:win_2004_datacenter_x64_en_without_ui |
| Windows Server Version 2004 with Container 数据中心版 64 位中文版（不含图形化桌面） | acs:win_2004_container_datacenter_x64_zh_without_ui |
| Windows Server Version 2004 with Container 数据中心版 64 位英文版（不含图形化桌面） | acs:win_2004_container_datacenter_x64_en_without_ui |


说明

微软已经于2020年01月14日停止对Windows Server 2008/2008 R2操作系统提供支持，于2023年10月10日停止对Windows Server 2012/2012 R2操作系统提供支持。因此，阿里云不再对使用上述操作系统的ECS实例提供技术支持。如果您有使用上述操作系统的ECS实例，建议您尽快更新至Windows Server 2016或更高版本。更多信息，请参见[Windows Server](products/ecs/documents/user-guide/windows-server-eol-guide.md)[操作系统](products/ecs/documents/user-guide/windows-server-eol-guide.md)。

- 

Linux系统镜像

- 

Anolis OS

| 操作系统版本 | 镜像族系 |
| --- | --- |
| Anolis OS 8.10 ANCK 64 位 | acs:anolis_8_10_anck_x64 |
| Anolis OS 8.10 RHCK 64 位 | acs:anolis_8_10_rhck_x64 |
| Anolis OS 8.10 ANCK 64 位 ARM 版 | acs:anolis_8_10_anck_arm64 |
| Anolis OS 8.10 RHCK 64 位 ARM 版 | acs:anolis_8_10_rhck_arm64 |
| Anolis OS 8.9 ANCK 64 位 | acs:anolis_8_9_anck_x64 |
| Anolis OS 8.9 RHCK 64 位 | acs:anolis_8_9_rhck_x64 |
| Anolis OS 8.9 ANCK 64 位 ARM 版 | acs:anolis_8_9_anck_arm64 |
| Anolis OS 8.9 RHCK 64 位 ARM 版 | acs:anolis_8_9_rhck_arm64 |
| Anolis OS 8.8 ANCK 64 位 | acs:anolis_8_8_anck_x64 |
| Anolis OS 8.8 RHCK 64 位 | acs:anolis_8_8_rhck_x64 |
| Anolis OS 8.8 ANCK 64 位 ARM 版 | acs:anolis_8_8_anck_arm64 |
| Anolis OS 8.8 RHCK 64 位 ARM 版 | acs:anolis_8_8_rhck_arm64 |
| Anolis OS 8.8 ANCK 64 位 UEFI 版 | acs:anolis_8_8_anck_x64_uefi |
| Anolis OS 8.8 RHCK 64 位 UEFI 版 | acs:anolis_8_8_rhck_x64_uefi |
| Anolis OS 8.8 ANCK 64 位 等保 2.0 三级版 | acs:anolis_8_8_anck_x64_dengbao2.0 |
| Anolis OS 8.8 ANCK 64 位 ARM 版 等保 2.0 三级版 | acs:anolis_8_8_anck_arm64_dengbao2.0 |
| Anolis OS 8.6 ANCK 64 位 | acs:anolis_8_6_anck_x64 |
| Anolis OS 8.6 RHCK 64 位 | acs:anolis_8_6_rhck_x64 |
| Anolis OS 8.6 ANCK 64 位 ARM 版 | acs:anolis_8_6_anck_arm64 |
| Anolis OS 8.6 RHCK 64 位 ARM 版 | acs:anolis_8_6_rhck_arm64 |
| Anolis OS 8.6 ANCK 64 位 UEFI 版 | acs:anolis_8_6_anck_x64_uefi |
| Anolis OS 8.6 RHCK 64 位 UEFI 版 | acs:anolis_8_6_rhck_x64_uefi |
| Anolis OS 8.4 ANCK 64 位 | acs:anolis_8_4_anck_x64 |
| Anolis OS 8.4 RHCK 64 位 | acs:anolis_8_4_rhck_x64 |
| Anolis OS 8.4 ANCK 64 位 ARM 版 | acs:anolis_8_4_anck_arm64 |
| Anolis OS 8.4 RHCK 64 位 ARM 版 | acs:anolis_8_4_rhck_arm64 |
| Anolis OS 8.4 ANCK 64 位 UEFI 版 | acs:anolis_8_4_anck_x64_uefi |
| Anolis OS 8.4 RHCK 64 位 UEFI 版 | acs:anolis_8_4_rhck_x64_uefi |
| Anolis OS 8.2 ANCK 64 位 | acs:anolis_8_2_anck_x64 |
| Anolis OS 8.2 RHCK 64 位 | acs:anolis_8_2_rhck_x64 |
| Anolis OS 8.2 ANCK 64 位 ARM 版 | acs:anolis_8_2_anck_arm64 |
| Anolis OS 8.2 RHCK 64 位 ARM 版 | acs:anolis_8_2_rhck_arm64 |
| Anolis OS 7.9 ANCK 64 位 | acs:anolis_7_9_anck_x64 |
| Anolis OS 7.9 RHCK 64 位 | acs:anolis_7_9_rhck_x64 |
| Anolis OS 7.9 ANCK 64 位 ARM 版 | acs:anolis_7_9_anck_arm64 |
| Anolis OS 7.9 RHCK 64 位 ARM 版 | acs:anolis_7_9_rhck_arm64 |
| Anolis OS 7.9 ANCK 64 位 UEFI 版 | acs:anolis_7_9_anck_x64_uefi |
| Anolis OS 7.9 RHCK 64 位 UEFI 版 | acs:anolis_7_9_rhck_x64_uefi |
| Anolis OS 7.7 ANCK 64 位 | acs:anolis_7_7_anck_x64 |
| Anolis OS 7.7 RHCK 64 位 | acs:anolis_7_7_rhck_x64 |
| Anolis OS 7.7 ANCK 64 位 ARM 版 | acs:anolis_7_7_anck_arm64 |
| Anolis OS 7.7 RHCK 64 位 ARM 版 | acs:anolis_7_7_rhck_arm64 |


- 

CentOS

| 操作系统版本 | 镜像族系 |
| --- | --- |
| CentOS 8.5 64 位 | acs:centos_8_5_x64 |
| CentOS 8.5 64 位 UEFI 版 | acs:centos_8_5_x64_uefi |
| CentOS 8.4 64 位 | acs:centos_8_4_x64 |
| CentOS 8.4 64 位 UEFI 版 | acs:centos_8_4_x64_uefi |
| CentOS 8.4 64 位 ARM 版 | acs:centos_8_4_arm64 |
| CentOS 8.4 64 位 SCC 版 | 无 |
| CentOS 8.3 64 位 | acs:centos_8_3_x64 |
| CentOS 8.3 64 位 UEFI 版 | acs:centos_8_3_x64_uefi |
| CentOS 8.3 64 位 ARM 版 | acs:centos_8_3_arm64 |
| CentOS 8.3 64 位 SCC 版 | 无 |
| CentOS 8.2 64 位 | acs:centos_8_2_x64 |
| CentOS 8.2 64 位 ARM 版 | acs:centos_8_2_arm64 |
| CentOS 8.2 64 位 AMD 版 | acs:centos_8_2_x64_amd |
| CentOS 8.1 64 位 | acs:centos_8_1_x64 |
| CentOS 8.0 64 位 | acs:centos_8_0_x64 |
| CentOS 7.9 64 位 | acs:centos_7_9_x64 |
| CentOS 7.9 64 位 UEFI 版 | acs:centos_7_9_x64_uefi |
| CentOS 7.9 64 位 ARM 版 | acs:centos_7_9_arm64 |
| CentOS 7.9 64 位 SCC 版 | 无 |
| CentOS 7.8 64 位 | acs:centos_7_8_x64 |
| CentOS 7.8 64 位 可信版 | acs:centos_7_8_x64_trust |
| CentOS 7.8 64 位 AMD 版 | acs:centos_7_8_x64_amd |
| CentOS 7.7 64 位 | acs:centos_7_7_x64 |
| CentOS 7.6 64 位 | acs:centos_7_6_x64 |
| CentOS 7.5 64 位 | acs:centos_7_5_x64 |
| CentOS 7.5 64 位 SCC 版 | acs:centos_7_5_x64_scc |
| CentOS 7.4 64 位 | acs:centos_7_4_x64 |
| CentOS 7.3 64 位 | acs:centos_7_3_x64 |
| CentOS 7.2 64 位 | acs:centos_7_2_x64 |
| CentOS 6.10 64 位 | acs:centos_6_10_x64 |
| CentOS 6.9 64 位 | acs:centos_6_9_x64 |
| CentOS 6.8 32 位 | acs:centos_6_8_x86 |


说明

- 

CentOS官方已计划停止维护CentOS Linux项目，阿里云上CentOS Linux公共镜像来源于CentOS官方，当CentOS Linux停止维护后，阿里云将会同时停止对该操作系统的支持。具体应对措施，请参见[CentOS](products/ecs/documents/user-guide/options-for-dealing-with-centos-linux-end-of-life.md)[操作系统](products/ecs/documents/user-guide/options-for-dealing-with-centos-linux-end-of-life.md)。

- 

CentOS 6操作系统版本结束了生命周期（EOL），按照社区规则，CentOS 6的源地址http://mirror.centos.org/centos-6/内容已移除，您在阿里云上继续使用默认配置的CentOS 6的源会发生报错。如果您需要使用CentOS 6系统中的一些安装包，则需要手动切换源地址。具体操作，请参见[CentOS 6 EOL](products/ecs/documents/user-guide/change-the-centos-6-source-address.md)[如何切换源？](products/ecs/documents/user-guide/change-the-centos-6-source-address.md)。

- 

使用32位操作系统，请选择内存小于或等于4 GiB的实例规格。更多信息，请参见[选择镜像的操作系统](products/ecs/documents/user-guide/select-an-image.md)。

- 

CentOS Stream

| 操作系统版本 | 镜像族系 |
| --- | --- |
| CentOS Stream 9 64 位 | acs:centos_stream_9_x64 |
| CentOS Stream 9 64 位 UEFI 版 | acs:centos_stream_9_x64_uefi |
| CentOS Stream 9 64 位 ARM 版 | acs:centos_stream_9_arm64 |
| CentOS Stream 8 64 位 | acs:centos_stream_8_x64 |
| CentOS Stream 8 64 位 UEFI 版 | acs:centos_stream_8_x64_uefi |
| CentOS Stream 8 64 位 ARM 版 | acs:centos_stream_8_arm64 |


- 

CoreOS

| 操作系统版本 | 镜像族系 |
| --- | --- |
| CoreOS 2345.3.0 64 位 | 无 |
| CoreOS 2303.4.0 64 位 | 无 |
| CoreOS 2303.3.0 64 位 | 无 |
| CoreOS 2247.6.0 64 位 | 无 |
| CoreOS 2023.4.0 64 位 | 无 |
| CoreOS 1745.7.0 64 位 | 无 |


说明

根据Fedora CoreOS社区的公告，CoreOS Container Linux已于2020年05月26日停止提供更新。因此阿里云做出以下说明：

- 

自2020年05月26日起，阿里云将不再为CoreOS Container Linux提供技术协助，但不影响您已安装该操作系统的ECS实例的继续使用。

- 

在2020年09月30日之后，您将无法使用阿里云提供的CoreOS Container Linux公共镜像创建新的ECS实例。

- 

已安装的CoreOS Container Linux在2020年05月26日后仍可继续使用，但是由于该操作系统已经结束生命周期，不会继续提供安全补丁。出于安全因素的考虑，阿里云不推荐您继续使用CoreOS Container Linux镜像。

- 

阿里云已上线Fedora CoreOS公共镜像，Fedora CoreOS社区推荐使用Fedora CoreOS操作系统替代CoreOS Container Linux。

- 

Debian

| 操作系统版本 | 镜像族系 |
| --- | --- |
| Debian 12.11 ARM 版 | acs:debian_12_11_arm64 |
| Debian 12.11 | acs:debian_12_11_x64 |
| Debian 12.10 ARM 版 | acs:debian_12_10_arm64 |
| Debian 12.10 | acs:debian_12_10_x64 |
| Debian 12.9 ARM 版 | acs:debian_12_9_arm64 |
| Debian 12.9 | acs:debian_12_9_x64 |
| Debian 12.8 64 位 | acs:debian_12_8_x64 |
| Debian 12.7 64 位 | acs:debian_12_7_x64 |
| Debian 12.7 ARM 版 | acs:debian_12_7_arm64 |
| Debian 12.6 64 位 | acs:debian_12_6_x64 |
| Debian 12.5 64 位 | acs:debian_12_5_x64 |
| Debian 12.4 64 位 | acs:debian_12_4_x64 |
| Debian 12.4 64 位 ARM 版 | acs:debian_12_4_arm64 |
| Debian 12.2 64 位 | acs:debian_12_2_x64 |
| Debian 12.2 64 位 UEFI 版 | acs:debian_12_2_x64_uefi |
| Debian 11.11 64 位 | acs:debian_11_11_x64 |
| Debian 11.11 64 位 ARM 版 | acs:debian_11_11_arm64 |
| Debian 11.10 64 位 | acs:debian_11_10_x64 |
| Debian 11.9 64 位 | acs:debian_11_9_x64 |
| Debian 11.8 64 位 | acs:debian_11_8_x64 |
| Debian 11.7 64 位 | acs:debian_11_7_x64 |
| Debian 11.6 64 位 | acs:debian_11_6_x64 |
| Debian 11.6 64 位 UEFI 版 | acs:debian_11_6_x64_uefi |
| Debian 11.5 64 位 | acs:debian_11_5_x64 |
| Debian 11.5 64 位 ARM 版 | acs:debian_11_5_arm64 |
| Debian 11.4 64 位 | acs:debian_11_4_x64 |
| Debian 11.3 64 位 | acs:debian_11_3_x64 |
| Debian 11.2 64 位 | acs:debian_11_2_x64 |
| Debian 11.2 64 位 ARM 版 | acs:debian_11_2_arm64 |
| Debian 11.1 64 位 | acs:debian_11_1_x64 |
| Debian 11.0 64 位 | acs:debian_11_0_x64 |
| Debian 10.13 64 位 | acs:debian_10_13_x64 |
| Debian 10.13 64 位 ARM 版 | acs:debian_10_13_arm64 |
| Debian 10.12 64 位 | acs:debian_10_12_x64 |
| Debian 10.12 64 位 UEFI 版 | acs:debian_10_12_x64_uefi |
| Debian 10.11 64 位 | acs:debian_10_11_x64 |
| Debian 10.10 64 位 | acs:debian_10_10_x64 |
| Debian 10.10 64 位 UEFI 版 | acs:debian_10_10_x64_uefi |
| Debian 10.9 64 位 | acs:debian_10_9_x64 |
| Debian 10.9 64 位 ARM 版 | acs:debian_10_9_arm64 |
| Debian 10.7 64 位 | acs:debian_10_7_x64 |
| Debian 10.7 64 位 AMD 版 | acs:debian_10_7_x64_amd |
| Debian 10.6 64 位 | acs:debian_10_6_x64 |
| Debian 10.5 64 位 | acs:debian_10_5_x64 |
| Debian 10.4 64 位 | acs:debian_10_4_x64 |
| Debian 10.3 64 位 | acs:debian_10_3_x64 |
| Debian 10.2 64 位 | acs:debian_10_2_x64 |
| Debian 9.13 64 位 | acs:debian_9_13_x64 |
| Debian 9.13 64 位 UEFI 版 | acs:debian_9_13_x64_uefi |
| Debian 9.12 64 位 | acs:debian_9_12_x64 |
| Debian 9.11 64 位 | acs:debian_9_11_x64 |
| Debian 9.9 64 位 | acs:debian_9_9_x64 |
| Debian 9.8 64 位 | acs:debian_9_8_x64 |
| Debian 9.6 64 位 | acs:debian_9_6_x64 |
| Debian 8.11 64 位 | acs:debian_8_11_x64 |
| Debian 8.9 64 位 | acs:debian_8_9_x64 |


- 

FreeBSD

| 操作系统版本 | 镜像族系 |
| --- | --- |
| FreeBSD 14.1 64 位 | acs:freebsd_14_1_x64 |
| FreeBSD 13.4 64 位 | acs:freebsd_13_4_x64 |
| FreeBSD 13.0 64 位 | acs:freebsd_13_0_x64 |
| FreeBSD 12.3 64 位 | acs:freebsd_12_3_x64 |
| FreeBSD 12.1 64 位 | acs:freebsd_12_1_x64 |
| FreeBSD 11.4 64 位 | acs:freebsd_11_4_x64 |
| FreeBSD 11.3 64 位 | acs:freebsd_11_3_x64 |
| FreeBSD 11.2 64 位 | acs:freebsd_11_2_x64 |


- 

OpenSUSE

| 操作系统版本 | 镜像族系 |
| --- | --- |
| OpenSUSE 15.6 64 位 | acs:opensuse_15_6_x64 |
| OpenSUSE 15.5 64 位 | acs:opensuse_15_5_x64 |
| OpenSUSE 15.4 64 位 | acs:opensuse_15_4_x64 |
| OpenSUSE 15.3 64 位 | acs:opensuse_15_3_x64 |
| OpenSUSE 15.2 64 位 | acs:opensuse_15_2_x64 |
| OpenSUSE 15.1 64 位 | acs:opensuse_15_1_x64 |
| OpenSUSE 42.3 64 位 | acs:opensuse_42_3_x64 |


- 

Red Hat

说明

- 

您在购买ECS实例时，只有购买已通过Red Hat Enterprise Linux认证的实例规格，才能选择不同版本的Red Hat镜像。已通过Red Hat Enterprise Linux认证的规格信息，请参见[Red Hat](products/ecs/documents/instance-families-supported-by-red-hat-images.md)[镜像支持哪些实例规格族？](products/ecs/documents/instance-families-supported-by-red-hat-images.md)。

- 

在您选择不同的实例规格时，Red Hat Enterprise Linux的镜像价格不同。有关Red Hat Enterprise Linux镜像的价格信息，请参见[镜像计费](products/ecs/documents/images.md)。

| 操作系统版本 | 镜像族系 |
| --- | --- |
| Red Hat Enterprise Linux 9.5 64 位 ARM 版 | 无 |
| Red Hat Enterprise Linux 9.5 64 位 x86 | 无 |
| Red Hat Enterprise Linux 9.4 64 位 x86 | 无 |
| Red Hat Enterprise Linux 9.4 64 位 ARM 版 | 无 |
| Red Hat Enterprise Linux 9.3 64 位 | 无 |
| Red Hat Enterprise Linux 9.3 64 位 ARM 版 | 无 |
| Red Hat Enterprise Linux 9.2 64 位 | 无 |
| Red Hat Enterprise Linux 9.2 64 位 UEFI | 无 |
| Red Hat Enterprise Linux 9.2 64 位 ARM 版 | 无 |
| Red Hat Enterprise Linux 9.1 64 位 | 无 |
| Red Hat Enterprise Linux 9.1 64 位 ARM 版 | 无 |
| Red Hat Enterprise Linux 9.0 64 位 | 无 |
| Red Hat Enterprise Linux 8.10 64 位 | 无 |
| Red Hat Enterprise Linux 8.10 64 位 ARM 版 | 无 |
| Red Hat Enterprise Linux 8.9 64 位 | 无 |
| Red Hat Enterprise Linux 8.9 64 位 ARM 版 | 无 |
| Red Hat Enterprise Linux 8.8 64 位 | 无 |
| Red Hat Enterprise Linux 8.8 64 位 UEFI | 无 |
| Red Hat Enterprise Linux 8.8 64 位 ARM 版 | 无 |
| Red Hat Enterprise Linux 8.7 64 位 | 无 |
| Red Hat Enterprise Linux 8.7 64 位 ARM 版 | 无 |
| Red Hat Enterprise Linux 8.6 64 位 | 无 |
| Red Hat Enterprise Linux 8.5 64 位 | 无 |
| Red Hat Enterprise Linux 8.4 64 位 | 无 |
| Red Hat Enterprise Linux 8.3 64 位 | 无 |
| Red Hat Enterprise Linux 8.2 64 位 | 无 |
| Red Hat Enterprise Linux 8.1 64 位 | 无 |
| Red Hat Enterprise Linux 8.0 64 位 | 无 |
| Red Hat Enterprise Linux 7.9 64 位 | 无 |
| Red Hat Enterprise Linux 7.9 64 位 UEFI | 无 |
| Red Hat Enterprise Linux 7.8 64 位 | 无 |
| Red Hat Enterprise Linux 7.7 64 位 | 无 |
| Red Hat Enterprise Linux 7.6 64 位 | 无 |
| Red Hat Enterprise Linux 7.5 64 位 | 无 |
| Red Hat Enterprise Linux 7.4 64 位 | 无 |
| Red Hat Enterprise Linux 6.10 64 位 | 无 |
| Red Hat Enterprise Linux 6.9 64 位 | 无 |


- 

SUSE Linux

| 操作系统版本 | 镜像族系 |
| --- | --- |
| SUSE Linux Enterprise Server 15 SP6 64 位 | 无 |
| SUSE Linux Enterprise Server 15 SP5 64 位 | 无 |
| SUSE Linux Enterprise Server 15 SP4 64 位 | 无 |
| SUSE Linux Enterprise Server 15 SP3 64 位 | 无 |
| SUSE Linux Enterprise Server 15 SP2 64 位 | 无 |
| SUSE Linux Enterprise Server 15 SP1 64 位 | 无 |
| SUSE Linux Enterprise Server for SAP Applications 15 SP6 64 位 | 无 |
| SUSE Linux Enterprise Server for SAP Applications 15 SP5 64 位 | 无 |
| SUSE Linux Enterprise Server for SAP Applications 15 SP4 64 位 | 无 |
| SUSE Linux Enterprise Server for SAP Applications 15 SP3 64 位 | 无 |
| SUSE Linux Enterprise Server for SAP Applications 15 SP2 64 位 | 无 |
| SUSE Linux Enterprise Server for SAP Applications 15 SP1 64 位 | 无 |
| SUSE Linux Enterprise Server 12 SP5 64 位 | 无 |
| SUSE Linux Enterprise Server for SAP Applications 12 SP5 64 位 | 无 |
| SUSE Linux Enterprise Server 12 SP4 64 位 | 无 |
| SUSE Linux Enterprise Server 12 SP3 64 位 | 无 |


- 

Ubuntu

| 操作系统版本 | 镜像族系 |
| --- | --- |
| Ubuntu 24.04 LTS 64 位 | acs:ubuntu_24_04_x64 |
| Ubuntu 24.04 LTS 64 位 ARM 版 | acs:ubuntu_24_04_arm64 |
| Ubuntu 22.04 LTS 64 位 | acs:ubuntu_22_04_x64 |
| Ubuntu 22.04 LTS 64 位 UEFI 版 | acs:ubuntu_22_04_x64_uefi |
| Ubuntu 22.04 LTS 64 位 ARM 版 | 无 |
| Ubuntu 20.04 LTS 64 位 | acs:ubuntu_20_04_x64 |
| Ubuntu 20.04 LTS 64 位 AMD 版 | acs:ubuntu_20_04_x64_amd |
| Ubuntu 20.04 LTS 64 位 UEFI 版 | acs:ubuntu_20_04_x64_uefi |
| Ubuntu 20.04 LTS 64 位 ARM 版 | acs:ubuntu_20_04_arm64 |
| Ubuntu 18.04 LTS 64 位 | acs:ubuntu_18_04_x64 |
| Ubuntu 18.04 LTS 64 位 AMD 版 | acs:ubuntu_18_04_x64_amd |
| Ubuntu 18.04 LTS 64 位 UEFI 版 | acs:ubuntu_18_04_x64_uefi |
| Ubuntu 18.04 LTS 64 位 ARM 版 | acs:ubuntu_18_04_arm64 |
| Ubuntu 16.04 LTS 64 位 | acs:ubuntu_16_04_x64 |
| Ubuntu 16.04 LTS 32 位 | acs:ubuntu_16_04_x86 |
| Ubuntu 14.04 LTS 64 位 | acs:ubuntu_14_04_x64 |
| Ubuntu 14.04 LTS 32 位 | acs:ubuntu_14_04_x86 |


说明

使用32位操作系统，请选择内存小于或等于4 GiB的实例规格。更多信息，请参见[选择镜像的操作系统](products/ecs/documents/user-guide/select-an-image.md)。

- 

Fedora CoreOS

| 操作系统版本 | 镜像族系 |
| --- | --- |
| Fedora CoreOS 34.20210529.3.0_3 | acs:fedora_coreos_34_20210529_3_0_3_x64 |
| Fedora CoreOS 33.20210217.3.0_3 | acs:fedora_coreos_33_20210217_3_0_3_x64 |


说明

使用该类镜像时，您需要注意：

- 

创建实例或更换系统盘时，登录凭证仅支持设置密钥对，且仅能使用实例第一次设置的密钥对登录实例，不支持更换或解绑该密钥对。

- 

创建实例或更换系统盘后，不支持为实例重置密码。

- 

Fedora

| 操作系统版本 | 镜像族系 |
| --- | --- |
| Fedora 41 64 位 ARM 版 | acs:fedora_41_arm64 |
| Fedora 41 64 位 | acs:fedora_41_x64 |
| Fedora 40 64 位 | acs:fedora_40_x64 |
| Fedora 39 64 位 | acs:fedora_39_x64 |
| Fedora 38 64 位 | acs:fedora_38_x64 |
| Fedora 37 64 位 | acs:fedora_37_x64 |
| Fedora 35 64 位 | acs:fedora_35_x64 |
| Fedora 34 64 位 | acs:fedora_34_x64 |
| Fedora 33 64 位 | acs:fedora_33_x64 |


- 

Rocky Linux

| 操作系统版本 | 镜像族系 |
| --- | --- |
| Rocky Linux 9.6 64 位 ARM 版 | acs:rocky_linux_9_6_arm64 |
| Rocky Linux 9.6 64 位 | acs:rocky_linux_9_6_x64 |
| Rocky Linux 9.5 64 位 ARM 版 | acs:rocky_linux_9_5_arm64 |
| Rocky Linux 9.5 64 位 | acs:rocky_linux_9_5_x64 |
| Rocky Linux 9.4 64 位 | acs:rocky_linux_9_4_x64 |
| Rocky Linux 9.4 64 位 ARM 版 | acs:rocky_linux_9_4_arm64 |
| Rocky Linux 9.3 64 位 | acs:rocky_linux_9_3_x64 |
| Rocky Linux 9.2 64 位 | acs:rocky_linux_9_2_x64 |
| Rocky Linux 9.1 64 位 | acs:rocky_linux_9_1_x64 |
| Rocky Linux 9.1 64 位 UEFI 版 | acs:rocky_linux_9_1_x64_uefi |
| Rocky Linux 9.0 64 位 | acs:rocky_linux_9_0_x64 |
| Rocky Linux 8.10 64 位 | acs:rocky_linux_8_10_x64 |
| Rocky Linux 8.10 64 位 ARM 版 | 无 |
| Rocky Linux 8.9 64 位 | acs:rocky_linux_8_9_x64 |
| Rocky Linux 8.8 64 位 | acs:rocky_linux_8_8_x64 |
| Rocky Linux 8.8 64 位 UEFI 版 | acs:rocky_linux_8_8_x64_uefi |
| Rocky Linux 8.7 64 位 UEFI 版 | acs:rocky_linux_8_7_x64_uefi |
| Rocky Linux 8.7 64 位 | acs:rocky_linux_8_7_x64 |
| Rocky Linux 8.6 64 位 | acs:rocky_linux_8_6_x64 |
| Rocky Linux 8.5 64 位 | acs:rocky_linux_8_5_x64 |


- 

AlmaLinux

| 操作系统版本 | 镜像族系 |
| --- | --- |
| AlmaLinux 9.6 64 位 ARM 版 | acs:almalinux_9_6_arm64 |
| AlmaLinux 9.6 64 位 | acs:almalinux_9_6_x64 |
| AlmaLinux 9.5 64 位 ARM 版 | acs:almalinux_9_5_arm64 |
| AlmaLinux 9.5 64 位 | acs:almalinux_9_5_x64 |
| AlmaLinux 9.4 64 位 | acs:almalinux_9_4_x64 |
| AlmaLinux 9.4 64 位 ARM 版 | acs:almalinux_9_4_arm64 |
| AlmaLinux 9.3 64 位 | acs:almalinux_9_3_x64 |
| AlmaLinux 9.2 64 位 | acs:almalinux_9_2_x64 |
| AlmaLinux 9.2 64 位 UEFI 版 | acs:almalinux_9_2_x64_uefi |
| AlmaLinux 9.1 64 位 | acs:almalinux_9_1_x64 |
| AlmaLinux 9.0 64 位 | acs:almalinux_9_0_x64 |
| AlmaLinux 8.10 64 位 | acs:almalinux_8_10_x64 |
| AlmaLinux 8.10 64 位 ARM 版 | acs:almalinux_8_10_arm64 |
| AlmaLinux 8.9 64 位 | acs:almalinux_8_9_x64 |
| AlmaLinux 8.8 64 位 | acs:almalinux_8_8_x64 |
| AlmaLinux 8.8 64 位 UEFI 版 | acs:almalinux_8_8_x64_uefi |
| AlmaLinux 8.7 64 位 | acs:almalinux_8_7_x64 |
| AlmaLinux 8.7 64 位 UEFI 版 | acs:almalinux_8_7_x64_uefi |
| AlmaLinux 8.6 64 位 | acs:almalinux_8_6_x64 |
| AlmaLinux 8.5 64 位 | acs:almalinux_8_5_x64 |


## 相关文档

Linux镜像默认是命令行形式，如果您需要在Linux操作系统中安装可视化桌面，请参见[为](products/ecs/documents/user-guide/installing-a-graphical-desktop-environment-for-a-linux-instance.md)[Linux](products/ecs/documents/user-guide/installing-a-graphical-desktop-environment-for-a-linux-instance.md)[实例安装图形化界面](products/ecs/documents/user-guide/installing-a-graphical-desktop-environment-for-a-linux-instance.md)。

[上一篇：镜像类型](products/ecs/documents/user-guide/image-types.md)[下一篇：Alibaba Cloud Linux](products/ecs/documents/user-guide/alibaba-cloud-linux.md)

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
