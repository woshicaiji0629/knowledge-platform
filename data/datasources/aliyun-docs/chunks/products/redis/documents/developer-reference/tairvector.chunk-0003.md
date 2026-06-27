## 注意事项
操作对象为Tair实例中的TairVector数据。
TairVector数据结构的index_name、Key等暂不支持Redis的Hashtags特性。
TairVector暂不支持MOVE等特性。
若业务场景对数据持久化要求较高，建议开启[半同步模式](../user-guide/modify-the-synchronization-mode-of-a-persistent-memory-optimized-instance.md)。
