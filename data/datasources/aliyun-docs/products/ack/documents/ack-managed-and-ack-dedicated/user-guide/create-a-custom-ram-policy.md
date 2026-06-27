# 集群及云资源权限-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/create-a-custom-ram-policy

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-managed-and-ack-dedicated/product-overview.md)

- [快速入门](products/ack/documents/ack-managed-and-ack-dedicated/getting-started.md)

- [操作指南](products/ack/documents/ack-managed-and-ack-dedicated/user-guide.md)

- [实践教程](products/ack/documents/ack-managed-and-ack-dedicated/use-cases.md)

- [安全合规](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference.md)

- [服务支持](products/ack/documents/ack-managed-and-ack-dedicated/support.md)

[首页](https://help.aliyun.com/zh)

# 使用RAM授予集群及云资源权限

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

默认情况下，RAM用户或RAM角色没有使用云服务OpenAPI的任何权限，您需要为RAM用户或RAM角色授予系统策略权限或自定义权限策略后，才能使用容器服务ACK的OpenAPI。本文介绍如何为RAM用户或RAM角色进行集群以及云资源维度的授权。

## 使用系统策略授权

系统策略授权用于指定全局资源的读写访问控制。当RAM用户或RAM角色需要阿里云账号下所有集群的运维管理权限时，建议使用系统策略进行快捷授权。容器服务ACK的常用系统策略如下表所示：

重要

系统策略中Full级别的权限为高风险权限，请谨慎授予，以免造成安全风险。

展开查看容器服务ACK常用系统策略

| 系统策略名称 | 说明 |
| --- | --- |
| AliyunCSFullAccess | 当 RAM 用户或 RAM 角色需要容器服务产品所有 OpenAPI 的访问权限。 说明 此系统策略仅包含针对 ACK 产品的 RAM 授权。如您需要对 ACK 集群中的应用进行运维，还需要进行 RBAC 授权，请参见 [RBAC](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/authorization-overview.md) [授权](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/authorization-overview.md) 。 |
| AliyunVPCReadOnlyAccess | 当 RAM 用户或 RAM 角色在创建集群时选择指定 VPC。 |
| AliyunECSReadOnlyAccess | 当 RAM 用户或 RAM 角色为集群添加已有节点或查看节点详细信息。 |
| AliyunContainerRegistryFullAccess | 当 RAM 用户或 RAM 角色需要全局管理阿里云账号内的业务镜像。 |
| AliyunLogReadOnlyAccess | 当 RAM 用户或 RAM 角色在创建集群时选择已有 Log Project 存储审计日志，或查看指定集群的配置巡检。 |
| AliyunAHASReadOnlyAccess | 当 RAM 用户或 RAM 角色需要使用集群拓扑功能。 |
| AliyunRAMFullAccess | 当 RAM 用户或 RAM 角色需要负责阿里云账号内的全局授权管理。 |
| AliyunYundunSASReadOnlyAccess | 当 RAM 用户或 RAM 角色需要查看指定集群的运行时安全监控。 |
| AliyunARMSReadOnlyAccess | 当 RAM 用户或 RAM 角色需要查看集群阿里云 Prometheus 插件的监控状态。 |
| AliyunKMSReadOnlyAccess | 当 RAM 用户或 RAM 角色在创建 Pro 集群时启用 Secret 落盘加密能力。 |
| AliyunESSReadOnlyAccess | 当 RAM 用户或 RAM 角色需要执行节点池的相关操作，例如查看、编辑和扩缩容等。 |


说明

阿里云账号对账号中的资源具有完全管理权限。您也可以创建一个RAM用户，授予AdministratorAccess权限，充当账号管理员。该管理员可以对账号下所有云资源进行管控操作，请参见[创建](products/ram/documents/create-admin-user.md)[RAM](products/ram/documents/create-admin-user.md)[用户作为账号管理员](products/ram/documents/create-admin-user.md)。

- 

使用RAM管理员登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。

- 

在左侧导航栏，选择身份管理>用户。

- 

在用户页面，单击目标RAM用户操作列的添加权限。

您也可以选中多个RAM用户，单击用户列表下方的添加权限，为RAM用户批量授权。

- 

在新增授权面板，为RAM用户添加权限。

- 

选择资源范围。

- 

账号级别：权限在当前阿里云账号内生效。

- 

资源组级别：权限在指定的资源组内生效。

重要

指定资源组授权生效的前提是该云服务及资源类型已支持资源组，详情请参见[支持资源组的云服务](https://help.aliyun.com/zh/resource-management/resource-group/product-overview/services-that-work-with-resource-group#concept-flc-p3m-4fb)。资源组授权示例，请参见[使用资源组限制](products/ram/documents/use-cases/use-a-resource-group-to-manage-an-ecs-instance.md)[RAM](products/ram/documents/use-cases/use-a-resource-group-to-manage-an-ecs-instance.md)[用户管理指定的](products/ram/documents/use-cases/use-a-resource-group-to-manage-an-ecs-instance.md)[ECS](products/ram/documents/use-cases/use-a-resource-group-to-manage-an-ecs-instance.md)[实例](products/ram/documents/use-cases/use-a-resource-group-to-manage-an-ecs-instance.md)。

- 

选择授权主体。

授权主体即需要添加权限的RAM用户。系统会自动选择当前的RAM用户。

- 

选择需要授予的系统权限策略。

- 

单击确认新增授权。

- 

单击关闭。

## 使用自定义策略授权

自定义策略授权用于对目标RAM用户或RAM角色实现细粒度的云资源访问控制。不同的云资源可能存在不同的安全性和访问控制要求，如果您需要对用户进行精细化的云资源访问控制，例如，限制某用户对某个具体集群的操作权限，您可以创建自定义授权策略满足这种细粒度要求。另外，如果目标RAM用户或RAM角色有基于SDK的二次开发需求，还可实现API级别的权限控制。关于RAM支持的授权项，请参见[授权信息](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/api-cs-2015-12-15-ram.md)。

说明

在创建自定义授权策略时，您需要了解授权策略语言的基本结构和语法。更多信息，请参见[权限策略基本元素](products/ram/documents/policy-elements.md)。

### 步骤一：创建自定义授权策略

- 

使用RAM管理员登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。

- 

在左侧导航栏，选择权限管理>权限策略。

- 

在权限策略页面，单击创建权限策略。

- 

在创建权限策略页面，单击脚本编辑页签，输入权限策略内容。

请将YOUR_CLUSTER_ID替换为目标集群ID。{"Statement":[{"Action":["cs:Get*","cs:List*","cs:Describe*","cs:ScaleCluster","cs:DeleteCluster"],"Effect":"Allow","Resource":["acs:cs:*:*:cluster/YOUR_CLUSTER_ID"]}],"Version":"1"}

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| Action | 所需授予的权限，所有的 Action 均支持通配符。 |
| Resource | 授予单集群权限 "Resource" : [ "acs:cs:*:*:cluster/ YOUR_CLUSTER_ID " ] 授予多个集群权限 "Resource" : [ "acs:cs:*:*:cluster/ YOUR_CLUSTER_ID_1 " , "acs:cs:*:*:cluster/ YOUR_CLUSTER_ID_2 " ] 授予所有集群的权限 "Resource": [ "*" ] |


- 

在创建权限策略页面，单击确定。

- 

在创建权限策略对话框，输入策略名称和备注，然后单击确定。

### 步骤二：为RAM用户或RAM角色授予自定义权限策略

关于自定义授权的具体操作和系统策略授权操作方法一样，当选择权限策略时，需选择您已创建的自定义策略。具体操作，请参见[使用系统策略授权](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-custom-ram-policy.md)。

## 自定义策略授权示例

### 示例1：授予指定集群的只读权限

{"Statement":[{"Action":["cs:Get*","cs:List*","cs:Describe*"],"Effect":"Allow","Resource":["acs:cs:*:*:cluster/YOUR_CLUSTER_ID"]}],"Version":"1"}

### 示例2：授予指定OSS Bucket的读取权限

请将YOUR_OSS_BUCKET_NAME替换为目标OSS Bucket名称。{"Version":"1","Statement":[{"Effect":"Allow","Action":["oss:ListBuckets","oss:GetBucketStat","oss:GetBucketInfo","oss:GetBucketTagging","oss:GetBucketAcl"],"Resource":"acs:oss:*:*:*"},{"Effect":"Allow","Action":["oss:ListObjects","oss:GetBucketAcl"],"Resource":"acs:oss:*:*:YOUR_OSS_BUCKET_NAME"},{"Effect":"Allow","Action":["oss:GetObject","oss:GetObjectAcl"],"Resource":"acs:oss:*:*:YOUR_OSS_BUCKET_NAME/*"}]}

### 示例3：授权不支持限制集群的OpenAPI的操作权限

部分OpenAPI不支持限制集群的授权（例如，DescribeEvents），如果您需要给RAM用户或RAM角色授权这些OpenAPI不支持限制集群的OpenAPI的操作权限，请勿在Resource中限定集群ID。修改前后的RAM权限策略对比如下：

| 修改前 RAM 权限策略 | 修改后 RAM 权限策略 |
| --- | --- |
| { "Statement" : [ { "Action" : [ "cs:Get*" , "cs:List*" , "cs:Describe*" ] , "Effect" : "Allow" , "Resource" : [ "acs:cs:*:*:cluster/ YOUR_CLUSTER_ID " ] } ] , "Version" : "1" } | { "Statement" : [ { "Action" : [ "cs:DescribeEvents" ] , "Effect" : "Allow" , "Resource" : [ "*" ] } , { "Action" : [ "cs:Get*" , "cs:List*" , "cs:Describe*" ] , "Effect" : "Allow" , "Resource" : [ "acs:cs:*:*:cluster/ YOUR_CLUSTER_ID " ] } ] , "Version" : "1" } |


## 后续操作

- 

RAM授权后，您需要继续完成集群内Kubernetes资源访问的RBAC授权，才能对集群内部资源进行操作。具体授权，请参见[使用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[RBAC](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[为集群内资源操作授权](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)。

- 

如需提升ACK集群内应用访问其他云服务的安全性，您可以通过RRSA配置ServiceAccount的RAM权限实现Pod权限隔离，请参见[通过](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RRSA](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[配置](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[ServiceAccount](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[的](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RAM](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[权限实现](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[权限隔离](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。

- 

如需精细化RAM授权，请参见[通过标签实现精细化权限管理](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-labels-to-enforce-fine-grained-access-control.md)、[手动收敛](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/manually-converges-the-worker-ram-role-permissions-of-the-ack-managed-version-cluster.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/manually-converges-the-worker-ram-role-permissions-of-the-ack-managed-version-cluster.md)[托管版集群的](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/manually-converges-the-worker-ram-role-permissions-of-the-ack-managed-version-cluster.md)[Worker RAM](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/manually-converges-the-worker-ram-role-permissions-of-the-ack-managed-version-cluster.md)[角色权限](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/manually-converges-the-worker-ram-role-permissions-of-the-ack-managed-version-cluster.md)。

- 

授权过程问题，请参见[授权管理](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-authorization-management.md)[FAQ](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-authorization-management.md)。

[上一篇：RAM授权](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ram-authorization.md)[下一篇：通过标签实现精细化权限管理](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-labels-to-enforce-fine-grained-access-control.md)

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
