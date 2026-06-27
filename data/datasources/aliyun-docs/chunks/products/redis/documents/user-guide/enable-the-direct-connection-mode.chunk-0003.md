## 注意事项
由于绕过了代理节点，连接性能有一定的下降，Redis开源版集群实例中单个分片的最大连接数为10,000；Tair（企业版）集群实例中单个分片的最大连接数为30,000。更多规格信息，请参见[实例规格](../product-overview/overview-4.md)。
如果存在数据倾斜，即某个分片被大量访问，其他分片基本处于空闲状态，可能引起该分片的连接数被耗尽，新的连接建立请求被拒绝，从而影响实例整体性能。
说明
数据倾斜通常由热点Key或大Key引起，排查方法，请参见[Top Key](use-the-real-time-key-statistics-feature.md)[统计](use-the-real-time-key-statistics-feature.md)和[离线全量](offline-key-analysis.md)[Key](offline-key-analysis.md)[分析](offline-key-analysis.md)。
开通直连地址后，将无法执行[升级大版本](upgrade-the-major-version-1.md)与[更换实例所属的可用区](migrate-an-instance-across-zones.md)操作，如需执行请先释放[直连地址](release-a-private-endpoint-from-an-apsaradb-for-redis-instance.md)。
开通直连地址后，集群实例在变配时，单次仅支持变配分片数或分片规格，更多信息请参见[分布式集群实例变配方案](../support/why-do-i-fail-to-change-the-configurations-of-a-cluster-instance-that-use-local-disks.md)。
