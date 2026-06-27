## 功能特点
地域和可用区：与主实例在同一地域，可以在不同的可用区。
[更改网络类型](change-the-network-type-of-an-apsaradb-rds-for-postgresql-instance.md)：可以与主实例不一致。
账号与数据库管理：不需要维护账号与数据库，全部通过主实例同步。
白名单：只读实例创建时会自动复制其主实例的白名单信息，但两者白名单相互独立。若您需要修改只读实例的白名单，请参见[设置白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance.md)。
监控与报警：提供系统性能指标的监控视图，如磁盘容量、IOPS、连接数、CPU使用率等。
自动读写分离：配合主实例数据库代理功能，可使写请求自动转发到主实例，读请求自动转发到各个只读实例，实现读写请求的自动分流，减轻主实例的压力。若您需要为主实例开通数据库代理功能，请参见[什么是数据库代理](what-are-database-proxies.md)。
只读实例的数量：云盘主实例最多创建32个只读实例，高性能本地盘主实例最多创建5个只读实例。
