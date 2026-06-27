## 常见问题
Q：如何切换VPC？
A：RDS PostgreSQL不支持切换VPC。
如果需要更换VPC，您可以购买新的实例（购买时选择目标VPC），然后将数据迁移到新的实例。详情请参见[使用一键上云迁移实例](use-the-cloud-migration-feature-to-migrate-data-between-apsaradb-rds-for-postgresql-instances.md)或[使用](use-dts-to-migrate-data-between-apsaradb-rds-for-postgresql-instances.md)[DTS](use-dts-to-migrate-data-between-apsaradb-rds-for-postgresql-instances.md)[迁移实例](use-dts-to-migrate-data-between-apsaradb-rds-for-postgresql-instances.md)。
如果不便进行实例迁移，您可以[使用](../../../vpc/documents/create-and-manage-vpc-peering-connection.md)[VPC](../../../vpc/documents/create-and-manage-vpc-peering-connection.md)[对等连接实现](../../../vpc/documents/create-and-manage-vpc-peering-connection.md)[VPC](../../../vpc/documents/create-and-manage-vpc-peering-connection.md)[私网互通](../../../vpc/documents/create-and-manage-vpc-peering-connection.md)。同一地域的VPC对等连接不收取任何费用，而跨地域的VPC对等连接则需支付相应费用。
