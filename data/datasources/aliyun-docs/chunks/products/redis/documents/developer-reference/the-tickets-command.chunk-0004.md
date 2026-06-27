## 注意事项
操作对象为Tair实例中的TairTS数据。
TairTS的优势为实时、高并发的写入与查询性能，缺陷为存储容量有限，请合理设置TTL，及时淘汰过期数据。
重要
Breaking Change公告：
2024年07月22日发布Tair内存型（兼容Redis 6.0）24.7.0.0版本，该版本中新增了ts-auto-del-empty-skey-enable参数，默认为yes，表示当Skey中的所有数据点都过期时，会自动删除Skey。但在Tair内存型（兼容Redis 6.0）24.7.0.0之前的版本中，默认不会删除数据点已过期的Skey。
在Tair内存型（兼容Redis 6.0）实例使用TairTS前，建议将实例升级至24.7.0.0及以上版本，并确认、手动调整ts-auto-del-empty-skey-enable参数的策略，避免因默认行为的改变对业务产生影响。
