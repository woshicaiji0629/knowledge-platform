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
从第8代及以后规格（如g8i、c8i、r8i、u2i、g8a、c8a、r8a、u2a等）开始，ECS 实例主要通过NVMe协议与云盘通信，必须安装相应的驱动。以下
