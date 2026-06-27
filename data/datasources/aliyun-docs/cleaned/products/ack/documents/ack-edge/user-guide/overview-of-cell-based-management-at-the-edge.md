# 云边协同场景下节点的统一管理运维-节点池-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/overview-of-cell-based-management-at-the-edge

# 节点池概述
在云边协同场景下，不同分组的节点间存在网络不互通、资源不共享、资源异构和应用独立等隔离属性。容器服务 Edge 版提供了节点池（NodePool）功能，将节点按照特定属性分组为节点池，以节点池的维度对不同分组的节点进行统一管理和运维。本文简要介绍节点池的概念，分类，以及工作原理。
## 节点池分类
在云边协同场景下，容器服务 Edge 版的节点池分成两种类型：云端节点池和边缘节点池。
云端节点池：云端节点池管理与集群位于同VPC中的云端ECS资源，其节点池与ACK托管集群Pro版[节点池](../../node-pool-management-18.md)保持一致。
云端节点池（默认）：ACK Edge集群创建时会自动创建一个云端节点池（default-nodepool），用于部署Edge系统控制面的组件。
重要
default-nodepool云端节点池不能删除且至少保持有一个节点，否则Edge集群能力将无法正常使用。
云端节点池（弹性）：开启[节点自动伸缩](https://help.aliyun.com/zh/document_detail/2746875.html)的云端节点池，可以充分利用云上弹性能力。
边缘节点池：管理线下分散地域的各种类型的节点集合，例如不同地域的ECS节点、IDC节点、其他厂商云节点，以及分布在工厂、门店、车辆和船舶中的服务器节点。
## 云端节点池
云端节点池的属性和操作与ACK托管集群Pro版一致。请参见[云端节点池概述](../../ack-managed-and-ack-dedicated/user-guide/node-pool-overview.md)。
## 边缘节点池
边缘节点池作为边缘节点分组的抽象，[创建边缘节点池](edge-node-pool-management.md)时您需要预先明确该节点池内节点的一些[基本属性](edge-node-pool-management.md)，如云边网络连接、节点间网络互通、Pod网络模式等。另外，我们也建议您根据其他属性，如CPU/GPU、地域、AMD64/Arm64等，将边缘节点分散到多个边缘节点池中管理。
在创建完成后，您可以通过[编辑边缘节点池](edge-node-pool-management.md)批量管理节点池内节点的标签和污点。当所有的边缘节点都移除集群后，您可以删除该边缘节点池。
当多个节点池都需要部署同一套应用时，您可以[使用应用集](node-pool-yurtappset-management.md)（YurtAppSet）将应用便捷地部署到多个节点池中。YurtAppSet提供了灵活的响应机制以感知节点池标签的变化，统一管理多个节点池的工作负载配置，如实例数量和软件版本等。
原生Kubernetes Service的后端可以分布在集群中任意节点。因此，当两个边缘节点池间网络不互通，跨越不同边缘节点池的Service流量，大概率会出现访问不可达或者访问效率低下的问题。[Service](configure-a-service-topology.md)[流量拓扑](configure-a-service-topology.md)支持将Service流量限制在同一个边缘节点池（或边缘节点）上，从而避免边缘场景下跨网域访问导致的Service网络不通的问题。
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
