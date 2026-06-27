### ACKContainerResourcesRange
规则说明：限制集群中某些应用 Pod 的资源配置必须在指定的上下限范围内。
重要等级：low。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| cpuRequests | object | 包含以下取值。 min ：容器 CPU requests 的最小值。 max ：容器 CPU requests 的最大值。 |
| cpuLimits | object | 包含以下取值。 min ：容器 CPU limits 的最小值。 max ：容器 CPU limits 的最大值。 |
| memoryRequests | object | 包含以下取值。 min ：容器内存 requests 的最小值。 max ：容器内存 requests 的最大值。 |
| memoryLimits | object | 包含以下取值。 min ：容器内存 limits 的最小值。 max ：容器内存 limits 的最大值。 |
