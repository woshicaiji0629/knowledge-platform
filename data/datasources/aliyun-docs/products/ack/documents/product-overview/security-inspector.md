# security-inspector-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/product-overview/security-inspector

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/product-overview.md)

- [操作指南](products/ack/documents/ack-user-guide.md)

- [服务支持](products/ack/documents/support.md)

[首页](https://help.aliyun.com/zh)

# security-inspector

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

security-inspector组件是实现安全巡检功能的关键组件。本文将介绍security-inspector组件的功能、使用说明和变更记录。

## 组件介绍

security-inspector组件支持对Workload配置进行多维度扫描，帮助您实时了解当前状态下应用是否有安全隐患。security-inspector组件的架构如下图所示。

## 使用说明

security-inspector组件目前支持安全的配置巡检功能。

- 

security-inspector组件通过支持使用Polaris进行配置巡检，让您可以实时扫描集群中的Workload配置是否存在安全隐患。

说明

Polaris是一款用于扫描集群中Workload配置是否有安全隐患的开源软件。详情请参见[Polaris](https://github.com/FairwindsOps/polaris)。

- 

security-inspector组件可以对Workload配置进行多维度扫描，并可以在巡检报告中查看巡检扫描结果，包括健康检查、镜像、网络、资源、安全等扫描信息。让您实时了解当前状态下运行应用的配置是否有安全隐患，并提供相应的安全修复建议以便进行相应的加固。详情请参见[配置巡检检查集群工作负载](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-the-inspection-feature-to-detect-security-risks-in-the-workloads-of-an-ack-cluster.md)。

## 变更记录

### 2026年05月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.16.8 | registry-cn-hangzhou.ack.aliyuncs.com/acs/security-inspector:v0.16.8 | 2026 年 05 月 22 日 | 升级组件使用的 Golang 版本为 1.25.10，提升组件稳定性。 | 此次升级不会对业务造成影响。 |


### 2025年12月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.16.7 | registry-cn-hangzhou.ack.aliyuncs.com/acs/security-inspector:v0.16.7 | 2025 年 12 月 03 日 | 升级组件使用的 Golang 版本为 1.24.11，提升组件稳定性。 | 此次升级不会对业务造成影响。 |


### 2025年08月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.16.6 | registry-cn-hangzhou.ack.aliyuncs.com/acs/security-inspector:v0.16.6 | 2025 年 08 月 11 日 | 升级组件使用的 Golang 版本为 1.24.6，提升组件稳定性。 | 此次升级不会对业务造成影响。 |


### 2025年07月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.16.5.2-gffa860c-aliyun | registry-cn-hangzhou.ack.aliyuncs.com/acs/security-inspector:v0.16.5.2-gffa860c-aliyun | 2025 年 07 月 09 日 | 升级组件使用的 Golang 版本为 1.24.4，提升组件稳定性。 | 此次升级不会对业务造成影响。 |


### 2025年04月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.16.3.3-ge515753-aliyun | registry-cn-hangzhou.ack.aliyuncs.com/acs/security-inspector:v0.16.3.3-ge515753-aliyun | 2025 年 04 月 16 日 | 升级组件使用的 Golang 版本为 1.24.2，提升组件稳定性。 | 此次升级不会对业务造成影响。 |
| v0.16.2.0-gbce6b15-aliyun | registry-cn-hangzhou.ack.aliyuncs.com/acs/security-inspector:v0.16.2.0-gbce6b15-aliyun | 2025 年 04 月 09 日 | 修复组件依赖的 security-inspector 命名空间下的资源被删除时，组件 Pod 会异常崩溃的问题。新版本将改为在组件容器日志中记录错误信息。 | 此次升级不会对业务造成影响。 |


### 2025年03月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.16.1.0-gea4d02f-aliyun | registry-cn-hangzhou.ack.aliyuncs.com/acs/security-inspector:v0.16.1.0-gea4d02f-aliyun | 2025 年 03 月 18 日 | 升级组件使用的 Golang 版本为 1.23.7，提升组件稳定性。 | 此次升级不会对业务造成影响。 |


### 2025年01月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.16.0.0-g4e93dcd-aliyun | registry-cn-hangzhou.ack.aliyuncs.com/acs/security-inspector:v0.16.0.0-g4e93dcd-aliyun | 2025 年 01 月 02 日 | 升级组件使用的 Golang 版本为 1.23.4，提升组件稳定性。 | 此次升级不会对业务造成影响。 |


### 2024年10月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.15.0.0-g4218661-aliyun | registry-cn-hangzhou.ack.aliyuncs.com/acs/security-inspector:v0.15.0.0-g4218661-aliyun | 2024 年 10 月 10 日 | 支持检查是否在环境变量中存储了明文 AK。 | 此次升级不会对业务造成影响。 |


### 2024年08月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.14.1.0-g829a93d-aliyun | registry-cn-hangzhou.ack.aliyuncs.com/acs/security-inspector:v0.14.1.0-g829a93d-aliyun | 2024 年 08 月 01 日 | 版本兼容改造。 | 此次升级不会对业务造成影响。 |


### 2024年07月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.14.0.0-gfc02c67-aliyun | registry-cn-hangzhou.ack.aliyuncs.com/acs/security-inspector:v0.14.0.0-gfc02c67-aliyun | 2024 年 07 月 26 日 | 从这个版本开始，组件改为在 security-inspector 命名空间执行巡检任务。 | 此次升级不会对业务造成影响。 |


### 2024年03月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.13.0.0-g88dfa8f-aliyun | registry-cn-hangzhou.ack.aliyuncs.com/acs/security-inspector:v0.13.0.0-g88dfa8f-aliyun | 2024 年 03 月 26 日 | RBAC 相关巡检内容扩展，包括通配符检测、cluster-admin 检测、集群默认配置篡改（system:basic-user, system:discovery, system:public-info-viewer）等。 | 此次升级不会对业务造成影响。 |


### 2024年02月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.12.0.7-g6f9d47f-aliyun | registry-cn-hangzhou.ack.aliyuncs.com/acs/security-inspector:v0.12.0.7-g6f9d47f-aliyun | 2024 年 02 月 21 日 | 新增支持在 组件管理 页面配置组件是否使用主机网络以及修改健康检查服务监听的端口。 | 此次升级不会对业务造成影响。 |


### 2023年12月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.11.0.3-ga2fad87-aliyun | registry-cn-hangzhou.ack.aliyuncs.com/acs/security-inspector:v0.11.0.3-ga2fad87-aliyun | 2023 年 12 月 21 日 | 新增组件升级时将保留用户对 security-inspector-polaris-cronjob 的 ttlSecondsAfterFinished 配置项的修改。 | 此次升级不会对业务造成影响。 |


### 2023年06月

- 

- 

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.10.1.2-g13c9de7-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.10.1.2-g13c9de7-aliyun | 2023 年 06 月 02 日 | 修复集群升级到 1.26.3-aliyun.1 版本后组件功能异常的问题。 优化定期扫描逻辑，确保每次只执行一个任务，避免集群内出现多个状态为 Pending 的任务 Pod。 | 此次升级不会对业务造成影响。 |


### 2023年04月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.10.0.3-g15b35c4-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.10.0.3-g15b35c4-aliyun | 2023 年 04 月 13 日 | 新增支持 Kubernetes 1.26。 | 此次升级不会对业务造成影响。 |


### 2023年02月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.9.1.0-gcdddfa7-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.9.1.0-gcdddfa7-aliyun | 2023 年 02 月 27 日 | 修复组件镜像使用的基础镜像中存在的 CVE-2023-0286。 | 此次升级不会对业务造成影响。 |


### 2022年12月

- 

- 

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.9.0.0-g1d38ec6-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.9.0.0-g1d38ec6-aliyun | 2022 年 12 月 22 日 | 新增支持 1.18 及以上版本的 ACK Serverless 集群 。 支持通过重启组件容器的方式自动修复被误删的 SLS 面板。 | 此次升级不会对业务造成影响。 |
| v0.8.3.2-ge5496db-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.8.3.2-ge5496db-aliyun | 2022 年 12 月 13 日 | 当前处于灰度发布中。 优化程序初始化速度，解决组件安装成功后需要等待几分钟才能成功执行巡检的问题。 | 此次升级不会对业务造成影响。 |


### 2022年08月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.8.3.1-gf7bf0e0-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.8.3.1-gf7bf0e0-aliyun | 2022 年 08 月 30 日 | 优化 SecurityInspectorConfigAuditHighRiskFound 和 SecurityInspectorConfigAuditFinished 事件的消息内容，增加详细信息的查看链接。 | 此次升级不会对业务造成影响。 |


### 2022年06月

- 

- 

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.8.2.16-gc84d60d-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.8.2.16-gc84d60d-aliyun | 2022 年 06 月 21 日 | 修复在 Kubernetes 1.22 集群中可能会出现 MountVolume.SetUp failed for volume "config" : object "kube-system"/"security-inspector-polaris-config" not registered 事件的问题。 优化组件对 API Server 的请求，进一步减轻大规模集群下 API Server 的压力。 | 此次升级不会对业务造成影响。 |


### 2022年04月

- 

- 

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.8.1.0-g58d1a56-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.8.1.0-g58d1a56-aliyun | 2022 年 04 月 11 日 | 修复组件配置不合理导致 Pod 所在的节点无法自动排水的问题。 修复当多个集群使用相同的日志项目时，出现巡检报告异常的问题。 | 此次升级不会对业务造成影响。 |


### 2022年02月

- 

- 

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.8.0.0-gb0edd1d-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.8.0.0-gb0edd1d-aliyun | 2022 年 02 月 15 日 | 调整检查项 privilegeEscalationAllowed 的风险等级为中。 优化对 Kubernetes 1.16 集群的支持功能，修复 [#84880](https://github.com/kubernetes/kubernetes/issues/84880) 导致的问题。 | 此次升级不会对业务造成影响。 |


### 2021年12月

- 

- 

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.7.0.5-g8cc37b6-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.7.0.5-g8cc37b6-aliyun | 2021 年 12 月 03 日 | 支持 Kubernetes 1.22 版。从该组件版本之后将只支持 Kubernetes 1.16 及以上版本的集群。 支持 ARM64 架构。 | 此次升级不会对业务造成影响。 |


### 2021年09月

- 

- 

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.6.0.4-gc12ad66-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.6.0.4-gc12ad66-aliyun | 2021 年 09 月 20 日 | 支持扫描 CIS Kubernetes V1.20 Benchmark v1.0.0 基线。 优化 capabilitiesAdded 检查项，检查 capabilities 时不区分大小写。更多信息，请参见 [配置巡检检查集群工作负载](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-the-inspection-feature-to-detect-security-risks-in-the-workloads-of-an-ack-cluster.md) 。 | 此次升级不会对业务造成影响。 |


### 2021年06月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.5.0.2-g5e33765-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.5.0.2-g5e33765-aliyun | 2021 年 06 月 24 日 | 解决多个集群使用同一个 SLS Project 时会出现报表数据显示异常的问题。 | 此次升级不会对业务造成影响。 |


### 2021年03月

- 

- 

- 

- 

- 

- 

- 

- 

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.4.0.0-g541eb31-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.4.0.0-g541eb31-aliyun | 2021 年 03 月 15 日 | 支持 CIS Kubernetes 基线检查。 新增以下 Kubernetes 事件（当您触发扫描时，可以在事件中心看到相应事件）： SecurityInspectorConfigAuditStart：开始执行配置巡检。 SecurityInspectorConfigAuditFinished：配置巡检完成。 SecurityInspectorConfigAuditHighRiskFound：配置巡检完成后发现高风险配置。 SecurityInspectorBenchmarkStart：开始执行基线检查。 SecurityInspectorBenchmarkFinished：执行基线检查完成。 SecurityInspectorBenchmarkFailedCheckFound：执行基线检查完成后发现未通过的计分检查项。 | 此次升级不会对业务造成影响。 |


### 2021年01月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.3.0.2-gcb49252-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.3.0.2-gcb49252-aliyun | 2021 年 01 月 05 日 | 支持通过扫描匿名用户访问权限配置找出存在安全隐患的 RBAC（Role-based access control）权限配置项。 | 此次升级不会对业务造成影响。 |


### 2020年12月

- 

- 

- 

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.2.0.22-gd1fbaff-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.2.0.22-gd1fbaff-aliyun | 2020 年 12 月 16 日 | 支持以 CRD（Custom Resource Definitions）方式存储最新巡检结果。 支持启用或禁用指定检查项。 支持配置工作负载白名单。 | 此次升级不会对业务造成影响。 |


### 2020年07月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.1.0.3-g69f71f6-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.1.0.3-g69f71f6-aliyun | 2020 年 07 月 06 日 | 支持手动触发配置巡检任务，对集群中的 Workload 进行检查并输出相应的巡检报告。 | 此次升级不会对业务造成影响。 |


[上一篇：kritis-validation-hook](products/ack/documents/product-overview/kritis-validation-hook.md)[下一篇：managed-security-inspector](products/ack/documents/product-overview/managed-security-inspector.md)

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
