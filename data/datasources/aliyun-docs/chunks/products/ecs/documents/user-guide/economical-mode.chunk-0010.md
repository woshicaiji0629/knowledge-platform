## 常见问题
- 打开默认启用节省停机模式后，是否支持单台ECS实例关机时不释放计算资源和网络资源？
打开默认启用节省停机模式后，在停止单台实例时仍然需要设置单台实例的停止模式，ECS实例不触发节省停机效果就不会释放计算资源和网络资源。
如果需要在短时间内停机再开机，建议您在调用[StopInstance](../api-stopinstance.md)时将StoppedMode设置为KeepCharging，或者在控制台上停止ECS实例时选择普通停机模式。
- 在ECS实例操作系统内关机能否触发节省停机效果？
不能。
在实例内部操作系统中，通过shutdown、poweroff、halt等命令或其他手动方式执行关机操作，不会进入节省停机模式。实例通过以下方式停机时才能触发节省停机效果。
ECS管理控制台。
通过阿里云CLI或SDK发起的API请求。
账号欠费自动停机。
- 本地盘实例是否支持自动触发节省停机效果？
本地盘实例不支持触发节省停机效果。
- 为什么开启实例的节省停机模式后，实例启动失败？
可能原因如下：
部分资源库存不足：可能因为部分资源库存不足导致启动失败，可以稍后尝试再次启动，或者尝试[更改实例规格](change-the-instance-type-of-a-pay-as-you-go-instance.md)。
账户欠费。
抢占式实例价格超过价格上限：创建抢占式实例时如果设置了价格上限，重启实例时可能会因市场价超过价格上限，导致重启失败。
- ECS实例触发节省停机效果后，为什么StartInstance时会报错OperationDenied.NoStock？
节省停机模式会释放计算资源。当再次启动实例时，系统需要重新申请资源。如果此时资源池库存不足，启动就会失败并返回OperationDenied.NoStock错误。建议稍后重试，或尝试更换实例规格。
- 启用了节省停机模式后，停机再开机时公网IP会变化，怎么保持公网IP不变？
ECS实例触发节省停机效果后，固定公网IP会被回收，下次启动时自动分配新的固定公网IP，因此会发生变化。
如需保持公网IP不变，您可以将ECS实例的固定公网IP转为弹性公网IP，因为ECS实例触发节省停机效果后不会释放弹性公网IP，可以保证公网IP不变。更多信息，请参见[固定公网](convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[IP](convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[转为弹性公网](convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[
