## 对接Grafana
登录Grafana。
在左侧导航栏，选择Configuration>Data Sources。
在Data Sources页签，单击Add data source。
选择Prometheus，单击Select。
在Settings页签中，请参考如下说明配置数据源。

| 参数 | 说明 |
| --- | --- |
| Name | 请您自定义一个数据源的名称，例如 Prometheus-01。 |
| HTTP | URL ：日志服务 MetricStore 的 URL，格式为 https://{project}.{sls-endpoint}/prometheus/{project}/{metricstore} 。其中 {sls-endpoint} 为 Project 所在地域的 Endpoint，详情请参见 [服务入口](developer-reference/service-entrance.md) ， {project} 和 {metricstore} 为您已创建的日志服务的 Project 和 Metricstore，请根据实际值替换。例如： https://sls-prometheus-test.cn-hangzhou.log.aliyuncs.com/prometheus/sls-prometheus-test/prometheus 。 说明 为保证传输安全性，请务必设置为 https 。 Whitelisted Cookies ：添加访问白名单，可选。 |
| Auth | 打开 Basic auth 开关。 |
| Basic Auth Details | User 为阿里云账号 AccessKeyID。 Password 为阿里云账号 AccessKeySecret。 建议您使用仅具备指定 Project 只读权限的 RAM 用户账号，详情请参见 [指定](use-custom-policies-to-grant-permissions-to-a-ram-user.md) [Project](use-custom-policies-to-grant-permissions-to-a-ram-user.md) [只读授权策略](use-custom-policies-to-grant-permissions-to-a-ram-user.md) 。 |

单击Save & Test。
