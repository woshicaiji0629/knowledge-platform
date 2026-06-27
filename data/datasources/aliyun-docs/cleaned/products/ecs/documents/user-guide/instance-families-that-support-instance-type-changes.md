# 哪些实例规格支持变配-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/instance-families-that-support-instance-type-changes

# 更改实例规格说明
本文指导您完成实例规格变更前的检查工作，并提供常见问题及其解决方案。
## 实例规格变更前自检表
| 确认项 | 限制说明 |
| --- | --- |
| 实例 | 跨平台变配限制 ：因为可能涉及到指令集和功能兼容问题，目前默认无法支持。该项主要涉及到 Intel 和 AMD 平台之间的变配动作。 |
| 老旧实例升级限制 ：6 代及之前的部分规格变配 8 代及以上实例规格时，可能涉及到架构变更、功能兼容、指令集兼容等一系列问题无法支持变配。请先参考 [可变配的实例规格](instance-families-that-support-instance-type-changes.md) ，确认当前实例规格支持升配到更高代系。 |  |
| 特殊规格族变配限制 ：安全增强、大数据、本地 SSD、持久内存等因为规格特殊逻辑，默认不支持变配。 |  |
| 镜像 | 镜像兼容性限制 ：请务必先参考下方 [实例规格变更前自检操作中 的 2. 检查操作系统兼容性](instance-families-that-support-instance-type-changes.md) 提前进行确认，对关键业务务必做好系统盘备份等动作。 同时请注意，如果基于不兼容镜像发起实例规格变配，我们强烈建议您在做好备份的基础上先基于单个节点进行验证，确认此行为对业务的影响可控。阿里云无法保证对不兼容操作系统的变配行为提供回滚能力。 |
| 云盘 | 云盘类型限制 ：如果待变配实例使用高效云盘、SSD 云盘、eSSD Entry 等云盘类型，且目标变配规格为 7 代以上新规格，您需要先将云盘变更为目标规格可支持的类型；您可以参考下方 [实例规格变更前自检操作中 的 4. 检查云盘类型兼容性](instance-families-that-support-instance-type-changes.md) 提前进行确认。 注：对于使用普通云盘的规格，请在变配之前先进行工单咨询。 |
| NVMe 驱动限制 ：当目标升配规格为 8 代以上规格时，需要提前确认 NVMe 驱动是否已经完成安装。 |  |
## 实例规格变更前自检操作
1. 检查当前规格是否支持变配、当前规格是否支持变配到目标规格
首先，需要确认当前实例是否允许变更规格，以及目标规格是否在可变更的范围内。
确认当前实例规格不在[不支持变配操作的实例规格](instance-families-that-support-instance-type-changes.md)列表中。
在[可变配的实例规格](instance-families-that-support-instance-type-changes.md)列表中，找到当前实例的规格族，确认目标规格族在其支持的范围内。
也可通过调用API接口[DescribeResourcesModification](../developer-reference/api-ecs-2014-05-26-describeresourcesmodification.md)来查询当前实例支持变更的目标规格列表。
2. 检查操作系统兼容性
部分实例规格（特别是基于不同CPU架构的，如AMD、Intel、倚天）对操作系统有特定要求。如果当前实例的操作系统与目标规格不兼容，变更将会失败。
请参考以下官方兼容性列表，确保当前操作系统受目标实例规格的支持。
[AMD](../compatibility-between-amd-instance-types-and-operating-systems.md)[实例规格与操作系统兼容性说明](../compatibility-between-amd-instance-types-and-operating-systems.md)
[Intel](../intel-instance-specifications-and-operating-system-compatibility.md)[实例规格与操作系统兼容性说明](../intel-instance-specifications-and-operating-system-compatibility.md)
[倚天处理器实例兼容的操作系统](the-migration-process.md)
若不兼容，仍需变更规格，请申请放开限制。
申请开放限制的方法
重要
申请放开限制对全地域生效，且生效后不支持再取消。
在[ECS](https://ecs-buy.aliyun.com)[控制台-自定义购买](https://ecs-buy.aliyun.com)，镜像类型选择自定义镜像，单击检查操作链接。
阅读相关风险信息后，勾选申请放开限制的勾选框后，单击确定，等待1分钟左右。
3. 检查当前实例NVMe驱动与目标规格兼容性
从第8代及以后规格（如g8i、c8i、r8i、u2i、g8a、c8a、r8a、u2a等）开始，ECS 实例主要通过NVMe协议与云盘通信，必须安装相应的驱动。以下变配场景，需要检查原实例的NVMe驱动：
场景一：从7代及以下规格变配到8代及以上规格
原ECS实例必须安装NVMe驱动，或实例使用的镜像进行支持安装NVMe驱动。
场景二：当前实例规格为8代及以上
原ECS实例必须安装NVMe驱动才支持变配。
实例规格的“代系”信息可通过实例规格族名称判断。[实例规格命名规则](instance-specification-naming-and-classification.md)
检查&安装NVMe驱动的方法
在[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)找到待变配实例，选择>设置 NVMe 驱动状态。
如果已安装NVMe驱动，可以看到状态为已安装。
若未安装，单击一键安装，安装NVMe驱动，系统会自动修改NVMe驱动状态为已安装。
相关API
查询实例规格是否支持NVMe：调用[DescribeInstanceTypes](../developer-reference/api-ecs-2014-05-26-describeinstancetypes.md)，若支持，则NvmeSupport=required。
查询镜像是否支持NVMe：调用[DescribeImages](../developer-reference/api-ecs-2014-05-26-describeimages.md)，若支持，则NvmeSupport=supported。
4. 检查云盘类型兼容性
不同的实例规格支持的云盘类型不同。例如，g7规格族仅支持ESSD系列云盘。如果当前实例挂载了目标规格不支持的云盘，则不支持变更。
在变更规格的操作页面，如果存在云盘兼容性问题，系统会自动检测并提示您需要同时变更云盘类型。如下图所示，请留意相关提示和费用变化。
## 可变配的实例规格
更改实例规格时，支持从以下源实例规格更改到目标实例规格：
说明
可通过调用API接口[DescribeResourcesModification](../developer-reference/api-ecs-2014-05-26-describeresourcesmodification.md)查询已有实例支持的更改情况。
表 1.入门级x86计算规格族
| 源实例规格族 | 可更改的目标实例规格族 |
| --- | --- |
| e | g7、c7、r7、g7ne、g7nex、c7nex、hfg7、hfc7、hfr7 g6、c6、r6、g6e、c6e、r6e、hfg6、hfc6、hfr6、re6 u1 e t6 、s6 |
| t6 、s6 | g7、c7、r7、hfg7、hfc7、hfr7、g7ne g6、c6、r6、hfg6、hfc6、hfr6、g6e、c6e、r6e、re6 t6 、s6 |
| t5 | g6、c6、r6、hfc6、hfg6、hfr6、g6a、c6a、r6a、re6 g5、g5ne、r5、c5、ic5、hfc5、hfg5 t5、t6 、s6 |
| n4、mn4、xn4、e4 | g6、c6、r6、hfc6、hfg6、hfr6、g6a、c6a、r6a、re6 g5、g5ne、r5、c5、ic5、hfc5、hfg5 t5、t6 、s6 se1、sn1ne、sn2ne、se1ne、c4、ce4、cm4、re4、n4、mn4、xn4、e4 |
| t1、s1、s2、s3、m1、m2、c1、c2 | g5、g5ne、r5、c5、ic5、hfc5、hfg5 t5 se1、sn1ne、sn2ne、se1ne、c4、ce4、cm4、re4、n4、mn4、xn4、e4 |
| n1、n2、e3 | g5、g5ne、r5、c5、ic5、hfc5、hfg5 t5 se1、sn1ne、sn2ne、se1ne、c4、ce4、cm4、re4、n4、mn4、xn4、e4 |
表 2.企业级计算规格族
| 源实例规格（族） | 可更改的目标实例规格族 |
| --- | --- |
| g9a、c9a、r9a、g9ae、c9ae、r9ae、u2a | g9a、c9a、r9a、g9ae、c9ae、r9ae、u2a |
| g9i、c9i、r9i、hfg9i、hfc9i、hfr9i | g9i、c9i、r9i、hfg9i、hfc9i、hfr9i、u2i |
| g8i、c8i、r8i hfg8i、hfc8i、hfr8i | g9i、c9i、r9i、hfg9i、hfc9i、hfr9i、u2i g8i、c8i、r8i、hfg8i、hfc8i、hfr8i 、g8ise |
| g8ise | g8i、c8i、r8i、hfg8i、hfc8i、hfr8i、g8ise |
| g8a、c8a、r8a g8ae、c8ae、r8ae | g9a、c9a、r9a、g9ae、c9ae、r9ae、u2a g8a、c8a、r8a、g8ae、c8ae、r8ae |
| g8y、c8y、r8y | g8y、c8y、r8y |
| g7se、c7se、r7se | g8i、c8i、r8i g7se、c7se、r7se |
| g7a、c7a、r7a | g9a、c9a、r9a、g9ae、c9ae、r9ae、u2a g8a、c8a、r8a、g8ae、c8ae、r8ae g7a、c7a、r7a、g7、c7、r7 g6a、c6a、r6a |
| ebmg7a、ebmc7a、ebmr7a | ebmg7a、ebmc7a、ebmr7a |
| ebmhfc7、ebmhfg7、ebmhfr7 | ebmhfc7、ebmhfg7、ebmhfr7 |
| g7、c7、r7 | g9i、c9i、r9i u2i g8i、c8i、r8i、hfg8i、hfc8i、hfr8i 、g8ise g7、c7、r7、g7ne、g7nex、c7nex、hfc7、hfg7、hfr7 |
| ebmg7、ebmc7、ebmr7 | ebmg7、ebmc7、ebmr7 |
| g7ne hfc7、hfg7、hfr7 g6e、c6e、r6e | g9i、c9i、r9i、hfg9i、hfc9i、hfr9i g8i、c8i、r8i、hfg8i、hfc8i、hfr8i 、g8ise g7、c7、r7、g7ne、g7nex、c7nex、hfc7、hfg7、hfr7 g6e、c6e、r6e |
| g7nex、c7nex | g8i、c8i、r8i、hfg8i、hfc8i、hfr8i 、g8ise g7、c7、r7、g7ne、g7nex、c7nex、hfc7、hfg7、hfr7 重要 ecs.g7nex.32xlarge 只能更改为 ecs.c7nex.32xlarge。 |
| g7h | g7h |
| g6h | g6h |
| g6r、c6r | g8y、c8y、r8y g6r、c6r |
| g6、c6、r6 hfg6、hfc6、hfr6 | g9i、c9i、r9i、hfg9i、hfc9i、hfr9i g8i、c8i、r8i、hfg8i、hfc8i、hfr8i g7、c7、r7、hfg7、hfc7、hfr7、g7ne g6、c6、r6、hfg6、hfc6、hfr6、g6e、c6e、r6e、re6 t6 、s6 |
| g6a、c6a、r6a | g9a、c9a、r9a、g9ae、c9ae、r9ae、u2a g8a、c8a、r8a、g8ae、c8ae、r8ae g7、c7、r7、g7a、c7a、r7a g6、c6、r6、g6a、c6a、r6a |
| g6t | g6t |
| c6t | c6t |
| ebmg6a、ebmc6a、ebmr6a | ebmg6a、ebmc6a、ebmr6a |
| g5、g5ne、r5、c5、ic5 | g7、c7、r7 g6、c6、r6、g6a、c6a、r6a、hfc6、hfg6、hfr6、re6 g5、g5ne、r5、c5、ic5、hfc5、hfg5、ebmg5s t5、t6 、s6 |
| hfc5、hfg5 | g7、c7、r7 g6、c6、r6、g6a、c6a、r6a、hfc6、hfg6、hfr6、re6 u1 hfc5、hfg5、g5、g5ne、r5、c5、ic5、t5 e t6 、s6 |
| u2i | u2i |
| u1 | g7、c7、r7、hfg7、hfc7、hfr7 u1、u2i、u2a |
| sn1ne、sn2ne、se1ne | g6、c6、r6、g6a、c6a、r6a、hfc6、hfg6、hfr6、re6 g5、g5ne、r5、c5、ic5、hfc5、hfg5 e t5、t6 、s6 sn1ne、sn2ne、se1ne、re4、n4、mn4、xn4、e4 |
| se1 | g7、c7、r7 u1 g5、g5ne、r5、c5、ic5、hfc5、hfg5 t5 se1、sn1ne、sn2ne、se1ne、c4、ce4、cm4、re4、n4、mn4、xn4、e4 |
| re6 | g6、c6、r6、hfc6、hfg6、hfr6、re6、ebmre6-6t re4、re4e |
| re4e | g7、c7、r7 u1 re6、ebmre6-6t re4e、re4 |
| re4 | g7、c7、r7 u1 g6、c6、r6、g6a、c6a、r6a、hfg6、hfc6、hfr6、re6、ebmre6-6t e g5、g5ne、r5、c5、ic5、hfc5、hfg5 t5、t6 、s6 se1、sn1ne、sn2ne、se1ne、c4、ce4、cm4、re4、n4、mn4、xn4、e4 |
| gn8v | gn8v |
| gn8v-tee | gn8v-tee |
| sgn8ia | sgn8ia |
| gn8is | gn8is |
| sgn7i-vws | sgn7i-vws |
| vgn7i-vws | vgn7i-vws |
| gn7e | gn7e |
| gn7r | gn7r |
| gn7s | gn7s |
| gn7i | gn7i |
| gn7 | gn7 |
| gn6i | gn6i |
| vgn6i | vgn6i、vgn6i-vws、sgn7i-vws |
| vgn6i-vws | vgn6i-vws |
| gn6e | gn6e |
| gn6v | gn6v |
| gn5i | gn5i |
| sn1、sn2、se1 | g7、c7、r7 u1 g5、g5ne、r5、c5、ic5、hfc5、hfg5 t5 se1、sn1ne、sn2ne、se1ne、c4、ce4、cm4、re4、n4、mn4、xn4、e4 |
| c4、ce4、cm4 | g6、c6、r6、g6a、c6a、r6a、hfc6、hfg6、hfr6、re6 e g5、g5ne、r5、c5、ic5、hfc5、hfg5 t5、t6 、s6 se1、sn1ne、sn2ne、se1ne、c4、ce4、cm4、re4、n4、mn4、xn4、e4 |
## 不支持变配操作的实例规格
重要
在 ECS 控制台的变配页面，如果当前实例不支持变配，系统通常会直接禁用操作按钮并给出提示。
以下实例规格族内的实例规格不支持变配操作：
| 规格族类型 | 实例规格族 |
| --- | --- |
| 企业级 x86 计算规格族 | RDMA 增强型：c7re 持久内存型：re6p、re6p-redis 、re7p、r7p 安全增强型：g7t、c7t、r7t 大数据型：d3s、d3c、d2c、d2s、d1、d1ne 本地 SSD 型：i1、i2、i2g、i2ne、i2gne、i3、i3g、i4、i4g、i4r、i4p、i5g、i5ge、i5、i5e |
| 企业级异构计算规格族 | GPU 计算型：gn5 GPU 虚拟化型：vgn5i 异构服务型：video-trans FPGA 计算型：f1、f3 |
| 弹性裸金属服务器规格族 | ebmgn8v、ebmgn8is、 ebmgn7ex、 ebmgn7e、ebmgn7i、 ebmgn7ix、 ebmgn7、ebmgn6ia、ebmgn6e、ebmgn6v、ebmgn6i ebmg8i、ebmc8i、ebmg8y、ebmc8y、ebmr8y、ebmg6、ebmg5s、ebmg5、ebmc6me、ebmc6、ebmc5s、ebmc4、ebmre6p、ebmre6-6t、ebmr6、ebmr5s ebmi2g ebmhfg6、ebmhfg5、ebmhfc6、ebmhfr6 |
| 高性能计算&超级计算集群实例规格族 | 超级计算集群 SCC sccgn7ex、 sccgn6e、sccgn6 sccg7、sccc7、 sccg5、scch5 scchfg6、scchfc6、scchfr6 高性能计算优化型：hpc8i、hpc8ae、hpc7ip、hpc6id |
## 常见问题与解决方案（FAQ）
如果在变更规格时遇到以下问题，请参考对应的解决方案。
| 问题 | 说明 | 解决方案 |
| --- | --- | --- |
| 规格不存在 | 选择的目标实例规格不存在。 | 选择其他目标实例规格。 [在售的实例规格族](overview-of-instance-families.md) |
| 规格已下线 | 选择的目标实例规格已下线。 | 选择其他目标实例规格。 [在售的实例规格族](overview-of-instance-families.md) |
| 该地域无库存 | 选择的目标实例规格在当前地域没有库存。在库存高度紧张的地域变配部分大核心规格时，也可能会出现变配动作发起但是最终失败的情况。 | 可选择变更到其他有库存的实例规格，或 [跨可用区更改实例规格（仅支持变配到同规格族）](change-instance-types-across-zones.md) 。 [查看实例可购买地域](https://ecs-buy.aliyun.com/instanceTypes) 通过 [API](../developer-reference/api-ecs-2014-05-26-describeresourcesmodification.md) 查询某一可用区下的实例规格库存 |
| 仅支持同一规格族内的变更 | 更改这部分实例规格时，只能选择同一规格族内的规格。 | 目标实例需选择与原实例在同一规格族内的规格。例如更改 gn7e 规格时，只能选择 gn7e 规格族内的规格，不能选择其他族内的规格。 |
| 目标规格族和源实例的规格族不匹配 | 所选目标实例规格与源实例规格不匹配，则不支持变更。 | 请参考 [可变配的实例规格](instance-families-that-support-instance-type-changes.md) ，选择与源实例规格族匹配的目标实例规格。 |
| 目标实例规格架构和源实例架构不匹配 | 所选目标实例的架构（ARM 架构或 x86 架构）与源实例不匹配，则不支持变更。 | 目标实例需选择与源实例架构匹配的实例规格。 |
| 目标实例规格的 CPU 核数或内存大小不在支持范围内 | 所选目标实例的 CPU 核数或内存大小与源实例不匹配，则不支持变更。例如 Windows 操作系统对实例的 CPU 核数和内存大小的限制说明请参见 [Windows 和 Windows Server 版本的内存限制](https://learn.microsoft.com/windows/win32/memory/memory-limits-for-windows-releases) 。 | 目标实例需选择与源实例 CPU 核数或内存大小匹配的实例规格。 |
| 目标规格启动模式和当前实例不匹配 | 例如所选目标实例是仅支持 UEFI 启动模式的安全增强型实例规格，要求源实例必须支持 UEFI 启动模式，否则不支持变更。 | 目标实例需选择与源实例启动模式匹配的实例规格。 |
| 目标规格不支持升降配为当前待变配规格 | 大部分实例升降配动作（特别是从老旧实例跨代系升级的动作）都是单向的，因为实例回退会遭遇驱动兼容性、CPU 指令集兼容、网络与存储功能兼容问题，且这些问题的处理方式完全不同于旧代系升级新代系的变配动作。 | 考虑进行操作系统或 SMC 迁移。先做好必要的业务备份，在操作前先小范围验证，并提前确认能否降配、回滚。 |
| 目标规格不支持当前规格使用的镜像版本 | 目标规格支持的操作系统列表中不包含当前规格的云盘系统盘安装的操作系统，常见于老旧实例的跨代系升配动作。 | 建议优先升级操作系统或走 SMC 迁移。如果需要通过实例升降配功能执行变配动作，请先做好必要的业务备份，在操作前先小范围验证，并提前确认能否降配、回滚。 如果业务条件允许，评估是否可以进行操作系统升级。 |
| 包年包月实例不支持在升配时同时调整云盘类型（或不支持在升级云盘类型时同步降配实例规格） | 当您使用包年包月实例时，如果您需要将当前实例升级到价格更高的目标规格，且需要同时变更云盘类型满足变配限制，则您无法选择单价更低的云盘类型。 | 如果您需要在升配实例规格的同时将云盘调整为更低单价的云盘类型，请先单独操作云盘类型变更等动作后，再发起实例升降配。您也可以在操作前先通过阿里云工单进行咨询。 |
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
