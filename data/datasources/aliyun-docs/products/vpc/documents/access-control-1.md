# VPC访问控制功能介绍与使用-专有网络VPC-阿里云

Source: https://help.aliyun.com/zh/vpc/access-control-1

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

# 使用专有网络VPC访问控制功能

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/vpc)

[我的收藏](https://help.aliyun.com/my_favorites.html)

为保证资源的数据安全，您可以通过访问控制策略，对专有网络VPC的访问进行控制，允许被授权的用户访问资源。

## 概述

专有网络VPC支持的访问控制功能包括：

- 

网络ACL：网络ACL是专有网络VPC中的网络访问控制功能。您可以在专有网络VPC中创建网络ACL并添加入方向和出方向规则。创建网络ACL后，您可以将网络ACL与交换机绑定，实现对交换机中ECS实例流量的访问控制。关于网络ACL的详细介绍，请参见[网络](products/vpc/documents/network-acl-overview.md)[ACL](products/vpc/documents/network-acl-overview.md)[概述](products/vpc/documents/network-acl-overview.md)。

- 

安全组：安全组是一种虚拟防火墙，用于控制安全组内ECS实例的入流量和出流量，从而提高ECS实例的安全性。更多信息，请参见[安全组概述](products/vpc/documents/user-guide/security-group.md)。

## 使用网络ACL功能

网络ACL是专有网络VPC中的网络访问控制功能。您可以在专有网络VPC中创建网络ACL并添加入方向和出方向规则。创建网络ACL后，您可以将网络ACL与交换机绑定，实现对交换机中ECS实例流量的访问控制。

### 配置网络ACL

网络ACL可以通过以下方式进行配置：

- 

登录专有网络控制台：关于如何通过专有网络控制台配置网络ACL，请参见[使用网络](products/vpc/documents/work-with-network-acls.md)[ACL](products/vpc/documents/work-with-network-acls.md)。

- 

调用相关API：您可以通过调用以下API配置网络ACL。

- 

[CreateNetworkAcl](products/vpc/documents/api-createnetworkacl.md)：创建网络ACL。

- 

[AssociateNetworkAcl](products/vpc/documents/api-associatenetworkacl.md)：绑定网络ACL至交换机。

- 

[ModifyNetworkAclAttributes](products/vpc/documents/api-modifynetworkaclattributes.md)：修改网络ACL的属性。

- 

[DescribeNetworkAcls](products/vpc/documents/api-describenetworkacls.md)：查看网络ACL的列表信息。

- 

[UpdateNetworkAclEntries](products/vpc/documents/api-updatenetworkaclentries.md)：更新网络ACL规则。

- 

[DescribeNetworkAclAttributes](products/vpc/documents/api-describenetworkaclattributes.md)：查询网络ACL的详细信息。

- 

[UnassociateNetworkAcl](products/vpc/documents/api-unassociatenetworkacl.md)：解除网络ACL与交换机的绑定。

- 

[CopyNetworkAclEntries](products/vpc/documents/api-copynetworkaclentries.md)：复制网络ACL规则。

- 

[DeleteNetworkAcl](products/vpc/documents/api-deletenetworkacl.md)：删除网络ACL。

- 

通过阿里云SDK设置ACL：您可以通过[阿里云](https://next.api.aliyun.com/api-tools/sdk/Ecs?version=2014-05-26&language=java-async-tea)[SDK](https://next.api.aliyun.com/api-tools/sdk/Ecs?version=2014-05-26&language=java-async-tea)配置网络ACL规则，阿里云SDK提供Java、Python、PHP等多种编程语言的SDK。

- 

通过CLI命令设置ACL：您可以通过命令行工具CLI配置网络ACL。关于CLI的更多信息，请参见[什么是阿里云](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)[CLI？](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)。

### 网络ACL应用

您可以通过网络ACL的功能特性和规则说明来自定义网络ACL的入方向和出方向规则。设置了网络ACL的入方向和出方向规则后，您可以更灵活的控制专有网络VPC内云资源的入方向和出方向的流量。更多信息，请参见[网络](products/vpc/documents/network-acl-overview.md)[ACL](products/vpc/documents/network-acl-overview.md)[概述](products/vpc/documents/network-acl-overview.md)和[典型应用](products/vpc/documents/typical-applications.md)。

### 网络ACL使用实例

您可以通过网络ACL功能限制不同交换机下ECS实例或者限制本地数据中心与云上的互通。具体操作，请参见[限制不同交换机下的](products/vpc/documents/manage-intercommunication-among-ecs-instances-connected-to-different-vswitches.md)[ECS](products/vpc/documents/manage-intercommunication-among-ecs-instances-connected-to-different-vswitches.md)[间的互通](products/vpc/documents/manage-intercommunication-among-ecs-instances-connected-to-different-vswitches.md)和[限制本地数据中心与云上的互通](products/vpc/documents/manage-communication-between-a-data-center-and-a-vpc.md)。

## 使用安全组功能

安全组是一种虚拟防火墙，用于控制安全组内ECS实例的入流量和出流量，从而提高ECS实例的安全性。安全组具备状态检测和数据包过滤能力，您可以基于安全组的特性和安全组规则的配置在云端划分安全域。

### 安全组和安全组规则

安全组分为普通安全组和企业安全组。企业安全组面向企业级场景，可以容纳更多的实例、弹性网卡和私网IP，而且访问策略更加严格。

- 

实例加入安全组的规则如下：实例至少加入一个安全组，可以同时加入多个安全组。实例上挂载的弹性网卡中，辅助网卡可以加入和实例不同的安全组。实例不支持同时加入普通安全组和企业安全组。

- 

安全组在未添加安全组规则时，自身已经具有控制出入流量的一些特性。在这些特性基础上，您可以继续新增、修改安全组规则更精细地控制出入流量。新增、修改安全组规则后，会自动应用于安全组内所有实例。安全组规则支持针对IP地址、CIDR地址块、其他安全组、前缀列表授权。更多信息，请参见[添加安全组规则](products/ecs/documents/user-guide/add-a-security-group-rule.md)。

- 

在控制台创建安全组时，系统会自动添加默认规则，您可以根据需要维护这些规则。

### 安全组使用指导

使用安全组控制实例流量的典型使用流程如下：

- 

创建安全组。

- 

添加安全组规则。

- 

将实例加入安全组。

- 

按需管理已有安全组和安全组规则。

使用安全组控制辅助网卡流量的典型使用流程如下：

- 

创建安全组。

- 

添加安全组规则。

- 

将辅助网卡加入安全组。

- 

将辅助网卡绑定至实例。

- 

按需管理已有安全组和安全组规则。

关于安全组的具体操作和应用案例，请参见[创建安全组](products/ecs/documents/user-guide/create-a-security-group-1.md)和[安全组应用案例](products/ecs/documents/user-guide/security-groups-for-different-use-cases.md)。

### 安全组配置案例

当您创建VPC类型的ECS实例时，可以使用系统提供的默认安全组规则，也可以选择VPC中已有的其他安全组。关于安全组配置案例，请参见[ECS](products/vpc/documents/user-guide/configure-security-groups-in-different-scenarios.md)[安全组配置案例](products/vpc/documents/user-guide/configure-security-groups-in-different-scenarios.md)。

[上一篇：专有网络VPC自定义权限策略参考](products/vpc/documents/vpc-custom-permission-policy-reference.md)[下一篇：使用标签限制 RAM 用户管理 VPC](products/vpc/documents/use-tags-to-restrict-ram-users-ability-to-manage-vpcs.md)

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
