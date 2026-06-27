## 附录
results结构
[{ "store_type": "log", "region": "cn-hangzhou", "project": "sls-alert-test", "store": "test", "query": "* | select count(1) as cnt", "start_time": 1616741485, "end_time": 1616745085, "dashboard_id": "mydashboard", "raw_results": [{ "cnt": "4" }], "raw_result_count": 1, "fire_result": { "cnt": "4" }, "truncated": false, "role_arn": "" }]
fire_results结构
[{ "host": "example.com", "host__1": "example.com", "pv": "836", "slbid": "slb-02", "status": "200" }, { "host": "example.com", "host__1": "example.com", "pv": "836", "slbid": "slb-02", "status": "200" }]
policy结构
{ "alert_policy_id": "sls.test-alert", "action_policy_id": "sls.test-action", "repeat_interval": "5m0s" }
