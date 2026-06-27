### Serverless实例的RCU

| 类别 | 说明 |
| --- | --- |
| 定义 | RDS Serverless 实例计算资源的费用。计费项名称为 计算单元 RCU（rds_serverless_rcu） 。 创建 Serverless 实例后，会产生该计费项。根据实际使用的 RCU 计费。如果暂停实例，该计费项也会暂停计费。 |
| 计费公式 | RDS MySQL、PostgreSQL：RCU 费用=单节点 RCU 单价 * 单节点 RCU 用量 * 节点数 * 使用时长 RDS SQL Server：RCU 费用=RCU 单价 * RCU 用量 * 使用时长 说明 RCU 单价请参见 [MySQL Serverless](https://help.aliyun.com/zh/document_detail/447753.html) [费用](https://help.aliyun.com/zh/document_detail/447753.html) 、 [PostgreSQL Serverless](../apsaradb-rds-for-postgresql/pricing-of-serverless-apsaradb-rds-for-sql-server-instances.md) [费用](../apsaradb-rds-for-postgresql/pricing-of-serverless-apsaradb-rds-for-sql-server-instances.md) 、 [SQL Server Serverless](../apsaradb-rds-for-sql-server/pricing-of-serverless-apsaradb-rds-for-sql-server-instances.md) [费用](../apsaradb-rds-for-sql-server/pricing-of-serverless-apsaradb-rds-for-sql-server-instances.md) 。 |
| 计费方式 | Serverless。 |
| 是否支持节省计划或资源包抵扣 | 支持。 [弹性型（特惠版）节省计划](../apsaradb-rds-for-mysql/elastic-savings-plan.md) 和 [通用型节省计划](savings-plan-introduction.md) 可以抵扣 RDS Serverless 实例的 RCU 费用。 |
