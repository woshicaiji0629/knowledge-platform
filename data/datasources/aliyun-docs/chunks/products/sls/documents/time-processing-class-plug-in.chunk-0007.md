### JSON配置方式
参数说明
配置type为processor_gotime，detail说明如下表所示。

| 参数 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| SourceKey | String | 是 | 原始字段名。 |
| SourceFormat | String | 是 | 原始时间的格式。 |
| SourceLocation | Int | 是 | 原始时间的时区。参数值为空时，表示 Logtail 所在主机或容器的时区。 |
| DestKey | String | 是 | 解析后的目标字段，该字段不支持设置为 __time__ 。 |
| DestFormat | String | 是 | 解析后的时间格式。 |
| DestLocation | Int | 否 | 解析后的时区。参数值为空时，表示本机时区。 |
| SetTime | Boolean | 否 | 是否将解析后的时间设置为日志时间。 true（默认值）：是 false：否 |
| KeepSource | Boolean | 否 | 被解析后的日志中是否保留原始字段。 true（默认值）：保留 false：不保留 |
| NoKeyError | Boolean | 否 | 原始日志中无您所指定的原始字段时，系统是否报错。 true（默认值）：报错 false：不报错 |
| AlarmIfFail | Boolean | 否 | 提取日志时间失败，系统是否报错。 true（默认值）：报错 false：不报错 |
