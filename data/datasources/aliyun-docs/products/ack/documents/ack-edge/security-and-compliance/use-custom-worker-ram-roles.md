# 为节点池指定自定义Worker RAM角色实现精细化权限控制-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/use-custom-worker-ram-roles

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

# 使用自定义Worker RAM角色实现节点池精细化权限控制

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

ACK托管集群会自动创建一个所有节点共享的默认Worker RAM角色。当您通过默认的Worker RAM角色授权时，权限将会共享给集群内所有的节点，可能会存在非预期的权限扩散的风险。您可以在创建节点池时为其指定一个自定义的Worker RAM角色，通过为不同的节点池分配特定的角色，可以将每个节点池的权限隔离开，降低集群内所有节点共享相同权限的风险。

## 前提条件

[创建](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)，且集群为1.22及以上版本。

## 步骤一：创建RAM角色

您可以通过控制台、OpenAPI或Terraform等方式创建一个Worker RAM角色。

重要

- 

RAM角色的名称不能以KubernetesMasterRole-或KubernetesWorkerRole-开头。

- 

RAM角色的受信服务必须是云服务。

### 通过控制台创建RAM角色

通过控制台创建RAM角色的具体操作，请参见[创建普通服务角色](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)。

### 通过OpenAPI或Terraform创建RAM角色

- 

[通过](products/ram/documents/developer-reference/api-ram-2015-05-01-createrole.md)[OpenAPI](products/ram/documents/developer-reference/api-ram-2015-05-01-createrole.md)[创建](products/ram/documents/developer-reference/api-ram-2015-05-01-createrole.md)[RAM](products/ram/documents/developer-reference/api-ram-2015-05-01-createrole.md)[角色](products/ram/documents/developer-reference/api-ram-2015-05-01-createrole.md)

- 

[通过](https://help.aliyun.com/zh/terraform/create-and-authorize-a-role-by-using-terraform)[Terraform](https://help.aliyun.com/zh/terraform/create-and-authorize-a-role-by-using-terraform)[创建](https://help.aliyun.com/zh/terraform/create-and-authorize-a-role-by-using-terraform)[RAM](https://help.aliyun.com/zh/terraform/create-and-authorize-a-role-by-using-terraform)[角色](https://help.aliyun.com/zh/terraform/create-and-authorize-a-role-by-using-terraform)

通过OpenAPI或Terraform创建RAM角色，请确保指定的角色信任策略已配置如下内容。如需修改RAM角色信任策略，请参见[修改](products/ram/documents/user-guide/edit-the-trust-policy-of-a-ram-role.md)[RAM](products/ram/documents/user-guide/edit-the-trust-policy-of-a-ram-role.md)[角色的信任策略](products/ram/documents/user-guide/edit-the-trust-policy-of-a-ram-role.md)。

{ "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Principal": { "Service": [ "ecs.aliyuncs.com" ] } } ], "Version": "1" }

## 步骤二：为新建节点池指定Worker RAM角色

重要

您只能在创建集群或创建节点池时使用自定义的Worker RAM角色。节点池创建后，已有的Worker RAM角色不支持修改。

[容器服务管理控制台](https://cs.console.aliyun.com)创建集群或节点池时，您可以在节点池的高级选项配置中，将Worker RAM 角色选择为[步骤一：创建](products/ack/documents/ack-edge/security-and-compliance/use-custom-worker-ram-roles.md)[RAM](products/ack/documents/ack-edge/security-and-compliance/use-custom-worker-ram-roles.md)[角色](products/ack/documents/ack-edge/security-and-compliance/use-custom-worker-ram-roles.md)所创建的自定义角色。

具体操作，请参见[创建集群时节点池高级选项](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)、[创建节点池时高级配置](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-node-pool.md)。

### 授予RAM 用户或 RAM 角色所需的权限

当您通过 RAM 用户或 RAM 角色使用本功能时，还需额外被授予ram:PassRole权限策略，以授权该用户或角色可以使用指定的 RAM 角色作为 Worker RAM 角色。具体操作，请参见[创建自定义权限策略](products/ram/documents/create-a-custom-policy.md)、[为](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)、[为](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色授权](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。

说明

如果 RAM 用户或 RAM 角色已被授予 AliyunCSFullAccess 权限，则无需额外进行ram:PassRole授权。

RAM 权限策略示例如下：

| 授权使用特定的 RAM 角色 | 授权使用所有 RAM 角色 |
| --- | --- |
| { "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "ram:PassRole", "Resource": [ "<role_arn>" // 替换为 RAM 角色的 ARN。 ], "Condition": { "StringEquals": { "acs:Service": [ "cs.aliyuncs.com" ] } } } ] } 请参见 [如何查看](products/ram/documents/support/faq-about-ram-roles-and-sts-tokens.md) [RAM](products/ram/documents/support/faq-about-ram-roles-and-sts-tokens.md) [角色的](products/ram/documents/support/faq-about-ram-roles-and-sts-tokens.md) [ARN？](products/ram/documents/support/faq-about-ram-roles-and-sts-tokens.md) 获取 RAM 角色 ARN。 | { "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "ram:PassRole", "Resource": "*", "Condition": { "StringEquals": { "acs:Service": [ "cs.aliyuncs.com" ] } } } ] } |


## 相关操作

创建RAM角色后，该RAM角色默认没有任何权限。

- 

如需通过控制台创建自定义策略并授权，请参见[创建自定义权限策略](products/ram/documents/create-a-custom-policy.md)、[为](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色授权](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。

- 

如需通过OpenAPI创建自定义策略并授权，请参见[CreatePolicy - 创建一个权限策略](products/ram/documents/developer-reference/api-ram-2015-05-01-createpolicy.md)、[AttachPolicyToRole - 为指定角色添加权限](products/ram/documents/developer-reference/api-ram-2015-05-01-attachpolicytorole.md)。

- 

如需通过Terraform创建自定义策略并授权，请参见[通过](https://help.aliyun.com/zh/terraform/create-and-authorize-a-role-by-using-terraform)[Terraform](https://help.aliyun.com/zh/terraform/create-and-authorize-a-role-by-using-terraform)[创建](https://help.aliyun.com/zh/terraform/create-and-authorize-a-role-by-using-terraform)[RAM](https://help.aliyun.com/zh/terraform/create-and-authorize-a-role-by-using-terraform)[角色并授权](https://help.aliyun.com/zh/terraform/create-and-authorize-a-role-by-using-terraform)。

当Worker RAM角色不再需要某些权限时，请及时将这些权限移除，请参见[为](products/ram/documents/remove-permissions-from-a-ram-role.md)[RAM](products/ram/documents/remove-permissions-from-a-ram-role.md)[角色移除权限](products/ram/documents/remove-permissions-from-a-ram-role.md)。

[上一篇：使用ServiceAccount Token卷投影](products/ack/documents/ack-edge/security-and-compliance/enable-service-account-token-volume-projection.md)[下一篇：为Pod动态配置阿里云产品白名单](products/ack/documents/ack-edge/security-and-compliance/dynamically-add-the-ip-addresses-of-pods-to-the-whitelists-of-alibaba-cloud-services.md)

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
