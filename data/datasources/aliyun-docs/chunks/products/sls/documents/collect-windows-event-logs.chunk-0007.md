t Log API，即只能在 Windows Vista 及以上的操作系统上使用。 |
| Provider | String 数组 | 否 | 根据事件来源过滤日志。例如设置为 ["App1", "App2"] 表示只采集来源名字为 App1 和 App2 的事件日志，其他事件日志都会被忽略。 默认为空，表示采集所有来源的事件。 说明 该参数仅支持 Windows Event Log API，即只能在 Windows Vista 及以上的操作系统上使用。 |
| IgnoreZeroValue | Boolean | 否 | 并非每条事件日志都拥有所有的字段，您可以使用此参数过滤空字段，空字段的定义根据类型而定，例如整数类型使用 0 表示空字段。 默认为 false ，表示不过滤空字段。 |
