### 预加载配置
部分插件在使用前，必须将其名称添加至数据库参数shared_preload_libraries中，否则创建（CREATE EXTENSION）时会失败。修改shared_preload_libraries参数的方法，请参见[设置实例参数](modify-the-parameters-of-an-apsaradb-rds-for-postgresql-instance.md)。
需要预加载的插件列表如下：
性能监控：pg_stat_statements、auto_explain、pg_prewarm
安全审计：auth_delay、passwordcheck、pgaudit
分区管理：pg_pathman
逻辑复制：pglogical
全文搜索：pg_bigm、zhparser、pg_jieba
任务调度：pg_cron
查询优化：pg_hint_plan
数据压缩：pg_squeeze
时序数据：timescaledb
查询加速：rds_duckdb
Oracle兼容：orafce
调试工具：pldebugger（参数值需配置为plugin_debugger）
