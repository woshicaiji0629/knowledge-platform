## 单节点
标准架构单节点类型采用单个数据库节点部署架构，没有可实时同步数据的备节点。由于该架构只有一个数据库节点，无热备节点用于HA。当数据库节点发生故障时，数据会丢失，系统会重新拉起一个新的Redis进程（没有数据）。当节点故障业务自动切换完成后，应用程序需要将数据重新预热。
警告
单节点架构不能保障数据可用性和服务连续性，选用前请务必确认风险，不建议您在生产环境中使用该架构的实例。
单节点架构不支持以下功能：[自动或手动备份](../user-guide/automatic-or-manual-backup.md)、[离线全量](../user-guide/offline-key-analysis.md)[Key](../user-guide/offline-key-analysis.md)[分析](../user-guide/offline-key-analysis.md)和[实例回收站](../user-guide/manage-instances-in-the-recycle-bin.md)。若您对数据有可靠性要求，推荐使用高可用架构。
特点及应用场景：
单节点架构具有明显的价格优势，性价比较高。适用于数据可靠性要求不高的纯缓存业务场景使用。
