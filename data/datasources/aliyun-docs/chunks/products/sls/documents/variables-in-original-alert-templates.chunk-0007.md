| 变量 | 说明 | 数据类型 | 举例 |
| --- | --- | --- | --- |
| role_arn | 使用服务角色。 | string | acs:ram::117918664953****:role/aliyunslsalertmonitorrole |
| store_type | 存储类型。 log：日志。 metric：时序数据。 meta：资源数据。 | string | log |
| region | 查询统计目标库所在地域。 存储类型为资源数据时，该变量值为空。 | string | cn-hangzhou |
| project | 查询统计目标库所在 Project。 存储类型为资源数据时，该变量值为空。 | string | sls-test-alert |
| store | 查询统计目标库名称。 | string | test-LogStore |
| query | 查询语句。 | string | error | select count(1) as cnt |
| start_time | 查询开始时间。 存储类型为资源数据时，该变量值为空。 | int | 2006-01-02 15:04:05 |
| start_time_ts | 查询开始时间，Unix 格式。 存储类型为资源数据时，该变量值为空。 | int | 1616741485 |
| end_time | 查询结束时间。 存储类型为资源数据时，该变量值为空。 | int | 2006-01-02 15:04:05 |
| end_time_ts | 查询结束时间，Unix 格式。 存储类型为资源数据时，该变量值为空。 | int | 1616745085 |
| dashboard_id | 查询时关联的仪表盘 ID。 | string | mydashboard |
| raw_results | 实际查询内容，数组格式，最多 100 行。 | array | [{ "host":"example.com", "slbid":"slb-02", "status":"200" },{ "host":"example.com", "slbid":"slb-01", "status":"200" },{ "host":"example.com", "slbid":"slb-02", "status":"306" },{ "host":"example.com", "slbid":"slb-02", "status":"200" },{ "host":"example.com", "slbid":"slb-01", "status":"200" },{ "host":"example.com", "slbid":"slb-02", "stat
