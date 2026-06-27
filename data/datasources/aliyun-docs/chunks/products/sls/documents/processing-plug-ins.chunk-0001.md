### 性能限制
使用扩展插件进行日志处理时，采集器会消耗更多的资源（以CPU为主），请根据实际情况调整采集器的参数配置，更多信息请参见[配置管理](loongcollector-management-linux.md)。
当原始数据量的生成速度超过5 MB/s时，不建议使用过于复杂的插件组合来处理日志，推荐使用扩展插件进行简单处理，再通过[数据加工](data-transformation-overview.md)完成进一步处理。
