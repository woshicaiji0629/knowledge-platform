# 基于gatekeeper组件配置Pod级别的安全策略管理-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/security-and-compliance/configure-and-enforce-ack-pod-security-policies

# 通过安全策略管理配置Pod的安全策略
为了满足集群合规性要求、提升集群安全性，推荐您启用安全策略管理功能。安全策略管理功能提供了符合Kubernetes容器应用场景的安全策略规则，包括Infra（基础设施层资源）、Compliance（Kubernetes合规规范）、PSP（基于PodSecurityPolicy能力的拓展）和K8s-general（通用策略）维度。您可以在控制台为容器应用开启或自定义安全策略，验证Pod的部署和更新是否安全可控。
## 策略治理介绍
自Kubernetes 1.21起，PodSecurityPolicy（PSP）被标记为弃用（Deprecated）状态。为此，ACK升级了原先基于PSP的策略管理功能。基于使用[OPA](https://www.openpolicyagent.org/)策略的Gatekeeper Admission Controller，ACK扩展了相应的策略治理状态统计、日志上报检索等能力，同时内置了种类丰富的策略治理规则库，提供符合更多Kubernetes应用场景的策略规则。在规则配置上，您可以在控制台上白屏化配置，降低使用策略治理相关能力的门槛。
## 前提条件
集群版本为1.16及以上。如需升级集群，请参见[手动升级集群](../user-guide/update-the-kubernetes-version-of-an-ack-cluster.md)。
如需使用RAM用户进行策略管理时，请确保该RAM用户拥有以下授权：
cs:DescribePolicies：列举策略治理规则库列表
cs:DescribePoliceDetails：获取策略规则模板详情
cs:DescribePolicyGovernanceInCluster：获取集群策略治理详情
cs:DescribePolicyInstances：获取集群中当前部署的策略实例列表
cs:DescribePolicyInstancesStatus：获取集群当前不同策略类型对应的实例部署状态
cs:DeployPolicyInstance：在指定集群中部署策略规则实例
cs:DeletePolicyInstance：在指定集群中删除策略规则实例
cs:ModifyPolicyInstance：在指定集群中修改策略规则实例
关于如何自定义RAM授权策略，请参见[使用](../user-guide/create-a-custom-ram-policy.md)[RAM](../user-guide/create-a-custom-ram-policy.md)[授予集群及云资源访问权限](../user-guide/create-a-custom-ram-policy.md)。
## 安全策略组件对比
ACK提供两种安全策略组件形态：托管版与非托管版。集群在同一时间只能启用其中一种。两者详细对比如下。
| 差异项 | 托管版 | 非托管版 |
| --- | --- | --- |
| 部署模式 | 控制面托管：部署在集群控制面，由 ACK 全面托管 | 数据面部署：通过工作负载的形式部署在集群中，默认安装在 kube-system 命名空间下，会占用 Worker 节点的 Pod 资源 |
| 适用集群 | 1.30 及以上版本的 [Auto Mode](../user-guide/auto-mode-overview.md) [集群](../user-guide/auto-mode-overview.md) | 1.16 及以上版本的 ACK 托管集群 、 ACK 专有集群 |
| 启用参数配置 | 组件的启动参数由系统默认配置，不支持自定义 | 可自定义修改组件的启动参数 |
| 核心组件安装 | managed-gatekeeper managed-policy-template-controller 在 控制台的 组件管理 页面，托管版组件卡片将显示托管 。 | gatekeeper policy-template-controller 日志采集组件（logtail-ds 或 loongcollector） |
| 策略日志采集 | 通过 [采集](../user-guide/collect-control-plane-component-logs-of-ack-managed-cluster.md) [ACK](../user-guide/collect-control-plane-component-logs-of-ack-managed-cluster.md) [托管集群控制面组件日志](../user-guide/collect-control-plane-component-logs-of-ack-managed-cluster.md) 发送到指定的 SLS Project 中 | 通过在集群中安装日志采集组件以采集日志，并发送至指定的 SLS Project 中 |
| 策略规则库 | [容器安全策略规则库说明](predefined-security-policies-of-ack.md) 中的所有策略 | [容器安全策略规则库说明](predefined-security-policies-of-ack.md) 中的所有策略 云安全中心提供的 [容器主动防御](https://help.aliyun.com/zh/security-center/user-guide/use-the-feature-of-proactive-defense-for-containers#section-i5h-11v-pag) |
## 注意事项
仅适用于Linux节点。
不支持自定义策略规则。所有规则均来自于阿里云容器服务内置的规则库。
## 步骤一：安装或升级安全策略管理组件
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择安全管理>策略管理。
在策略管理页面，根据页面提示安装或升级组件。
启用安全策略管理功能时，需安装以下组件。以下组件本身不收取费用，但会占用您的Pod资源。
gatekeeper组件：基于OPA策略引擎的Kubernetes策略准入控制器，便于您管理和应用集群内的OPA策略，实现命名空间标签管理等功能。
说明
仅支持使用ACK集群提供的gatekeeper组件。如您通过其他途径安装了gatekeeper组件，请卸载后重新安装。关于gatekeeper组件的版本发布信息，请参见[gatekeeper](../../product-overview/gatekeeper.md)。
日志采集组件：用于收集和检索不符合策略约束的拦截或告警事件。
policy-template-controller组件：基于阿里云策略模板开发的Kubernetes控制器，便于您更好地管理基于不同策略模板部署的策略实例和集群整体的治理状态。
## 步骤二：使用安全策略管理功能
### 操作入口
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择安全管理>策略管理。
在策略管理页面，按页面提示完成组件的安装或升级（如有），然后按需进行以下操作。
### 查看集群当前安全策略执行状态
您可以单击策略实施总览页签，查看集群当前的策略治理状态。
策略开启总览，包括高危和中危防护策略的总数和已开启数展示，以及建议开启的策略列表等。
近7天拦截和告警结果统计。
近7天策略实施记录，当前页面表格中会默认展示7天内最近100条的拦截或告警日志，如果您想查看更多审计日志，可以单击近7天策略实施记录后的图标，并单击悬浮窗口中的日志服务链接在SLS日志服务控制台指定的logstore中查看全部日志。页面下方近7天策略实施记录表格展示每条策略的实施时间、策略类型、策略名称、策略描述、风险等级、实施动作和详细信息，可通过搜索框和筛选按钮定位具体记录。
### 创建并管理安全策略实例
单击我的策略页签，然后单击创建策略实例，在创建策略实例对话框配置相关参数。
| 配置项 | 说明 |
| --- | --- |
| 策略类型 | 首先选择策略类型，包括： infra：基础设施层资源相关的策略类型。 compliance：基于 阿里云 K8s 加固 等 Kubernetes 合规规范定制的策略类型。 psp：替代 Pod Security Policy（PSP）能力的策略类型。 k8s-general：基于最佳安全实践对 Kubernetes 资源配置进行安全加固约束的通用策略类型。 详见 [容器安全策略规则库说明](predefined-security-policies-of-ack.md) 。 |
| 策略名称 | 根据选择的策略类型，在策略名称下拉列表中选择需要部署的策略模板名称。 |
| 实施动作 | 拦截：违反策略规则约束的指定资源部署会被拦截。 警告：违反策略规则约束的指定资源仍旧可以部署，只会产生对应违规审计的告警日志。 |
| 作用范围 | 选择策略实例实施在集群中哪些指定的命名空间。 |
| 参数配置 | 如果参数配置输入框中默认为空，说明规则不需要进行参数配置。 如果输入框中包含需要配置的参数模板，则请参考策略参数说明按照指定格式配置参数。 |
### 查看安全策略列表和集群中已部署的安全策略实例
单击我的策略页签，查看集群所有可部署的策略名称。
可在列表右上角筛选显示的策略。已开启的策略名称会优先展示。策略实例数会显示对应策略在集群中已部署的实例个数。
如果策略实例数为空，表明该策略还未在集群中部署，可在操作列单击开启配置参数并部署对应的策略实例。
单击操作列中的编辑可以修改策略实例的配置。
当策略在集群中已部署超过1个实例时，可单击操作列的查看策略实例，然后单击编辑修改相关配置。
单击操作列中的删除，可删除该策略在集群中部署的所有实例。
关于策略说明和模板示例的更多信息，请参见[容器安全策略规则库说明](predefined-security-policies-of-ack.md)。
## 相关操作
### 为命名空间或Service开启删除保护
参见[步骤一：安装或升级安全策略管理组件](configure-and-enforce-ack-pod-security-policies.md)启用安全策略管理功能后，您还可以为涉及关键业务、敏感数据的命名空间或Service开启删除保护功能，以避免误删除带来的维护成本。启用后，仅当您手动关闭删除保护后，对应的资源才可以被删除。
下文以为存量命名空间的开启删除保护为例，介绍流程步骤。其他操作步骤流程类似，您可以进入控制台对应页面，按照页面提示完成配置。
为存量命名空间开启删除保护
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择命名空间与配额。
在命名空间列表的操作列，单击编辑，在对话框中按照页面完成删除保护的启用。
为存量Service开启删除保护
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择网络>服务。
在服务列表的操作列，单击，然后单击开启删除保护，在对话框中按照页面完成删除保护的启用。
### 通过ack-policy-external-provider实现跨资源验证
默认情况下，Gatekeeper 策略的决策依据仅限于被审查的资源本身。但在许多复杂的安全场景中，策略需要引用集群中的其他资源状态才能做出正确判断。
托管组件 ack-policy-external-provider 可充当 Gatekeeper 的外部数据源，让策略开发者可以在策略代码（Rego）中查询Kubernetes资源（如内置的CRD保护策略）。
重要
ack-policy-external-provider需配合[gatekeeper](../../product-overview/gatekeeper.md)使用。请确保集群中已部署 gatekeeper。
安装和配置ack-policy-external-provider
在[ACK](https://cs.console.aliyun.com)[集群列表](https://cs.console.aliyun.com)页面，单击目标集群名称，在集群详情页左侧导航栏，单击组件管理。
搜索并定位ack-policy-external-provider，按照页面提示完成配置。
ProviderPodNumber：组件的实例个数。
ProtectedKinds：添加需要保护 CRD 对应的资源类型。
CRD 删除保护需要检查集群中是否存在该资源类型的实例。遵循最小化权限原则，ack-policy-external-provider默认不具备该检查所需的查询权限，需手动配置。
设置ProviderPodNumber（副本数量，默认为1）。在ProtectedKinds区域，输入资源类型名称（如pods、policies、customresources），单击添加可增加多个条目，单击删除可移除条目，完成后单击确认。
接口定义及参数说明
ack-policy-external-provider 实现了一个标准的 Gatekeeper 外部数据 Provider。可在 Rego 策略模板中，通过调用external_data函数并指定provider: ack-policy-external-data-provider，来向该组件发起资源查询请求。
请求参数以 JSON 格式定义，示例如下。
// 示例 1 { "action": "ListK8sResource", "namespaced": false, "group": "", "version": "v1", "resource": "persistentvolumeclaims" "requestID": review.uid, "userInfo": review.userInfo, "requestFrom": "PVCProtector", "labelSelector": "protected", "limit": 1 } // 示例 2 { "action": "GetK8sResource", "namespaced": true, "namespace": "default", "group": "apps", "version": "v1", "resource": "deployments", "requestID": review.uid, "userInfo": review.userInfo, "requestFrom": "FinOpsPolicy", "labelSelector": "protected", "limit": 1 }
核心参数说明：
| 参数 | 说明 | 是否必选 |
| --- | --- | --- |
| action | 操作类型，支持 ListK8sResource 和 GetK8sResource 。 | 是 |
| group | 目标资源的 API Group。 | 是 |
| version | 目标资源的 API Version。 | 否 |
| resource | 目标资源的复数名称（例如 persistentvolumeclaims ）。 | 是 |
| namespaced | 目标资源是否位于命名空间内。 true 或 false 。 集群范围内资源请使用 false 。 | 是 |
| namespace | 当 namespaced 为 true 时，指定查询的命名空间。 | 否 |
| name | 当 action 为 GetK8sResource 时，指定要获取的资源名称。 | 否 |
| labelSelector | 基于标签筛选资源，遵循 Kubernetes [Label Selector 规范](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors) 。 | 否 |
| limit | ListK8sResource 返回的资源数量上限。 | 否 |
| requestID | 请求的唯一 ID，建议使用 review.uid 。 | 否 |
| userInfo | 发起请求的用户信息，建议使用 review.userInfo 。 | 否 |
| requestFrom | 请求来源标识，通常为策略模板名称，用于日志追溯。 | 是 |
场景示例：防止CRD被删除
本示例展示利用 ack-policy-external-provider 实现一个常见的高级策略：当 CRD 仍然存在关联的 CR 实例时，禁止删除该 CRD。
此策略已作为内置规则集成到策略库中，无需手动部署。仅作为原理说明。
策略逻辑
触发：Gatekeeper 监听到DELETECRD 操作。
查询：Rego 策略通过external_data调用 ack-policy-external-provider。
判断：ack-policy-external-provider 根据请求参数查询集群中是否存在对应的 CR 实例。
决策：如果查询结果返回了至少一个 CR 实例，ack-policy-external-provider 会将结果返回给 Rego 策略，策略最终会deny(拒绝) 本次删除操作。
策略模板（ConstraintTemplate）
定义策略的逻辑。
apiVersion: templates.gatekeeper.sh/v1beta1 kind: ConstraintTemplate metadata: name: blockcrddeletion annotations: meta.helm.sh/release-name: gatekeeper meta.helm.sh/release-namespace: kube-system metadata.gatekeeper.sh/version: 1.0.0 labels: app.kubernetes.io/managed-by: Helm spec: crd: spec: names: kind: BlockCrdDeletion validation: legacySchema: true targets: - target: admission.k8s.gatekeeper.sh rego: | package block_crd_deletion violation[{"msg": msg}] { before(input.review.operation) response := handle(input.review) msg := after(response) } before(operation) { operation == "DELETE" } handle(review) = response { customrequest := { "action": "ListK8sResource", "namespaced": false, "group": review.object.spec.group, "version": "", "resource": review.object.spec.names.plural, "requestID": review.uid, "userInfo": review.userInfo, "requestFrom": "BlockCrdDeletion", "labelSelector": "protected", "limit": 1 } request_keys := [json.marshal(customrequest)] response := external_data({ "provider": "ack-policy-external-data-provider", "keys": request_keys }) } after(response) = msg { count(response.responses[0]) > 0 msg := sprintf( "The CRD %v is not allowed to be deleted. Reason: It is not allowed to delete a CRD object when it contains a collection of custom resources. Current existing custom resources: %v, etc.", [input.review.name, response.responses[0][0]] ) }
策略实例（Constraint）
将模板应用到具体资源。本示例应用到所有CRD。
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: BlockCrdDeletion metadata: name: block-crd-deletion-rule spec: enforcementAction: deny match: kinds: - apiGroups: - '*' kinds: - CustomResourceDefinition
效果验证
创建一个测试 CRD 和对应的 CR 实例：
# 创建 CRD apiVersion: apiextensions.k8s.io/v1 kind: CustomResourceDefinition metadata: name: simplestthings.example.com spec: group: example.com scope: Namespaced names: plural: simplestthings singular: simplestthing kind: SimplestThing versions: - name: v1 served: true storage: true schema: openAPIV3Schema: type: object properties: spec: type: object properties: message: type: string --- # 创建 CR 实例 apiVersion: example.com/v1 kind: SimplestThing metadata: name: my-simple-thing namespace: default labels: protected: "false" spec: message: "Hello"
尝试删除该 CRD。
kubectl delete crd simplestthings.example.com
查看删除操作是否被策略拦截，并返回明确的错误信息。
预期输出：
Error from server (Forbidden): admission webhook "delete.validation.gatekeeper.sh" denied the request: [block-crd-deletion-rule] The CRD simplestthings.example.com is not allowed to be deleted. Reason: It is not allowed to delete a CRD object when it contains a collection of custom resources. Current existing custom resources: my-simple-thing, etc.
## 相关文档
配置巡检功能可以扫描集群中工作负载配置的安全隐患。更多信息，请参见[配置巡检检查集群工作负载](use-the-inspection-feature-to-detect-security-risks-in-the-workloads-of-an-ack-cluster.md)。
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
