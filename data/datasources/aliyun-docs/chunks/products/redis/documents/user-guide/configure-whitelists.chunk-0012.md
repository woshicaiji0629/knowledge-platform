### 实例里自动生成的白名单分组，它们的来源是什么？可以删除吗？
初始情况下，实例的白名单分组仅包含default，随着对实例执行某些操作，白名单分组会逐渐增多，详情请参见下表。

| 白名单分组名称 | 来源说明 |
| --- | --- |
| default | 系统默认的白名单分组，不可删除。 |
| ali_dms_group | 通过 DMS 登录实例时，DMS 自动创建的白名单分组。具体操作，请参见 [通过](log-on-to-an-apsaradb-for-redis-instance-by-using-dms.md) [DMS](log-on-to-an-apsaradb-for-redis-instance-by-using-dms.md) [连接实例](log-on-to-an-apsaradb-for-redis-instance-by-using-dms.md) 。请勿删除或修改该白名单分组，否则可能导致无法通过 DMS 登录实例。 |
| hdm_security_ips | 使用 CloudDBA 相关功能时（例如 [离线全量](offline-key-analysis.md) [Key](offline-key-analysis.md) [分析](offline-key-analysis.md) ），DAS 自动创建的白名单分组。请勿删除或修改该白名单分组，否则可能导致 CloudDBA 功能使用异常。 |
