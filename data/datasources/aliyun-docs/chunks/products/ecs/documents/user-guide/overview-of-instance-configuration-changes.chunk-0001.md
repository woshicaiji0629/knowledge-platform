## 修改实例规格
一个实例规格已预定义vCPU和内存。修改实例规格时，您需要选择目标实例规格，不能单独修改vCPU或内存。
说明
修改实例规格前，您需要了解以下实例规格信息和变配支持情况，具体可修改的实例规格以变配页面显示为准。
实例规格：请参见[实例规格族](overview-of-instance-families.md)。
实例规格变配支持情况：请参见[规格变更限制与自检](instance-families-that-support-instance-type-changes.md)。
实例计费方式不同升降配的方式不同，您可以参见下表选择合适的方式。

| 实例计费方式 | 操作时段 | 何时生效 | 相关操作 |
| --- | --- | --- | --- |
| 包年包月实例 | 到期前 | 重启实例后生效 | [包年包月实例升配规格](upgrade-the-instance-types-of-subscription-instances.md) [包年包月实例降配规格](downgrade-the-instance-types-of-subscription-instances.md) |
| 到期前 15 日内 | 进入新的计费周期后，7 天内重启实例生效 | [包年包月实例续费降配](../downgrade-instance-configurations-during-renewal.md) |  |
| 到期后释放前 | 重启实例后生效 | [包年包月实例续费变配](../a-renewal-variable-2.md) |  |
| 按量付费实例 | 不涉及 | 重启实例后生效 | [更改按量付费实例规格](change-the-instance-type-of-a-pay-as-you-go-instance.md) |
