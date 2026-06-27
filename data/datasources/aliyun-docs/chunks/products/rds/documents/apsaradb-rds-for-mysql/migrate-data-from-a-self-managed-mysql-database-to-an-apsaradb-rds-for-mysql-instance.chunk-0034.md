## 阶段四：数据验证与业务切换
等待DTS迁移任务完成
未包含增量迁移的任务：在全量迁移完成后自动结束，任务运行状态变为已完成。
包含增量迁移的任务：任务不会自动结束，增量迁移会持续进行（任务运行状态为运行中）。当增量迁移显示无延迟时，表示源库与目标库数据一致，可以进行数据验证。
数据验证
当迁移任务结束或增量迁移无延迟（低延迟）时，可以进行源库和目标库的数据验证：
自动校验：在DTS中[配置数据校验任务](https://help.aliyun.com/zh/dts/user-guide/enable-data-verification#task-2249288)，自动对比源库和目标库的数据。
手动抽样校验：您可以从多种维度手动校验数据（如对比源库和目标库的表行数、核心业务数据等），抽样验证数据一致性。以下为示例代码：
-- 示例1：在源库和目标库分别执行，对比表行数 SELECT COUNT(*) FROM your_table; -- 示例2：在源库和目标库分别执行，对比关键业务指标，如某时间段内的订单总金额 SELECT SUM(amount) FROM orders WHERE create_time >= '2024-01-01';
业务切换
数据验证完成后，建议您选择业务低峰期，将应用服务内的自建数据库连接地址修改为[RDS MySQL](view-and-change-the-internal-and-public-endpoints-and-port-numbers-of-an-apsaradb-rds-for-mysql-instance.md)[实例的连接地址](view-and-change-the-internal-and-public-endpoints-and-port-numbers-of-an-apsaradb-rds-for-mysql-instance.md)，完成业务切换。如果DTS迁移任务中包含增量迁移，请在切换完成后及时释放该任务，避免迁移任务持续计费。
