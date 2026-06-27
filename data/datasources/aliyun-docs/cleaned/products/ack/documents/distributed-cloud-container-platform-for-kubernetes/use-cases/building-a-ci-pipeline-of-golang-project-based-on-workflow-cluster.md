# 基于工作流集群构建Golang项目的CI Pipeline-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster

# 基于工作流集群构建Golang项目的CI Pipeline
ACK One工作流集群基于开源Argo Workflows项目构建，全托管Argo Workflows，具有极致弹性、自动扩展、无运维成本等优势，可以帮助您快速实现更简单、低成本、高效率的CI流水线。本文为您介绍如何基于工作流集群构建Golang项目的CI Pipeline。
## 方案介绍
ACK One工作流集群构建CI Pipeline，主要使用[BuildKit](https://github.com/moby/buildkit)实现容器镜像的构建和推送，并使用[BuildKit Cache](https://github.com/moby/buildkit?tab=readme-ov-file#cache)加速镜像的构建。使用NAS存储Go mod cache，可加速go test和go build运行过程，最终大幅加速CI Pipeline的流程。
## 预置工作流模板说明
工作流集群中默认已经预置了名为ci-go-v1的CI工作流模板（ClusterWorkflowTemplate），其使用BuildKit Cache和NAS存储Go mode cache，可大幅加速CI Pipeline的流程。
您可以直接使用预置模板，也可以基于预置模板自定义自己的CI工作流模板。
预置的CI工作流模板中包含以下流程：
Git Clone & Checkout
用于Clone Git仓库，将Git仓库Checkout到目标分支。
获取Commit ID，在构建镜像时根据Commit ID追加Tag后缀。
Run Go Test
默认运行Git Repo（Go项目）中的所有测试用例。
可通过工作流参数enable_test控制是否运行该步骤。
其中Go mod cache存储在NAS的/pkg/mod目录，用于go test和后续的go build的加速。
Build & Push Image
使用BuildKit构建和推送容器镜像，并使用BuildKit Cache中registry类型的cache来加速镜像构建。
镜像Tag默认使用{container_tag}-{commit_id}格式，可在提交工作流时通过参数控制是否追加Commit ID。
推送镜像的同时，也会推送覆盖其latest版本镜像。
预置的CI工作流模板内容如下：
展开查看模板内容
apiVersion: argoproj.io/v1alpha1 kind: ClusterWorkflowTemplate metadata: name: ci-go-v1 spec: entrypoint: main volumes: - name: run-test emptyDir: {} - name: workdir persistentVolumeClaim: claimName: pvc-nas - name: docker-config secret: secretName: docker-config arguments: parameters: - name: repo_url value: "" - name: repo_name value: "" - name: target_branch value: "main" - name: container_image value: "" - name: container_tag value: "v1.0.0" - name: dockerfile value: "./Dockerfile" - name: enable_suffix_commitid value: "true" - name: enable_test value: "true" templates: - name: main dag: tasks: - name: git-checkout-pr inline: container: image: alpine:latest command: - sh - -c - | set -eu apk --update add git cd /workdir echo "Start to Clone "{{workflow.parameters.repo_url}} git -C "{{workflow.parameters.repo_name}}" pull || git clone {{workflow.parameters.repo_url}} cd {{workflow.parameters.repo_name}} echo "Start to Checkout target branch" {{workflow.parameters.target_branch}} git checkout --track origin/{{workflow.parameters.target_branch}} || git checkout {{workflow.parameters.target_branch}} git pull echo "Get commit id" git rev-parse --short origin/{{workflow.parameters.target_branch}} > /workdir/{{workflow.parameters.repo_name}}-commitid.txt commitId=$(cat /workdir/{{workflow.parameters.repo_name}}-commitid.txt) echo "Commit id is got: "$commitId echo "Git Clone and Checkout Complete." volumeMounts: - name: "workdir" mountPath: /workdir resources: requests: memory: 1Gi cpu: 1 activeDeadlineSeconds: 1200 - name: run-test when: "{{workflow.parameters.enable_test}} == true" inline: container: image: golang:1.22-alpine command: - sh - -c - | set -eu if [ ! -d "/workdir/pkg/mod" ]; then mkdir -p /workdir/pkg/mod echo "GOMODCACHE Directory /pkg/mod is created" fi export GOMODCACHE=/workdir/pkg/mod cp -R /workdir/{{workflow.parameters.repo_name}} /test/{{workflow.parameters.repo_name}} echo "Start Go Test..." cd /test/{{workflow.parameters.repo_name}} go test -v ./... echo "Go Test Complete." volumeMounts: - name: "workdir" mountPath: /workdir - name: run-test mountPath: /test resources: requests: memory: 4Gi cpu: 2 activeDeadlineSeconds: 1200 depends: git-checkout-pr - name: build-push-image inline: container: image: moby/buildkit:v0.13.0-rootless command: - sh - -c - | set -eu tag={{workflow.parameters.container_tag}} if [ {{workflow.parameters.enable_suffix_commitid}} == "true" ] then commitId=$(cat /workdir/{{workflow.parameters.repo_name}}-commitid.txt) tag={{workflow.parameters.container_tag}}-$commitId fi echo "Image Tag is: "$tag echo "Start to Build And Push Container Image" cd /workdir/{{workflow.parameters.repo_name}} buildctl-daemonless.sh build \ --frontend \ dockerfile.v0 \ --local \ context=. \ --local \ dockerfile=. \ --opt filename={{workflow.parameters.dockerfile}} \ --opt build-arg:GOPROXY=http://goproxy.cn,direct \ --output \ type=image,\"name={{workflow.parameters.container_image}}:${tag},{{workflow.parameters.container_image}}:latest\",push=true,registry.insecure=true \ --export-cache mode=max,type=registry,ref={{workflow.parameters.container_image}}:buildcache \ --import-cache type=registry,ref={{workflow.parameters.container_image}}:buildcache echo "Build And Push Container Image {{workflow.parameters.container_image}}:${tag} and {{workflow.parameters.container_image}}:latest Complete." env: - name: BUILDKITD_FLAGS value: --oci-worker-no-process-sandbox - name: DOCKER_CONFIG value: /.docker volumeMounts: - name: workdir mountPath: /workdir - name: docker-config mountPath: /.docker securityContext: seccompProfile: type: Unconfined runAsUser: 1000 runAsGroup: 1000 resources: requests: memory: 4Gi cpu: 2 activeDeadlineSeconds: 1200 depends: run-test
模板中暴露的参数如下：
| 参数 | 说明 | 示例值 |
| --- | --- | --- |
| entrypoint | 定义入口模板。 | main |
| repo_url | Git 仓库的 url。 | https://github.com/ivan-cai/echo-server.git |
| repo_name | 仓库名称。 | echo-server |
| target_branch | 仓库的目标分支。 默认为 main。 | main |
| container_image | 要构建的镜像。格式如下： <ACR EE Domain>/<ACR EE 命名空间>/<仓库名>。 | test-registry.cn-hongkong.cr.aliyuncs.com/acs/echo-server |
| container_tag | 要构建的镜像 Tag。 默认为 v1.0.0。 | v1.0.0 |
| dockerfile | Dockerfile 目录和文件名。 项目根目录下的相对路径，默认为 ./Dockerfile 。 | ./Dockerfile |
| enable_suffix_commitid | 是否在镜像 Tag 后追加 Commit ID。 true：追加 false：不追加 默认值为 true。 | true |
| enable_test | 是否开启运行 Go Test 步骤。 true：开启 false：不开启 默认值为 true。 | true |
## 前提条件
[创建分布式工作流](../user-guide/create-a-workflow-cluster.md)[Argo](../user-guide/create-a-workflow-cluster.md)[集群](../user-guide/create-a-workflow-cluster.md)
从[ACK One](https://cs.console.aliyun.com/one)[控制台](https://cs.console.aliyun.com/one)获取工作流集群的KubeConfig，并通过kubectl连接至工作流集群。具体操作，请参见[获取集群](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[KubeConfig](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[并通过](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[工具连接集群](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)。
[安装阿里云](../user-guide/create-a-workflow.md)[Argo CLI](../user-guide/create-a-workflow.md)
[完成](https://help.aliyun.com/zh/document_detail/2252086.html#task-2322675)[RAM](https://help.aliyun.com/zh/document_detail/2252086.html#task-2322675)[用户授权](https://help.aliyun.com/zh/document_detail/2252086.html#task-2322675)
[创建](https://help.aliyun.com/zh/nas/user-guide/create-a-file-system)[NAS](https://help.aliyun.com/zh/nas/user-guide/create-a-file-system)[文件系统](https://help.aliyun.com/zh/nas/user-guide/create-a-file-system)
[创建容器镜像服务企业版实例（ACR EE）](https://help.aliyun.com/zh/acr/user-guide/create-a-container-registry-enterprise-edition-instance)
## 操作步骤
本文以公共Git仓库为例为您介绍构建CI Pipeline的操作，如果您在工作流的CI Pipeline中使用的是私有Git仓库，则需要在CI流程中先成功Clone该私有仓库。具体的Clone操作，请参见[在](clone-private-git-repository-in-ci-pipeline.md)[CI Pipeline](clone-private-git-repository-in-ci-pipeline.md)[中](clone-private-git-repository-in-ci-pipeline.md)[Clone](clone-private-git-repository-in-ci-pipeline.md)[私有](clone-private-git-repository-in-ci-pipeline.md)[Git](clone-private-git-repository-in-ci-pipeline.md)[仓库](clone-private-git-repository-in-ci-pipeline.md)。
重要
保存容器镜像访问凭证的Secret和挂载的NAS存储卷都需要与最终提交的工作流在同一个命名空间下。
### 步骤一：在工作流集群中创建ACR EE访问凭证
ACR EE访问凭证主要用于BuildKit推送镜像。
为ACR EE配置访问凭证。具体操作，请参见[配置访问凭证](https://help.aliyun.com/zh/acr/user-guide/configure-access-credentials)。
执行如下命令，在工作流集群中创建Secret保存ACR EE的密码，供BuildKit使用。
$username:$password需要替换为您实际为ACR EE配置的访问凭证信息。
kubectl create secret generic docker-config --from-literal="config.json={\"auths\": {\"$repositoryDomain\": {\"auth\": \"$(echo -n $username:$password|base64)\"}}}"
### 步骤二：在工作流集群中挂载NAS存储卷
使用NAS存储卷的目的如下：
在工作流的各任务之间共享数据，如Clone的代码仓库信息等。
存储Go mod cache，用于加速CI Pipeline中的go test和go build过程。
在工作流集群中使用NAS存储卷的步骤如下：
获取NAS文件系统的挂载点地址。具体操作，请参见[管理挂载点](https://help.aliyun.com/zh/nas/user-guide/manage-mount-targets)。
使用以下内容在工作流集群中创建PV/PVC。具体操作，请参见[使用](../user-guide/use-volumes.md)[NAS](../user-guide/use-volumes.md)[存储卷](../user-guide/use-volumes.md)。
apiVersion: v1 kind: PersistentVolume metadata: name: pv-nas labels: alicloud-pvname: pv-nas spec: capacity: storage: 100Gi accessModes: - ReadWriteMany csi: driver: nasplugin.csi.alibabacloud.com volumeHandle: pv-nas # 必须与PV Name保持一致。 volumeAttributes: server: <your nas filesystem mount point address> path: "/" mountOptions: - nolock,tcp,noresvport - vers=3 --- kind: PersistentVolumeClaim apiVersion: v1 metadata: name: pvc-nas spec: accessModes: - ReadWriteMany resources: requests: storage: 100Gi selector: matchLabels: alicloud-pvname: pv-nas
### 步骤三：基于预置模板启动工作流
## 通过控制台提交工作流
登录[ACK One](https://cs.console.aliyun.com/one)[控制台](https://cs.console.aliyun.com/one)，在左侧导航栏选择工作流集群>集群信息。
在集群信息页面，单击基础信息页签，然后在下方常用操作区域，单击工作流控制台（Argo）。
在Argo工作台左侧导航栏单击Cluster Workflow Templates，然后单击ci-go-v1预置模板名称。
在模板详情页左上角单击+ SUBMIT，然后在弹出的面板中填写相关参数，并在面板下方单击+ SUBMIT。
参数填写请参考[模板参数说明](building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)将参数值设置为您实际使用的参数值。
操作完成后，您可在Workflows详情页查看工作流运行情况：
## 通过Argo CLI提交工作流
使用以下内容创建workflow.yaml文件，按照[模板参数说明](building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)将参数值修改为您实际使用的参数值。
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: ci-go-v1- labels: workflows.argoproj.io/workflow-template: ackone-ci spec: arguments: parameters: - name: repo_url value: https://github.com/ivan-cai/echo-server.git - name: repo_name value: echo-server - name: target_branch value: main - name: container_image value: "test-registry.cn-hongkong.cr.aliyuncs.com/acs/echo-server" - name: container_tag value: "v1.0.0" - name: dockerfile value: ./Dockerfile - name: enable_suffix_commitid value: "true" - name: enable_test value: "true" workflowTemplateRef: name: ci-go-v1 clusterScope: true
执行以下命令提交工作流。
argo submit workflow.yaml
## 相关文档
本文以公共Git仓库为例为您介绍构建CI Pipeline的操作，如果您在工作流的CI Pipeline中使用的是私有Git仓库，则需要在CI流程中先成功Clone该私有仓库。具体的Clone操作，请参见[在](clone-private-git-repository-in-ci-pipeline.md)[CI Pipeline](clone-private-git-repository-in-ci-pipeline.md)[中](clone-private-git-repository-in-ci-pipeline.md)[Clone](clone-private-git-repository-in-ci-pipeline.md)[私有](clone-private-git-repository-in-ci-pipeline.md)[Git](clone-private-git-repository-in-ci-pipeline.md)[仓库](clone-private-git-repository-in-ci-pipeline.md)。
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
