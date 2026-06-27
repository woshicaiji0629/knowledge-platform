# 创建工作流集群用于管理多个工作流任务-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/distributed-cloud-container-platform-for-kubernetes/user-guide/create-a-workflow-cluster

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

# 创建工作流集群

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

工作流集群采用无服务器模式，使用阿里云弹性容器实例ECI运行工作流，通过优化Kubernetes集群参数，实现大规模工作流的高效弹性调度，同时配合抢占式ECI实例，优化成本。本文介绍如何创建工作流集群。

## 前提条件

- 

[已开通分布式云容器平台](https://www.aliyun.com/product/aliware/adcp)[ACK One](https://www.aliyun.com/product/aliware/adcp)。

- 

[已开通阿里云弹性容器实例](https://www.aliyun.com/product/eci)[ECI](https://www.aliyun.com/product/eci)。

- 

[已创建专有网络和交换机](products/vpc/documents/user-guide/create-and-manage-a-vpc.md)

- 

已安装阿里云CLI并配置凭证，且CLI版本为3.0.159及以上。具体操作，请参见[安装阿里云](https://help.aliyun.com/zh/cli/installation-guide/)[CLI](https://help.aliyun.com/zh/cli/installation-guide/)和[配置凭证](https://help.aliyun.com/zh/cli/configure-credentials/)。

- 

已授予RAM用户AliyunAdcpFullAccess权限。具体操作，请参见[为](products/ack/documents/grant-permissions-to-a-ram-user-1.md)[RAM](products/ack/documents/grant-permissions-to-a-ram-user-1.md)[用户授权](products/ack/documents/grant-permissions-to-a-ram-user-1.md)。

## 创建工作流集群

## 通过控制台创建集群

- 

登录[ACK One](https://cs.console.aliyun.com/one#/argowf/cluster/detail)[工作流集群控制台](https://cs.console.aliyun.com/one#/argowf/cluster/detail)。

- 

在工作流集群页面右上角单击创建工作流集群，在弹出的面板中填写相关参数，然后单击创建。

- 

- 

| 参数 | 描述 |
| --- | --- |
| 集群名称 | 填写集群的名称。 说明 长度为 1~63 个字符，可包含字母、数字、下划线（_）或中划线（-），且仅允许以字母开头。 |
| 地域 | 选择集群所在的地域。 |
| 专有网络 | 设置集群的专有网络 VPC，在下拉列表中选择已创建的 VPC。 |
| 虚拟交换机 | 在下拉列表中选择已创建的交换机。 |
| APIServer 负载均衡（SLB） | 无需设置，创建 工作流集群 时会默认为 API Server 创建一个规格为 标准型 I（slb.s2.small） 的 SLB 实例，若删除该实例会导致 API Server 无法访问。 如 SLB 实例规格不满足要求，您可以前往 SLB 控制台修改，具体操作，请参见 [SLB](products/slb/documents/classic-load-balancer/product-overview/change-the-configurations-of-subscription-instances.md) [实例升配](products/slb/documents/classic-load-balancer/product-overview/change-the-configurations-of-subscription-instances.md) 。 SLB 实例计费信息，请参见 [SLB](products/slb/documents/classic-load-balancer/product-overview/billing-overview.md) [计费说明](products/slb/documents/classic-load-balancer/product-overview/billing-overview.md) 。 |
| 创建并绑定 EIP | 选择是否为集群绑定 EIP。 开启后，系统将为内网 SLB 实例创建并绑定一个 EIP（弹性公网 IP），获得从公网访问集群 API Server 的能力。EIP 绑定后不支持解绑，因为可能有子集群已经使用舰队的公网访问链接。 若选择不开启，则无法通过外网访问集群 API Server。 EIP 计费信息，请参见 [弹性公网](products/eip/documents/billing-overview.md) [IP](products/eip/documents/billing-overview.md) [计费说明](products/eip/documents/billing-overview.md) 。 |
| 开启组件及审计日志 | 选择是否开启日志服务功能。 开启后，系统将自动创建一个名称为 k8s-log-{ClusterID} 的日志服务，并收集托管侧控制平面组件（包括 kube-apiserver、kube-controller-manager 等）的日志到日志服务中。以便您后续对 工作流集群 的日志进行审计。 日志服务计费信息，请参见 [日志服务计费说明](products/sls/documents/billing-overview.md) 。 |


## 通过阿里云CLI创建集群

- 

执行以下命令，创建工作流集群。

aliyun configure set --region cn-zhangjiakou aliyun adcp CreateHubCluster --Profile XFlow --RegionId cn-zhangjiakou --VpcId vpc-xxx --VSwitches "[\"vsw-xxx\",\"vsw-xxx\"]" --Name workflow1 --ApiServerPublicEip true --IsEnterpriseSecurityGroup true

| 参数 | 说明 |
| --- | --- |
| Profile | 必选，输入 XFlow 。 |
| RegionId | 必选， 工作流集群 所在地域。本示例选择 cn-zhangjiakou 。 |
| VpcId | 必选， 工作流集群 所在专有网络 VPC ID。 |
| VSwitches | 必选，工作流运行 ECI 所在的交换机 vSwtich ID，格式为数组。请输入多可用区的交换机 ID。 |
| Name | 可选， 工作流集群 名称。 |
| IsEnterpriseSecurityGroup | 必选，使用企业安全组，输入 true 。 |
| ApiServerPublicEip | 可选，是否使用公网 EIP 暴露工作流引擎实例 APIServer 地址。 |


预期输出如下，并记录ClusterId。

{ "ClusterId": "xxx", "RequestId": "xxx", "TaskId": "xxx" }

- 

执行以下命令，查看工作流集群的状态。

替换以下XXX为您上一步获取的ClusterId。

aliyun adcp DescribeHubClusterDetails --ClusterId XXX | jq .Cluster.ClusterInfo

等待直到预期输出的State为running状态。

- 

执行以下命令，安装jq。

- 

macOS：

brew install jq

- 

CentOS：

yum install jq

- 

Ubuntu：

apt-get install jq

- 

执行以下命令，自动解析文本并生成KubeConfig。

aliyun adcp DescribeHubClusterKubeconfig --ClusterId <cluster id> | jq -r .Kubeconfig | tee ack-argo-workflow-kubeconfig # 设置KUBECONFIG环境变量准备运行kubectl和Argo CLI。 export KUBECONFIG=ack-argo-workflow-kubeconfig

## 删除工作流集群

重要

删除工作流集群前，请先删除集群上的工作流，以触发删除Pod以及Pod相关的ECI资源。

## 通过控制台删除集群

- 

登录[ACK One](https://cs.console.aliyun.com/one#/argowf/cluster/detail)[工作流集群控制台](https://cs.console.aliyun.com/one#/argowf/cluster/detail)。

- 

在页面左上角单击集群名称后的下拉列表，选择需要删除的集群。

- 

在工作流集群页面右上角单击删除工作流集群，然后在弹出的提示框中单击确定。

## 通过阿里云CLI删除集群

- 

使用以下命令关闭Argo Server同时删除相关SLB和ECI等资源。

aliyun adcp UpdateHubClusterFeature --ArgoServerEnabled false --ClusterId <cluster id>

- 

使用以下命令删除工作流集群。

aliyun adcp DeleteHubCluster --ClusterId <cluster id>

## 相关文档

- 

如需修改工作流集群的配置，请参见[修改工作流集群配置](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/modify-the-configuration-of-a-workflow-cluster.md)。

- 

工作流集群创建完成后，您可以[创建工作流](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/create-a-workflow.md)。

[上一篇：管理工作流集群](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/managing-workflow-clusters.md)[下一篇：开启Argo Server访问工作流集群](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/enable-argo-server-for-a-workflow-cluster.md)

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
