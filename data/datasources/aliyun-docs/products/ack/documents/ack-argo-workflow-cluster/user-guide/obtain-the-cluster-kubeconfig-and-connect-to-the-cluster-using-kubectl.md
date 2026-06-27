# 获取KubeConfig并使用kubectl连接管理集群-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-argo-workflow-cluster/user-guide/obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-argo-workflow-cluster/product-overview.md)

- [服务支持](products/ack/documents/ack-argo-workflow-cluster/support.md)

- [实践教程](products/ack/documents/ack-argo-workflow-cluster/use-cases.md)

- [操作指南](products/ack/documents/ack-argo-workflow-cluster/user-guide.md)

[首页](https://help.aliyun.com/zh)

# 获取集群KubeConfig并通过kubectl工具连接集群

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

除控制台外，还可以使用Kubernetes命令行工具kubectl来管理集群与应用。通过kubectl连接集群时，需先获取包含当前用户身份信息的集群KubeConfig。

## 步骤一：安装并配置kubectl客户端

确定待安装kubectl的客户端机器，根据运行环境和集群版本[安装](https://kubernetes.io/docs/tasks/kubectl/install/)[kubectl](https://kubernetes.io/docs/tasks/kubectl/install/)。

## 步骤二：获取并使用KubeConfig

在控制台获取 KubeConfig 后，kubectl 可依据该文件连接并管理集群。

RAM用户连接集群前，除容器服务的系统权限外，还需要被授予集群操作的权限，请参见[为](products/ack/documents/ack-argo-workflow-cluster/user-guide/obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[RAM](products/ack/documents/ack-argo-workflow-cluster/user-guide/obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[用户授予](products/ack/documents/ack-argo-workflow-cluster/user-guide/obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[RBAC](products/ack/documents/ack-argo-workflow-cluster/user-guide/obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[权限](products/ack/documents/ack-argo-workflow-cluster/user-guide/obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)。

- 

登录[容器](https://csnew.console.aliyun.com/#/next/argowf)[Argo](https://csnew.console.aliyun.com/#/next/argowf)[工作流集群控制台](https://csnew.console.aliyun.com/#/next/argowf)，单击目标集群名称。

- 

在集群信息页面，单击连接信息页签，选择公网访问或内网访问，然后复制KubeConfig。

- 

内网访问：获取内网访问的KubeConfig，此时kubectl客户端机器必须与集群位于同一VPC。通过阿里云内网连接时，延迟更低，更安全。

- 

公网访问：获取公网访问的KubeConfig，通过公网中的任意机器作为客户端来连接集群。依赖[EIP](products/eip/documents/product-overview/what-is-eip.md)连接 API Server，适用于本地开发或远程运维。

EIP 绑定后，相关费用请参见[按量付费](products/eip/documents/pay-as-you-go.md)。

- 

将复制的KubeConfig内容粘贴至客户端的$HOME/.kube/config文件中，保存并退出。

如果$HOME/.kube/config文件不存在，可通过mkdir -p $HOME/.kube和touch $HOME/.kube/config来创建。

- 

配置完成后，执行kubectl命令以验证集群连通性。

以查询命名空间为例。

kubectl get namespaces

预期输出：

NAME STATUS AGE default Active 4h39m kube-node-lease Active 4h39m kube-public Active 4h39m kube-system Active 4h39m

## 为RAM用户授予RBAC权限

- 

登录[容器](https://csnew.console.aliyun.com/#/next/argowf)[Argo](https://csnew.console.aliyun.com/#/next/argowf)[工作流集群控制台](https://csnew.console.aliyun.com/#/next/argowf)，单击目标集群名称。

- 

在权限管理页面，在目标RAM用户右侧单击管理授权，为RAM用户授予下列权限：

| RBAC 权限 | 权限说明 |
| --- | --- |
| admin（管理员） | 具有集群范围和所有命名空间下资源的读写权限。 |
| dev（开发人员） | 具有所选命名空间下的资源读写权限。 |


展开查看集群及命名空间资源列表

- 

集群范围资源列表

| Kind | apiVersion |
| --- | --- |
| Namespace | v1 |
| PersistentVolumes | v1 |
| ImageCaches | eci.alibabacloud.com |


- 

命名空间下资源列表

| Kind | apiVersion |
| --- | --- |
| ConfigMap | v1 |
| Secret | v1 |
| ServiceAccount | v1 |
| PersistentVolumeClaim | v1 |
| Pod | v1 |
| Workflow WorkflowTemplate CronWorkflow | argoproj.io |
| EventSource EventBus Sensor | argoproj.io |


## 容器Argo工作流集群中的kubectl权限

不同于普通的Kubernetes集群，kubectl在容器Argo工作流集群中部分操作会受限，权限说明如下：

| 集群资源 | 权限说明 |
| --- | --- |
| PriorityClass | 可以管理 PriorityClasse，并在工作流中指定 PriorityClass，达到通过 Pod 优先级控制调度顺序的目的。 |
| Namespace | 可以创建 Namespace，拥有自建 Namespace 的全部权限，并可访问自建 Namespace 下的资源。不能访问系统 Namespace 下的资源，即以 kube- 开头的 Namespace。 重要 以集群 ID 命名的命名空间为 Argo 的系统命名空间，您可以操作此系统命名空间，例如，修改 workflow-controller-configmap 配置 Argo Workflow 的运行参数。 |
| Persistentvolume | 全部权限。 |
| Persistentvolumeclaim | 自建 Namespaces 下的全部权限。 |
| Secret Configmap Serviceaccount | 自建 Namespaces 下的全部权限。 |
| Pod | 自建 Namespaces 下的读权限。 |
| Pods/logevents | 自建 Namespaces 下的读权限。 |
| Pods/exec | 自建 Namespaces 下的创建权限。 |
| Argo 资源： workflows workflowtasksets workflowtemplates cronworkflows | 自建 Namespaces 下的全部权限。 |


[上一篇：创建Argo工作流集群](products/ack/documents/ack-argo-workflow-cluster/user-guide/create-an-argo-workflow-cluster.md)[下一篇：开启Argo Server并访问工作流控制台](products/ack/documents/ack-argo-workflow-cluster/user-guide/enable-argo-server-for-a-workflow-cluster.md)

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
