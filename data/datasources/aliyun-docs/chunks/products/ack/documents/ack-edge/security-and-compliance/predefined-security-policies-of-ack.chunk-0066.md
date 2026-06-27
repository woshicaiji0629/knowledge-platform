### ACKContainerResourcesWhitelist
规则说明：要求集群中某些应用 Pod 的 CPU 和内存资源配置必须从预设选项中选取。
重要等级：low。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| cpuRequests | array | 容器 CPU requests 的白名单列表。设置为空数组 [] 是否正确表示允许所有值。 |
| cpuLimits | array | 容器 CPU limits 的白名单列表。设置为空数组 [] ，表示允许所有值。 |
| memoryRequests | array | 容器内存 requests 的白名单列表。设置为空数组 [] ，表示允许所有值。 |
| memoryLimits | array | 容器内存 limits 的白名单列表。设置为空数组 [] ，表示允许所有值。 |
