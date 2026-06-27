# 如何手动升级ACK集群或单独升级集群控制面和节点池-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/update-the-kubernetes-version-of-an-ack-cluster

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

# 手动升级ACK集群

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

为避免过期版本存在的安全和稳定性风险，请及时升级集群。集群升级包括控制面升级和节点池升级。

重要

升级集群前，请确保已参见[升级集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/upgrade-clusters.md)了解升级流程、升级方式和注意事项。

## 操作入口

您可以先升级控制面，再升级节点池。升级控制面之前，请确保节点的kubelet和容器运行时版本与控制面版本保持匹配，避免引发升级失败或业务中断。例如，如控制面版本为1.32，而节点的版本为1.31，则需将节点的版本升级至1.32后，才能将控制面升级至1.33。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择运维管理>集群升级。

- 

在集群升级页面选择可升级的目标版本，按照页面提示完成升级。

## 升级控制面

### 1. 前置检查

控制面升级前置检查包括检查废弃API、组件兼容性、集群状态等。

1.20及以上版本的集群会检查当前版本是否使用了[废弃](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cluster-check-items-and-suggestions-on-how-to-fix-cluster-issues.md)[API](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cluster-check-items-and-suggestions-on-how-to-fix-cluster-issues.md)。检查结果不影响升级流程，仅作为提示信息。建议在升级前完成修复，避免影响下一版本集群的正常运行。

在集群升级页面单击前置检查，提前扫描集群升级可能存在的潜在风险。检查完成后，在前置检查结果区域查看检查结果。示例如下。

- 

结果正常：升级检查成功，继续执行升级。

- 

结果异常：不影响当前集群的运行及集群状态。请参见解决方案完成修复。更多信息，请参见[集群检查项及修复方案](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cluster-check-items-and-suggestions-on-how-to-fix-cluster-issues.md)。

### 2. 执行升级

耗时：ACK托管集群、ACK Serverless集群由ACK托管升级，约5分钟；ACK专有集群的Master节点需逐一串行升级，每个节点约8分钟。

前置检查处理完成后，单击立即升级，按照页面提示进行控制面的升级。

控制面升级后，新扩容节点的版本也将遵循控制面版本。

### 3. 升级后验证

控制面完成升级后，建议检查如下内容：

控制面升级成功，在集群列表查看集群版本时已更新至新版本。

API Server和核心组件状态正常。

业务应用运行正常。

可正常创建Pod。

可正常添加节点。

## 升级节点池

控制面升级完成后，请尽快在业务低峰期完成节点池升级，包括节点kubelet和容器运行时升级。

### 1. 前置检查

节点池升级前置检查包括检查节点状态、系统资源、磁盘状态、网络环境等。

在节点池升级页面的节点池列表，单击目标节点池对应的升级，然后在页面下方单击前置检查，提前扫描升级过程中可能存在的风险。检查完成后，在前置检查结果区域查看检查结果。

- 

结果正常：升级检查成功，继续执行升级。

- 

结果异常：不影响当前集群的运行及集群状态。请参见[集群检查项及修复方案](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cluster-check-items-and-suggestions-on-how-to-fix-cluster-issues.md)及控制台提示完成修复。

### 2.配置升级策略并执行升级

耗时：取决于节点分批情况。原地升级每批次约5～10分钟；替盘升级（不涉及快照）约8分钟，具体时长受排水情况影响；如需创建快照，升级需等待快照结束后执行，快照创建时间受数据量影响。

参见下表配置升级策略，然后单击立即升级，按照页面提示进行节点池的升级。

- 

- 

- 

- 

- 

- 

- 

| 配置项 | 说明 |
| --- | --- |
| 版本信息 | kubelet 和容器运行时的当前版本及可升级版本。 |
| 升级节点 | 可升级所有节点，也可先升级部分节点，观测无误后再陆续完成升级。 |
| 升级方式 | 原地升级 ：直接在原节点上更新替换所需的组件。不替换系统盘，也不会重新初始化节点，原节点的数据不受影响。 替盘升级 ：通过替换节点系统盘的方式重新初始化节点。节点的实例属性（如节点名称、实例 ID、IP 等）不发生改变，但节点系统盘上的数据将被删除。额外挂载到该节点上的数据盘不受影响。 可参见 [参考信息：原地升级和替盘升级](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/node-pool-updates.md) 了解升级逻辑和流程说明。 |
| 批量升级策略 | 每批次执行最多节点数 ：ACK 同一时间只升级一个节点池，节点池内部根据此配置执行分批升级。如需暂停后重新恢复升级，依然遵循该分批策略。批次节点数递增：1、2、4、8……直至达到最大并行数，之后每批均按最大并行数执行。 例如：最大并行数为 4 时，批次节点数依次为 1、2、4、4、4……详细说明请参见 [参考信息：原地升级和替盘升级](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/node-pool-updates.md) 。 自动暂停策略 ：节点升级过程中的暂停策略。如选择 不暂停 时，还可配置 每批次间隔时间 ，即每个升级批次之间是否需要时间间隔或间隔的时长（5～120 分钟）。 自动快照 ：如节点系统盘上有重要业务数据，可选择是否在升级节点池前为节点创建 [快照](products/ecs/documents/user-guide/snapshot-overview.md) ，以便进行节点数据的备份和恢复。 重要 替盘升级时建议开启自动快照。 使用快照将产生 [快照计费](products/ecs/documents/snapshots-1.md) ， [创建快照耗时](products/ecs/documents/user-guide/create-a-snapshot.md) 会动态变化。快照默认保留 7 天，升级后若快照无需使用，请及时 [删除快照](products/ecs/documents/user-guide/delete-a-snapshot-1.md) 。 |


### 3.升级后验证

节点池完成升级后，建议检查如下内容：

节点升级成功，且在节点详情页面查看kubelet和containerd版本时已更新至新版本。

Pod调度正常。

业务应用运行正常。

## 相关文档

- 

关于升级集群前和升级过程中可能遇到的常见问题，请参见[常见问题](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/upgrade-clusters.md)。

- 

ACK对Kubernetes版本支持的机制，请参见[版本说明](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/support-for-kubernetes-versions.md)。

- 

自1.24版本起不再支持将Docker作为内置容器运行时，升级至1.24及更高版本时需要[将节点容器运行时从](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/change-the-container-runtime-from-docker-to-containerd.md)[Docker](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/change-the-container-runtime-from-docker-to-containerd.md)[迁移到](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/change-the-container-runtime-from-docker-to-containerd.md)[containerd](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/change-the-container-runtime-from-docker-to-containerd.md)。

- 

自1.30版本起不再支持CentOS和Alibaba Cloud Linux 2，可转而使用其他支持中的[操作系统](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/overview-of-os-images.md)。

- 

您也可以启用集群自动升级功能，降低版本运维压力，请参见[自动升级集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/automatically-upgrade-an-ack-cluster.md)。

[上一篇：升级集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/upgrade-clusters.md)[下一篇：自动升级集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/automatically-upgrade-an-ack-cluster.md)

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
