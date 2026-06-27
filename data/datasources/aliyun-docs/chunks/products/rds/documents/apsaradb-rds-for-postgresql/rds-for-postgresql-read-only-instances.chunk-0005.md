## 常见问题
Q：只读实例的计费方式可以转化吗？
A：可以。具体操作，请参见[按量付费转包年包月](switch-an-apsaradb-rds-for-postgresql-instance-from-pay-as-you-go-to-subscription.md)或[包年包月转按量付费](package-year-package-month-to-pay-by-volume.md)。
Q：变更只读实例的配置、释放只读实例、转化只读实例计费方式会影响主实例吗？
A：不会。
Q：主实例上创建的账号在只读实例上可以用吗？
A：主实例创建的账号会同步到只读实例，只读实例无法管理账号。账号在只读实例上只能进行读操作，不能进行写操作。
Q：只读实例可以转变为常规实例吗？比如作为容灾实例？
A：暂不支持。
Q：能否对只读实例的数据进行备份？实例的自动备份能否在只读实例上进行？
A：无需对只读实例进行备份，备份在主实例上进行，由于RDS PostgreSQL的备份使用快照备份，对主实例没有性能开销。
Q：只读实例是否支持并行复制？
A：RDS PostgreSQL采用的是物理流复制，基于WAL日志文件同步加回放来实现数据复制能力，效率高，无需使用并行复制。
Q：事务日志的清除机制是怎样的？
A：RDS PostgreSQL的WAL日志备份完成后，由内核在Checkpoint操作中自动清理。
Q：如何通过只读实例延迟时间判断复制是否正常？
A：通常情况下只读实例延迟时间在1秒以内，如果超过1秒，说明数据同步延迟，极端场景下也可能出现断开的场景。
Q：复制延迟通常是什么原因引起的？
A：常见原因及解决办法如下：
原因1：主实例规格大，只读实例规格过小，导致主备延迟过大。
解决方法：升级只读实例规格，更多信息，请参见[变更配置](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)。
原因2：参数max_standby_streaming_delay设置不合理，导致复制延迟较高。参数设置方法，请参见[设置实例参数](modify-the-parameters-of-an-apsaradb-rds-for-postgresql-instance.md)。
解决办法：调整参数max_standby_streaming_delay取值：
该值设置较小时可以减少只读实例与主实例之间数据复制延迟，但过小时可能会导致只读实例的事务被取消。
该值设置过大时可能会造成复制延迟。
该文章对您有帮助吗？
反馈
