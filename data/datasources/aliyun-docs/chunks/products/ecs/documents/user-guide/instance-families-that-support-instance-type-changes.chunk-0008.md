| 问题 | 说明 | 解决方案 |
| --- | --- | --- |
| 规格不存在 | 选择的目标实例规格不存在。 | 选择其他目标实例规格。 [在售的实例规格族](overview-of-instance-families.md) |
| 规格已下线 | 选择的目标实例规格已下线。 | 选择其他目标实例规格。 [在售的实例规格族](overview-of-instance-families.md) |
| 该地域无库存 | 选择的目标实例规格在当前地域没有库存。在库存高度紧张的地域变配部分大核心规格时，也可能会出现变配动作发起但是最终失败的情况。 | 可选择变更到其他有库存的实例规格，或 [跨可用区更改实例规格（仅支持变配到同规格族）](change-instance-types-across-zones.md) 。 [查看实例可购买地域](https://ecs-buy.aliyun.com/instanceTypes) 通过 [API](../developer-reference/api-ecs-2014-05-26-describeresourcesmodification.md) 查询某一可用区下的实例规格库存 |
| 仅支持同一规格族内的变更 | 更改这部分实例规格时，只能选择同一规格族内的规格。 | 目标实例需选择与原实例在同一规格族内的规格。例如更改 gn7e 规格时，只能选择 gn7e 规格族内的规格，不能选择其他族内的规格。 |
| 目标规格族和源实例的规格族不匹配 | 所选目标实例规格与源实例规格不匹配，则不支持变更。 | 请参考 [可变配的实例规格](instance-families-that-support-instance-type-changes.md) ，选择与源实例规格族匹配的目标实例规格。 |
| 目标实例规格架构和源实例架构不匹配 | 所选目标实例的架构（ARM 架构或 x86 架构）与源实例不匹配，则不支持变更。 | 目标实例需选择与源实例架构匹配的实例规格。 |
| 目标实例规格的 CPU 核数或内存大小不在支持范围内 | 所选目标实例的 CPU 核数或内存大小与源实例不匹配，则不支持变更。例如 Windows 操作系统对实例的 CPU 核数和内存大小的限制说明请参见 [Windows 和 Windows Server 版本的内存限制](https://learn.microsoft.com/windows/win32/memory/memory-limits-for-windows-releases) 。 | 目标实例需选择与源实例 CPU 核数或内存大小匹配的实例规格。 |
| 目标规格启动模式和当前实例不匹配 | 例如所选目标实例是仅支持 UEFI 启动模式的安全增强型实例规格，要求源实例必须支持
