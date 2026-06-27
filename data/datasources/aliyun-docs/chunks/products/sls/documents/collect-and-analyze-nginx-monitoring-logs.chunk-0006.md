| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 数据源类型，固定为 metric_http 。 |
| IntervalMs | int | 是 | 每次请求的间隔，单位：ms。 |
| Addresses | 数组 | 是 | 配置为您需要监控的 URL 列表。 |
| IncludeBody | boolean | 否 | 是否采集请求体，默认值：false。如果为 true，则采集后，将请求体内容存放在 content 字段中。 |

完成采集配置1分钟后，即可查看日志，样例如下所示。日志服务默认生成nginx_status仪表盘，展示查询和分析结果。
_address_: http://127.0.0.1/nginx_status _method_: GET _result_: success _http_response_code_: 200 _response_time_ms_: 0.418 accepts: 6 connection: 3 handled: 6 reading: 0 requests: 6 waiting: 2 writing: 1
