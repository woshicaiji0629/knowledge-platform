## 修改公网带宽峰值
根据实例的计费方式以及对带宽的需求不同，您可以采用不同的方式修改公网带宽。
重要
将公网带宽由非0值设置为0 Mbit/s，固定公网IP地址立即释放。
将公网带宽由0 Mbit/s设置为一个非零值：系统会为实例分配固定公网IP地址。

| 公网 IP 类型 | 适用范围 | 何时生效 | 相关文档 |
| --- | --- | --- | --- |
| 固定公网 IP | 包年包月实例修改基础公网带宽 | 立即生效 | [修改固定公网带宽包年包月实例修改带宽](modify-the-bandwidth-configurations.md) |
| 包年包月实例在续费的同时修改基础公网带宽 | 进入新的计费周期后生效 | [包年包月实例续费降配](../downgrade-instance-configurations-during-renewal.md) |  |
| 包年包月实例临时升级公网带宽 | 在设置的时间内生效 | [包年包月实例临时升级固定公网带宽（连续时间段）](temporary-bandwidth-upgrade.md) [包年包月实例临时升级固定公网带宽（周期性）](temporary-upgrade-bandwidth-on-a-daily-basis.md) |  |
| 按量付费实例修改基础公网带宽 | 立即生效 | [按量付费实例修改带宽](modify-the-bandwidth-configurations-of-pay-as-you-go-instances.md) |  |
| 弹性公网 IP | 包年包月实例或按量付费实例变配弹性公网带宽 | 立即生效 | [变更](modify-the-bandwidth-of-an-eip.md) [EIP](modify-the-bandwidth-of-an-eip.md) [带宽](modify-the-bandwidth-of-an-eip.md) |
