# 节省停机模式（原停机不收费）-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/economical-mode

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

# 按量付费实例（含抢占式实例）的节省停机模式

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

针对非连续运行的按量付费ECS实例，节省停机模式通过释放vCPU、内存、固定公网IP等资源，在保留云盘数据和实例配置的同时，最大限度地降低成本。

在实例开启节省停机模式时，会执行以下动作：

- 

释放以下资源：实例的vCPU、内存、GPU、FPGA、固定公网IP等资源，这些资源以及镜像License将会停止计费。

- 

保留以下资源：实例的云盘（系统盘和数据盘）、云盘关联的快照、私网IP等资源。

详情查看节省停机模式[与普通停机模式的区别](products/ecs/documents/user-guide/economical-mode.md)。

## 影响与风险

节省停机模式的成本优势源于其特殊的资源回收机制，但也引入了风险，请仔细评估是否可接受：

- 启动不确定性（不能100%启动成功）

由于节省停机模式会释放计算资源，再次启动实例相当于重新申请资源，如果所在可用区的资源库存不足，实例将无法启动。此风险在资源热门地域和时段更高。对于需要保证高可用性的生产环境，请谨慎使用此模式。

- 实例固定公网IP必然变更

如果服务依赖此实例的固定公网IP（非弹性公网IP），该IP将在停机后被释放。实例再次启动时，系统会为其分配一个新的固定公网IP。如需保留公网IP，请在启用节省停机模式前，[将固定公网](products/ecs/documents/user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[IP](products/ecs/documents/user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[转为弹性公网](products/ecs/documents/user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[IP](products/ecs/documents/user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)。

- 突发性能实例CPU积分清零

对于[突发性能实例](products/ecs/documents/user-guide/burst-performance-instance-overview.md)（如t5、t6等规格族），进入节省停机模式后，当前累积的所有[CPU](products/ecs/documents/user-guide/burst-performance-instance-overview.md)[积分](products/ecs/documents/user-guide/burst-performance-instance-overview.md)将全部清零，将影响实例的突发能力。

## 适用范围

要使用节省停机模式，ECS 实例必须同时满足以下所有条件：

- 

计费方式：按量付费（包括抢占式实例）。

- 

网络类型：仅支持专有网络实例。

- 

实例规格：

- 

不包含本地盘。例如，[大数据型（d](products/ecs/documents/user-guide/big-data-instance-families.md)[系列）](products/ecs/documents/user-guide/big-data-instance-families.md)、[本地](products/ecs/documents/user-guide/instance-families-with-local-ssds.md)[SSD](products/ecs/documents/user-guide/instance-families-with-local-ssds.md)[型（i](products/ecs/documents/user-guide/instance-families-with-local-ssds.md)[系列）](products/ecs/documents/user-guide/instance-families-with-local-ssds.md)等规格族不支持。可在[实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)中的本地存储列查询是否包含本地盘。

- 

不包含持久内存。例如，re6p、re6p-redis 等规格族不支持。可在[实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)中的持久内存列查询是否包含持久内存。

## 为实例开启节省停机模式

重要

在实例内部操作系统中，通过shutdown、poweroff、halt等命令或其他手动方式执行关机操作，不会进入节省停机模式。请在控制台或通过API/CLI操作。

## 控制台

- 

进入[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，选择地域与资源组。

- 

在实例列表找到待操作实例后，单击操作列下的停止。

- 

在弹出的对话框中，设置停止模式为节省停机模式，然后单击确定。

预期结果

实例会首先进入停止中状态，在实例停止完成后，状态列会显示已停止和节省停机模式的标签。

## CLI

可以调用[停止实例](products/ecs/documents/developer-reference/api-ecs-2014-05-26-stopinstance.md)操作，并将StoppedMode参数设置为StopCharging。

示例：使用节省停机模式停止杭州地域实例ID为i-t4n5xxxxxxxxxxx的实例。

aliyun ecs StopInstance \ --RegionId cn-hangzhou \ --InstanceId i-t4n5xxxxxxxxxxx \ --StoppedMode StopCharging \ --ForceStop false \ --DryRun false

## API

- 

调用[StopInstance](products/ecs/documents/api-stopinstance.md)停止按量付费（含抢占式）ECS实例时，将StoppedMode设置为StopCharging，即可使ECS实例进入节省停机模式。

重要

对于不满足节省停机模式条件的实例，调用该接口并设置StoppedMode=StopCharging不会报错，实例会以普通模式正常停机。要确认实例是否成功进入节省停机模式，请通过[DescribeInstances](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstances.md)接口查询实例状态。

- 

调用[RunInstances](products/ecs/documents/developer-reference/api-ecs-2014-05-26-runinstances.md)和[CreateInstance](products/ecs/documents/developer-reference/api-ecs-2014-05-26-createinstance.md)创建抢占式实例时，将SpotInterruptionBehavior设置为Stop，实例中断时，将进入节省停机模式。

## 在停止实例时默认选择节省停机

默认情况下，在控制台停止实例时默认选择普通停机模式，可通过设置该选项，调整控制台默认选择节省停机模式。

该配置仅调整控制台的默认选项，在实际停止实例时，依然可选择使用普通停机模式停止实例。

- 

进入[ECS](https://ecs.console.aliyun.com/home)[控制台-概览](https://ecs.console.aliyun.com/home)页面。

请将ECS控制台切换为标准版进行设置。

- 

在页面右侧的常用功能区域，单击用户设置。

- 

打开节省停机模式开关。

- 

阅读提醒信息，确认后在底部单击开启默认 VPC 内实例节省停机模式。

## 应用于生产环境

对于需要大规模或周期性管理实例开关机的集群环境，可以结合阿里云的系统运维管理（OOS）服务，实现定时自动进入节省停机模式，从而实现无人值守的成本优化。

- 

场景举例：有一批ECS实例作为开发测试环境，通常只在工作日的白天（例如 9:00 - 18:00）被使用。在夜间和周末，这些实例虽然闲置，但仍在持续产生费用。

- 

解决方案：可通过阿里云的运维编排服务（OOS）， 创建[定时开关机](https://help.aliyun.com/zh/oos/use-cases/scheduled-startup-and-shutdown)任务，确保资源在不被使用时自动进入最经济的状态，从而节省成本。关键配置如下：

- 

执行周期：周一～周五

- 

开机时间：09:00

- 

关机时间：18:00

- 

停机模式：节省停机模式

## 与普通停机模式的区别

节省停机模式与普通停机模式的主要差异如下：

| 功能特性 | 节省停机模式 | 普通停机模式 |
| --- | --- | --- |
| 资源保留 | 仅保留云盘和实例元数据， 释放 vCPU、内存、GPU、FPGA、固定公网 IP、本地盘等资源 。 | 保留所有资源。 |
| 主要计费项 | vCPU、内存、GPU、FPGA、固定公网 IP 等资源 停止计费 。镜像 License、云盘、弹性公网 IP（EIP）、快照等资源 继续计费 。 | 继续计费 。 |
| 重启速度 | 相对较慢，因为需要重新申请和分配计算资源。 | 较快，因为计算资源未被释放。 |
| 重启成功率 | 不保证成功 。在资源紧张的地域可能因库存不足而启动失败。 | 不会因资源库存不足导致重启失败。 |
| 固定公网 IP | 实例的固定公网 IP 会被释放，重启后将分配一个新的公网 IP。 | 固定公网 IP 保持不变。 |


## 常见问题

- 打开默认启用节省停机模式后，是否支持单台ECS实例关机时不释放计算资源和网络资源？

打开默认启用节省停机模式后，在停止单台实例时仍然需要设置单台实例的停止模式，ECS实例不触发节省停机效果就不会释放计算资源和网络资源。

如果需要在短时间内停机再开机，建议您在调用[StopInstance](products/ecs/documents/api-stopinstance.md)时将StoppedMode设置为KeepCharging，或者在控制台上停止ECS实例时选择普通停机模式。

- 在ECS实例操作系统内关机能否触发节省停机效果？

不能。

在实例内部操作系统中，通过shutdown、poweroff、halt等命令或其他手动方式执行关机操作，不会进入节省停机模式。实例通过以下方式停机时才能触发节省停机效果。

- 

ECS管理控制台。

- 

通过阿里云CLI或SDK发起的API请求。

- 

账号欠费自动停机。

- 本地盘实例是否支持自动触发节省停机效果？

本地盘实例不支持触发节省停机效果。

- 为什么开启实例的节省停机模式后，实例启动失败？

可能原因如下：

- 

部分资源库存不足：可能因为部分资源库存不足导致启动失败，可以稍后尝试再次启动，或者尝试[更改实例规格](products/ecs/documents/user-guide/change-the-instance-type-of-a-pay-as-you-go-instance.md)。

- 

账户欠费。

- 

抢占式实例价格超过价格上限：创建抢占式实例时如果设置了价格上限，重启实例时可能会因市场价超过价格上限，导致重启失败。

- ECS实例触发节省停机效果后，为什么StartInstance时会报错OperationDenied.NoStock？

节省停机模式会释放计算资源。当再次启动实例时，系统需要重新申请资源。如果此时资源池库存不足，启动就会失败并返回OperationDenied.NoStock错误。建议稍后重试，或尝试更换实例规格。

- 启用了节省停机模式后，停机再开机时公网IP会变化，怎么保持公网IP不变？

ECS实例触发节省停机效果后，固定公网IP会被回收，下次启动时自动分配新的固定公网IP，因此会发生变化。

如需保持公网IP不变，您可以将ECS实例的固定公网IP转为弹性公网IP，因为ECS实例触发节省停机效果后不会释放弹性公网IP，可以保证公网IP不变。更多信息，请参见[固定公网](products/ecs/documents/user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[IP](products/ecs/documents/user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[转为弹性公网](products/ecs/documents/user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[IP](products/ecs/documents/user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)和[ConvertNatPublicIpToEip](products/ecs/documents/api-convertnatpubliciptoeip.md)。

重要

固定公网IP转成弹性公网IP后，使用弹性公网IP访问公网会收取公网出网带宽费用、EIP配置费（满足特定条件时不收取）和EIP绑定费（满足特定条件时不收取）。具体收费细则，请参见[弹性公网](products/eip/documents/billing-overview.md)[IP](products/eip/documents/billing-overview.md)[计费概述](products/eip/documents/billing-overview.md)。

- 调用StopInstance并指定StoppedMode=StopCharging后，实例没有进入节省停机模式？

对于不满足节省停机模式条件的实例，调用[StopInstance](products/ecs/documents/api-stopinstance.md)接口并设置StoppedMode=StopCharging时，系统不会拦截该操作，系统将优先确保实例正常停机。要确认实例是否成功进入节省停机模式，请通过[DescribeInstances](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstances.md)接口查询实例状态。

- 如何将普通停机模式切换到节省停机模式？

无法直接切换，需先启动实例至运行中状态，再启用节省停机模式。

[上一篇：停止实例](products/ecs/documents/user-guide/stop-an-instance.md)[下一篇：管理实例](products/ecs/documents/user-guide/management-and-operation-and-maintenance.md)

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
