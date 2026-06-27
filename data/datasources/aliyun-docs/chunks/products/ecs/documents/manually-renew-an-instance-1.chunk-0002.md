### （推荐）通过PC端续费
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，并在顶部菜单栏选择实例所在地域。
在实例列表页选择待续费实例，并进入实例详情页面，在实例信息的到期时间字段下方单击续费，按页面提示选择续费时长并完成支付。
说明
阿里云为您提供了多台实例批量续费功能。
若您想对单一地域下多台实例进行批量续费，您可以在实例列表勾选多台目标实例，并在列表底部选择更多>费用> 续费进行批量操作。
若您想对不同地域下的多台实例进行批量续费，您可以前往[续订管理](https://usercenter2.aliyun.com/renew/manual)页面，在手动续订页签下的列表中勾选一台或多台ECS实例进行续费。请注意，云服务器ECS暂不支持和其他产品一起批量续费。
通过阿里云App续费
登录阿里云App，选择控制台 > 续费管理。
单击云服务器 ECS-包年包月，并选择实例所在地域。
勾选一台或多台实例，单击立即续费。
单击提交订单，并按照页面提示完成支付。
通过API续费
您可以调用[续费实例](developer-reference/api-ecs-2014-05-26-renewinstance.md)API，设置待续费的实例ID，及根据续费场景选择的续费时长参数（Period、PeriodUnit或ExpectedRenewDay的其中一个的值），即可为单个ECS实例完成续费的操作。若您想通过API批量续费多台ECS实例，您可以多次调用此接口实现批量操作。
我们也为您提供了其他包年包月实例续费相关的API接口：
开启自动续费：您可以调用[修改实例的自动续费属性](developer-reference/api-ecs-2014-05-26-modifyinstanceautorenewattribute.md)，通过设置实例IDInstanceId、续费时长Duration、和自动续费状态参数AutoRenew为实例开通自动续费。
查询实例续费价格：您可以调用[查询资源续费价格](developer-reference/api-ecs-2014-05-26-describerenewalprice.md)接口，传入查询实例的地域、规格、续费时长等参数查询实例续费费用。
查询指定范围内到期的云服务器：通过调用[查询实例的详细信息列表](developer-reference/api-ecs-2014-05-26-describeinstances.md)，并设置过滤参数ExpiredStartTime和ExpiredEndTime，查询一定时间范围内到期的实例信息。
查询ECS实例
