### 时间解析
配置 processor_parse_timestamp_native 插件对日志中的时间字段进行解析，并将解析结果设置为日志的__time__字段。

| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，固定值 processor_parse_timestamp_native 。 | # ...在 spec.config 下... processors: # 配置原生时间解析插件 - Type: processor_parse_timestamp_native # 原始日志字段来源，通常为 content SourceKey: content # 时间格式定义，需与日志中的时间字段格式完全匹配 SourceFormat: '%Y-%m-%d %H:%M:%S' SourceTimezone: 'GMT+00:00' |
| SourceKey String （必选） 源字段名。 |  |
| SourceFormat String （必选） [时间格式](time-parsing.md) ，需与日志中的时间字段格式完全匹配。 |  |
| SourceTimezone String （可选） 日志时间所属时区，默认使用机器时区，即 LoongCollector 进程所在环境的时区。 格式： GMT+HH:MM ：东区 GMT-HH:MM ：西区 |  |
