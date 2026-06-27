# 通过部署集提高业务可用性或降低ECS实例间通信延时-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/overview-43

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 部署集

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

为规避底层物理机单点故障，或满足高频交易等应用对极致低延迟的需求，可通过配置部署集来控制ECS实例的分布。选择高可用策略可打散实例以提升容灾能力，选择低时延策略可集中实例以加快网络通信。

## 适用范围

- 

部署集不支持创建专有宿主机。

- 

地域与可用区限制：实例与部署集必须在同一地域；策略为网络低时延的部署集内的实例，必须都在同一可用区。

- 

实例规格族限制：大部分6代及以上实例支持高可用、部署集组高可用及网络低时延策略部署集。

不同部署策略仅支持创建特定的实例规格族

具体支持的规格族，以[DescribeDeploymentSetSupportedInstanceTypeFamily](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describedeploymentsetsupportedinstancetypefamily.md)接口返回结果为准。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 部署策略 | 支持的实例规格族 |
| --- | --- |
| 高可用策略和部署集组高可用策略 | g9a、g9ae、g9i、g8a、g8i、g8ine、g8ise、g8y、g7、g7a、g7h、g7ne、g7nex、g7se、g7t、g6、g6a、g6e、g6h、g5、g5ne c9a、c9ae、c9i、c8a、c8i、c8ine、c8y、c7、c7a、c7nex、c7se、c7t、c6、c6a、c6e、c5 r9a、r9ae、r9i、r8a、r8i、r8y、r7、r7a、r7se、r7t、r6、r6a、r6e、r5 hfc9i、hfg9i、hfr9i、hfc8i、hfg8i、hfr8i、hfc7、hfg7、hfr7、hfc6、hfg6、hfr6、hfc5、hfg5 ebmc9i、ebmg9a、ebmg9i、ebmr9i、ebmc8a、ebmc8i、ebmc8y、ebmg8a、ebmg8i、ebmg8y、ebmr8a、ebmr8y、ebmc7、ebmc7a、ebmg7、ebmg7a、ebmg7se、ebmhfc7、ebmhfg7、ebmhfr7、ebmr7、ebmr7a、ebmg5 i5、i5g、i5ge、ic5、i4、i4g、i4r、i3、i3g、i2、i2g、i2gne、i2ne gn6i d3c、d3s、d2c、d2s、d1ne re6、re6p、s6、t6、e4、mn4、n4、re4、xn4、sn2ne、u2a、u2i、se1、se1ne、sn1ne、u1、e |
| 网络低时延策略 | g9a、g9ae、g9i、g8a、g8ae、g8i、g8ise、g8y、g7、g5ne c9a、c9ae、c9i、c8a、c8ae、c8i、c8ine、c8y、c7、c7nex r9a、r9ae、r9i、r8a、r8ae、r8i、r8y、r7 hfc9i、hfg9i、hfr9i、hfc8i、hfg8i、hfr8i ebmc9i、ebmg9a、ebmg9i、ebmr9i、ebmc8a、ebmc8i、ebmc8y、ebmg8a、ebmg8i、ebmg8y、ebmgn8v、ebmr8a、ebmr8y、ebmc7、ebmc7a、ebmg7、ebmg7a、ebmg7se、ebmgn7ex、ebmhfc7、ebmhfg7、ebmhfr7、ebmr7、ebmr7a i5、i5g、i5ge、i4 gn8v hpc8ae、hpc8i、hpc7ip、hpc6id、u2a、u2i |


## 快速使用

### 步骤一：创建部署集

通过控制台

- 

