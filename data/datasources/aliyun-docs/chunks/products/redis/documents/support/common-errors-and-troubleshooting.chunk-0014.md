### OOM command not allowed when used memory > 'maxmemory'
可能原因：Tair实例已使用的内存超过该实例的最大配置（maxmemory）。
说明
如果是Tair集群实例，可能是其中一个节点已使用的内存已超过该节点的最大配置。
解决方法：
若实例的总内存使用率达到100%，建议升级实例配置，更多信息请参见[升级实例配置](../user-guide/change-the-configurations-of-an-instance.md)。
若集群实例仅有单个节点的内存使用率达到100%，该实例中可能存在大Key，您可以通过[离线全量](../user-guide/offline-key-analysis.md)[Key](../user-guide/offline-key-analysis.md)[分析](../user-guide/offline-key-analysis.md)或[实例诊断](../user-guide/create-a-diagnostic-report.md)进行定位分析。
