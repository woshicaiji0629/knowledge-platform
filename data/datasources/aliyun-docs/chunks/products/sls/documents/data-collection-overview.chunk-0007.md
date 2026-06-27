### 与现有三方生态集成
[集成其他开源](collect-data-using-other-open-source-agents.md)[Agent](collect-data-using-other-open-source-agents.md)[与协议采集日志](collect-data-using-other-open-source-agents.md)：支持如下方式。
使用Loggie的Sink配置，将采集到的日志上传到日志服务。
使用Log4j2 Appender将日志采集到日志服务。
使用Syslog-ng采集日志并通过Syslog协议上传。
使用Kafka Producer SDK、Beats系列软件、Collectd、Fluentd、Logstash、Telegraf、Vector等采集工具采集日志，并通过Kafka协议上传到日志服务。
[接入](import-metrics-collected-by-telegraf.md)[Telegraf](import-metrics-collected-by-telegraf.md)[监控](import-metrics-collected-by-telegraf.md)：日志服务支持将Telegraf采集的监控数据（MySQL监控数据、Redis监控数据、Elasticsearch监控数据、Clickhouse监控数据、Kafka监控数据、Tomcat监控数据等）通过InfluxDB协议写入LoongCollector（原Logtail），再将监控数据上传到日志服务。
[采集](collect-metric-data-from-open-falcon.md)[Open-Falcon](collect-metric-data-from-open-falcon.md)[监控数据](collect-metric-data-from-open-falcon.md)：配置Transfer将Open-Falcon数据上传至日志服务,Open-Falcon版本需包含[Influxdb support](https://github.com/open-falcon/falcon-plus/commit/df7a2f80e27902a7e081c595bd1a24080cc624e7)功能。
[通过](collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[Remote Write](collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[协议接入](collect-metric-data-from-prometheus-by-
