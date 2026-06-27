### 特性
高兼容性：兼容Redis 6.0大部分的数据结构和命令，具体限制请参见[Tair（企业版）命令支持与限制](../developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。
低成本：最低为Redis开源版的15%。
性能：约为Redis开源版的60%，更多信息请参见[磁盘（ESSD）型性能白皮书](../support/performance-white-paper-of-essd-based-instances.md)、[磁盘（SSD）型性能白皮书](../support/disk-ssd-performance-white-paper.md)。
同步模式：额外支持[半同步模式](../user-guide/modify-the-synchronization-mode-of-a-persistent-memory-optimized-instance.md)。
磁盘存储：数据分布在ESSD或SSD中，容量可达百TB级别，拥有高数据可靠性。
数据分布：采用阿里云TairDB存储引擎，数据通过磁盘持久化，内存用于请求加速。
使用场景：温数据和冷数据。
