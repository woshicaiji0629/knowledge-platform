# 删除ACK Edge集群及后续资源释放与失败处理-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/untitled-document

# 如何删除ACK Edge集群
您可以通过容器服务管理控制台删除不再使用的集群。删除集群页面展示了集群内已有的资源，您可以查看即将被删除的资源，并按需选择是否保留资源。请仔细阅读页面中的提示信息，确保您是在知晓操作风险的情况下进行删除操作。
## 集群删除及节点释放规则
删除集群时，将依次删除集群内的节点池，以完成集群内节点的释放。
对于集群内的边缘节点池：
集群删除后，需要您手动清理节点上的系统组件。相关操作，请参见[移除边缘节点](remove-edge-nodes.md)。
对于集群内的云端节点池：
已开启期望节点数的节点池：节点池内所有按量付费的节点将会被释放，包年包月的节点不会被释放。如需释放包年包月的节点，请登录[ECS](https://ecs.console.aliyun.com/)[控制台](https://ecs.console.aliyun.com/)，将包年包月的节点转换为按量付费的节点，再在[ECS](https://ecs.console.aliyun.com/)[控制台](https://ecs.console.aliyun.com/)释放节点。节点被释放后，节点的系统盘也随之释放。
未开启期望节点数的节点池：节点池内通过手动及自动添加到节点池的已有节点、包年包月的节点不会被释放，其余节点将被释放。
关于如何判断节点池是否开启了期望节点数，请参见[如何判断节点池是否已经开启期望节点数？](../../ack-managed-and-ack-dedicated/user-guide/delete-a-cluster-1.md)。
## 操作步骤
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，选择所需的集群并单击右侧的更多>删除。
在删除集群面板，确认将自动删除的资源（例如ECS、ECI、ACS等），按需选择待保留的资源，仔细阅读页面上关于资源删除和计费的注意事项，并按照页面提示完成删除操作。
## 释放资源
集群删除后，请根据控制台的资源提示，依次确认是否需要清除，确认资源无需使用之后，请及时通过控制台或OpenAPI手动清理这些资源。例如：
删除包年包月的ECS节点
控制台：参见[包年包月转按量付费](../../../../ecs/documents/change-the-billing-method-of-an-instance-from-subscription-to-pay-as-you-go-1.md)将包年包月ECS实例转换为按量付费ECS实例，再[释放实例](../../../../ecs/documents/user-guide/release-an-instance.md)。
OpenAPI：通过API接口[ModifyInstanceChargeType](../../../../ecs/documents/api-modifyinstancechargetype.md)将包年包月ECS实例转换为按量付费ECS实例，再[通过](../../../../ecs/documents/user-guide/release-an-instance.md)[API](../../../../ecs/documents/user-guide/release-an-instance.md)[释放实例](../../../../ecs/documents/user-guide/release-an-instance.md)。
删除专有网络VPC，相关操作请参见：
控制台：[强制删除](../../../../vpc/documents/unable-to-delete-vpc.md)[VPC](../../../../vpc/documents/unable-to-delete-vpc.md)[实例](../../../../vpc/documents/unable-to-delete-vpc.md)。
OpenAPI：[DeleteVpc - 删除一个](../../../../vpc/documents/developer-reference/api-vpc-2016-04-28-deletevpc.md)[VPC](../../../../vpc/documents/developer-reference/api-vpc-2016-04-28-deletevpc.md)。
删除包年包月的CLB实例，需要将其转换为按量付费实例后进行删除。相关操作请参见：
控制台：参见[包年包月转为按量付费](../../../../slb/documents/classic-load-balancer/support/faq-about-billing.md)将包年包月的CLB实例转换为按量付费的CLB实例，然后再[释放负载均衡实例](../../../../slb/documents/classic-load-balancer/getting-started/release-a-clb-instance.md)。
删除关联的日志服务SLS Project，相关操作请参见：
控制台：[删除项目](../../../../sls/documents/manage-a-project.md)[Project](../../../../sls/documents/manage-a-project.md)。
OpenAPI：[DeleteProject - 删除指定](../../../../sls/documents/developer-reference/api-sls-2020-12-30-deleteproject.md)[Project](../../../../sls/documents/developer-reference/api-sls-2020-12-30-deleteproject.md)。
删除NAT网关，相关操作请参见：
控制台：[创建和管理公网](../../../../nat-gateway/documents/user-guide/use-internet-nat-gateway-for-public-network-access.md)[NAT](../../../../nat-gateway/documents/user-guide/use-internet-nat-gateway-for-public-network-access.md)[网关实例](../../../../nat-gateway/documents/user-guide/use-internet-nat-gateway-for-public-network-access.md)。
OpenAPI：[DeleteNatGateway - 删除指定的](../../../../nat-gateway/documents/developer-reference/api-vpc-2016-04-28-deletenatgateway-natgws.md)[NAT](../../../../nat-gateway/documents/developer-reference/api-vpc-2016-04-28-deletenatgateway-natgws.md)[网关](../../../../nat-gateway/documents/developer-reference/api-vpc-2016-04-28-deletenatgateway-natgws.md)。
删除交换机，相关操作请参见：
控制台：[删除交换机](../../../../vpc/documents/user-guide/create-and-manage-vswitch.md)。
OpenAPI：[DeleteVSwitch - 删除交换机](../../../../vpc/documents/developer-reference/api-vpc-2016-04-28-deletevswitch.md)。
删除安全组，相关操作请参见：
控制台：[删除安全组](../../../../ecs/documents/user-guide/manage-security-groups.md)。
OpenAPI：[DeleteSecurityGroup - 删除安全组](../../../../ecs/documents/developer-reference/api-ecs-2014-05-26-deletesecuritygroup.md)。
## 常见问题
### 删除集群失败怎么办？
如果您在阿里云资源编排服务ROS（Resource Orchestration Service）创建的资源下手动添加了一些资源，ROS是没有权限删除这些资源的。例如在ROS创建的VPC下手动添加了一个VSwitch，这样就会导致ROS删除时无法处理该VPC，从而最终删除集群失败。
容器服务提供了强制删除集群的功能。通过强制删除功能，您可以在集群删除失败后，强制删除集群记录和ROS资源栈。但是，强制删除操作不会自动释放ROS创建的资源及您手动创建的这些资源，您需要手动进行释放。
集群删除失败时，会显示如下信息。
单击删除失败的集群对应的更多>删除。
在弹出的对话框里，您可以看到删除失败的资源，单击确定，即可删除集群和ROS资源栈。
说明
如果在删除集群提示页面，选中保留资源，则不会释放这些资源，您需要手动释放。
### 如何关闭集群删除保护状态？
如果集群开启了集群删除保护功能，在删除集群时，页面会提示需先关闭删除保护。您可以执行以下步骤关闭集群删除保护功能：
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表的操作列，选择更多>关闭集群删除保护状态。
在关闭集群删除保护状态对话框中，关闭集群删除保护开关。
### 如何判断节点池是否已经开启期望节点数？
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点池。
单击目标节点池名称，单击基本信息页签，在节点配置区域，查看期望节点数是否开启。如果未开启，期望节点数后面则显示-。
### 集群删除中或删除失败时，是否会产生计费？
集群处于删除中（deleting）、删除失败（delete_failed）状态时，不会产生集群管理计费以及节点管理费，但阿里云仍然会收取其他云产品产生的资源费用。关于集群生命周期的更多信息，请参见[集群生命周期](../../ack-managed-and-ack-dedicated/user-guide/cluster-abnormal-states.md)；关于ACK Edge集群的计费说明，请参见[ACK Edge](../product-overview/billing-of-ack-edge-clusters.md)[集群计费说明](../product-overview/billing-of-ack-edge-clusters.md)。
### 集群处于异常状态不活跃（inactive）或不可用（unavailable）时，ACK Edge集群如何计费？
集群处于“不活跃（inactive）”或“不可用（unavailable）”状态时，仍会继续收取相关集群管理费用和云产品资源费用。计费详细说明，请参见[ACK Edge](../product-overview/billing-of-ack-edge-clusters.md)[集群计费说明](../product-overview/billing-of-ack-edge-clusters.md)。
### 集群处于哪些生命周期状态时，将不会产生集群管理费用？
集群处于初始化中（initial）、创建失败（failed）、删除中（deleting）、删除失败（delete_failed）、已删除（deleted，该状态用户不可见）状态时，不会产生集群管理计费，但阿里云仍然会收取其他云产品产生的资源费用。关于集群生命周期的更多信息，请参见[集群生命周期](../../ack-managed-and-ack-dedicated/user-guide/cluster-abnormal-states.md)；关于ACK Edge集群的计费说明，请参见[ACK Edge](../product-overview/billing-of-ack-edge-clusters.md)[集群计费说明](../product-overview/billing-of-ack-edge-clusters.md)。
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
