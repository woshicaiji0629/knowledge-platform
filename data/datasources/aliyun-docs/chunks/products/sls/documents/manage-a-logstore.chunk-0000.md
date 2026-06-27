### 什么是LogStore
日志库（LogStore）是日志服务的数据容器。一个[Project（项目）](manage-a-project.md)下可以创建多个LogStore，用于隔离和管理不同业务或来源的日志。
此外，部分云产品或SLS自身功能也会自动创建专用的LogStore，这些LogStore有特定用途，不支持写入其他数据。例如：
internal-operation_log：用于存储日志服务自身的[详细操作日志](manage-service-logs.md)。
oss-log-store：在配置[OSS](usage-notes-of-oss-access-log.md)[访问日志](usage-notes-of-oss-access-log.md)转存时，自动创建的专属LogStore。
