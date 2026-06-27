。
查询指定范围内到期的云服务器：通过调用[查询实例的详细信息列表](developer-reference/api-ecs-2014-05-26-describeinstances.md)，并设置过滤参数ExpiredStartTime和ExpiredEndTime，查询一定时间范围内到期的实例信息。
查询ECS实例的自动续费状态：您可以调用[查询实例自动续费属性](developer-reference/api-ecs-2014-05-26-describeinstanceautorenewattribute.md)，通过设置实例IDInstanceId和实例自动续费状态RenewalStatus，查询实例的自动续费状态或处于特定自动续费状态下的实例列表。
