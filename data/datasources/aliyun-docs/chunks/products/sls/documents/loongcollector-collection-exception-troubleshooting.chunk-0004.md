### 采集时间延迟
采集时间延迟有几类情况：
几秒内的延迟是在预期范围内的，若介意可以配置[时间插件](extract-log-time.md)。
若有大量数据延迟，检查是否有重启现象。重启后会向前采集，产生延时采集的现象。查看最新数据是否实时，若最新数据实时就没问题。
只延时一行，检查日志文件的最后一行是否没有回车。
某台机器出现延时，可能是该机器采集器启动较晚，可以通过/usr/local/ilogtail/app_info.json的时间确认，或/usr/local/ilogtail/ilogtail.LOG中是否存在“network error”网络原因导致延时。
若不符合上述场景，则在[控制台通过诊断信息排查采集错误](loongcollector-collection-exception-troubleshooting.md)或[使用](use-cloudlens-for-sls-to-analyze-loongcollector-log-collection-latency.md)[CloudLens for SLS](use-cloudlens-for-sls-to-analyze-loongcollector-log-collection-latency.md)[分析](use-cloudlens-for-sls-to-analyze-loongcollector-log-collection-latency.md)[LoongCollector](use-cloudlens-for-sls-to-analyze-loongcollector-log-collection-latency.md)[日志采集延迟问题](use-cloudlens-for-sls-to-analyze-loongcollector-log-collection-latency.md)。
