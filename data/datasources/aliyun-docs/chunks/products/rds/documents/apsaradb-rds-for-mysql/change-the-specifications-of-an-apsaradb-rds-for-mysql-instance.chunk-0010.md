### 配置升级影响
Q：CPU、内存、磁盘同时升配，会导致多长时间的服务不可用？
A：无论单项目或多项目升配，不可用时间均为分钟级。升配过程中，可能会出现实例切换或实例重启，而且与数据库、账号、网络等相关的大部分操作都无法执行，请在可维护时间段内执行变配操作。各变更项的业务影响，请参见[变更项业务影响](change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。
Q：变配时长受哪些因素影响？
A：请参见[RDS MySQL](../support/which-factors-affect-the-time-that-is-required-to-change-the-specifications-of-my-apsaradb-rds-for-mysql-instance.md)[实例变配时长受哪些因素影响](../support/which-factors-affect-the-time-that-is-required-to-change-the-specifications-of-my-apsaradb-rds-for-mysql-instance.md)。
Q：变更配置会影响线上业务吗？
A：请参见本文[影响](change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。
