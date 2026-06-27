### 停止实例
调用[StopInstance](../api-stopinstance.md)停止一台运行中（Running）的ECS实例，正常关机（ForceStop为 false）且停机模式为普通停机模式（StoppedMode为KeepCharging，即停止后仍旧保留实例并继续收费），预检查后正常停止ECS实例。
场景示例：实例ID为i-bp1aq39j2yul5y01****，地域为华东1（杭州）（cn-hangzhou）。
请求示例
aliyun ecs StopInstance \ --RegionId cn-hangzhou \ --InstanceId i-bp1aq39j2yul5y01**** \ --ForceStop false \ --StoppedMode KeepCharging \ --DryRun false
返回示例
{ "RequestId": "121B5745-4983-57B1-BC97-C3A3536E****" }
