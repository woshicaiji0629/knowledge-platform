## CLI
可以调用[停止实例](../developer-reference/api-ecs-2014-05-26-stopinstance.md)操作，并将StoppedMode参数设置为StopCharging。
示例：使用节省停机模式停止杭州地域实例ID为i-t4n5xxxxxxxxxxx的实例。
aliyun ecs StopInstance \ --RegionId cn-hangzhou \ --InstanceId i-t4n5xxxxxxxxxxx \ --StoppedMode StopCharging \ --ForceStop false \ --DryRun false
