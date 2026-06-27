# 基于EventBridge的事件驱动CI Pipeline-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-argo-workflow-cluster/use-cases/event-driven-ci-pipeline-via-eventbridge

# 基于EventBridge的事件驱动CI Pipeline
基于事件总线EventBridge和分布式工作流Argo Workflows，可以构建高效、快速、低成本的事件驱动自动化CI Pipeline，大幅简化和加速应用交付过程。本文介绍如何构建基于事件驱动的自动化CI Pipeline流程。
## 前提条件
已[开通事件总线](https://help.aliyun.com/zh/eventbridge/getting-started/activate-eventbridge-and-grant-permissions-to-a-ram-user#task-1947668)[EventBridge](https://help.aliyun.com/zh/eventbridge/getting-started/activate-eventbridge-and-grant-permissions-to-a-ram-user#task-1947668)[并授权](https://help.aliyun.com/zh/eventbridge/getting-started/activate-eventbridge-and-grant-permissions-to-a-ram-user#task-1947668)。
已[创建](../user-guide/create-an-argo-workflow-cluster.md)[Argo](../user-guide/create-an-argo-workflow-cluster.md)[工作流集群](../user-guide/create-an-argo-workflow-cluster.md)。
已[创建文件系统](https://help.aliyun.com/zh/nas/user-guide/create-a-file-system)。
已[创建企业版实例](https://help.aliyun.com/zh/acr/user-guide/create-a-container-registry-enterprise-edition-instance)。
已授予RAM用户AliyunAdcpFullAccess权限。具体操作，请参见[为](../../distributed-cloud-container-platform-for-kubernetes/user-guide/authorization-overview.md)[RAM](../../distributed-cloud-container-platform-for-kubernetes/user-guide/authorization-overview.md)[用户授权](../../distributed-cloud-container-platform-for-kubernetes/user-guide/authorization-overview.md)。
## 工作原理
基于事件驱动的自动化CI Pipeline，包含2部分：
基于Git事件的触发，代码提交到Git仓库时，触发相应的事件。
CI系统运行构建前的测试，构建Docker镜像，并推送至镜像仓库。
镜像构建成功后，可使用CD系统（如[ACK One GitOps](../../distributed-cloud-container-platform-for-kubernetes/user-guide/gitops-overview.md)）将新的Image Tag同步到Kubernetes集群中。
在本实践中，事件驱动方案采用了在可用性、易用性、安全性、可扩展性等多方面具有[优势](https://help.aliyun.com/zh/eventbridge/product-overview/benefits#section-hf0-60r-chs)的[事件总线](https://help.aliyun.com/zh/eventbridge/product-overview/what-is-eventbridge)[EventBridge](https://help.aliyun.com/zh/eventbridge/product-overview/what-is-eventbridge)，CI部分基于CNCF毕业项目Argo Workflows来构建。工作流集群全托管Argo Workflows，可提升稳定性和可观测性，提供运维能力，帮助您实现更大规模、具有更快的运行速度和更低成本的CI Pipeline。
用户向Git仓库提交代码。
EventBridge根据配置的规则，捕获Git事件并将其传递给ACK One工作流集群，从而触发CI工作流的执行。
[基于](../../distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)[ACK One](../../distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)[工作流集群的](../../distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)[CI](../../distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)[工作流](../../distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)构建Docker Image，并推送至镜像仓库中。之后可通过GitOps自动同步相应镜像变化至ACK集群。
## 步骤一：在Argo工作流集群中准备CI环境
创建ACR EE访问凭证并挂载NAS存储卷。具体操作，请参见[基于工作流集群构建](../../distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)[Golang](../../distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)[项目的](../../distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)[CI Pipeline](../../distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)中的[步骤一](../../distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)和[步骤二](../../distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)。
说明
请确保命名空间与Workflow资源保持一致。
Apps Code Repo示例为[echo-server](https://github.com/AliyunContainerService/echo-server/tree/main/manifests/directory)[项目](https://github.com/AliyunContainerService/echo-server/tree/main/manifests/directory)，请将其Fork到您的GitHub账号下，并参考[在](../../distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline.md)[CI Pipeline](../../distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline.md)[中](../../distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline.md)[Clone](../../distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline.md)[私有](../../distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline.md)[Git](../../distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline.md)[仓库](../../distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline.md)来修改WorkflowTemplate。
## 步骤二：使用EventBridge实现Git事件驱动CI Pipeline
[创建自定义事件总线](https://help.aliyun.com/zh/eventbridge/user-guide/manage-custom-event-buses#section-sfl-pcs-6rh)。
事件总线EventBridge与GitHub进行集成对接。具体操作，请参见[GitHub](https://help.aliyun.com/zh/eventbridge/use-cases/integrate-github)[集成](https://help.aliyun.com/zh/eventbridge/use-cases/integrate-github)。
配置事件规则（可选），以下为本示例配置内容。详细配置事件规则的方式，请参见[管理事件规则](https://help.aliyun.com/zh/eventbridge/user-guide/manage-event-rules)。
事件模式：如下设置为只触发来自release-v1分支的变更。
{ "source": [ "github.event" ], "data": { "body": { "ref": [ "refs/heads/release-v1" ] } } }
配置事件目标。
服务类型：选择容器服务Kubernetes。
集群配置文件 KubeConfig：输入工作流集群专有网络访问的KubeConfig。
YAML配置：本示例选择模板。
变量：增加workflowName，配置事件ID。
{ "workflowName": "$.id" }
模板：填入Workflow CI CR。以下示例仅供参考，请根据您的实际信息构建CR。
重要
资源配置的要求是必须明确设置name和namespace，不能使用generateName。如果资源属于默认命名空间default，也必须声明。
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: name: ci-go-v1-eb-${workflowName} namespace: default labels: workflows.argoproj.io/workflow-template: ackone-ci spec: arguments: parameters: - name: repo_url value: https://github.com/ivan-cai/echo-server.git - name: repo_name value: echo-server - name: target_branch value: release-v1 - name: container_image value: "YOUR-IMAGE-REGISTRY-ADDRESS" # 容器镜像库的地址，请根据您的实际信息替换. - name: container_tag value: "v1.0.0" - name: dockerfile value: ./Dockerfile - name: enable_suffix_commitid value: "true" - name: enable_test value: "true" workflowTemplateRef: name: ci-go-v1 clusterScope: true
网络访问：推荐使用专有网络，选择工作流集群的VPC，交换机和安全组。
根据上述配置，当您在GitHub仓库的release-v1分支上进行代码修改并提交时，该操作会触发自动化流程，您可以通过以下方式验证。
查看事件轨迹。
- 登录[事件总线](https://eventbridge.console.aliyun.com/)[EventBridge](https://eventbridge.console.aliyun.com/)[控制台](https://eventbridge.console.aliyun.com/)，在左侧导航栏，单击事件总线。
单击对应事件总线名称，在左侧导航栏，单击事件追踪。
进入事件追踪页面，可查看对应事件轨迹。
事件轨迹详情中，事件 ID 为b91299ae-355d-4f66-ac53-8d84e5d84b97，事件类型为eventbridge:Events:HTTPEvent，总线名称为ci-test，事件源为github.event。在事件投递区域，规则ttt成功将事件投递至目标https://8.217.97.153:6443，投递状态为成功，投递耗时 59 毫秒，投递响应为[200]NoMessage。
查看新建的Workflow的执行拓扑。
在工作流集群查看新建的Workflow的执行拓扑。具体操作，请参见[开启](../../distributed-cloud-container-platform-for-kubernetes/user-guide/enable-argo-server-for-a-workflow-cluster.md)[Argo Server](../../distributed-cloud-container-platform-for-kubernetes/user-guide/enable-argo-server-for-a-workflow-cluster.md)[访问工作流集群](../../distributed-cloud-container-platform-for-kubernetes/user-guide/enable-argo-server-for-a-workflow-cluster.md)。
Workflow 名称为ci-go-v1-eb-3999580c-1ee4-4e10-a75b-af6e8eddccde，DAG 执行拓扑依次为git-checkout-pr（已成功）、run-test（已成功）、build-push-image（运行中）。
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
