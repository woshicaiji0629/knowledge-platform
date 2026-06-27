# 配置并管理集群安全组-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/configure-security-group-rules-to-enforce-access-control-on-ack-clusters

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

# 配置并管理集群安全组

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

ACK集群使用安全组来约束控制面节点和Worker节点之间的网络流量。安全组还用于控制节点、VPC资源和外部IP地址之间的流量。创建集群或节点池时，系统会默认自动为您分配一个安全组，您也可以指定关联已有安全组。指定已有安全组时，系统默认不会为安全组配置额外的访问规则，请自行管理并收敛安全组规则。

您可以通过添加安全组规则，允许或禁止安全组内的ECS实例对公网或私网的访问。更多信息，请参见[安全组概述](products/ecs/documents/user-guide/overview-44.md)、[添加安全组规则](products/ecs/documents/user-guide/add-a-security-group-rule.md)。

## 集群安全组出、入规则推荐配置

### 普通安全组

入方向

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 集群访问规则 | 协议 | 端口 | 授权对象 |
| --- | --- | --- | --- |
| 推荐范围 | ICMP | -1/-1（不限制端口） | 0.0.0.0/0 |
| 所有协议 | -1/-1（不限制端口） | 集群默认安全组 ID 集群 Pod 网络地址段（Flannel 网络模式添加安全组规则，Terway 网络模式不添加安全组规则） |  |
| 最小范围 | 所有协议 | 53/53（DNS） | 集群默认安全组 ID 集群 Pod 网络地址段（Flannel 网络模式添加安全组规则，Terway 网络模式不添加安全组规则） |
| ICMP | -1/-1（不限制端口） |  |  |
| TCP | 10250（kubelet） 10255（kubelet） 443（Webhook） 6443（ API Server ） 8082（heapster） 集群内提供 Webhook 服务的应用或组件容器监听的端口（例如 Gatekeeper 组件监听的 8443 端口） |  |  |
| TCP | 9082 | [Poseidon](products/ack/documents/serverless-kubernetes/user-guide/using-the-network-policy-networkpolicy.md) 组件使用的端口。如不使用，则无需配置。 |  |
| 所有协议 | 所有应用或组件期望被访问的端口 | 所有应用或组件期望被访问的来源地址或者来源安全组 |  |


出方向

- 

- 

- 

- 

- 

- 

- 

| 集群访问规则 | 协议 | 端口 | 授权对象 |
| --- | --- | --- | --- |
| 推荐范围 | 所有协议 | -1/-1（不限制端口） | 0.0.0.0/0 |
| 最小范围 | 所有协议 | -1/-1（不限制端口） | 100.64.0.0/10 （云产品网段） |
| 所有协议 | 53/53（DNS） | 集群 APIServer SLB 地址 集群默认安全组 ID 集群 Pod 网络地址段（Flannel 网络模式添加安全组规则，Terway 网络模式不添加安全组规则） |  |
| TCP | 10250（kubelet） 10255（kubelet） 443（API Server） 6443（API Server） |  |  |
| 所有协议 | 所有应用或组件期望访问的端口 | 所有应用或组件期望访问的目的地址或者目的安全组 |  |


### 企业安全组

入方向

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 集群访问规则 | 协议 | 端口 | 授权对象 |
| --- | --- | --- | --- |
| 推荐范围 | ICMP | -1/-1（不限制端口） | 0.0.0.0/0 |
| 所有协议 | -1/-1（不限制端口） | 集群所属的 VPC 网段 集群所属的附加 VPC 网段 集群 Pod 网络地址段（Flannel 网络模式添加安全组规则，Terway 网络模式不添加安全组规则） |  |
| 最小范围 | 所有协议 | 53/53（DNS） | 集群内所有关联的 vSwitch 网段，包括 Node vSwitch 和 Pod vSwitch 集群 Pod 网络地址段（Flannel 网络模式添加安全组规则，Terway 网络模式不添加安全组规则） |
| ICMP | -1/-1（不限制端口） |  |  |
| TCP | 10250（Kubelet） 10255（Kubelet） 443（Webhook） 6443（APIServer） 8082（heapster） 集群内提供 Webhook 服务的应用或组件容器监听的端口（例如 Gatekeeper 组件监听的 8443 端口） |  |  |
| TCP | 9082 | [Poseidon](products/ack/documents/serverless-kubernetes/user-guide/using-the-network-policy-networkpolicy.md) 组件使用的端口。如不使用，则无需配置。 |  |
| 所有协议 | 所有应用或组件期望被访问的端口 | 所有应用或组件期望被访问的来源地址或者来源安全组 |  |


出方向

- 

- 

- 

- 

- 

- 

- 

| 集群访问规则 | 协议 | 端口 | 授权对象 |
| --- | --- | --- | --- |
| 推荐范围 | 所有协议 | -1/-1（不限制端口） | 0.0.0.0/0 |
| 最小范围 | 所有协议 | -1/-1（不限制端口） | 100.64.0.0/10 （云产品网段） |
| 所有协议 | 53/53（DNS） | 集群 APIServer SLB 地址 集群内所有关联的 vSwitch 网段，包括 Node vSwitch 和 Pod vSwitch 集群 Pod 网络地址段（Flannel 网络模式添加安全组规则，Terway 网络模式不添加安全组规则） |  |
| TCP | 10250（Kubelet） 10255（Kubelet） 443（APIServer） 6443（APIServer） |  |  |
| 所有协议 | 所有应用或组件期望访问的端口 | 所有应用或组件期望访问的目的地址或者目的安全组 |  |


## 关闭安全组删除保护

为了防止集群关联的安全组被误删除，ACK会为所有集群关联的安全组开启删除保护功能。当您在ECS控制台释放安全组时遇到如下报错，表明该安全组被ACK开启了删除保护功能。

报错信息显示安全组状态为不可删除，原因为"存在实例，将实例移出安全组后再删除安全组"。

目前安全组的删除保护功能无法通过控制台或API手动关闭。只有当所有依赖该安全组的集群均被删除后，ACK才会自动释放对该安全组的删除保护。请依次查询ACK集群所关联的安全组，并删除所有依赖该安全组的集群。查询步骤如下。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称。单击基本信息页签，查看集群所在的安全组。

当所有依赖该安全组的集群均已删除后，您可以通过ECS控制台继续释放该安全组。如果释放失败，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)给容器服务团队。

关于如何删除安全组，请参见[删除安全组](products/ecs/documents/user-guide/delete-a-security-group-1.md)。

## 相关文档

- 

关于网络安全的最佳实践，例如默认允许或拒绝规则、命名空间隔离等，请参见[网络安全](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/network-security.md)。

- 

关于如何规划Kubernetes集群网络，包括ECS地址、Kubernetes Pod地址、Service地址等，请参见[ACK](products/ack/documents/plan-cidr-blocks-for-an-ack-cluster-2.md)[托管集群网络规划](products/ack/documents/plan-cidr-blocks-for-an-ack-cluster-2.md)。

[上一篇：集群维护窗口说明](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cluster-maintenance-window.md)[下一篇：管理命名空间与配额](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/manage-namespaces-and-resource-quotas-1.md)

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
