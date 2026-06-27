## 现象说明
实例基本信息页实例运行状态为锁定中。
实例为锁定中时，无法INSERT和UPDATE数据。
说明
以RDS MySQL 5.6、5.7、8.0中20190815及之后的小版本为例，实例的锁定状态有以下三种：
LOCK_WRITE_GROWTH：禁止磁盘增长锁，一般由于主实例磁盘满，禁止会使磁盘用量上升的操作。DELETE语句会产生大量binlog，会导致磁盘用量上升，如需清理数据，可使用DROP和TRUNCATE语句。
LOCK_READ：禁读锁，一般由于只读实例磁盘满，禁止执行查询和写入。
LOCK_WRITE：禁写锁，可能是由于实例过期、主机过期（仅MyBase产品有的状态）、实例迁移等产生，除LOCK_WRITE_GROWTH限制外，额外禁止了其他数据写入，如DROP和TRUNCATE等。
在实例锁定时，执行部分SQL语句会报ERROR 1290 (HY000): The MySQL server is running with the LOCK_WRITE_GROWTH option so it cannot execute this statement的错误提示。
对于RDS MySQL 5.1、5.5所有小版本以及5.6、5.7、8.0中20190815之前的小版本，各种原因导致实例一旦被锁定，锁定后将无法进行任何操作。
