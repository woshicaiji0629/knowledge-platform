# 为ACK Edge集群提供容器存储功能-ACK Edge存储-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/storage-overview

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-edge/product-overview.md)

- [快速入门](products/ack/documents/ack-edge/quick-start.md)

- [操作指南](products/ack/documents/ack-edge/user-guide.md)

- [实践教程](products/ack/documents/ack-edge/use-cases.md)

- [安全合规](products/ack/documents/ack-edge/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-edge/developer-reference.md)

- [服务支持](products/ack/documents/ack-edge/support.md)

[首页](https://help.aliyun.com/zh)

# ACK Edge存储概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

ACK Edge集群的CSI（csi-plugin和csi-provisioner）插件复用ACK集群的CSI插件，以确保在ECS上的使用和ACK集群保持完全一致，详情请参见[存储](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/csi-overview-1.md)。本文将详细介绍不同节点类型和接入方式下，与ACK集群的CSI插件使用和限制条件。

## 使用限制

### CSI插件限制

您在使用存储CSI插件时既要关注CSI插件本身的使用限制，也要注意CSI插件支持的阿里云存储产品的使用限制。相关信息，请参见[存储](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/csi-overview-1.md)[CSI](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/csi-overview-1.md)[插件的使用限制](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/csi-overview-1.md)。

重要

请务必根据您的节点类型和接入方式，来确定CSI插件支持的存储卷能力。

### 集群版本限制

- 

使用CSI插件时，需确保ACK Edge集群版本为1.14及以上，且kubelet运行参数--enable-controller-attach-detach需要设置为true。

- 

使用ECS云盘能力时，需确保ACK Edge集群版本为1.24及以上。

- 

使用ENS云盘能力时，需确保ACK Edge集群版本为1.20以上。

## 容器存储能力概览

容器存储接口（CSI）插件是当前Kubernetes社区推荐的插件实现方案。ACK Edge集群的容器存储功能也是基于CSI插件实现。除完全兼容Kubernetes原生的存储卷类型，例如EmptyDir、HostPath、Secret、ConfigMap等之外，根据节点类型和接入方式，CSI插件支持的存储卷如下。

重要

- 

ENS节点使用阿里云NAS和CPFS（注意：不是ENS的NAS）时需要专线和集群VPC打通，可以通过ENS[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)咨询。

- 

使用本地存储的LVM时，需要确保云端节点能够访问存储节点的TCP 1736端口。相关信息，请参见[使用](products/ack/documents/ack-edge/user-guide/use-lvm-to-manage-local-storage.md)[LVM](products/ack/documents/ack-edge/user-guide/use-lvm-to-manage-local-storage.md)[本地存储](products/ack/documents/ack-edge/user-guide/use-lvm-to-manage-local-storage.md)。

## CSI组件介绍

ACK Edge集群的CSI组件包括csi-plugin、csi-provisioner、csi-ens-plugin和csi-ens-provisioner，需要您手动安装。具体操作，请参见[管理组件](products/ack/documents/manage-system-components.md)。

如需使用ENS云盘，您需要安装csi-ens-plugin组件和csi-ens-provisioner组件。对于其他存储卷，则需安装csi-plugin和csi-provisioner组件。

根据节点类型以及接入方式，支持的存储卷以及对应的操作指南如下。

| 节点类型 | 存储服务 | 静态存储卷 | 动态存储卷 | 操作链接 |
| --- | --- | --- | --- | --- |
| ECS | 阿里云云盘 | 支持 | 支持 | [云盘存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/disk-volume-overview-3.md) |
| 阿里云 NAS | 支持 | 支持 | [NAS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/nas-volume-overview-1.md) [存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/nas-volume-overview-1.md) |  |
| 阿里云 CPFS | 支持 | 支持 | [CPFS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cpfs-volume-overview.md) [通用版存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cpfs-volume-overview.md) |  |
| 阿里云 OSS | 支持 | 支持 | [OSS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/oss-volume-overview-1.md) [存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/oss-volume-overview-1.md) |  |
| 本地存储 | 支持 | 支持 | [本地存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/overview-17.md) |  |
| ENS | ENS 云盘 | 支持 | 支持 | [使用](products/ack/documents/ack-edge/user-guide/use-ens-disks.md) [ENS](products/ack/documents/ack-edge/user-guide/use-ens-disks.md) [云盘](products/ack/documents/ack-edge/user-guide/use-ens-disks.md) |
| 阿里云 NAS（使用专线打通） | 支持 | 支持 | [NAS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/nas-volume-overview-1.md) [存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/nas-volume-overview-1.md) |  |
| 阿里云 CPFS（使用专线打通） | 支持 | 支持 | [CPFS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cpfs-volume-overview.md) [通用版存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cpfs-volume-overview.md) |  |
| 阿里云 OSS | 支持 | 不支持 | [OSS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/oss-volume-overview-1.md) [存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/oss-volume-overview-1.md) |  |
| 本地存储 | 支持 | 支持 | [本地存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/overview-17.md) |  |
| 专线接入 边缘节点 | 阿里云 NAS | 支持 | 支持 | [NAS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/nas-volume-overview-1.md) [存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/nas-volume-overview-1.md) |
| 阿里云 CPFS | 支持 | 支持 | [CPFS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cpfs-volume-overview.md) [通用版存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cpfs-volume-overview.md) |  |
| 阿里云 OSS | 支持 | 不支持 | [OSS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/oss-volume-overview-1.md) [存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/oss-volume-overview-1.md) |  |
| 本地存储 | 支持 | 支持 | [本地存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/overview-17.md) |  |
| 公网接入 边缘节点 | 阿里云 OSS | 支持 | 不支持 | [OSS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/oss-volume-overview-1.md) [存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/oss-volume-overview-1.md) |


## 升级CSI相关组件

您可以在控制台查看CSI相关组件版本并升级组件。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。

- 

单击存储页签，在csi-ens-plugin、csi-ens-provisioner、csi-plugin及csi-provisioner组件区域，查看当前版本是否需要升级，并升级组件。

[上一篇：使用Gateway with Inference Extension访问服务](products/ack/documents/ack-edge/user-guide/using-gateway-with-inference-extension-to-access-services.md)[下一篇：边缘扩展功能](products/ack/documents/ack-edge/user-guide/application-management.md)

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
