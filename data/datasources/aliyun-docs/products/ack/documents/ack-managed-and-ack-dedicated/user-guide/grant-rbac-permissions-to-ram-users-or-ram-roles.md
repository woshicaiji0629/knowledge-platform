# 使用RBAC为集群内资源操作授权-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles

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

# 使用RBAC为集群内资源操作授权

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

操作ACK集群需遵循RAM和Kubernetes RBAC的双重授权。默认情况下，仅阿里云账号和集群创建者拥有集群的完整权限。其他RAM用户或角色在获得访问集群的RAM授权后，仍需具有RBAC权限，才能对集群内的Kubernetes资源进行操作。

## 工作原理

ACK的[授权](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/authorization-overview.md)体系包括阿里云RAM和Kubernetes[RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)两个层级，构成了从云资源到集群资源的完整授权链路。

- 

[RAM](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-custom-ram-policy.md)：决定了谁能“进入”集群的大门。负责在云资源层面进行授权，控制用户对ACK集群及其依赖云产品的OpenAPI操作权限。

- 

RBAC：决定了用户“进入”大门后能做什么。负责在集群内部进行精细化授权，定义用户能对哪些Kubernetes资源（如Pod、Deployment）执行何种操作（如创建、删除）。

### Kubernetes RBAC 机制

- 

ClusterRole：定义一个在整个集群范围生效的权限集合，再通过ClusterRoleBinding将其绑定至授权主体，使其权限在整个集群内生效。

- 

Role：定义一个仅在单个命名空间内有效的权限集合，再通过RoleBinding将其绑定至授权主体，使其权限仅在当前命名空间内生效。

## 场景一：使用阿里云账号进行RBAC授权

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择授权管理。

- 

在授权管理页面配置管理权限。

- 

为RAM用户授权：单击RAM 用户页签，定位目标 RAM 用户，单击操作列的管理权限，进入权限管理页面。

- 

为RAM角色授权：单击RAM 角色页签，定位目标 RAM 角色，单击管理权限，进入权限管理页面。

- 

单击+添加权限，按照页面提示为目标RAM用户或角色添加集群或命名空间级别的权限配置，并选择预置角色。

## 场景二：使用RAM用户或角色进行RBAC授权

默认情况下，RAM用户或角色无法为其他账号授予RBAC权限。为便于权限管理，ACK支持指定某个RAM用户或角色为权限管理员，使其能够为其他用户授予RBAC权限。

### 步骤一：将RAM用户或角色设置为权限管理员

1. 获得授权所需的RAM权限

## 方式一：系统策略授权

重要

系统策略需使用AliyunRAMReadOnlyAccess和AliyunCSFullAccess，权限较大。如需精细化授权，请使用[方式二：自定义策略精细化授权](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)。

- 

