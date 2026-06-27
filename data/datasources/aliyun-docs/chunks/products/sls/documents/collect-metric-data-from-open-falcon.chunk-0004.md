查。
在数据源设置页签中，设置配置名称和插件配置，然后单击下一步。
重要
inputs为数据源配置，必选项。一个inputs中只允许配置一个类型的数据源。
{ "inputs": [ { "detail": { "Format": "influx", "Address": ":127.0.0.1:8476" }, "type": "service_http_server" } ], "global": { "AlwaysOnline": true, "DelayStopSec": 500 } }
