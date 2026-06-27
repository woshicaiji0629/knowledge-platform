# 集群节点资源自动扩缩容-节点自动伸缩-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/overview-of-node-scaling

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

# 云端节点伸缩概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

ACK Edge集群可以管理各种类型的线上线下节点资源，例如不同地域的ECS节点、IDC节点、其他厂商节云节点，以及分布在工厂、门店、车辆和船舶中的服务器节点，当线下节点资源不足时，节点自动伸缩能力可以为ACK Edge集群自动扩容云上节点，进行调度容量的补充。这种弹性的扩缩容能力能够极大地节省资源成本。

## 阅读前提示

为了让您更好地了解ACK提供的节点伸缩方案，并结合您的业务诉求进行方案选型，建议您在启用节点伸缩能力前阅读本篇概述。

阅读本文前，推荐您参见[Kubernetes](https://kubernetes.io/docs/concepts/workloads/autoscaling/)[官方文档](https://kubernetes.io/docs/concepts/workloads/autoscaling/)了解手动伸缩、自动伸缩、水平伸缩、垂直伸缩等伸缩概念。

## 工作原理

在Kubernetes中，节点伸缩的工作原理与传统意义上基于使用率阈值的模型有所差别。这也是从传统IDC或其他编排系统迁移到Kubernetes集群后往往需要解决的问题。

阈值是如何选择与判断的？

在一个集群中，部分热点节点的利用率可能较高，而其他节点的利用率可能较低。

- 

如果根据整个集群的平均资源利用率来决定是否弹性伸缩，使得热点节点的差异被平均，那么会造成对热点节点的扩缩不够及时。

- 

如果依据最高的节点利用率来决定是否弹性伸缩，那么会造成弹出资源的浪费，影响集群的整体服务。

弹出实例后如何缓解压力？

在Kubernetes集群中，应用以Pod为最小单元部署在集群的不同节点上。当一个Pod资源利用率较高时，即使该Pod所在的节点或者集群触发了弹性扩容，但该应用的Pod数量以及Pod对应的Limit并没有发生变化，节点负载的压力也无法转移到新扩容的节点上。

如何判断以及执行实例的缩容？

如果基于资源利用率的方式判断节点是否缩容，那么很有可能出现Request（资源请求）较大、但Usage（实际资源使用）很小的Pod被驱逐。当集群中这种类型的Pod较多时，会占用集群大量的调度资源，导致部分Pod无法调度。

如何判断节点的弹出？

节点伸缩会监听Pod是否处于调度失败的状态，以判断是否需要触发扩容。当Pod由于调度资源不足而调度失败时，节点伸缩会开始模拟调度，计算在开启弹性的节点池中哪个节点池可为这些Pod提供所需的节点资源，并在满足需求时弹出相应的节点。

说明

模拟调度时将一个开启弹性的节点池作为一个的抽象节点，开启弹性的节点池中配置的机型规格对应会成为抽象节点的CPU、内存或GPU的容量，且其配置的Label、Taint也会成为抽象节点的Label与Taint。模拟调度器会在调度模拟时，将该抽象节点纳入调度参考范围。符合调度条件时，调度模拟器会计算所需的节点数目，驱动节点池弹出节点。

如何判断节点的缩容？

节点伸缩仅缩容开启了弹性的节点池中的节点，无法管理静态节点（不在开启了弹性的节点池中的其他节点）。每个节点会单独判断是否进行缩容。当任意一个节点的调度利用率低于所设置的调度阈值时，就会触发缩容判断。此时，节点伸缩会尝试模拟驱逐节点上的负载，判断当前节点是否可以排水。部分特殊的Pod（例如kube-system命名空间的非DaemonSet Pod、PDB控制的Pod等）则会跳过该节点而选择其他的候选节点。当节点发生驱逐时，会先进行排水，将节点上的Pod驱逐到其他的节点，然后再下线该节点。

如何提高弹性伸缩的成功率？

弹性伸缩的成功率主要取决于以下两个因素：

- 

调度策略是否满足

配置开启弹性的节点池后，您需要先确认该节点池可以承载的Pod的调度策略范围。如果无法直接判断，您可以通过nodeSelector直接选择节点池的Label，来进行预弹模拟。

- 

资源配置是否充分

当模拟调度通过后，系统会选择开启弹性的节点池，以弹出实例。但开启弹性的节点池中配置的ECS规格库存会直接影响是否可以成功弹出实例。因此，推荐您配置多个可用区、多个不同机型组合，以提高弹出成功率。

如何提高弹性伸缩的速度？

- 

方法一：使用极速模式加速弹出速度。当开启弹性的节点池预热后（已完成一次扩容和一次缩容），节点池即可进入极速伸缩模式。更多信息，请参见[启用节点自动伸缩](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/auto-scaling-of-nodes.md)。

- 

方法二：使用自定义镜像的方式，以Alibaba Cloud Linux 3作为基础镜像，大大提升IaaS层的资源交付速度（50%）。更多信息，请参见[弹性优化之自定义镜像](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-custom-images.md)。

## 节点自动伸缩方案

节点自动伸缩指资源层弹性，即当集群的容量规划无法满足应用Pod调度时，自动扩缩节点资源，进行调度容量的补充。节点自动伸缩通过cluster-autoscaler组件，以轮询的方式，周期性地维护和检查集群状态，以发现满足扩缩容条件的情况，从而自动扩缩容集群节点。

### 伸缩速度与效率

- 

单次伸缩时，标准模式的伸缩速度约为60s，极速模式为50s。

- 

当达到1分钟的伸缩量级时，伸缩速度会遇到瓶颈，并且在不同规模（多节点池）、不同场景（连续伸缩）下，弹性速度也会有比较明显的抖动。例如，当节点池数量超过100时，伸缩速度将衰减为100～150s。

- 

使用轮询式模型，且受制于对集群状态维护的依赖，弹性灵敏度最低为5s。

## 注意事项

### 配额与限制

- 

在专有网络下创建的单个路由表可创建的自定义路由数限额是200条。如需更大的配额，请前往[配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=route)提交申请。关于其他资源的配额限制及升配详情，请参见[依赖底层云产品配额限制](products/ack/documents/product-overview/limits.md)。

- 

请合理配置开启自动伸缩的节点池的最大实例数，保证此范围内的节点所依赖的资源和配额充足，例如合理规划VPC网段、交换机等网络资源，以避免节点扩容失败。配置开启自动伸缩的节点池的最大实例数，请参见[配置实例数量](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/auto-scaling-of-nodes.md)。关于ACK的网络规划，请参见[Kubernetes](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/kubernetes-cluster-network-planning.md)[集群网络规划](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/kubernetes-cluster-network-planning.md)。

- 

节点伸缩功能不支持包年包月付费类型的节点。如需新建开启自动伸缩的节点池，请勿选择付费类型为包年包月。如需为已有节点池开启自动伸缩，请确保节点池内没有包年包月付费类型的节点。

### 依赖资源的维护

选择绑定EIP时，请勿通过ECS控制台直接删除节点伸缩扩容出的ECS节点，否则会导致EIP无法自动释放。

## 后续阅读

如在使用节点自动伸缩过程中遇到问题，您可以参见[节点自动伸缩常见问题](products/ack/documents/ack-edge/user-guide/auto-scaling-of-nodes.md)进行自排查。

展开查看节点自动伸缩的FAQ索引

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

- 

- 

- 

- 

| 分类 | 二级分类 | 跳转链接 |
| --- | --- | --- |
| 节点自动伸缩 的扩缩容行为 | [已知限制](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) |  |
| [扩容行为相关](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) | [cluster-autoscaler](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [组件使用哪些调度策略来判断不可调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [能否调度到开启了弹性的节点池？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [cluster-autoscaler](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [组件可模拟判断的资源有哪些？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [为什么节点自动伸缩组件无法弹出节点？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [如果一个伸缩组内配置了多资源类型的实例规格，弹性伸缩时如何计算这个伸缩组的资源呢？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [弹性伸缩时，如何在多个开启弹性的节点池之间进行选择？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [开启弹性的节点池如何配置自定义资源？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) |  |
| [缩容行为相关](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) | [为什么](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [cluster-autoscaler](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [组件无法缩容节点？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [如何启用或禁用特定](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [DaemonSet](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [的驱逐？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [什么类型的](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [可以阻止](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [cluster-autoscaler](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [组件移除节点？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) |  |
| [拓展支持相关](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) | [cluster-autoscaler](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [组件是否支持](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [CRD？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) |  |
| 自定义的扩缩容行为 | [通过](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [控制扩缩容行为](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) | [如何延迟](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [cluster-autoscaler](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [组件对不可调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [的扩容反应时间？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) |
| [通过节点控制扩缩容行为](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) | [如何指定节点不被](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [cluster-autoscaler](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [组件缩容？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [如何通过](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [Pod Annotation](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [影响](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [cluster-autoscaler](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [组件的节点缩容？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) |  |
| cluster-autoscaler 组件 相关 | [如何升级](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [cluster-autoscaler](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [组件至最新版本？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [哪些操作会触发](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [cluster-autoscaler](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [组件自动更新？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) [托管集群已经完成了角色授权，但节点伸缩活动仍然无法正常运行？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-node-auto-scaling.md) |  |


[上一篇：云上弹性](products/ack/documents/ack-edge/user-guide/cloud-elasticity.md)[下一篇：启用节点自动伸缩](products/ack/documents/ack-edge/user-guide/auto-scaling-of-nodes.md)

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
