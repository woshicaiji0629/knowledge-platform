800 表示东八区。 |
| AlarmIfFail | Boolean | 否 | 提取日志失败时，系统是否报错。 true（默认值）：报错。 false：不报错。 |
| KeepSource | Boolean | 否 | 被解析后的日志中，是否保留原始字段。 true（默认值）：保留。 false：不保留。 |

示例
将%Y/%m/%d %H:%M:%S格式的原始时间（log_time字段的值）解析为对应的日志时间，时区使用机器所在时区。
示例1：假设时区为东八区。
原始日志
"log_time":"2016/01/02 12:59:59"
Logtail插件处理配置
{ "processors":[ { "type":"processor_strptime", "detail": { "SourceKey": "log_time", "Format": "%Y/%m/%d %H:%M:%S" } } ] }
处理结果
"log_time":"2016/01/02 12:59:59" Log.Time = 1451710799
示例2：假设时区为东七区。
原始日志
"log_time":"2016/01/02 12:59:59"
Logtail插件处理配置
{ "processors":[ { "type":"processor_strptime", "detail": { "SourceKey": "log_time", "Format": "%Y/%m/%d %H:%M:%S", "AdjustUTCOffset": true, "UTCOffset": 25200 } } ] }
处理结果
"log_time":"2016/01/02 12:59:59" Log.Time = 1451714399
示例3：假设时区为东七区。
原始日志
"log_time":"2016/01/02 12:59:59.123"
Logtail插件处理配置
{ "processors":[ { "type":"processor_strptime", "detail": { "SourceKey": "log_time", "Format": "%Y/%m/%d %H:%M:%S.%f" } } ] }
处理结果
"log_time":"2016/01/02 12:59:59.123" Log.Time = 1451714399
常见的时间表达式
说明
processor_strptime插件支持%f格式解析，表示秒的小数部分，最高精度为纳秒。
