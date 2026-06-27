# 使用kube-eventer将Kubernetes事件采集到K8s事件中心-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/collect-kubernetes-events

# 采集Kubernetes事件
本文档主要介绍如何使用eventer将Kubernetes中的事件采集到日志服务。
Kubernetes的架构设计基于状态机，不同的状态之间进行转换会生成相应的事件，正常的状态之间转换会生成Normal等级的事件，正常状态与异常状态之间的转换会生成Warning等级的事件。
ACK提供开箱即用的容器场景事件监控方案，通过ACK维护的NPD以及包含在NPD中的kube-eventer提供容器事件监控能力。
NPD（node-problem-detector）是Kubernetes节点诊断的工具，可以将节点的异常（例如Docker Engine Hang、Linux Kernel Hang、网络出网异常、文件描述符异常等）转换为节点的事件，结合kube-eventer可以实现节点事件告警的闭环。更多信息，请参见[NPD](https://github.com/AliyunContainerService/node-problem-detector)。
kube-eventer是ACK维护的开源Kubernetes事件离线工具，可以将集群的事件推送至钉钉、SLS、EventBridge等系统，并提供不同等级的过滤条件，实现事件的实时采集、定向告警、异步归档。更多信息，请参见[kube-eventer](https://github.com/AliyunContainerService/kube-eventer)。
NPD（node-problem-detector）是Kubernetes节点诊断的工具，可以将节点的异常（例如Docker Engine Hang、Linux Kernel Hang、网络出网异常、文件描述符异常等）转换为节点的事件，结合kube-eventer可以实现节点事件告警的闭环。更多信息，请参见[NPD](https://github.com/AliyunContainerService/node-problem-detector)。
kube-eventer是ACK维护的开源Kubernetes事件离线工具，可以将集群的事件推送至钉钉、SLS、EventBridge等系统，并提供不同等级的过滤条件，实现事件的实时采集、定向告警、异步归档。更多信息，请参见[kube-eventer](https://github.com/AliyunContainerService/kube-eventer)。
## 前提条件
已创建Kubernetes集群（例如阿里云ACK集群、ACK Serverless集群等）。
## 计费说明
K8s事件中心具备如下条件时，免费使用。
K8s事件中心关联的Logstore的存储时间为90天（默认90天）。
每天写入K8s事件中心的数据量少于256 MB（大约25万条事件）。
例如：
不调整存储时间（默认90天），且K8s集群每天产生1000条事件，则K8s事件中心免费使用。
调整存储时间为105天，且K8s集群每天产生1000条事件，则超过90天后，K8s事件中心会产生Logstore存储费用（计费项为存储空间-日志存储），每天费用约0.1元。关于存储空间-日志存储计费项的更多信息，请参见[按使用功能计费模式计费项](billable-items.md)。
## 步骤一：部署kube-eventer和node-problem-detector
### 阿里云Kubernetes
如果是ACK集群，则对应阿里云Kubernetes组件中的ack-node-problem-detector组件已集成eventer和node-problem-detector功能，您只需要部署该组件。更多信息，请参见[事件监控](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/event-monitoring.md)。如果是ACK Serverless集群，您需要部署kube-eventer组件。
NPD根据配置与第三方插件检测节点的问题或故障并生成相应的集群事件。而Kubernetes集群自身也会因为集群状态的切换产生各种事件，例如Pod驱逐、镜像拉取失败等异常情况。日志服务SLS（Log Service）的Kubernetes事件中心实时汇聚Kubernetes中的所有事件并提供存储、查询、分析、可视化、告警等能力。将集群事件接入日志服务的Kubernetes事件中心操作步骤如下：
如果在创建集群时，已选中安装node-problem-detector并创建事件中心，可直接按照[步骤二](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/event-monitoring.md)查看Kubernetes事件中心。关于如何通过创建集群时安装NPD组件，请参见[创建](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[ACK](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。
若创建集群时未选中安装node-problem-detector并创建事件中心，则需手动安装，具体的操作步骤如下。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择运维管理>组件管理。
在日志与监控页签，查找并安装ack-node-problem-detector。
### 其他Kubernetes
部署eventer。
安装kubectl工具。具体操作，请参见[获取集群](../../ack/documents/serverless-kubernetes/user-guide/connect-to-an-ack-cluster-by-using-kubectl.md)[KubeConfig](../../ack/documents/serverless-kubernetes/user-guide/connect-to-an-ack-cluster-by-using-kubectl.md)[并通过](../../ack/documents/serverless-kubernetes/user-guide/connect-to-an-ack-cluster-by-using-kubectl.md)[kubectl](../../ack/documents/serverless-kubernetes/user-guide/connect-to-an-ack-cluster-by-using-kubectl.md)[工具连接集群](../../ack/documents/serverless-kubernetes/user-guide/connect-to-an-ack-cluster-by-using-kubectl.md)。
使用以下样例创建名为eventer.yaml的配置文件。
apiVersion: apps/v1 kind: Deployment metadata: labels: name: kube-eventer name: kube-eventer namespace: kube-system spec: replicas: 1 selector: matchLabels: app: kube-eventer template: metadata: labels: app: kube-eventer annotations: scheduler.alpha.kubernetes.io/critical-pod: '' spec: dnsPolicy: ClusterFirstWithHostNet serviceAccount: kube-eventer containers: - image: registry.cn-hangzhou.aliyuncs.com/acs/kube-eventer:v1.2.5-cc7ec54-aliyun name: kube-eventer command: - "/kube-eventer" - "--source=kubernetes:https://kubernetes.default" ## .send to sls ## --sink=sls:https://{endpoint}?project={project}&logStore=k8s-event&regionId={region-id}&internal=false&accessKeyId={accessKeyId}&accessKeySecret={accessKeySecret} - --sink=sls:https://cn-beijing.log.aliyuncs.com?project=k8s-xxxx&logStore=k8s-event&regionId=cn-beijing&internal=false&accessKeyId=xxx&accessKeySecret=xxx env: # If TZ is assigned, set the TZ value as the time zone - name: TZ value: "Asia/Shanghai" volumeMounts: - name: localtime mountPath: /etc/localtime readOnly: true - name: zoneinfo mountPath: /usr/share/zoneinfo readOnly: true resources: requests: cpu: 10m memory: 50Mi limits: cpu: 500m memory: 250Mi volumes: - name: localtime hostPath: path: /etc/localtime - name: zoneinfo hostPath: path: /usr/share/zoneinfo --- apiVersion: rbac.authorization.k8s.io/v1 kind: ClusterRole metadata: name: kube-eventer rules: - apiGroups: - "" resources: - events verbs: - get - list - watch --- apiVersion: rbac.authorization.k8s.io/v1 kind: ClusterRoleBinding metadata: name: kube-eventer roleRef: apiGroup: rbac.authorization.k8s.io kind: ClusterRole name: kube-eventer subjects: - kind: ServiceAccount name: kube-eventer namespace: kube-system --- apiVersion: v1 kind: ServiceAccount metadata: name: kube-eventer namespace: kube-system
| 配置项 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| endpoint | string | 必选 | 日志服务的 Endpoint。更多信息，请参见 [服务入口](developer-reference/service-entrance.md) 。 |
| project | string | 必选 | 日志服务的 Project。 |
| logStore | string | 必选 | 日志服务的 Logstore。 |
| internal | string | 自建 Kubernetes：必选。 | 自建 Kubernetes 必须设置为 false。 |
| regionId | string | 自建 Kubernetes：必选。 | 日志服务所在地域 ID。更多信息，请参见 [服务入口](developer-reference/service-entrance.md) 。 |
| accessKeyId | string | 自建 Kubernetes：必选。 | AccessKey ID，建议使用 RAM 用户的 AccessKey 信息。更多信息，请参见 [访问密钥](developer-reference/access-key.md) 。 |
| accessKeySecret | string | 自建 Kubernetes：必选。 | AccessKey Secret，建议使用 RAM 用户的 AccessKey 信息。更多信息，请参见 [访问密钥](developer-reference/access-key.md) 。 |
执行以下命令，将eventer.yaml中的配置应用到集群。
kubectl apply -f eventer.yaml
预期输出：
deployment.apps/kube-eventer created clusterrole.rbac.authorization.k8s.io/kube-eventer created clusterrolebinding.rbac.authorization.k8s.io/kube-eventer created serviceaccount/kube-eventer created
部署node-problem-detector。
具体操作，请参见[Github](https://github.com/kubernetes/node-problem-detector)。
## 步骤二：创建K8s事件中心实例
说明
创建K8s事件中心后，日志服务自动在目标Project中生成一个名为k8s-event的Logstore，并生成相关联的仪表盘等。
登录[日志服务控制台](https://sls.console.aliyun.com)。
在日志应用区域的智能运维页签中，单击K8s事件中心。
在事件中心管理页面，单击页面右上角的添加。
在创建事件中心面板，配置相关参数，然后单击下一步。
如果选择已有Project，则从Project下拉框中选择已创建的Project，用于管理K8s事件中心相关资源（Logstore、仪表盘等）。
如果选择从容器服务选择K8s集群，则从K8s集群下拉框中选择已创建的K8s集群。通过此方式创建K8s事件中心，日志服务默认创建一个名为k8s-log-{cluster-id}的Project，用于管理K8s事件中心相关资源（Logstore、仪表盘等）。
## 步骤三：使用K8s事件中心实例
创建K8s事件中心并部署eventer和NPD后，即可在K8s事件中心查看事件总览、查询事件详情、查看Pod生命周期、查看节点事件、查看核心组件事件、设置告警、自定义查询和更新版本等。
在K8s事件中心页面，找到目标K8s事件中心实例，单击图标，可进行如下操作。
| 操作 | 说明 |
| --- | --- |
| 查看事件总览 | 事件总览 页面用于展示核心事件的汇总统计信息。例如事件总数、今天 Error 事件数与昨天的对比、告警项统计、Error 事件趋势、Pod OOM 详细信息等。 说明 目前 Pod OOM 信息不能精确到 Pod，只能定位到事件发生的节点、进程名、进程号。您可以通过自定义查询查找 Pod OOM 发生时间点附近的 Pod 重启事件，以此定位到具体的 Pod。 |
| 查询事件详情 | 事件详情查询 页面用于展示经过各种维度（事件类型、事件目标、Host、Namespace、Name）过滤后的事件详细信息。 |
| 查看 Pod 生命周期 | Pod 生命周期 页面以图形化方式展示 Pod 整个生命周期中的事件信息。您还可以通过事件等级筛选重要的 Pod 事件。 |
| 查看节点事件 | 节点事件 页面用于展示节点事件详情。例如 Node 生命周期、事件列表等。 |
| 查看核心组件事件 | 核心组件事件 页面用于展示核心组件事件详情。例如 ECS 重启失败、URL 模式未执行等。 |
| 设置告警 | 在 告警配置 页面，您可以为 K8s 事件中心设置告警。具体操作，请参见 [设置告警](configure-alerts-2-k8s.md) 。 |
| 自定义查询 | 在 自定义查询 页面，您可以自定义查询和分析语句。 K8s 事件中心的所有事件都保存在 Logstore 中，您可以使用 Logstore 中的所有功能，例如自定义查询、消费事件、创建自定义报表、创建自定义告警等。更多信息，请参见 [查询与分析快速指引](quick-guide-to-query-and-analysis.md) 。 如果您要访问 K8s 事件中心所在的 Project，可通过以下两种方式获取 Project 名称。 通过 自定义查询 页面的 URL 定位到 Project。URL 规则为 https://sls.console.aliyun.com/lognext/app/k8s-event/project/k8s-log-xxxx/logsearch/k8s-event ，Project 字段的后一个字段即为日志服务 Project 名称，例如 k8s-log-xxxx。 在 事件中心管理 页签的 K8s 事件中心列表中，查看目标 K8s 事件中心实例对应的 Project 名称。 |
| 更新版本 | 在 版本更新 页面，您可以升级 K8s 事件中心的版本。 |
## 日志样例
采集到的日志样例如下所示。
hostname: cn-hangzhou.i-***********" level: Normal pod_id: 2a360760-**** pod_name: logtail-ds-blkkr event_id: { "metadata":{ "name":"logtail-ds-blkkr.157b7cc90de7e192", "namespace":"kube-system", "selfLink":"/api/v1/namespaces/kube-system/events/logtail-ds-blkkr.157b7cc90de7e192", "uid":"2aaf75ab-****", "resourceVersion":"6129169", "creationTimestamp":"2019-01-20T07:08:19Z" }, "involvedObject":{ "kind":"Pod", "namespace":"kube-system", "name":"logtail-ds-blkkr", "uid":"2a360760-****", "apiVersion":"v1", "resourceVersion":"6129161", "fieldPath":"spec.containers{logtail}" }, "reason":"Started", "message":"Started container", "source":{ "component":"kubelet", "host":"cn-hangzhou.i-***********" }, "firstTimestamp":"2019-01-20T07:08:19Z", "lastTimestamp":"2019-01-20T07:08:19Z", "count":1, "type":"Normal", "eventTime":null, "reportingComponent":"", "reportingInstance":"" }
| 日志字段 | 数据类型 | 说明 |
| --- | --- | --- |
| hostname | String | 事件发生所在的主机名。 |
| level | String | 日志等级，包括 Normal、Warning。 |
| pod_id | String | Pod 的唯一标识，仅在该事件类型和 Pod 相关时才具有此字段。 |
| pod_name | String | Pod 名，仅在该事件类型和 Pod 相关时才具有此字段。 |
| event_id | JSON | 事件的详细内容。该字段为 JSON 类型的字符串。 |
## 常见问题
### K8s事件中心实例无数据
部署好K8s事件中心后，新产生的事件会自动采集到K8s事件中心，您可以在自定义查询页面进行搜索（建议将右上角时间范围调整到1天）。如果无数据，一般有两个原因：
部署K8s事件中心后，K8s集群还未产生事件。
您可以通过kubectl get events --all-namespaces命令检查集群内是否有新事件产生。
部署eventer和node-problem-detector时，参数填写错误。
如果您使用的是阿里云Kubernetes集群，请参考如下步骤。
登录[容器服务控制台](https://cs.console.aliyun.com/)。
在集群列表页面中，单击目标集群。
在左侧导航栏中，选择应用>Helm。
在Helm页面中，单击ack-node-problem-detector后的更新。
检查并修改参数配置。更多信息，请参见[步骤一：部署](create-and-use-an-event-center.md)[eventer](create-and-use-an-event-center.md)[和](create-and-use-an-event-center.md)[node-problem-detector](create-and-use-an-event-center.md)。
如果您使用的是自建Kubernetes集群，参数配置请参见[采集](collect-kubernetes-events.md)[Kubernetes](collect-kubernetes-events.md)[事件](collect-kubernetes-events.md)。
### 如何查看事件对应容器的日志？
如果您使用的是阿里云Kubernetes集群，请参考如下步骤。
登录[容器服务控制台](https://cs.console.aliyun.com/)。
在集群列表页面中，单击目标集群。
在左侧导航栏中，选择工作负载>容器组。
将命名空间选择为kube-system。
在容器组列表中，单击目标容器组对应的日志。
如果您使用的是自建Kubernetes集群，请查看namespace为kube-system下文件名前缀为eventer-sls的Pod日志。
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
