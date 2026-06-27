巡检规则

| 规则名称 | 开启状态 | 巡检算法 | 巡检指标 |
| --- | --- | --- | --- |
| total | 默认开启 | Time2Graph | pv body_bytes_sent_avg body_bytes_sent_sum request_length_avg request_length_sum upstream_response_time_avg request_time_avg |
| host | 默认开启 | Time2Graph | pv:host body_bytes_sent_avg:host body_bytes_sent_sum:host request_length_avg:host request_length_sum:host upstream_response_time_avg:host request_time_avg:host |
| host_status | 默认关闭 | Time2Graph | pv:host:status body_bytes_sent_avg:host:status body_bytes_sent_sum:host:status request_length_avg:host:status request_length_sum:host:status upstream_response_time_avg:host:status request_time_avg:host:status |

专属仪表盘

| 仪表盘名称 | 关联的 Logstore、Metricstore | 说明 |
| --- | --- | --- |
| 运营大盘 | 访问日志 Logstore 名称 | 展示用户请求相关的信息，包括 PV、UV、移动端分布、国家/省/市分布等。 说明 此部分信息基于原始访问日志全量计算，数据量超大的情况下会有一定延迟。 |
| 概览 | 访问日志 Logstore 名称 -metrics | 展示 Kubernetes 总体的监控信息，包括 PV、失败率、5XX 比例、状态码分布、流量等。 |
| 监控大盘 | 访问日志 Logstore 名称 -metrics | 支持以 host、status 等维度过滤出实例详细的监控信息。 |
| 异常事件 | 访问日志 Logstore 名称 -metrics 访问日志 Logstore 名称 -metrics-result | 展示流式巡检算法检测出的 Service 粒度异常信息，包括异常统计以及具体指标上异常的实时显示。 |