访问[ECS](https://ecs.console.aliyun.com/deploymentSet/region)[控制台-部署集](https://ecs.console.aliyun.com/deploymentSet/region)。

- 

在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

在部署集页面，单击创建部署集。

- 

在创建部署集对话框，输入部署集名称和描述，选择策略。如果选择高可用策略，还可以设置部署类型（物理机、机架或交换机）和亲和度（1~10）。[如何选择部署策略？](products/ecs/documents/user-guide/overview-43.md)

通过API

调用[CreateDeploymentSet](products/ecs/documents/developer-reference/api-ecs-2014-05-26-createdeploymentset.md)在指定的地域内创建一个部署集，并设置部署集策略。

- 

如果部署策略为部署集组高可用策略，可指定参数GroupCount设置分组数量。

- 

如果部署策略为高可用策略，可指定参数Type设置部署类型（host、rack或sw），默认值为host。

- 

如果部署策略为高可用策略，可指定参数Affinity设置亲和度（1~10），默认值为1。

### 步骤二：在部署集内创建或添加ECS实例

通过控制台

重要

ECS实例的规格、地域、数量需符合使用限制要求。具体，请参见[使用限制](products/ecs/documents/user-guide/overview-43.md)。

- 

在部署集内创建新实例：

在部署集列表页面，找到目标部署集，在部署集的操作列中，单击创建实例，跳转到自定义购买页面完成实例配置选项。

- 

将已创建实例加入部署集：具体操作，可参见[调整实例所属部署集](products/ecs/documents/user-guide/overview-43.md)。

通过API

- 

在部署集内创建新实例：调用[RunInstances](products/ecs/documents/developer-reference/api-ecs-2014-05-26-runinstances.md)接口，并指定DeploymentSetId（部署集ID）。

为部署集组高可用策略设置分组数量。

- 

将已创建实例加入至部署集：调用[ModifyInstanceDeployment](products/ecs/documents/developer-reference/api-ecs-2014-05-26-modifyinstancedeployment.md)接口，并指定参数InstanceId（实例ID）和DeploymentSetId（部署集ID）。

说明

如果指定的部署集对应策略为AvailabilityGroup（部署集组高可用策略），可以通过参数DeploymentSetGroupNo指定实例在部署集中的分组号。

## 部署策略

部署策略用于确定ECS实例在物理服务器上的部署方式，您可以根据业务对于高可用性、网络延迟和部署规模等要求来选择。

| 场景 | 推荐策略 | 关键限制 |
| --- | --- | --- |
| 小规模集群，严格隔离故障 | 高可用策略 | 单可用区最多 20~100 台（取决于部署类型和亲和度） |
| 大规模部署，分组隔离 | 部署集组高可用策略 | 单可用区最多 7 组×20 台/组 |
| 低网络延迟 | 网络低时延策略 | 必须同可用区，最多 20 台 |


### 高可用策略

将实例分散部署在不同的物理机、机架或交换机上，避免单点故障导致多台实例同时不可用。

说明

打散粒度越细（如交换机级别），容灾能力越强，但可能面临更高的创建失败率。如果当前可用区没有足够的独立物理机/机架/交换机满足打散要求，实例创建将失败，请等待一段时间后重试或选择其他可用区。

- 

适用场景：小规模部署，且对服务连续性和隔离性有较高要求的系统，如Hadoop分布式计算集群、SQL数据库集群等。

- 

可用区：实例可部署在不同可用区。

- 

实例数量：单个可用区的实例数上限取决于部署类型和亲和度设置。

部署类型

部署类型指定部署集内ECS实例的打散维度，取值如下：

| 取值 | 打散维度 | 说明 |
| --- | --- | --- |
| host （默认值） | 物理机级别 | 实例分散部署在不同物理服务器上，避免单台物理机故障影响多个实例。 |
| rack | 机架级别 | 实例分散部署在不同机架上，规避因机架电力故障导致的批量实例不可用风险。 |
| sw | 交换机级别 | 实例分散部署在不同交换机下，规避因交换机故障导致的网络中断风险。 |


亲和度

亲和度表示每个物理机上允许部署的最大实例数。取值范围为1~10，默认值为1。

- 

亲和度为1时，实现严格打散，即每个物理机上最多部署1台实例。

- 

亲和度大于1时，实现尽力打散，适用于实例数量较多但仍需一定程度容灾隔离的场景。

以下示例以部署类型为物理机（host）的场景，说明亲和度如何影响实例分布：

场景一：基于部署集创建实例

创建 HOST 类型部署集（Affinity=2），在该部署集中创建 3 台 ECS 实例。系统根据亲和度约束，将实例分散部署到不同物理机上，单台物理机最多承载 2 个实例。

场景二：调整部署集亲和度（调大）

将已有部署集的 Affinity 从 1 调整为 2。调大亲和度后，系统将允许单台物理机承载更多实例，为后续扩容提供空间。已有实例无需迁移。

实例数量上限

部署集的实例数量上限取决于部署类型和亲和度的组合：

| 部署类型（Type） | 亲和度（Affinity） | 单地域 上限 |
| --- | --- | --- |
| sw （交换机） | 1~10 | 20 台 |
| rack （机架） | 1~10 | 20 台 |
| host （物理机） | 1~10 | 20 台 |


### 部署集组高可用策略

将实例分配到多个分组中（最多7组），不同分组严格分散在不同物理服务器上，同组内允许集中部署。

不同分组的ECS实例会在指定地域内严格分散在不同的物理服务器上，避免单点故障；同组内多台ECS实例不保证分散部署，可能部署在同一物理机，从而降低互访延时。

说明

通过接口[DescribeInstances](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstances.md)可查询实例在部署集中分组的位置（DeploymentSetGroupNo）。分布式应用（如HDFS、Cassandra）可利用分组号信息做智能副本放置决策，确保不同副本分布在不同分组中，从而在分组级故障时仍保持数据可用。

- 

适用场景：大规模部署且需要高隔离性的应用，尤其是已具备内部高可用机制（如Redis主从复制、Nginx负载均衡）的业务。

- 

可用区：实例可部署在不同可用区。

- 

实例数量：单可用区单组的实例上限20台，单可用区最多可有7个组。

### 网络低时延策略

将实例集中部署在同一网络拓扑范围内，最大限度降低实例间网络通信延迟。

重要

该策略以牺牲高可用性换取低延迟——多台实例可能集中在同一台物理服务器上。请确保您的应用已自身实现了高可用机制（如多副本、主从切换）。

- 

适用场景：高性能计算（HPC）、实时数据分析、AI推理等对网络延迟有严苛要求的应用。

- 

可用区：实例必须部署在同一个可用区。

- 

实例数量：不可超过20台。

- 

容量不足时：如果同一网络拓扑范围内没有足够资源，实例创建将失败。建议等待后重试，或联系客服确认资源可用性。

## 更多操作

### 调整实例所属部署集

根据业务需求，更改ECS实例所属的部署集，将其从一个部署集转移到另一个部署集，或将未加入部署集的实例添加到符合业务需求的目标部署集中。

通过控制台

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。

- 

在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

单击目标实例ID进入实例详情页，单击全部操作展开所有操作面板，然后搜索并单击调整实例所属部署集。

- 

在调整实例所属部署集对话框中，选择目标部署集，并设置是否强制调整。

- 

是：允许更换实例物理服务器。该操作可能会导致实例重启，影响服务的连续性，请谨慎操作。

- 

否：不会更换实例的物理服务器，而是尝试将实例加入到指定的部署集。这种方式避免了实例重启的风险，但如果当前实例不满足新部署集的要求，会导致调整失败。

通过API

调用接口[ModifyInstanceDeployment](products/ecs/documents/developer-reference/api-ecs-2014-05-26-modifyinstancedeployment.md)，并指定以下参数，调整实例所属部署集：

- 

RegionId：选择实例所属地域。例如，cn-hangzhou，即华东1（杭州）。

- 

InstanceId：实例ID。例如，i-bp67acfmxazb4ph***。

- 

DeploymentSetId：目标部署集ID。例如，ds-bp67acfmxazb4ph****。

- 

Force：实例在调整部署集时，是否强制更换物理服务器。取值：

- 

true：允许更换实例物理服务器。该操作可能会导致实例重启，影响服务的连续性，请谨慎操作。

- 

false（默认）：不会更换实例的物理服务器，而是尝试将实例加入到指定的部署集。这种方式避免了实例重启的风险，但如果当前实例不满足新部署集的要求，会导致调整失败。

### 将实例移出部署集

如果在删除部署集时，需要保留当前部署集内的实例，可以从部署集中移除实例后再进行删除，移除后实例保持原有状态。

重要

目标实例必须处于运行中或者已停止状态。具体操作，请参见[启动实例](products/ecs/documents/user-guide/start-an-instance.md)和[停止实例](products/ecs/documents/user-guide/stop-an-instance.md)。

- 

调用[ModifyInstanceDeployment](products/ecs/documents/developer-reference/api-ecs-2014-05-26-modifyinstancedeployment.md)，并指定以下参数，将实例移出部署集：

- 

RegionId：选择实例所属地域。例如，cn-hangzhou，即华东1（杭州）。

- 

InstanceId：实例ID。例如，i-bp67acfmxazb4ph***。

- 

DeploymentSetId：部署集ID。例如，ds-bp67acfmxazb4ph****。

- 

RemoveFromDeploymentSet：是否将所选实例移出所选部署集。选择：true。

- 

验证实例是否移除成功：接口调用成功，且返回状态码：200，证明移除成功。

### 修改或删除部署集

在[ECS](https://ecs.console.aliyun.com/deploymentSet/region)[控制台-部署集](https://ecs.console.aliyun.com/deploymentSet/region)，找到目标部署集，单击操作列的修改信息或删除，按照界面提示完成操作。

- 

修改部署集：修改部署集的名称和描述。

- 

删除部署集：当您不再需要使用部署集时，您可以删除部署集，以免造成不必要的资源占用。

重要

删除部署集时，请确保部署集内没有实例。如果存在实例，必须移出实例后才能删除部署集。具体操作，请参见[调整实例所属部署集](products/ecs/documents/user-guide/overview-43.md)或[将实例移出部署集](products/ecs/documents/user-guide/overview-43.md)。

## 使用限制

重要

遇到地域内供货紧缺时，可能无法创建ECS实例，或者重启按量付费ECS实例（节省停机模式）失败。一般情况下，您可以等待一段时间后重试创建或重启操作。更多信息，请参见[节省停机模式](products/ecs/documents/user-guide/economical-mode.md)。

- 

部署集数量限制：单个阿里云账户可拥有的部署集的数量有上限，具体可在[配额中心](https://quotas.console.aliyun.com/products/ecs/quotas)查看。

- 

部署类型（Type）不支持变更：部署集创建后，其部署类型无法修改。如需变更，需新建部署集并迁移实例。

- 

亲和度（Affinity）调整规则：

- 

调大亲和度：无约束，可直接修改。当部署类型为host时，调大亲和度可能会同步上调实例数量上限。

- 

调小亲和度：需要先将部署集内的实例全部移出，清空部署集后再修改。

- 

部署集之间不支持相互合并。

## 费用说明

使用部署集不会收取服务费用，但创建和使用的ECS实例、磁盘、快照、镜像和公网带宽等服务将收取费用。更多信息，请参见[计费概述](products/ecs/documents/billing-overview.md)。

[上一篇：高可用架构](products/ecs/documents/user-guide/high-availability-architecture.md)[下一篇：共享部署集](products/ecs/documents/user-guide/shared-deployment-sets.md)

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
