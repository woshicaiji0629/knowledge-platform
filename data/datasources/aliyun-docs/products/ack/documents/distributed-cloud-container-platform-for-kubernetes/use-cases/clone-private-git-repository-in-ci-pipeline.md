# 使用Argo Workflows构建CI Pipeline时Clone私有Git仓库-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/product-overview.md)

- [快速入门](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/getting-started.md)

- [操作指南](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide.md)

- [实践教程](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases.md)

- [开发参考](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/developer-reference.md)

- [服务支持](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/support.md)

[首页](https://help.aliyun.com/zh)

# 在CI Pipeline中Clone私有Git仓库

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

ACK One工作流集群构建CI Pipeline，其使用BuildKit Cache和NAS存储Go mode cache，可大幅加速CI Pipeline的流程。通过工作流集群构建基于Golang项目CI Pipeline时，若您使用的Git仓库为私有仓库，您需要在CI流程中先成功Clone该私有仓库，再进行CI Pipeline的构建操作。本文为您介绍如何在CI Pipeline中Clone私有Git仓库。

## 背景信息

使用公共Git仓库构建CI Pipeline的最佳实践，请参见[基于工作流集群构建](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)[Golang](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)[项目的](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)[CI Pipeline](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)。

若您使用私有Git仓库，则需要在上述最佳实践操作前，先Clone私有Git仓库。

本文为您提供以下三种方法Clone私有Git仓库：

- 

[方法一：基于](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline.md)[Argo Workflows Git Artifact](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline.md)[与用户名密码](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline.md)

- 

[方法二：基于](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline.md)[Argo Workflows Git Artifact](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline.md)[与](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline.md)[SSH Private Key](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline.md)

- 

[方法三：基于](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline.md)[Git Clone](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline.md)[命令与用户名密码](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/clone-private-git-repository-in-ci-pipeline.md)

## 在工作流集群中保存私有仓库凭据

Clone私有仓库前，您需要先在工作流集群中执行如下命令保存私有仓库所需的用户名、密码和ssh private key。

username、password和ssh-private-key需要替换为您实际使用的参数值。

kubectl create secret generic git-creds --from-literal="username=${username}" --from-literal="password=${password or token}" --from-file=ssh-private-key=${ssh private key path} # example # kubectl create secret generic git-creds --from-literal="username=demo" --from-literal="password=ghp_GePB****************d407" --from-file=ssh-private-key=$HOME/.ssh/id_rsa

## 方法一：基于Argo Workflows Git Artifact与用户名密码

该方法主要是在执行构建CI Pipeline的操作前，先执行Git Clone私有仓库操作，再进行Git Checkout操作。

以下YAML为了方便展示，和上文[预置工作流模板](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)内容相比，仅保留了上述CI Pipeline中的git-checkout-pr任务（其他方法均相同），基于此增加git-clone任务，并设置git-checkout-pr依赖git-clone。

- 

git-checkout-pr的command中，shell script无需修改。

- 

git-clone的artifacts中引用保存的私有仓库凭据的git-credssecret中的用户名、密码。

### 示例模板

apiVersion: argoproj.io/v1alpha1 kind: ClusterWorkflowTemplate metadata: name: ci-git-artifact spec: entrypoint: main volumes: - name: run-test emptyDir: {} - name: workdir persistentVolumeClaim: claimName: pvc-nas - name: docker-config secret: secretName: docker-config arguments: parameters: - name: repo_url value: "" - name: repo_name value: "" - name: target_branch value: "main" templates: - name: main dag: tasks: - name: git-clone arguments: artifacts: - name: git-repo path: /workdir git: repo: "{{arguments.parameters.repo_url}}" revision: main usernameSecret: name: git-creds key: username passwordSecret: name: git-creds key: password sshPrivateKeySecret: name: git-creds key: ssh-private-key inline: container: image: golang:1.10 command: - sh - -c - | cd {{workflow.parameters.repo_name}} git status && ls workingDir: /workdir volumeMounts: - name: "workdir" mountPath: /workdir - name: git-checkout-pr inline: container: image: alpine:latest command: - sh - -c - | set -eu apk --update add git cd /workdir echo "Start to Clone "{{workflow.parameters.repo_url}} git -C "{{workflow.parameters.repo_name}}" pull || git clone {{workflow.parameters.repo_url}} cd {{workflow.parameters.repo_name}} echo "Start to Checkout target branch" {{workflow.parameters.target_branch}} git checkout {{workflow.parameters.target_branch}} echo "Get commit id" git rev-parse --short origin/{{workflow.parameters.target_branch}} > /workdir/{{workflow.parameters.repo_name}}-commitid.txt commitId=$(cat /workdir/{{workflow.parameters.repo_name}}-commitid.txt) echo "Commit id is got: "$commitId echo "Git Clone and Checkout Complete." volumeMounts: - name: "workdir" mountPath: /workdir resources: requests: memory: 1Gi cpu: 1 activeDeadlineSeconds: 1200 depends: git-clone

### 提交Workflow参数说明

涉及参数和CI Pipeline保持一致，如下图所示：

## 方法二：基于Argo Workflows Git Artifact与SSH Private Key

和方法一基本相同，主要差异如下：

- 

git-clone的artifacts中引用保存的私有仓库凭据的git-credssecret中的ssh private key。

- 

在提交Workflow时，repo_url需要为ssh格式，例如：git@github.com:ivan-cai/gitops-demo-private.git。

### 示例模板

apiVersion: argoproj.io/v1alpha1 kind: ClusterWorkflowTemplate metadata: name: ci-git-artifact-sshkey spec: entrypoint: main volumes: - name: run-test emptyDir: {} - name: workdir persistentVolumeClaim: claimName: pvc-nas - name: docker-config secret: secretName: docker-config arguments: parameters: - name: repo_url value: "" - name: repo_name value: "" - name: target_branch value: "main" templates: - name: main dag: tasks: - name: git-clone arguments: artifacts: - name: git-repo path: /workdir git: repo: "{{arguments.parameters.repo_url}}" revision: main sshPrivateKeySecret: name: git-creds key: ssh-private-key inline: container: image: golang:1.10 command: - sh - -c - | cd {{workflow.parameters.repo_name}} git status && ls workingDir: /workdir volumeMounts: - name: "workdir" mountPath: /workdir - name: git-checkout-pr inline: container: image: alpine:latest command: - sh - -c - | set -eu apk --update add git cd /workdir echo "Start to Clone "{{workflow.parameters.repo_url}} git -C "{{workflow.parameters.repo_name}}" pull || git clone {{workflow.parameters.repo_url}} cd {{workflow.parameters.repo_name}} echo "Start to Checkout target branch" {{workflow.parameters.target_branch}} git checkout {{workflow.parameters.target_branch}} echo "Get commit id" git rev-parse --short origin/{{workflow.parameters.target_branch}} > /workdir/{{workflow.parameters.repo_name}}-commitid.txt commitId=$(cat /workdir/{{workflow.parameters.repo_name}}-commitid.txt) echo "Commit id is got: "$commitId echo "Git Clone and Checkout Complete." volumeMounts: - name: "workdir" mountPath: /workdir resources: requests: memory: 1Gi cpu: 1 activeDeadlineSeconds: 1200 depends: git-clone

### 提交Workflow参数说明

涉及参数如下：

说明

repo_url需要为ssh格式。

## 方法三：基于Git Clone命令与用户名密码

和前两种方法不同，该方法不需要增加DAG（Directed Acyclic Graph）任务，但需要修改git-checkout-pr中git clone的命令，并通过env引用git-credssecret中的用户名、密码。命令如下：

git clone https://${GIT_USER}:${GIT_TOKEN}@github.com/${GITHUB_REPOSITORY}

### 示例模板

apiVersion: argoproj.io/v1alpha1 kind: ClusterWorkflowTemplate metadata: name: ci-git spec: entrypoint: main volumes: - name: run-test emptyDir: {} - name: workdir persistentVolumeClaim: claimName: pvc-nas - name: docker-config secret: secretName: docker-config arguments: parameters: - name: repo_url value: "" - name: repo_name value: "" - name: target_branch value: "main" templates: - name: main dag: tasks: - name: git-checkout-pr inline: container: image: alpine:latest env: - name: GIT_USER valueFrom: secretKeyRef: name: git-creds key: username - name: GIT_TOKEN valueFrom: secretKeyRef: name: git-creds key: password command: - sh - -c - | set -eu apk --update add git cd /workdir echo "Start to Clone "{{workflow.parameters.repo_url}} git -C "{{workflow.parameters.repo_name}}" pull || git clone https://$GIT_USER:$GIT_TOKEN@{{workflow.parameters.repo_url}} cd {{workflow.parameters.repo_name}} echo "Start to Checkout target branch" {{workflow.parameters.target_branch}} git checkout {{workflow.parameters.target_branch}} echo "Get commit id" git rev-parse --short origin/{{workflow.parameters.target_branch}} > /workdir/{{workflow.parameters.repo_name}}-commitid.txt commitId=$(cat /workdir/{{workflow.parameters.repo_name}}-commitid.txt) echo "Commit id is got: "$commitId echo "Git Clone and Checkout Complete." volumeMounts: - name: "workdir" mountPath: /workdir resources: requests: memory: 1Gi cpu: 1 activeDeadlineSeconds: 1200

### 提交Workflow参数说明

涉及参数如下：

说明

repo_url参数不能包含https://前缀。

## 相关文档

使用公共Git仓库构建CI Pipeline的最佳实践，请参见[基于工作流集群构建](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)[Golang](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)[项目的](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)[CI Pipeline](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)。

[上一篇：基于工作流集群构建Golang项目的CI Pipeline](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)[下一篇：基于EventBridge的事件驱动CI Pipeline](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases/event-driven-ci-pipeline-based-on-eventbridge.md)

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
