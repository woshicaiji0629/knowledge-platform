。
在数据源设置页签中，设置配置名称和插件配置，然后单击下一步。
重要
inputs为数据源配置，必选项。一个inputs中只允许配置一个类型的数据源。
{ "inputs": [ { "detail": { "IntervalMs": 30000 }, "type": "metric_system_v2" } ] }

| 参数 | 类型 | 是否必选 | 参数说明 |
| --- | --- | --- | --- |
| type | string | 是 | 数据源类型，固定为 metric_system_v2。 |
| IntervalMs | int | 是 | 每次请求的间隔，单位：ms。不能低于 5000，建议设置为 30000。 |

单击查询日志，进入时序库。
