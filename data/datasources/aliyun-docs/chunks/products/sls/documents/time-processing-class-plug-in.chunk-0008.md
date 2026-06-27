lse：不保留 |
| NoKeyError | Boolean | 否 | 原始日志中无您所指定的原始字段时，系统是否报错。 true（默认值）：报错 false：不报错 |
| AlarmIfFail | Boolean | 否 | 提取日志时间失败，系统是否报错。 true（默认值）：报错 false：不报错 |

示例
原始时间（s_key字段）的格式为2006-01-02 15:04:05（东八区），现将原始时间解析为2006/01/02 15:04:05（东九区）格式，添加到d_key字段中，并设置解析结果为日志服务中的日志时间。
原始日志
"s_key":"2019-07-05 19:28:01"
Logtail插件处理配置
{ "processors":[ { "type":"processor_gotime", "detail": { "SourceKey": "s_key", "SourceFormat":"2006-01-02 15:04:05", "SourceLocation":8, "DestKey":"d_key", "DestFormat":"2006/01/02 15:04:05", "DestLocation":9, "SetTime": true, "KeepSource": true, "NoKeyError": true, "AlarmIfFail": true } } ] }
处理结果
"s_key":"2019-07-05 19:28:01" "d_key":"2019/07/05 20:28:01"（）
