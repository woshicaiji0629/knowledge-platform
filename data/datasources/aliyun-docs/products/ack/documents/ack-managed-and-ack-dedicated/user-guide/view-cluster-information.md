# 查看集群信息-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/view-cluster-information

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

# 查看集群信息

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

容器服务 Kubernetes 版集群提供集群信息页面，展示集群的基本信息、巡检信息、相关云资源、集群资源监控等。

## 操作入口

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择集群信息。

- 

单击不同页签，查看不同维度信息。

具体内容，请参见[集群信息内容](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/view-cluster-information.md)。

## 集群信息内容

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 页签 | 说明 |
| --- | --- |
| 概览 | 查看集群资源概览和健康状态。 集群健康状态 ：集群控制面、组件 、节点池 、工作负载的健康状况。可单击存在异常的资源卡片，跳转至对应界面。 搭配 [阿里云](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md) [Prometheus](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md) [监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md) 功能使用，支持配置告警等操作。 集群巡检风险 ：开启集群巡检功能后，支持自动扫描集群并提示潜在风险和对应的解决方案，防止业务受损。 搭配 [使用集群巡检](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-the-cluster-inspection-feature.md) 功能使用，支持设定扫描时间和扫描周期。 资源监控 ：展示集群 [CPU](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/#meaning-of-cpu) 和 [内存](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/#meaning-of-memory) 的用量和总量。 事件与告警 ：集群告警、错误事件等。 搭配 [事件监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/event-monitoring.md) 和 [容器服务报警管理](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/alert-management.md) 功能使用。 |
| 安全概览 | 该功能目前仅针对 ACK 托管集群 Pro 版 白名单开放，请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 申请。 对集群的安全配置进行巡检后，展示集群配置巡检的扫描结果，包括节点漏洞、容器镜像风险、容器运行时风险等，以了解当前集群中运行应用的配置是否存在安全隐患。 巡检结果支持以报表化的方式展示，同时展示巡检对应扫描项的说明和修复建议。还支持配置定期巡检，并将扫描结果写入到指定的 SLS Project。详情请参见 [配置巡检检查集群工作负载](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-the-inspection-feature-to-detect-security-risks-in-the-workloads-of-an-ack-cluster.md) 。 |
| 基本信息 | 基本信息 ：集群的基本信息，例如集群 ID、地域、集群规格、集群时区、Kubernetes 版本、是否开启删除保护等。 ACK 托管集群 Pro 版 中，可启用 [ACK Pro 预设控制面](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane.md) ，预先分配并固化控制面资源，以保障控制面性能始终可预期。 网络 ：集群网络的信息，例如 容器网络插件、 虚拟交换机、 API Server 端点、Service 网段等。 查询 ACK 集群公网出口 IP ACK 中的资源需要访问公网时，默认使用集群所在 VPC 中的 NAT 网关作为公网出口。 [创建](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md) [ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md) [托管集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md) 时，如果勾选 为专有网络配置 SNAT 选项，VPC 中将自动新建 NAT 网关并配置 SNAT 规则，可以通过控制台查看 NAT 网关详细信息： 如果创建集群时未勾选此选项，可以在创建集群后 [为集群开启访问公网的能力](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/enable-an-existing-ack-cluster-to-access-the-internet.md) 。 在 基本信息 页签中，单击 公网 NAT 网关 右侧的链接，查看网关详情。 重要 如果 [为](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/associate-an-eip-with-a-pod-1.md) [Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/associate-an-eip-with-a-pod-1.md) [挂载独立公网](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/associate-an-eip-with-a-pod-1.md) [EIP](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/associate-an-eip-with-a-pod-1.md) ，或为节点 ECS 绑定了 [弹性公网](products/ecs/documents/user-guide/associate-or-disassociate-an-eip.md) [IP](products/ecs/documents/user-guide/associate-or-disassociate-an-eip.md) ，Pod 或节点访问公网时可能不使用 NAT 网关，请以实际情况为准。 安全与审计 ：集群安全与审计信息，例如开启集群审计日志等。 集群资源 ：集群所用 ROS 资源栈、日志服务 Project 等。单击相应的资源 ID 可以跳转至对应控制台。 重要 这些资源由 ACK 进行管理，请勿随意删除或自行修改，避免集群异常，影响集群内应用的正常运行。 标签分组 ：集群的资源组和标签。 |
| 连接信息 | 获取公网和内网环境下的 KubeConfig，用于配置通过 kubectl 客户端访问集群。详情请参见 [连接集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/access-clusters.md) 。 |
| 集群监控 | 对接阿里云可观测监控 Prometheus 版，对集群进行资源监控，支持快速查看负载的 CPU、内存、网络等指标的使用率，提供监控与报警能力和更合适的容器场景指标。详情请参见 [接入与配置阿里云](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md) [Prometheus](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md) [监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md) 。 |
| 成本概览 | 启用成本洞察功能后，支持查看指定财务治理周期内，指定集群、部门、应用的成本和资源使用情况，满足多种场景的成本估算、分摊与核算的需求。详情请参见 [成本洞察](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cost-analysis-overview.md) 。 |
| 集群日志 | 集群的运行日志。 |
| 集群任务 | 查看集群任务、任务状态、涉及资源、变更时间等。失败任务将提示失败信息，协助问题的排查和诊断。 |
| 运维计划 | 仅针对托管节点池。可参见 [创建和管理节点池](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-node-pool.md) 开启，使用其提供的自动化运维能力。 查询 ACK 自动运维任务生成的执行计划，例如 ECS 系统事件自动响应、节点池 kubelet 自动升级、CVE 漏洞自动修复等。您可以单击计划 ID，查看运维任务详细信息和事件记录。关于 ACK 提供的自动化运维能力，请参见 [自动化运维能力](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/node-pool-overview.md) 。 |


[上一篇：管理集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/manage-clusters.md)[下一篇：集群生命周期](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cluster-abnormal-states.md)

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
