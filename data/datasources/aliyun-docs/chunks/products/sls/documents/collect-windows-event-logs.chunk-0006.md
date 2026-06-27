| 参数 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| type | String | 是 | 数据源类型，固定为 service_wineventlog 。 |
| Name | String | 是 | 待采集事件日志所属的通道名称。不配置时，默认为 Application，表示采集 应用程序 通道中的事件日志。您可以在 Windows 系统中查看通道全名。更多信息，请参见 [步骤](collect-windows-event-logs.md) [4](collect-windows-event-logs.md) 。 |
| IgnoreOlder | UINT | 否 | 根据事件时间过滤日志，此配置是相对于采集开始时间的偏移量，单位为秒，早于此设置的日志会被忽略。 例如： 设置为 3600，表示相对于采集开始时间一小时前的日志都会被忽略。 设置为 14400，表示相对于采集开始时间四小时前的日志都会被忽略。 默认为空，表示不根据事件时间进行过滤，采集服务器上所有的历史事件日志。 说明 该选项仅在首次配置采集时生效，Logtail 会记录事件采集的 Checkpoint，保证不会重复采集事件日志。 |
| Level | String | 否 | 根据事件等级过滤日志，默认值为 information, warning, error, critical ，表示采集除了 verbose 等级外的其他所有日志。 可选值包括：information、warning、error、critical、verbose。您可以使用半角逗号（,）指定多个等级。 说明 该参数仅支持 Windows Event Log API，即只能在 Windows Vista 及以上的操作系统上使用。 |
| EventID | String | 否 | 根据事件 ID 过滤日志，可以指定正向过滤（单个或范围）或者反向过滤（不支持范围设置）。默认为空，表示采集所有事件。例如： 1-200 表示只采集事件 ID 在 1-200 范围内的事件日志。 20 表示只采集事件 ID 为 20 的事件日志。 -100 表示采集除了事件 ID 为 100 以外的所有事件日志。 1-200,-100 表示采集 1-200 范围内除了 100 以外的事件日志。 您可以使用半角逗号（,）指定多个值。 说明 该参数仅支持 Windows Event Log API，即只能在 Windows Vista 及以上的操作系统上使用。 |
| Provider | String 数组 | 否 | 根据事件来源过滤日志。例如设置为 ["App1", "App2"] 表示只采集来源名字为 App1 和 App2 的事件日志，其他事件日志都会被忽略。 默认为空，表示采集所有
