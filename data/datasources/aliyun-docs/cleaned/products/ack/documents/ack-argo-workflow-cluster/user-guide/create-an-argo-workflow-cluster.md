# 创建Argo工作流集群-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-argo-workflow-cluster/user-guide/create-an-argo-workflow-cluster

# 创建Argo工作流集群
容器Argo工作流集群采用无服务器模式，使用阿里云容器计算服务ACS运行工作流，通过优化Kubernetes集群参数，实现大规模工作流的高效弹性调度，同时配合BestEffort，优化成本。本文介绍如何创建容器Argo工作流集群。
## 适用范围
[已开通分布式云容器平台](https://www.aliyun.com/product/aliware/adcp)[ACK One](https://www.aliyun.com/product/aliware/adcp)。
已开通容器计算服务ACS。
已[创建专有网络和交换机](../../../../vpc/documents/user-guide/create-and-manage-a-vpc.md)
RAM用户需具有AliyunAdcpFullAccess权限才能创建集群。具体操作，请参见[为](../../grant-permissions-to-a-ram-user-1.md)[RAM](../../grant-permissions-to-a-ram-user-1.md)[用户授权](../../grant-permissions-to-a-ram-user-1.md)。
## 创建工作流集群
登录[容器](https://csnew.console.aliyun.com/#/next/argowf)[Argo](https://csnew.console.aliyun.com/#/next/argowf)[工作流集群控制台](https://csnew.console.aliyun.com/#/next/argowf)。
单击创建工作流集群，在弹出的面板中填写相关参数，然后单击下一步。完成依赖检查后，单击创建集群。
| 参数 | 描述 |
| --- | --- |
| 集群名称 | 填写集群的名称。 长度为 1～63 个字符，可包含字母、数字、下划线（_）或中划线（-），且仅允许以字母开头。 |
| 地域 | 选择集群所在的地域。 |
| 专有网络 | 设置集群的专有网络 VPC，在下拉列表中选择已创建的 VPC。 |
| 虚拟交换机 | 在下拉列表中选择已创建的交换机。 |
| 资源组 | 将集群归属于选择的 [资源组](../../../../ecs/documents/user-guide/resource-groups.md) ，便于权限管理和成本分摊。 一个资源只能归属于一个资源组。 |
| 标签 | 为集群绑定键值对 [标签](https://help.aliyun.com/zh/resource-management/tag/product-overview/tag-overview) ，作为云资源的标识。 |
| API Server 访问 | 无需设置，创建 容器 Argo 工作流集群 时会默认自动新建一个按量付费的私网 CLB 实例作为 API Server 的内网连接端点。 重要 请勿删除该实例，否则会导致集群 API Server 无法访问。 |
| 创建并绑定 EIP | 开启后，集群 API Server 使用的 CLB 实例将绑定一个弹性公网 IP，使集群 API Server 支持公网访问。 |
| 开启组件及审计日志 | 同时将启用集群 API Server 审计功能，收集对 Kubernetes API 的请求以及请求结果。如需后续启用，请参见 [采集](../../ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) [ACK](../../ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) [集群容器日志](../../ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) 、 [使用集群](../../ack-managed-and-ack-dedicated/security-and-compliance/work-with-cluster-auditing.md) [API Server](../../ack-managed-and-ack-dedicated/security-and-compliance/work-with-cluster-auditing.md) [审计功能](../../ack-managed-and-ack-dedicated/security-and-compliance/work-with-cluster-auditing.md) 。 |
## 删除工作流集群
重要
删除容器Argo工作流集群前，请先删除集群上的工作流，以释放ACS资源。
登录[容器](https://csnew.console.aliyun.com/#/next/argowf)[Argo](https://csnew.console.aliyun.com/#/next/argowf)[工作流集群控制台](https://csnew.console.aliyun.com/#/next/argowf)。
在需要删除的集群右侧操作列单击>删除集群，然后在弹出的提示框中单击确定。
## 相关文档
使用集群前，需[开启](enable-argo-server-for-a-workflow-cluster.md)[Argo Server](enable-argo-server-for-a-workflow-cluster.md)[并访问工作流控制台](enable-argo-server-for-a-workflow-cluster.md)。
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
