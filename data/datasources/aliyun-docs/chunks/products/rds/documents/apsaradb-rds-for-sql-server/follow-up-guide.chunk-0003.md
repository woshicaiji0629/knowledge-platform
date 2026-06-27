## 只读实例与读写分离（集群系列）
功能简介：在对数据库有少量写请求，但有大量读请求的应用场景下，单个实例可能无法承受读取压力，甚至对业务产生影响。为了实现读取能力的弹性扩展，分担数据库压力，您可以在集群系列的主实例中创建一个或多个只读实例分散数据库读取压力，增加应用的吞吐量。且当前对于满足条件的主实例支持[只读实例快速初始化能力](../overview-of-read-only-apsaradb-rds-for-sql-server-instances.md)，该能力将有效缩短只读实例的创建时间至分钟级别，且该过程对主实例I/O无任何影响。
只读实例创建后开通只读地址，并在应用程序中配置主实例地址和只读地址，可以实现写请求转发到主实例，读请求转发到只读地址，只读地址会根据权重将读请求自动转发给各个只读实例。
涉及功能：[RDS SQL Server](rds-cluster-edition.md)[集群系列](rds-cluster-edition.md)、[创建](create-a-read-only-apsaradb-rds-for-sql-server-instance.md)[SQL Server](create-a-read-only-apsaradb-rds-for-sql-server-instance.md)[只读实例](create-a-read-only-apsaradb-rds-for-sql-server-instance.md)、[读写分离简介/开通读写分离](enable-the-read-or-write-splitting-endpoint-for-an-apsaradb-rds-for-sql-server-instance.md)
