Key String （必选） 源字段名。 |  |
| Regex integer （必选） 正则表达式。 |  |
| Keys String （必选） 提取的字段列表。 |  |
| Extra Format String （必选） Apache 配置文件中的日志配置部分，通常以 LogFormat 开头。 LogType String （必选） 解析日志类型，固定值为 Apache 。 SubType String （必选） 日志格式。 common combined 自定义 |  |
| KeepingSourceWhenParseFail boolean （可选） 解析失败时是否保留原始字段，默认为 false 。 |  |
| KeepingSourceWhenParseSucceed boolean （可选） 解析成功时是否保留原始字段，默认为 false 。 |  |
| RenamedSourceKey String （可选） 保留原始字段时，用于存储原始的字段名，默认不改名。 |  |