使用阿里云账号登录[RAM](https://ram.console.aliyun.com/)[管理控制台](https://ram.console.aliyun.com/)，定位目标RAM用户或角色。

- 

RAM用户：选择身份管理>用户，在用户列表的操作列，单击添加权限。

- 

RAM角色：选择身份管理>角色，在角色列表的操作列，单击添加权限。

- 

选择资源范围为账号级别，在权限策略区域定位并选中系统策略AliyunRAMReadOnlyAccess和AliyunCSFullAccess，按照页面提示完成授权。

## 方式二：自定义策略精细化授权

权限管理员需具备以下能力：

- 

查看其他RAM身份信息

- 

查看集群列表和详情

- 

查看集群已有的RBAC配置

- 

在集群中执行RBAC授权操作

请登录[RAM](https://ram.console.aliyun.com/)[管理控制台](https://ram.console.aliyun.com/)，参考以下代码示例，为目标RAM用户或角色授予所需的RAM权限。具体操作，请参见[使用自定义策略授权](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-custom-ram-policy.md)。

{ "Statement": [{ "Action": [ "ram:Get*", "ram:List*", "cs:Get*", "cs:Describe*", "cs:List*", "cs:GrantPermission" ], "Resource": "*", "Effect": "Allow" } ], "Version": "1" }

2. 获得RBAC管理员权限

使用阿里云账号登录[容器服务管理控制台](https://cs.console.aliyun.com/)，为目标RAM用户或角色在集群维度授予预置角色管理员。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择授权管理。

- 

在授权管理页面配置管理权限。

- 

为RAM用户授权：单击RAM 用户页签，定位目标 RAM 用户，单击操作列的管理权限，进入权限管理页面。

- 

为RAM角色授权：单击RAM 角色页签，定位目标 RAM 角色，单击管理权限，进入权限管理页面。

- 

单击+添加权限，按照页面提示添加集群和命名空间级别的权限配置，选择预置角色为管理员。

如果在所有集群维度进行授权，权限管理员的身份将自动应用到未来新建的集群，无需重复授权。

### 步骤二：为其他RAM用户或角色授予RBAC权限

完成前置授权后，权限管理员即可在授权管理页面为其他RAM用户或角色授予RBAC权限。

## 适用于生产环境

为提升权限管理的安全性和可维护性，建议遵循以下建议。

- 

遵循最小权限原则

仅授予RAM用户、角色等主体完成其工作所必需的最小权限集。避免无差别授予管理员等高权限角色。

- 

实施精细化授权

- 

分层授权：区分RAM（负责云资源访问）和RBAC（负责集群内资源访问）的职责。

- 

收敛作用域：优先使用RoleBinding将权限限制在特定的命名空间内，而非集群级别的ClusterRoleBinding。

- 

精确选择角色：优先使用ACK提供的预置角色。如需自定义角色，应精确定义权限规则，避免使用通配符（*）。

- 

持续治理

权限管理是一个动态过程。应建立定期审计机制，及时回收冗余或过度的授权，并对权限管理员等高权限角色的操作进行记录和监控。

## 附录：预置角色说明

为了简化权限管理并快速满足常见的用户场景，ACK基于RBAC机制封装了多种标准化的预置角色。

| 预置角色 | 集群内 RBAC 权限 |
| --- | --- |
| 管理员 | 对集群所有命名空间下 Kubernetes 资源的 RBAC 读写权限，对集群节点、存储卷、命名空间、配额的读写权限。 |
| 只读管理员 | 对集群所有命名空间下 Kubernetes 资源的 RBAC 只读权限，对集群节点、存储卷、命名空间、配额的只读权限。 |
| 运维人员 | 对集群所有命名空间下控制台可见 Kubernetes 资源的 RBAC 读写权限，对集群节点、存储卷、命名空间的读取与更新权限，对其他资源的只读权限。 |
| 开发人员 | 对集群所有命名空间或所选命名空间下控制台可见 Kubernetes 资源的 RBAC 读写权限。 |
| 受限用户 | 对集群所有命名空间或所选命名空间下控制台可见 Kubernetes 资源的 RBAC 只读权限。 |
| 自定义 | 权限由您所选择的 ClusterRole 决定，请在确定所选 ClusterRole 对各类资源的操作权限后再进行授权，以免 RAM 用户或 RAM 角色获得不符合预期的权限。关于自定义权限的授权，请参见 [使用自定义](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-an-rbac-role.md) [RBAC](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-an-rbac-role.md) [限制集群内资源操作](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-an-rbac-role.md) 。 重要 RAM 用户或 RAM 角色被授予 cluster-admin 权限后，在该集群内可视为与阿里云账号有相同权限的超级账号，拥有操作集群内所有资源的任意权限。请谨慎授予。 |


## 常见问题

### 操作时遇到无权限错误码怎么办？

通过控制台或OpenAPI所做的部分操作缺少所需的RBAC权限时，将返回相应的无权限错误码。可参见下表解决。

| 错误码或错误信息 | 说明 | 解决方案 |
| --- | --- | --- |
| ForbiddenCheckControlPlaneLog | 查看控制面日志被拒绝。 | 为用户授予管理员或运维人员权限。 |
| ForbiddenHelmUsage | 执行 Helm 操作被拒绝。 | 为用户授予管理员权限。 |
| ForbiddenRotateCert | 证书轮换被拒绝。 | 为用户授予管理员权限。 |
| ForbiddenAttachInstance | 添加节点被拒绝。 | 为用户授予管理员或运维人员权限。 |
| ForbiddenUpdateKMSState | 修改集群 KMS 落盘加密状态被拒绝。 | 为用户授予管理员或运维人员权限。 |
| Forbidden get trigger | 获取应用触发器信息被拒绝。 | 为用户授予管理员、运维人员或开发人员权限。 |
| ForbiddenQueryClusterNamespace | 查询集群命名空间被拒绝。 | 为用户授予管理员、运维人员、开发人员或受限用户的权限。 |


### RBAC预置角色不满足需求，如何创建自定义权限？

可通过编写YAML来创建自定义Role或ClusterRole。例如，创建一个只允许查看Pod的ClusterRole，然后在授权时选择自定义权限并绑定对应的ClusterRole。具体操作，请参见[使用自定义](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-an-rbac-role.md)[RBAC](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-an-rbac-role.md)[限制集群内资源操作](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-an-rbac-role.md)。

RBAC的权限策略仅支持允许（Allow）访问资源，不支持显式拒绝（Deny）访问资源。

## 相关文档

- 

如果预置的角色不满足需求，需要自定义RBAC获取集群内资源的访问权限，请参见[使用自定义](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-an-rbac-role.md)[RBAC](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-an-rbac-role.md)[限制集群内资源操作](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-an-rbac-role.md)。

- 

针对不同运维角色的完整授权流程（包含RAM授权和RBAC授权），请参见

- 

如果授权对象为集群与集群内应用的运维人员，请参见[场景二：授权对象为集群与集群内应用的运维人员](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/best-practices-of-authorization.md)。

- 

如果授权对象为集群内应用的开发人员，请参见[场景三：授权对象为集群内应用的开发人员](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/best-practices-of-authorization.md)。

- 

如果授权对象为集群内应用的权限管理员，请参见[场景四：授权对象为集群内应用的权限管理员](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/best-practices-of-authorization.md)。

- 

ACK提供的服务角色，请参见[容器服务](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ack-default-roles.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ack-default-roles.md)[服务角色](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ack-default-roles.md)。

- 

授权过程中如遇问题，请参见[授权管理](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-authorization-management.md)[FAQ](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-authorization-management.md)。

[上一篇：RBAC授权](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/rbac-authorization.md)[下一篇：使用自定义RBAC限制集群内资源操作](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-an-rbac-role.md)

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
