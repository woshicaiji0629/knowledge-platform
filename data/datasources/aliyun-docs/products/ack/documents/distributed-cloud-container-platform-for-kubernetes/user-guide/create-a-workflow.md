# 使用Argo CLI或kubectl创建工作流并配置CPU与Memory-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/distributed-cloud-container-platform-for-kubernetes/user-guide/create-a-workflow

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

# 创建工作流

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

工作流集群基于开源Argo Workflow项目构建，适用于CI/CD流水线、数据处理、机器学习和仿真计算等。本文通过示例介绍如何使用Argo CLI创建工作流，并设置CPU和Memory资源。

## 前提条件

- 

[已创建分布式工作流](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/create-a-workflow-cluster.md)[Argo](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/create-a-workflow-cluster.md)[集群](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/create-a-workflow-cluster.md)

- 

[已完成](https://help.aliyun.com/zh/document_detail/2252086.html#task-2322675)[RAM](https://help.aliyun.com/zh/document_detail/2252086.html#task-2322675)[用户授权](https://help.aliyun.com/zh/document_detail/2252086.html#task-2322675)

## 使用说明

### 工作流ServiceAccount

工作流可指定ServiceAccount用于运行中访问其他Kubernetes资源，您可以创建自己的ServiceAccount，工作流集群会为ServiceAccount自动绑定权限，若权限不足，请加入钉钉群（钉钉群号：35688562），联系产品技术专家进行咨询。

### 阿里云Argo CLI

阿里云Argo CLI完全兼容开源Argo CLI，并增强了Metrics能力和日志能力。您可以使用阿里云Argo CLI查看工作流的CPU、内存资源消耗及运行成本，并获取已删除Pod的日志。

安装步骤如下：

说明

以下安装步骤以Linux系统为例，Darwin和Linux系统的下载链接分别如下：

- 

Darwin：[argo-cli-aliyun-darwin](https://ack-one.oss-cn-hangzhou.aliyuncs.com/cli/v3.4.12/argo-cli-aliyun-darwin)

- 

Linux：[argo-cli-aliyun-linux](https://ack-one.oss-cn-hangzhou.aliyuncs.com/cli/v3.4.12/argo-cli-aliyun-linux)

- 

执行如下命令，下载阿里云Argo CLI。

wget https://ack-one.oss-cn-hangzhou.aliyuncs.com/cli/v3.4.12/argo-cli-aliyun-linux

- 

执行如下命令为argo-cli-aliyun-linux授予可执行权限。

chmod +x argo-cli-aliyun-linux

- 

将执行文件移动到环境变量包含的目录下，例如：/usr/local/bin/。

mv argo-cli-aliyun-linux /usr/local/bin/argo

## 创建工作流

您可以通过以下阿里云Argo CLI和kubectl两种方式操作创建工作流。

### 使用阿里云Argo CLI操作工作流

- 

使用以下内容，创建helloworld-workflow.yaml文件。

apiVersion: argoproj.io/v1alpha1 kind: Workflow # new type of k8s spec. metadata: generateName: hello-world- # name of the workflow spec. spec: entrypoint: whalesay # invoke the whalesay template. templates: - name: whalesay # name of the template. container: image: docker/whalesay command: [ cowsay ] args: [ "hello world" ]

- 

执行以下命令，提交工作流。

argo submit helloworld-workflow.yaml

- 

查看工作流状态。

- 

执行以下命令，获取工作流列表。

argo list

预期输出：

NAME STATUS AGE DURATION PRIORITY hello-world-lgdpp Succeeded 2m 37s 0

- 

执行以下命令，查看工作流状态。

argo get hello-world-lgdpp

预期输出：

Name: hello-world-lgdpp Namespace: default ServiceAccount: unset (will run with the default ServiceAccount) Status: Succeeded Conditions: PodRunning False Completed True .... Duration: 37 seconds Progress: 1/1 ResourcesDuration: 17s*(1 cpu),17s*(100Mi memory) STEP TEMPLATE PODNAME DURATION MESSAGE ✔ hello-world-lgdpp whalesay hello-world-lgdpp 27s

### 使用kubectl操作工作流

KubeConfig设置完成后，您可以通过kubectl操作工作流集群，但不同于普通的Kubernetes集群，部分操作会受限。相关权限说明如下。

| 资源 | 权限说明 |
| --- | --- |
| priorityclasses | 可以管理 priorityclasses，并在工作流中制定 priorityclasses，达到通过 Pod 优先级控制调度顺序的目的。 |
| namespaces | 可以创建 Namespaces，拥有自建 Namespaces 的全部权限，并可访问自建 Namespaces 下的资源。不能访问系统 Namespaces 下的资源。系统 Namespaces 即以 kube- 开头的 Namespaces。 重要 以集群 ID 命名的命名空间为 Argo 的系统命名空间，您可以操作此系统命名空间，例如，修改 workflow-controller-configmap 配置 Argo Workflow 的运行参数。 |
| persistentvolumes | 全部权限。 |
| persistentvolumeclaims | 自建 Namespaces 下的全部权限。 |
| secretsconfigmapsserviceaccounts | 自建 Namespaces 下的全部权限。 |
| pods | 自建 Namespaces 下的读权限。 |
| pods/logevents | 自建 Namespaces 下的读权限。 |
| pods/exec | 自建 Namespaces 下的创建权限。 |
| Argo: workflows workflowtasksets workflowtemplates cronworkflows | 自建 Namespaces 下的全部权限。 |


## 设置容器CPU和内存

工作流集群优先使用抢占式ECI实例，并配合按量付费ECI应优化成本。抢占式ECI实例的保护期为1小时，请确保工作流的子步骤在此时间内完成。

抢占式ECI实例仅支持2 vCPU及以上规格，不支持小于2 vCPU的配置。

- 

如果容器未配置资源请求或配置小于2 vCPU/4 GiB，系统默认使用2 vCPU/4 GiB。

- 

如果容器配置的资源请求大于2 vCPU/4 GiB，系统会自动匹配满足规格的ECI。

支持指定的vCPU和内存规格如下表所示。不建议使用大于8 vCPU的配置。

| vCPU | 内存（GiB） |
| --- | --- |
| 2 | 4、8、16 |
| 4 | 4、8、16、32 |
| 8 | 4、8、16、32、64 |


## 强制使用按量计费ECI运行工作流

在成本优先模式下，如需运行关键任务，不希望使用抢占式ECI实例。您可以设置工作流使用按量计费ECI实例运行工作流。

配置Container的requests和limits字段，示例代码如下。

apiVersion: argoproj.io/v1alpha1 kind: Workflow # new type of k8s spec. metadata: generateName: hello-world- # name of the workflow spec. spec: entrypoint: whalesay # invoke the whalesay template. templates: - name: whalesay # name of the template. container: image: docker/whalesay command: [ cowsay ] args: [ "hello world" ] resources: requests: cpu: 0.5 memory: 1Gi limits: cpu: 0.5 memory: 1Gi

[上一篇：管理工作流](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/workflow.md)[下一篇：使用指定ECS规格运行工作流](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/run-a-workflow-using-a-specified-ecs-specification.md)

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
