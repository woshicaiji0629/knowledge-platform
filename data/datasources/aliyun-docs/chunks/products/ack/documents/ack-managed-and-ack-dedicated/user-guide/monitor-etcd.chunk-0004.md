说明
如下资源使用率指标已废弃，请及时去除依赖该指标的告警和监控。
cpu_utilization_ratio：CPU使用率。
memory_utilization_ratio：内存使用率。
请使用resource_utilization_level指标做资源使用水位相关的告警和监控，该指标在灰度开放中。如果内存和CPU资源水位相关看板不可见，请先[升级监控组件](../../../../arms/documents/prometheus-monitoring/update-monitoring-components.md)再[升级托管探针](../../../../arms/documents/prometheus-monitoring/update-monitoring-components.md)。
