## API
调用[StopInstance](../api-stopinstance.md)停止按量付费（含抢占式）ECS实例时，将StoppedMode设置为StopCharging，即可使ECS实例进入节省停机模式。
重要
对于不满足节省停机模式条件的实例，调用该接口并设置StoppedMode=StopCharging不会报错，实例会以普通模式正常停机。要确认实例是否成功进入节省停机模式，请通过[DescribeInstances](../developer-reference/api-ecs-2014-05-26-describeinstances.md)接口查询实例状态。
调用[RunInstances](../developer-reference/api-ecs-2014-05-26-runinstances.md)和[CreateInstance](../developer-reference/api-ecs-2014-05-26-createinstance.md)创建抢占式实例时，将SpotInterruptionBehavior设置为Stop，实例中断时，将进入节省停机模式。
