### 插件查询与限制
查询可用插件：在数据库中执行SELECT * FROM pg_available_extensions;可获取当前实例所有可用插件的完整列表。
安全限制：为了规范插件管理，提升RDS PostgreSQL在插件侧的安全防护，RDS在内核版本迭代中陆续对部分存在安全风险的插件进行优化，因此，部分插件在某些内核版本中无法新创建，已创建的插件使用不受影响。更多信息，请参见[限制创建插件说明](limits-on-the-creation-of-the-pg-cron-extension.md)。
