## 附录2：增量迁移时支持的SQL操作

| 操作类型 | SQL 操作语句 |
| --- | --- |
| DML | INSERT、UPDATE、DELETE |
| DDL | ALTER TABLE、ALTER VIEW CREATE FUNCTION、CREATE INDEX、CREATE PROCEDURE、CREATE TABLE、CREATE VIEW DROP INDEX、DROP TABLE RENAME TABLE 重要 RENAME TABLE 操作可能导致迁移数据不一致。例如迁移对象只包含某个表，如果迁移过程中源实例对该表执行了重命名操作，那么该表的数据将不会迁移到目标库。为避免该问题，您可以在数据迁移配置时将该表所属的整个数据库作为迁移对象，且确保 RENAME TABLE 操作前后的表所属的数据库均在迁移对象中。 TRUNCATE TABLE |
