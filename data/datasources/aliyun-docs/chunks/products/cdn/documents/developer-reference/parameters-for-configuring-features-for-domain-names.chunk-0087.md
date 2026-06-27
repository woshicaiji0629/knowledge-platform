携带的参数来限速，还可以设定限速开始和结束时间。
根据用户请求URL中携带的参数来限速：通过traffic_limit_arg和traffic_limit_unit这两个参数的组合来实现。
设定限速开始和结束时间：通过ali_limit_start_hour和ali_limit_end_hour这两个参数的组合来实现。

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| ali_limit_rate | String | 是 | 指定单请求限速的具体速率（例如：200 KByte/s、1 MByte/s 等），支持“数值+字母单位”的参数值（字母单位支持 k、m），单位 Byte/s。 最小只能设定为 100k，低于 100k 的值将会按 100k 来执行。 | 1m：表示单请求限速为 1 MByte/s 100k：表示单请求限速为 100 KByte/s |
| ali_limit_rate_after | String | 否 | 不限速大小，在发送了多少数据之后才开始限速。支持“数值+字母单位”的参数值（字母单位支持 k、m），单位 Byte。 | 1000 |
| traffic_limit_arg | String | 否 | 限速参数名称，根据 URL 中提取的 arg 进行限速，例如：rate。 当请求中不带限速参数时，按默认限速值 ali_limit_rate 限速，如果想达到请求中没限速参数时不限速的效果，则把默认限速值 ali_limit_rate 配置为 0k。 | rate |
| traffic_limit_unit | String | 否 | 限速参数 traffic_limit_arg 的单位，支持 m（MByte/s）、k（KByte/s）。限速参数单位设定为 m 的情况下，当用户请求 URL 中携带的 rate=1 时，实际限速值为 1MByte/s。 最小只能设定为 100k，低于 100k 的值将会按 100k 来执行。 | m |
| ali_limit_start_hour | Integer | 否 | 限速开始时间，取值范围[0,24]，小于限速结束时间，默认值为 0。 说明 表示时间点，24 小时制的整点，例如：0 表示 00:00:00，24 表示 24:00:00。 | 20 |
| ali_limit_end_hour | Integer | 否 | 限速结束时间，取值范围[0,24]，大于限速开始时间，默认值为 24。 | 23 |
