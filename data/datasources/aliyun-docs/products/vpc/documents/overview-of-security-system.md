# 安全原理功能与管控机制-专有网络VPC-阿里云

Source: https://help.aliyun.com/zh/vpc/overview-of-security-system

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

# 安全体系概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/vpc)

[我的收藏](https://help.aliyun.com/my_favorites.html)

阿里云致力于为您提供稳定、可靠、安全、合规的云计算服务，帮助您保护您系统及数据的机密性、完整性、可用性。本文介绍了专有网络VPC（Virtual Private Cloud）的安全体系、提供的安全能力和安全管控运作机制。

## 安全体系

### 专有网络原理

专有网络VPC是一个隔离的网络环境，专有网络之间逻辑上彻底隔离。基于目前主流的隧道技术，专有网络隔离了虚拟网络。每个VPC都有一个独立的隧道号，一个隧道号对应着一个虚拟化网络。

- 

一个VPC内的ECS（Elastic Compute Service）实例之间的传输数据包都会加上隧道封装，带有唯一的隧道号标识，然后通过物理网络进行传输。

- 

不同VPC内的ECS实例由于所在的隧道号不同，本身处于两个不同的路由平面，因此不同VPC内的ECS实例无法进行通信，天然地进行了隔离。

### 安全防护功能

专有网络VPC可以通过以下功能保障云服务的安全性和可靠性。

| 功能 | 描述 |
| --- | --- |
| ECS 安全组 | 安全组是一种虚拟防火墙，具备状态检测和数据包过滤能力，用于在云端划分安全域。通过配置安全组规则，您可以控制安全组内一台或多台 ECS 实例的入流量和出流量。详细信息，请参见 [安全组概述](products/ecs/documents/user-guide/overview-44.md) 。 |
| 网络 ACL | 网络 ACL 是 VPC 中的网络访问控制功能。您可以自定义设置网络 ACL 规则，并将网络 ACL 与交换机绑定，实现对交换机中 ECS 实例的流量的访问控制。详细信息，请参见 [网络](products/vpc/documents/network-acl-overview.md) [ACL](products/vpc/documents/network-acl-overview.md) [概述](products/vpc/documents/network-acl-overview.md) 。 |
| 流日志 | 专有网络 VPC 提供流日志功能，可以记录 VPC 网络中弹性网卡 ENI（Elastic Network Interface）传入和传出的流量信息，帮助您检查访问控制规则、监控网络流量和排查网络故障。详细信息，请参见 [流日志概述](products/vpc/documents/vpc-flow-logs.md) 。 |
| 流量镜像 | VPC 流量镜像功能可以镜像经过弹性网卡 ENI 且符合筛选条件的报文。通过流量镜像功能，您可以复制 VPC 中 ECS 实例的网络流量，然后将复制后的网络流量转发给指定的弹性网卡或私网传统型负载均衡 CLB（Classic Load Balancer）实例，用于内容检查、威胁监控和问题排查等场景。详细信息，请参见 [流量镜像概述](products/vpc/documents/traffic-mirroring-overview.md) 。 |


### 使用RAM权限策略

您可以通过RAM访问控制策略，对专有网络VPC的访问权限进行控制。

权限用来描述用户、用户组、角色对具体资源的访问能力，策略是具体授权的方法。您可以通过RAM权限策略，决定哪些用户或角色可以访问哪些资源，或执行哪些操作。

权限策略配置

您可以通过以下常用的权限策略对VPC的访问权限进行控制。关于VPC的权限定义，请参见[授权信息（VPC）](products/vpc/documents/developer-reference/api-vpc-2016-04-28-ram.md)和[授权信息（VPC](products/vpc/documents/developer-reference/api-vpcpeer-2022-01-01-ram.md)[对等连接）](products/vpc/documents/developer-reference/api-vpcpeer-2022-01-01-ram.md)。

| 权限策略 | 描述 |
| --- | --- |
| AliyunVPCFullAccess | 为 RAM 用户授予 VPC 的完全管理权限。 |
| AliyunVPCReadOnlyAccess | 为 RAM 用户授予 VPC 的只读访问权限。 |


您可以为用户创建系统权限策略，当系统权限策略不能满足您的要求时，您可以创建自定义权限策略。关于如何创建自定义权限策略，请参见[通过](products/ram/documents/use-cases/use-ram-roles-to-manage-vpc-permissions.md)[RAM](products/ram/documents/use-cases/use-ram-roles-to-manage-vpc-permissions.md)[对](products/ram/documents/use-cases/use-ram-roles-to-manage-vpc-permissions.md)[VPC](products/ram/documents/use-cases/use-ram-roles-to-manage-vpc-permissions.md)[进行权限管理](products/ram/documents/use-cases/use-ram-roles-to-manage-vpc-permissions.md)。

[上一篇：安全合规](products/vpc/documents/security-and-compliance.md)[下一篇：使用RAM进行访问控制](products/vpc/documents/identity-management-and-access-control.md)

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
