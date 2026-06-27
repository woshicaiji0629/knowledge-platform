义标识机器组](create-a-user-defined-identity-machine-group.md)。
确认目标机器组已在应用机器组区域，单击下一步。
重要
创建机器组后立刻应用，可能因为连接未生效，导致心跳为FAIL，您可单击自动重试。如果还未解决，请参见[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[机器组无心跳](troubleshoot-the-errors-related-to-logtail-machine-groups.md)进行排查。
在数据源设置页签中，粘贴以下代码到插件配置栏，其中${服务器IP}请替换成您的服务器IP地址，然后单击下一步。
{ "inputs": [ { "type": "metric_http", "detail": { "IntervalMs": 60000, "Addresses": [ "http://${服务器IP}/nginx_status", "http://${服务器IP}/nginx_status", "http://${服务器IP}/nginx_status" ], "IncludeBody": true } } ], "processors": [ { "type": "processor_regex", "detail": { "SourceKey": "content", "Regex": "Active connections: (\\d+)\\s+server accepts handled requests\\s+(\\d+)\\s+(\\d+)\\s+(\\d+)\\s+Reading: (\\d+) Writing: (\\d+) Waiting: (\\d+)[\\s\\S]*", "Keys": [ "connection", "accepts", "handled", "requests", "reading", "writing", "waiting" ], "FullMatch": true, "NoKeyError": true, "NoMatchError": true, "KeepSource": false } } ] }
inputs为数据源配置，必选项。
重要
一个inputs中只允许配置一个类型的数据源。
processors为处理配置，用于解析数据。可选项，您可以配置一种或多种处理方式。
如果当前的inputs配置无法满足日志解析需求，您可以在插件配置中添加processors配置，即添加Logtail插件处理数据。例如提取字段、提取日志时间、脱敏数据、过滤日志等。更多信息，请参见[使用](overview-22.md)[Logtail](overvie
