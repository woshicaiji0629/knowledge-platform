### Tair-Binlog
Tair（企业版）内存型不仅支持上述两种持久化策略，还优化了基于AOF（Append-only-file）的持久化机制，实现AOF增量归档，避免了AOF Rewrite对服务性能的影响，同时完整保留了每一次写操作与其时间戳，可以将实例整体或指定Key的数据恢复至某个秒级的时间点（PITR，point-in-time recovery）。更多信息，请参见[通过数据闪回按时间点恢复数据](use-data-flashback-to-restore-data-by-point-in-time.md)。
