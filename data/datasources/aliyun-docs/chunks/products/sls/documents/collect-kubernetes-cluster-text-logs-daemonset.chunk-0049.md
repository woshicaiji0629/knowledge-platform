### 时间解析
对日志中的时间字段进行解析，并将解析结果设置为日志的__time__字段。
效果示例：

| 未经任何处理的原始日志 | 时间解析 |
| --- | --- |
| {"level":"INFO","timestamp":"2025-09-23T19:11:47+0800","cluster":"yilu-cluster-0728","message":"User logged in successfully","userId":"user-123"} | 解析后的日志以结构化键值对显示，时间字段被正确解析为日志时间（如 09-29 09:56:01），其余字段如 cluster 、 level 、 message 、 userId 等独立展示。 |

配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>时间解析：
原始字段：解析日志前，用于存放日志内容的原始字段。
时间格式：根据日志中的时间内容设置对应的[时间格式](time-processing-class-plug-in.md)。
时区：选择日志时间字段所在的时区。默认使用机器时区，即LoongCollector（Logtail）进程所在环境的时区。
