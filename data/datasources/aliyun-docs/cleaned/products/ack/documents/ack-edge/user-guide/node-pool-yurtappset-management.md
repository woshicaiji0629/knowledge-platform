# 使用应用集YurtAppSet将应用部署至多个节点池-容器服务Kubernetes版ACK-阿里云-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/node-pool-yurtappset-management

# 通过YurtAppSet应用集管理ACK Edge应用
在ACK Edge集群中，您可以使用应用集（YurtAppSet）将应用便捷地部署到多个节点池中。YurtAppSet提供了灵活的响应机制以感知节点池标签的变化，从而能够统一管理多个节点池的工作负载配置，如实例数量和软件版本等。本文将介绍如何使用YurtAppSet来高效地管理和部署ACK Edge集群的应用。
## 背景信息
传统方案
在边缘计算场景下，计算节点具有很明显的地域分布属性，相同的应用可能需要部署在不同地域下的计算节点上。以Deployment为例，传统的做法是先将相同地域的计算节点设置成相同的标签，然后创建多个Deployment，不同Deployment通过NodeSelectors选定不同的标签，从而实现将相同的应用部署到不同地域的需求。
随着地域分布越来越多，以及不同地域对应用的差异化需求，运维变得越来越复杂，具体表现在以下几个方面：
更新繁琐：当应用版本更新时，需要手动修改所有Deployment以保持应用在各地域的一致性，降低了更新效率。
管理复杂：随着管理地域的增多，需要人工地对不同地域的Deployment进行区分和维护，增加了运维工作量。
配置冗余：多个地域的Deployment配置高度相似，导致配置管理繁琐且易出错。
应用集管理方案
应用集（YurtAppSet）是容器服务 Edge 版提供的功能，旨在简化边缘计算场景下分散部署的复杂性。通过更上层的抽象，对多个工作负载（Workload资源，如Deployment）进行统一管理，比如创建、更新和删除等操作。
YurtAppSet提供以下能力，可以帮助您有效解决传统方案的更新效率低、管理复杂和配置冗余等问题，提高运维效率和应用部署的灵活性。
workloadTemplate：统一模板定义
YurtAppSet允许您通过单一的workloadTemplate定义来统一管理位于多个地域的工作负载。这种方式不仅减少了重复的部署配置，还可以让批量操作如创建、更新和删除变得更加高效和一致。
nodepoolSelector：自动化部署
YurtAppSet通过nodepoolSelector机制灵活选择目标节点池，实现了与节点池动态变化的同步。随着新节点池的创建或现有节点池的移除，nodepoolSelector将自动识别并匹配最新的合适节点池进行Workload分发部署，帮助您减轻运维负担。
workloadTweaks：地域差异化定制配置
当地域间的应用需求存在差异时，YurtAppSet提供了workloadTweaks功能，允许对特定区域的Workload进行定制化调整，从而满足各地域的特定要求，您无需独立管理或更新每个Workload。
## 创建应用集实例
ACK Edge集群为1.26及之后版本时，使用YurtAppSet部署。
ACK Edge集群为1.26之前版本时，使用UnitedDeployment部署。
## 1.26及之后版本
创建一个Workload模板为Deployment的YurtAppSet应用集实例。
完整的YAML示例模板如下：
apiVersion: apps.openyurt.io/v1beta1 kind: YurtAppSet metadata: name: example namespace: default spec: revisionHistoryLimit: 5 pools: - np1xxxxxx - np2xxxxxx nodepoolSelector: matchLabels: yurtappset.openyurt.io/type: "nginx" workload: workloadTemplate: deploymentTemplate: metadata: labels: app: example spec: replicas: 2 selector: matchLabels: app: example template: metadata: labels: app: example spec: containers: - image: nginx:1.19.1 imagePullPolicy: Always name: nginx workloadTweaks: - pools: - np2xxxxxx tweaks: replicas: 3 containerImages: - name: nginx targetImage: nginx:1.20.1 patches: - path: /metadata/labels/test operation: add value: test
相关字段的解释如下表所示：
| 字段 | 含义 | 是否必选 |
| --- | --- | --- |
| spec.pools | 指定需要部署应用的节点池名称列表（slice 类型，推荐优先使用 nodepoolSelector 指定 nodepool）。 | 否 |
| spec.nodepoolSelector | 通过 labelSelector 选择需要部署应用的节点池（当与 pools 同时指定时，取并集）。 nodepoolSelector 通过匹配 NodePool 资源的标签（metadata.Labels）来选择节点池。如需修改这些标签，请在集群控制台的自定义资源页面，找到并编辑相应 NodePool 的 YAML。 | 否 |
| spec.workload.workloadTemplate | 指定管理的 Workload 模板，目前支持 deploymentTemplate 和 statefulSetTemplate 模板。 | 是 |
| spec.workload.workloadTweaks | 指定对 Workload 的定制修改。 | 否 |
| spec.workload.workloadTweaks[*].pools | 指定该项修改应用在哪些节点池上（slice 类型）。 | 否 |
| spec.workload.workloadTweaks[*].nodepoolSelector | 通过 labelSelector 选择哪些节点池将会被修改。 | 否 |
| spec.workload.workloadTweaks[*].tweaks.replicas | 指定被修改的 workload 的 replicas 数。 | 否 |
| spec.workload.workloadTweaks[*].tweaks.containerImages | 指定被修改的 workload 的容器镜像。 | 否 |
| spec.workload.workloadTweaks[*].tweaks.patches | 通过 patch 字段可以修改 workloadTemplate 的任意字段。 | 否 |
| spec.workload.workloadTweaks[*].tweaks.patches[*].path | 指定需要修改的字段在 workloadTemplate 中的路径。 | 否 |
| spec.workload.workloadTweaks[*].tweaks.patches[*].operation | 指定需要在 path 上执行的操作（目前支持：add/remove/replace）。 | 否 |
| spec.workload.workloadTweaks[*].tweaks.patches[*].value | 指定修改后的最新取值（只对 add/replace 操作生效）。 | 否 |
| status.conditions | 表示 YurtAppSet 当前状态，包括节点池选中状态、workload 状态等。 |  |
| status.readyWorkloads | 表示 YurtAppSet 当前管理的 workload 中，所有副本都 ready 的 workload 数量。 |  |
| status.updatedWorkloads | 表示 YurtAppSet 当前管理的 workload 中，所有副本都已经更新到最新版本的 workload 数量。 |  |
| status.totalWorkloads | 表示 YurtAppSet 当前管理的 workload 数量。 |  |
## 1.26之前版本
创建一个Workload模板为Deployment的UnitedDeployment部署实例。
完整的YAML示例模板如下：
apiVersion: apps.kruise.io/v1alpha1 kind: UnitedDeployment metadata: name: example namespace: default spec: revisionHistoryLimit: 5 selector: matchLabels: app: example template: deploymentTemplate: metadata: creationTimestamp: null labels: app: example spec: selector: matchLabels: app: example template: metadata: creationTimestamp: null labels: app: example spec: containers: - image: nginx:1.19.3 imagePullPolicy: Always name: nginx dnsPolicy: ClusterFirst restartPolicy: Always topology: subsets: - name: cloud nodeSelectorTerm: matchExpressions: - key: alibabacloud.com/nodepool-id operator: In values: - np4b9781c40f0e46c581b2cf2b6160**** replicas: 2 - name: edge nodeSelectorTerm: matchExpressions: - key: alibabacloud.com/nodepool-id operator: In values: - np47832359db2e4843aa13e8b76f83**** replicas: 2 tolerations: - effect: NoSchedule key: apps.openyurt.io/taints operator: Exists
相关字段的解释如下表所示：
| 字段 | 含义 |
| --- | --- |
| spec.workloadTemplate | 代表支持的 Workload 模板，目前节点池支持 deploymentTemplate/statefulSetTemplate 两种模板。 |
| spec.topology.subsets | 指定多个节点池。 |
| spec.topology.subsets[*].name | 节点池的名称。 |
| spec.topology.pools[*].nodeSelectorTerm | 节点池的主机亲和性配置若需与节点池 NodePool 相对应，Key 使用 apps.openyurt.io/nodepool ，Values 使用节点池 ID。 说明 您可以在 节点池 页面，在对应云端和边缘侧的节点池 名称 的下方查看节点池 ID。 |
| spec.topology.pools[*].tolerations | 节点池的主机容忍性配置。 |
| spec.topology.pools[*].replicas | 每个节点池下 Pod 的实例数。 |
## 如何使用应用集管理边缘应用
应用版本升级：通过修改spec.workload.workloadTemplate中的字段触发升级流程，控制器把新的模板更新到各个节点池下的Workload中以触发节点池控制器升级Pod。
应用在某地域灰度更新：通过修改spec.workload.workloadTweak[*].containerImages配置，触发相应节点池下应用Pod的镜像更新。
应用在某地域扩缩容：通过修改spec.workload.workloadTweak[*].replicas配置，触发相应节点池下应用Pod的扩缩容操作。
应用需要部署到一个新的地域：新创建一个匹配spec.nodepoolSelector标签的节点池，YurtAppSet会感知到节点池资源的变化，自动为该节点池创建一个Workload。之后将该地域的节点加入该节点池即可。
应用需要在某个地域下线：删除对应地域的节点池，YurtAppSet会自动删除该地域对应的Workload。
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
