### ESSD型分片规格
ESSD型实例仅支持[标准架构](standard-master-replica-instances.md)，暂不支持集群架构。

| 规格名称 | 规格代码（API 使用） | CPU 核数 | 内存（GB） | 可选存储性能级别与容量（GB） | 最大连接数 | 带宽 |
| --- | --- | --- | --- | --- | --- | --- |
| 4C - 16GB | tair.essd.standard.xlarge | 4 | 16 | PL1：60~250 | 60,000 | 1,500 Mbps（187.5 MB/s） |
| 8C - 32GB | tair.essd.standard.2xlarge | 8 | 32 | PL1：60~500 PL2：470~1000 | 60,000 | 2,000 Mbps（250 MB/s） |
| 16C - 64GB | tair.essd.standard.4xlarge | 16 | 64 | PL1：60~1000 PL2：470~2000 PL3：1270~4000 | 60,000 | 3,000 Mbps（375 MB/s） |
| 32C - 128GB | tair.essd.standard.8xlarge | 32 | 128 | PL2：470~4000 PL3：1270~8000 | 100,000 | 5,000 Mbps（625 MB/s） |
| 64C - 256GB | tair.essd.standard.16xlarge | 64 | 256 | PL2：470~8000 PL3：1270~16000 | 100,000 | 8,000 Mbps（1,000 MB/s） |

说明
ESSD PL3（Performance Level 3）的性能优于PL2与PL1，更多信息请参见[ESSD](../../../ecs/documents/user-guide/essds.md)。
