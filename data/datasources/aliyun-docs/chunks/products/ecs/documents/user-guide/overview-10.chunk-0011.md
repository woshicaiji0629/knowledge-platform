### 批量命令执行状态
为便于管理批量执行或者定时执行，您可以从总执行状态、实例级别执行状态以及执行记录级别的状态概念出发管理命令运行的生命周期，对应[DescribeInvocations](../api-describeinvocations.md)中Invocation下的InvocationStatus字段。状态各级别之间的包含关系如下图所示。
在多台实例上运行一条命令，总执行状态说明如下表所示。

| API 状态 | 状态显示 | 描述 |
| --- | --- | --- |
| Pending | 系统正在校验或发送命令 | 存在至少一台实例的命令执行状态为 Pending ，则总执行状态为 Pending 。 |
| Scheduled | 定时执行的命令已发送，等待运行 | 存在至少一台实例的命令执行状态为 Scheduled ，则总执行状态为 Scheduled 。 |
| Running | 命令正在实例上运行 | 存在至少一台实例的命令执行状态为 Running ，则总执行状态为 Running 。 |
| Success | 命令执行成功 | 各个实例上的命令执行状态均为 Stopped 或 Success ，且至少一个实例的命令执行状态是 Success ，则总执行状态为 Success 。 立即运行的任务：命令执行完成，且退出码为 0。 定时运行的任务：最近一次执行成功且退出码为 0，且指定的时间已全部完成。 |
| Failed | 命令执行失败 | 各个实例上的命令执行状态均为 Stopped 或 Failed ，则总执行状态为 Failed 。实例上的命令执行状态一项或多项为以下状态时，返回值均为 Failed 状态： 命令校验失败（ Invalid ）。 命令发送失败（ Aborted ）。 命令执行完成但退出码非 0（ Failed ）。 命令执行超时（ Timeout ）。 命令执行异常（ Error ）。 |
| Stopping | 正在停止任务 | 存在至少一台实例的命令执行状态为 Stopping ，则总执行状态为 Stopping 。 |
| Stopped | 任务已停止 | 所有实例的命令执行状态是 Stopped ，则总执行状态为 Stopped 。实例上的命令执行状态为以下状态时，返回值均为 Stopped 状态： 任务已取消（ Cancelled ）。 任务已终止（ Terminated ）。 |
| PartialFailed | 部分实例执行成功且部分实例执行失败 | 各个实例的命令执行状态均为 Success 、 Failed 或 Stopped ，则总执行状态为 PartialFailed 。 |
