0 分钟以上。如果 DTS 在设置的重试时间内相关操作执行成功，迁移任务将自动恢复。否则，迁移任务将会失败。 重要 源库、目标库出现其他问题后的重试时间 的值需要小于 源库、目标库无法连接后的重试时间 的值。 |
| 是否限制全量迁移速率 | 在全量迁移阶段，DTS 将占用源库和目标库一定的读写资源，可能会导致数据库的负载上升。您可以根据实际情况，选择是否对全量迁移任务进行限速设置（设置 每秒查询源库的速率 QPS 、 每秒全量迁移的行数 RPS 和 每秒全量迁移的数据量(MB)BPS ），以缓解目标库的压力。 说明 仅当 迁移类型 选择了 全量迁移 ，才有此配置项。 您也可以在迁移实例运行后， [调整全量迁移的速率](https://help.aliyun.com/zh/dts/user-guide/enable-throttling-for-data-migration) 。 |
| 是否限制增量迁移速率 | 您也可以根据实际情况，选择是否对增量迁移任务进行限速设置（设置 每秒增量迁移的行数 RPS 和 每秒增量迁移的数据量(MB)BPS ），以缓解目标库的压力。 说明 仅当 迁移类型 选择了 增量迁移 ，才有此配置项。 您也可以在迁移实例运行后， [调整增量迁移的速率](https://help.aliyun.com/zh/dts/user-guide/enable-throttling-for-data-migration) 。 |
| 环境标签 | 您可以根据实际情况，选择用于标识实例的环境标签。本示例无需选择。 |
| 是否去除正反向任务的心跳表 SQL | 根据业务需求选择是否在 DTS 实例运行时，在源库中写入心跳 SQL 信息。 是 ：不在源库中写入心跳 SQL 信息，DTS 实例可能会显示有延迟。 否 ：在源库中写入心跳 SQL 信息，可能会影响源库的物理备份和克隆等功能。 |
| 配置 ETL 功能 | 根据业务需求选择是否配置 [ETL](https://help.aliyun.com/zh/dts/user-guide/what-is-etl#task-2101705) [功能](https://help.aliyun.com/zh/dts/user-guide/what-is-etl#task-2101705) ，对数据进行加工处理。 是 ：配置 ETL 功能，您还需要在文本框中输入 [数据处理语句](https://help.aliyun.com/zh/dts/user-guide/configure-etl-in-a-data-migration-or-data-synchronization-task#task-2189872) 。 否 ：不配置 ETL 功能。 |
| 监控告警 | 根据业务需求选择是否设置告警并接收告警通
