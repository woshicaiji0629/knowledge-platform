### 自研增强特性
阿里云自研的AliSQL与AliPG在开源数据库的基础上，进行了一系列创新与优化，以满足企业级的性能和稳定性需求。
AliSQL提供了类似于MySQL企业版的诸多功能。例如，Binlog in Redo在事务提交时同步Binlog至Redo Log，以减少磁盘操作和提升性能；Statement Queue确保执行计划的稳定性；Inventory Hint快速提交/回滚事务以提高业务吞吐能力；Thread Pool优化了并发控制机制，保证了数据库在高并发环境下的高性能；Faster DDL提升了在线DDL的并发处理性能。
AliPG在开源PostgreSQL的基础上进行了许多增强。例如，Ganos时空引擎提供室内外、地上下、动静态全空间数据处理能力；TDE支持表级别加密；全密态数据库支持数据在存储、计算、传输的全程加密；Babelfish插件提供解析和执行SQL Server T-SQL语句的能力。rds_ccl插件通过SQL限流避免过高的负载，保障数据库稳定性。
更多选择理由，请参见[RDS](competitive-advantages-of-apsaradb-rds-instances-over-self-managed-databases.md)[与自建数据库对比优势](competitive-advantages-of-apsaradb-rds-instances-over-self-managed-databases.md)。
