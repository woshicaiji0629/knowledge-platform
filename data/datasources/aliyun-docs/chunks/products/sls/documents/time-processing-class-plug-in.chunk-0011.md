### JSON配置方式
参数说明
配置type为processor_strptime，detail说明如下表所示。

| 参数 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| SourceKey | String | 是 | 原始字段名。 |
| Format | String | 是 | 原始时间的格式。 |
| AdjustUTCOffset | Boolean | 否 | 是否调整时区。 true：是。 false（默认值）：否 |
| UTCOffset | Int | 否 | 用于调整的时区偏移秒数。例如 28800 表示东八区。 |
| AlarmIfFail | Boolean | 否 | 提取日志失败时，系统是否报错。 true（默认值）：报错。 false：不报错。 |
| KeepSource | Boolean | 否 | 被解析后的日志中，是否保留原始字段。 true（默认值）：保留。 false：不保留。 |
