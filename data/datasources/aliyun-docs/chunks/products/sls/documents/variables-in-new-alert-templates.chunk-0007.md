| 变量 | 说明 | 数据类型 | 取值示例 |
| --- | --- | --- | --- |
| store_type | 存储类型。 log：日志。 metric：时序数据。 meta：资源数据。 | string | log |
| region | 查询统计目标库所在地域。 存储类型为资源数据时，该变量值为空。 | string | cn-hangzhou |
| project | 查询统计目标库所在 Project。 存储类型为资源数据时，该变量值为空。 | string | sls-test-alert |
| store | 查询统计中的目标库名称。 | string | test-LogStore |
| query | 查询分析语句。 | string | error | select count(1) as cnt |
| start_time | 查询开始时间。 存储类型为资源数据时，该变量值为空。 | int | 1616741485 |
| end_time | 查询结束时间。 存储类型为资源数据时，该变量值为空。 | int | 1616745085 |
| raw_results | 实际查询内容，数组格式，最多 100 行。 raw_results 变量值超过 2KB，并且查询结果字段内容的长度超过 1KB 时，超出部分会被截断。 | array | [{ "host": "example.com", "slbid": "slb-02", "status": "200" }, { "host": "example.com", "slbid": "slb-01", "status": "200" }] |
| raw_results_count | 实际查询数据的总条数，可能多于 100。 | int | 20 |
| fire_result | 告警触发内容中的第一条数据。告警触发结果集可能包含多条数据，该参数只返回第一条数据。 | map | { "host": "example.com", "slbid": "slb-02", "status": "200" } |
| query_url | 查询的 URL 地址。 存储类型为资源数据时，该变量值为空。 | string | https://sls.console.aliyun.com/lognext/project/test-xxx/logsearch/test-alert-access?encode=base64&endTime=1617175989&queryString=KiB8IHNlbGVjdCBjb3VudCgxKSBhcy*******&queryTimeType=99&startTime=1617175089 |
| dashboard_url
