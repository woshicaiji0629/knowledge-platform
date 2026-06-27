### 单条命令执行状态
在一台实例上运行一条命令时，实例级别的状态如下表所示，对应[DescribeInvocations](../api-describeinvocations.md)中InvokeInstance下的InvocationStatus字段，或[DescribeInvocationResults](../api-describeinvocationresults.md)中的InvocationStatus字段。

| API 状态 | 状态显示 | 描述 |
| --- | --- | --- |
| Pending | 下发中 | 系统正在校验或发送命令。 |
| Invalid | 校验不通过 | 指定命令类型或参数有误。 |
| Aborted | 下发失败 | 向实例发送命令失败。实例必须在运行中，且命令可以 1 分钟内发送完成。 |
| Running | 执行中 | 命令正在被执行。 |
| Success | 执行成功 | 单次执行的命令：命令执行完成，且退出码为 0。 定时执行的命令：上一次运行成功且退出码为 0，且指定的时间已结束。 |
| Failed | 执行完成，退出码非 0 | 单次执行的命令：命令执行完成，且退出码非 0。 定时执行的命令：上一次运行成功且退出码非 0，且指定的时间将中止。 |
| Error | 执行异常 | 命令执行时发生异常无法继续。 |
| Timeout | 执行超时 | 命令执行超时。 |
| Cancelled | 执行取消 | 命令的执行动作已经取消，命令未曾启动。 |
| Stopping | 停止执行中 | 命令正在被停止执行。 |
| Stopped | 已停止执行 | 命令已经被停止。 |
| Terminated | 执行已终止 | 命令运行时被终止。 |
| Scheduled | 命令等待运行 | 定时执行的命令等待运行。 |
