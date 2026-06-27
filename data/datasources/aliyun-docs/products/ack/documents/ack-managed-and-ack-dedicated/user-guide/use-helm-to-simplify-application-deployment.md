# 使用Helm部署和管理应用-容器服务Kubernetes版ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/use-helm-to-simplify-application-deployment/

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-managed-and-ack-dedicated/product-overview.md)

- [快速入门](products/ack/documents/ack-managed-and-ack-dedicated/getting-started.md)

- [操作指南](products/ack/documents/ack-managed-and-ack-dedicated/user-guide.md)

- [实践教程](products/ack/documents/ack-managed-and-ack-dedicated/use-cases.md)

- [安全合规](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference.md)

- [服务支持](products/ack/documents/ack-managed-and-ack-dedicated/support.md)

[首页](https://help.aliyun.com/zh)

# 使用Helm简化应用部署

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Helm 能将 Kubernetes 应用所需的多种资源（如工作负载、Service、Ingress）打包管理，简化在 ACK 集群中部署与升级应用的流程。

## 创建Helm应用

以通过控制台使用Helm部署Dify应用为例。确保ACK 集群至少有 2 核 CPU 和 4 GB 内存 的可用资源。

- 

为 Dify 创建其依赖的 CNFS 和 NAS 存储类。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，选择集群列表。在集群列表页面，单击目标集群名称，然后选择存储>存储类。

- 

在存储类页面，单击使用YAML创建资源，将以下YAML内容复制到模板内，然后单击创建。

如果系统提示已存在同名资源，说明集群已自动创建CNFS及NAS存储类，可直接进行部署应用操作。 创建NAS存储会产生费用，详情请参见[NAS](https://help.aliyun.com/zh/nas/product-overview/billable-items/)[计费](https://help.aliyun.com/zh/nas/product-overview/billable-items/)。apiVersion: storage.alibabacloud.com/v1beta1 kind: ContainerNetworkFileSystem metadata: name: cnfs-nas-filesystem spec: description: "cnfs" type: nas reclaimPolicy: Retain # 仅支持Retain，删除CNFS时不会删除后端的NAS实例。 --- apiVersion: storage.k8s.io/v1 kind: StorageClass metadata: name: alibabacloud-cnfs-nas mountOptions: - nolock,tcp,noresvport - vers=3 parameters: volumeAs: subpath # 每个PVC都会在NAS下创建一个独立的子目录。 containerNetworkFileSystem: cnfs-nas-filesystem # 关联到上面定义的CNFS实例。 path: "/" provisioner: nasplugin.csi.alibabacloud.com reclaimPolicy: Retain allowVolumeExpansion: true # 可选：指定为true则允许对存储卷的目录配额进行扩容。

- 

部署Dify应用。

在集群详情页面，选择应用>Helm。在Helm页面，单击创建。

- 

基本信息：在Chart中搜索ack-dify，勾选搜索结果。

- 

参数配置：Chart版本选择最新版。

- 

访问Dify应用。

- 

为ack-dify服务开启公网访问功能。

公网访问便于演示操作，如果在生产环境中部署，为了应用数据安全，建议开启访问控制功能。

选择网络>服务，选择命名空间为dify-system。选择Service名称为ack-dify，单击更新操作，配置开启公网访问完成后单击确定。

- 

服务类型为负载均衡 (LoadBalancer)。

- 

访问方式为公网访问。

- 

虚拟交换机勾选专有网络中对应可用区的交换机。

- 

访问Dify应用。

配置完成后，将外部 IP 地址（External IP）输入浏览器地址栏即可访问Dify服务。

## 管理Helm应用

在控制台Helm应用列表页面，可对目标应用执行更新、删除等管理操作。

| 操作 | 说明 |
| --- | --- |
| 查看应用 | 单击目标应用名称或 详情 ，查看该应用的资源、YAML 文件、历史版本等信息。 |
| 更新应用 | 单击 更新 ，在 更新发布 面板中修改相关参数，然后单击 确定 。 重要 更新将直接影响关联应用的运行状态，导致服务重启或功能异常。建议在变更前充分评估影响范围，并在业务低峰期执行操作。 |
| 删除应用 | 单击 删除 ，在 删除应用 对话框中，选中 清除发布记录 ，然后单击 确定 ，删除应用以及包含的 Service、Deployment 等资源。 本示例删除 Dify 应用时，不会自动同步删除 NAS 资源，需手动 [删除](https://help.aliyun.com/zh/nas/user-guide/delete-a-file-system) [NAS](https://help.aliyun.com/zh/nas/user-guide/delete-a-file-system) [文件系统](https://help.aliyun.com/zh/nas/user-guide/delete-a-file-system) 。 重要 如果删除时未选中 清除发布记录 ，此时该应用会保留在发布列表中，后续部署同名应用时，会因命名冲突而失败。 |


## 常见问题

如何使用Helm CLI部署第三方库应用？如果ACK提供的Chart无法满足需求，可使用Helm命令行工具部署应用。

- 

连接集群。

## 云端

[在](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-kubectl-on-cloud-shell-to-manage-ack-clusters-1690962464408.md)[Workbench](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-kubectl-on-cloud-shell-to-manage-ack-clusters-1690962464408.md)[或](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-kubectl-on-cloud-shell-to-manage-ack-clusters-1690962464408.md)[CloudShell](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-kubectl-on-cloud-shell-to-manage-ack-clusters-1690962464408.md)[上使用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-kubectl-on-cloud-shell-to-manage-ack-clusters-1690962464408.md)[kubectl](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-kubectl-on-cloud-shell-to-manage-ack-clusters-1690962464408.md)[连接集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-kubectl-on-cloud-shell-to-manage-ack-clusters-1690962464408.md)。

阿里云提供浏览器命令行工具已预装 Helm，无需额外配置。

## 本地

- 

[获取集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[KubeConfig](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[并通过](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[工具连接集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)。

- 

[安装](https://helm.sh/docs/intro/install/)[Helm CLI](https://helm.sh/docs/intro/install/)。

curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

- 

添加Chart仓库。

将<REPO_NAME>替换为仓库别名，<REPO_URL>替换为仓库地址。helm repo add <REPO_NAME> <REPO_URL>

- 

更新仓库信息。

helm repo update

- 

第三方库部署应用。

将<APP_NAME>替换为应用实例名，<CHART_NAME>替换为要安装的 Chart 名称。helm install <APP_NAME> <REPO_NAME>/<CHART_NAME>

Helm更多命令请参见[Helm 官方文档](https://helm.sh/docs/intro/using_helm/)。

为什么Helm应用无法删除？

问题现象

- 

在控制台删除Helm应用时，应用长时间停留在“卸载”状态。

- 

通过Helm CLI删除应用时，命令行返回以下错误：

no matches for kind "***" in version "***" ensure CRDs are installed first

问题原因

该问题通常发生在集群升级后旧版本API被废弃，若Helm应用中包含使用已废弃API的资源，删除时会因API版本不存在而失败。

Kubernetes不同版本的废弃API列表，请参见[Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/)。

解决方案

- 

使用 Helm 官方[helm-mapkubeapis](https://github.com/helm/helm-mapkubeapis)插件将Release中已废弃的API版本映射到新版支持的API版本，然后重新删除。

将<RELEASE_NAME>和<NAMESPACE>替换为Helm应用名称及所在的命名空间。helm plugin install https://github.com/helm/helm-mapkubeapis helm mapkubeapis <RELEASE_NAME> -n <NAMESPACE>

预期输出...completed successfully说明API版本已映射成功。

- 

完成API版本映射后，即可正常删除该应用。

helm uninstall <RELEASE_NAME> -n <NAMESPACE>

预期输出release "***" uninstalled，表明Helm应用删除成功。

## 相关文档

- 

为确保集群安全并使用更完善的功能，建议[将](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/update-helm-v2-to-helm-v3.md)[Helm V2](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/update-helm-v2-to-helm-v3.md)[升级迁移至](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/update-helm-v2-to-helm-v3.md)[Helm V3](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/update-helm-v2-to-helm-v3.md)。

- 

容器镜像服务企业版的Helm Chart功能支持[推送和拉取](https://help.aliyun.com/zh/acr/user-guide/push-and-pull-helm-chart/)[Helm Chart](https://help.aliyun.com/zh/acr/user-guide/push-and-pull-helm-chart/)。

[上一篇：管理自定义资源](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/manage-custom-resources.md)[下一篇：将Helm V2升级迁移至Helm V3](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/update-helm-v2-to-helm-v3.md)

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
