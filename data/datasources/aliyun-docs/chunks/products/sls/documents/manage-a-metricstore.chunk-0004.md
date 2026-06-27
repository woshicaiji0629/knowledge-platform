，当区间为【0,0】时，不进行数据写入时间范围规则判断。
说明
此特性仅对按Prometheus Remote Write协议写入的数据有效，采集接入方式参见[通过](collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[Remote Write](collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[协议接入](collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[Prometheus](collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[监控数据](collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)。
写入处理器
数据写入前进行处理。支持字段修改、字段解析、数据过滤、数据脱敏等多种使用场景。详情参见[数据写入时处理（写入处理器）](sls-write-processor.md)。
标签
支持对MetricStore添加标签信息,当您需要对MetricStore进行分组管理时，可以使用标签来区分MetricStore。
单击保存。
