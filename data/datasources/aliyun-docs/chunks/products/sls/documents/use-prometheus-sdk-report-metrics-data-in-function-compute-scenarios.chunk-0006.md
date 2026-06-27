## 验证采集数据
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表区域，单击目标Project。
在时序存储>时序库页签中，单击目标MetricStore。
在页面右上角，设置查询和分析的时间范围。输入[PromQL](time-metric-data-query-and-analysis-syntax.md)[语句](time-metric-data-query-and-analysis-syntax.md)，计算整体耗时情况的P50百分位数值，单击立即执行。
histogram_quantile(0.5, sum by (le) (rate(server_handling_seconds_bucket[1m])))
执行后，页面将展示 P50 延迟指标的折线图，表明数据已成功采集。
该文章对您有帮助吗？
反馈
