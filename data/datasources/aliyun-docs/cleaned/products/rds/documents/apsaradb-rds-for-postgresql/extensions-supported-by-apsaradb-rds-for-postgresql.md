# RDS PostgreSQL支持的插件-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/extensions-supported-by-apsaradb-rds-for-postgresql

# 支持插件列表
RDS PostgreSQL各版本支持的扩展插件及版本信息，帮助您快速确定实例对各插件的支持情况并选择合适的扩展功能。
加入RDS PostgreSQL插件交流钉钉群（103525002795），获取更多关于插件的信息，进行咨询、交流和反馈。
## 使用说明
在使用RDS PostgreSQL扩展插件前，请阅读以下兼容性要求、配置方法和查询限制，确保插件能够正确安装和使用。
### 版本兼容性
内核版本依赖：插件的支持情况与内核版本密切相关。如果实例当前支持的插件与本文列表不符，请将实例升级至最新的[内核小版本](update-the-minor-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md)。
规格差异：不同规格（标准版、倚天版）的实例支持的插件列表存在差异。详情请参考本文中对应规格的标签页。
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
### 插件查询与限制
查询可用插件：在数据库中执行SELECT * FROM pg_available_extensions;可获取当前实例所有可用插件的完整列表。
安全限制：为了规范插件管理，提升RDS PostgreSQL在插件侧的安全防护，RDS在内核版本迭代中陆续对部分存在安全风险的插件进行优化，因此，部分插件在某些内核版本中无法新创建，已创建的插件使用不受影响。更多信息，请参见[限制创建插件说明](limits-on-the-creation-of-the-pg-cron-extension.md)。
## 插件支持列表
## 标准版规格
| 插件名 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 11 | 10 | 描述 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [rds_online_migrate](use-the-rds-online-migrate-extension-to-partition-tables-online.md) | 无 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 无 | 无 | 无 | 提供在线分区功能。 |
| [pgroonga](https://github.com/pgroonga/pgroonga) | 4.0.5 | 4.0.4 | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 为 PostgreSQL 提供全文检索功能。 |
| [pg_textsearch](https://github.com/timescale/pg_textsearch) | 1.0.0 | 1.0.0 | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 提供高级全文检索功能。 |
| [clickhouse_fdw](https://github.com/ildus/clickhouse_fdw) | 无 | 1.4 | 1.4 | 1.4 | 1.4 | 1.4 | 无 | 无 | 无 | 让 PostgreSQL 可以直接查询 ClickHouse 数据库中的数据，就像查询本地表一样。 |
| [pg_permissions](https://github.com/cybertec-postgresql/pg_permissions) | 无 | 1.4 | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 用来查看和审计 PostgreSQL 数据库中所有对象（表、视图、函数等）的权限设置，方便进行权限管理和安全审计。 |
| [address_standardizer](https://postgis.net/docs/standardize_address.html) | 无 | 3.3.7 | 3.3.4 | 3.3.2 | 3.1.4 | 3.1.4 | 3.1.4 | 3.1.4 | 3.1.4 | 基于 [PAGC](http://www.pagcgeo.org/docs/html/pagc-11.html) 标准的地名标准化插件。 |
| [address_standardizer_data_us](https://postgis.net/docs/standardize_address.html) | 无 | 3.3.7 | 3.3.4 | 3.3.2 | 3.1.4 | 3.1.4 | 3.1.4 | 3.1.4 | 3.1.4 | 基于 [PAGC](http://www.pagcgeo.org/docs/html/pagc-11.html) 标准的地名标准化（美国）数据插件。 |
| [aggs_for_arrays](https://github.com/pjungwir/aggs_for_arrays/) | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 1.3.1 | 提供计算数字数组的统计信息的扩展函数。 |
| [age](https://github.com/apache/age) | 1.6.0 | 1.6.0 | 1.6.0 | 1.6.0 | 1.6.0 | 无 | 无 | 无 | 无 | 为 PostgreSQL 提供图形数据库功能。 |
| [bloom](https://www.postgresql.org/docs/14/bloom.html) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 提供一种基于布鲁姆过滤器的索引访问方法。 |
| [btree_gin](https://www.postgresql.org/docs/14/btree-gin.html) | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 1.2 | 提供一个为多种数据类型和所有 enum 类型实现 B 树等价行为的 GIN 操作符类示例。 |
| [btree_gist](https://www.postgresql.org/docs/14/btree-gist.html) | 1.8 | 1.7 | 1.7 | 1.7 | 1.6 | 1.5 | 1.5 | 1.5 | 1.5 | 提供一个为多种数据类型和所有 enum 类型实现 B 树等价行为的 GiST 操作符类示例。 |
| [chkpass](https://www.postgresql.org/docs/10/chkpass.html) | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 1.0 | 实现了一种数据类型，用来存储加密的口令。 |
| [citext](https://www.postgresql.org/docs/14/citext.html) | 1.8 | 1.6 | 1.6 | 1.6 | 1.6 | 1.6 | 1.6 | 1.5 | 1.4 | 提供一种大小写不敏感的字符串类型。 |
| [cube](https://www.postgresql.org/docs/14/cube.html) | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 1.4 | 1.4 | 1.4 | 1.2 | 提供一种数据类型来表示多维立方体。 |
| [dblink](use-the-dblink-and-postgres-fdw-extensions-for-cross-database-operations.md) | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 跨库操作表。 |
| [decoderbufs](https://github.com/debezium/postgres-decoderbufs) | 无 | 无 | 无 | 无 | 无 | 0.1.0 | 0.1.0 | 0.1.0 | 0.1.0 | 根据 Protocol Buffers 协议、输出能够适配 [Debezium](http://debezium.io) 平台的数据。 |
| [dict_int](https://www.postgresql.org/docs/14/dict-int.html) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 附加全文搜索词典模板的示例。 |
| [earthdistance](https://www.postgresql.org/docs/14/earthdistance.html) | 1.2 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 提供两种不同的方法来计算地球表面的大圆距离。 |
| [encdb](fully-encrypted-database.md) | 无 | 1.1.14 | 1.1.14 | 1.1.14 | 1.1.14 | 1.1.14 | 1.1.14 | 1.1.14 | 1.1.13 | 提供全密态数据库功能。 |
| [encdb_btree](use-encdb-btree-to-facilitate-operations-on-ciphertext-indexes.md) | 无 | 1.0.0 | 1.0.0 | 1.0.0 | 1.0.0 | 1.0.0 | 1.0.0 | 1.0.0 | 1.0.0 | 用于在全密态数据库上加速密文查询。 |
| [fuzzystrmatch](use-the-fuzzystrmatch-extension-to-calculate-the-similarity-between-strings.md) | 1.2 | 1.2 | 1.2 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 判断字符串之间的相似性和距离。 |
| [ganos_address_standardizer](https://postgis.net/docs/standardize_address.html) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 6.9 | 6.3 | 6.3 | 基于 [PAGC](http://www.pagcgeo.org/docs/html/pagc-11.html) 标准的地名标准化插件。 |
| [ganos_address_standardizer_data_us](https://postgis.net/docs/standardize_address.html) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 6.9 | 6.3 | 6.3 | 基于 [PAGC](http://www.pagcgeo.org/docs/html/pagc-11.html) 标准的地名标准化美国部分数据插件。 |
| [ganos_geometry](geometry-model.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 6.9 | 6.3 | 6.3 | 提供空间几何类型的计算分析功能。 |
| [ganos_geometry_pyramid](data-and-hardware-requirements.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 6.9 | 6.3 | 6.3 | 用于二维空间几何大数据的快速显示。 |
| [ganos_geometry_sfcgal](data-and-hardware-requirements.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 6.9 | 6.3 | 6.3 | 提供空间几何 SFCGAL 插件扩展功能。 |
| [ganos_geometry_topology](data-and-hardware-requirements.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 6.9 | 6.3 | 6.3 | 提供空间几何类型的计算分析功能。 |
| [ganos_geomgrid](geomgrid-sql-reference.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 6.9 | 6.3 | 6.3 | 提供 H3、GeoSOT 等网格剖分、编码、索引及分析能力。 |
| [ganos_networking](path-model.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 6.9 | 6.3 | 6.3 | 提供空间几何网络类型的计算分析功能。 |
| [ganos_pointcloud](point-cloud-model.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 6.9 | 6.3 | 6.3 | 提供点云的存储、计算分析功能。 |
| [ganos_pointcloud_geometry](point-cloud-model.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 6.9 | 6.3 | 6.3 | 提供点云的存储、计算分析功能。 |
| [ganos_raster](terms-1.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 6.9 | 6.3 | 6.3 | 提供空间栅格数据的存储、计算分析功能。 |
| [ganos_spatialref](st-srequal.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 6.9 | 6.3 | 6.3 | 提供空间参考的计算分析功能。 |
| [ganos_tiger_geocoder](https://postgis.net/docs/Extras.html) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 6.9 | 6.3 | 6.3 | 提供 USCB Tiger 数据类型支持。 |
| [ganos_trajectory](basic-concepts.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 6.9 | 6.3 | 6.3 | Ganos 移动对象（MOD）数据计算分析功能。 |
| [hll](use-the-hll-plug-in.md) | 2.18 | 2.19 | 2.18 | 2.18 | 2.18 | 2.15 | 2.14 | 2.14 | 无 | 快速预估 PV、UV 等业务指标。 |
| [hstore](https://www.postgresql.org/docs/14/hstore.html) | 1.8 | 1.8 | 1.8 | 1.8 | 1.8 | 1.7 | 1.6 | 1.5 | 1.4 | 在单一 PostgreSQL 实例中存储键值对。 |
| [hypopg](use-the-hypopg-extension-to-create-hypothetical-indexes.md) | 1.4.2 | 1.4.1 | 1.4.1 | 1.4.1 | 1.4.1 | 1.3.1 | 1.3.1 | 1.3.1 | 1.3.1 | 创建虚拟索引。 |
| [h3](https://github.com/uber/h3) | 无 | 4.2.3 | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 提供 Uber 的 H3 六边形层次空间索引功能。 |
| [index_adviser](using-the-index-adviser-extension-on-an-apsaradb-rds-for-postgresql-instance.md) | 无 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 提供索引推荐。 |
| [intagg](https://www.postgresql.org/docs/14/intagg.html) | 无 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 提供一个整数聚集器和一个枚举器。 |
| [intarray](https://www.postgresql.org/docs/14/intarray.html) | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 1.3 | 1.2 | 1.2 | 1.2 | 提供一些有用的函数和操作符来操纵不含空值的整数数组。 |
| [ip4r](https://github.com/RhodiumToad/ip4r) | 2.4 | 2.4 | 2.4 | 2.4 | 2.4 | 2.4 | 无 | 无 | 无 | 使 PostgreSQL 支持 IP 地址范围类型。 |
| [isn](https://www.postgresql.org/docs/14/isn.html) | 1.3 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.1 | 按照一个硬编码的前缀列表对输入进行验证，也被用来在输出时连接号码。 |
| [ltree](https://www.postgresql.org/docs/14/ltree.html) | 1.3 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.1 | 1.1 | 1.1 | 用于表示存储在一个层次树状结构中的数据的标签。 |
| [log_fdw](use-the-log-fdw-extension-to-query-logs.md) | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 1.0 | 无 | 查询数据库日志。 |
| [mysql_fdw](use-the-mysql-fdw-extension-to-read-data-from-and-write-data-to-a-mysql-database.md) | 无 | 2.9.2 | 1.2 | 1.2 | 1.2 | 1.1 | 1.1 | 1.1 | 1.1 | 读写 RDS MySQL 实例或自建 MySQL 数据库里的数据。 |
| [oracle_fdw](use-the-oracle-fdw-plug-in.md) | 无 | 无 | 无 | 无 | 无 | 无 | 1.1 | 无 | 无 | 支持对 PostgreSQL 表同步更新 Oracle 数据库中的表。 |
| [orafce](https://github.com/orafce/orafce) | 4.15 | 无 | 4.9.2 | 4.9.2 | 4.9.2 | 无 | 无 | 3.8 | 3.6 | 提供一系列 Oracle 兼容函数。 |
| [oss_fdw](use-the-oss-fdw-extension-to-read-and-write-foreign-data-text-files.md) | 无 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 读写 OSS 里的数据。 |
| [pase](use-pase-for-efficient-vector-search.md) | 无 | 无 | 0.0.1 | 0.0.1 | 0.0.1 | 0.0.1 | 0.0.1 | 0.0.1 | 无 | 高效向量检索。 |
| [pg_bigm](use-the-pg-bigm-extension-to-perform-fuzzy-match-based-queries.md) | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 创建一个二元语法（2-gram）的 GIN 索引来加速全文搜索过程。 |
| [pg_buffercache](https://www.postgresql.org/docs/14/pgbuffercache.html) | 1.6 | 1.4 | 1.4 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 提供一种方法实时检查共享缓冲区。 |
| [pg_concurrency_control](use-the-pg-concurrency-control-plug-in.md) | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 1.0 | 1.0 | 用于对 SQL 进行并发控制。 |
| [pg_cron](use-the-pg-cron-extension-to-configure-scheduled-tasks.md) | 1.6 | 1.6 | 1.6 | 1.6 | 1.6 | 1.5 | 1.1 | 1.1 | 1.1 | 设置定时任务。 |
| [pg_freespacemap](https://www.postgresql.org/docs/14/pgfreespacemap.html) | 1.3 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 检查空闲空间映射（FSM）。 |
| [pg_jieba](use-the-pg-jieba-extension-on-an-apsaradb-rds-for-postgresql-instance.md) | 1.2.0 | 1.2.0 | 1.2.0 | 1.2.0 | 1.2.0 | 1.1.0 | 1.1.0 | 1.1.0 | 1.1.0 | 对中文全文实现分词。 |
| [pg_hint_plan](use-the-pg-hint-plan-extension-to-customize-query-plans.md) | 1.8.0 | 1.7.0 | 1.6.1 | 1.5.2 | 1.4.3 | 1.3.9 | 1.3.9 | 1.3.9 | 1.3.0 | 通过特殊的注释语句提示，使 PostgreSQL 改变其既定的执行计划。 |
| [pg_partman](https://github.com/pgpartman/pg_partman) | 5.2.4 | 5.2.4 | 5.1.0 | 5.1.0 | 5.1.0 | 4.7.3 | 4.7.3 | 无 | 无 | 创建和管理基于时间和基于序列的表分区集。 |
| [pg_pathman](https://help.aliyun.com/zh/polardb/polardb-for-postgresql/pg-pathman-usage#task-2311142) | 无 | 无 | 无 | 无 | 无 | 1.5 | 1.5 | 1.5 | 1.5 | 高性能分区表插件。 |
| [pg_prewarm](https://www.postgresql.org/docs/14/pgprewarm.html) | 1.2 | 无 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.1 | 提供一种方便的方法把数据载入到操作系统缓冲区或者 PostgreSQL 缓冲区。 |
| [pg_profile](use-the-pg-profile-extension-to-collect-statistics-on-resource-intensive-activities.md) | 无 | 无 | 4.4 | 4.4 | 4.4 | 4.1 | 4.1 | 4.1 | 4.1 | 资源密集活动统计。 |
| [pg_proctab](https://gitlab.com/pg_proctab/pg_proctab/-/blob/main/doc/README.pg_proctab?ref_type=heads) | 无 | 0.0.13 | 0.0.10 | 0.0.10 | 0.0.10 | 0.0.10 | 0.0.10 | 0.0.10 | 无 | 允许用户通过 SQL 查询的方式，访问操作系统层面的进程和系统资源消耗数据。 |
| [pg_repack](use-the-pg-repack-extension-to-clear-tablespaces.md) | 无 | 1.5.1 | 1.5.0 | 1.5.0 | 1.5.0 | 1.4.6 | 1.4.6 | 1.4.6 | 1.4.6 | 在线清理表空间功能。 |
| [pg_sphere](https://postgrespro.github.io/pgsphere/) | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 1.0 | 提供 PostgreSQL 的球面的数据类型、函数、运算符和索引。 |
| [pg_stat_kcache](use-the-pg-stat-kcache-extension-to-collect-statistics-on-system-read-and-write-operations.md) | 无 | 2.3.0 | 2.2.3 | 2.2.3 | 2.2.3 | 2.2.1 | 2.2.1 | 2.2.1 | 2.2.1 | 系统读写信息统计。 |
| [pg_stat_statements](https://www.postgresql.org/docs/14/pgstatstatements.html) | 1.12 | 1.10 | 1.10 | 1.10 | 1.9 | 1.8 | 1.7 | 1.6 | 1.6 | 提供一种方法追踪服务器执行的所有 SQL 语句的执行统计信息。 |
| [pg_trgm](https://www.postgresql.org/docs/14/pgtrgm.html) | 1.6 | 1.6 | 1.6 | 1.6 | 1.6 | 1.5 | 1.4 | 1.4 | 1.3 | 提供字母数字文本相似度的函数和操作符，以及支持快速搜索相似字符串的索引操作符类。 |
| [pg_squeeze](shrink-inflate-tables-and-indexes-pg-squeeze.md) | 1.8 | 1.7 | 1.6 | 1.6 | 1.6 | 1.6 | 1.6 | 1.6 | 无 | 在线收缩膨胀表和索引。 |
| [pg_wait_sampling](https://github.com/postgrespro/pg_wait_sampling) | 1.1 | 1.1 | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 用于监控和分析数据库的等待状态。 |
| [pgaudit](use-the-pgaudit-extension-to-generate-audit-logs.md) | 无 | 17.0 | 16.0 | 1.6.1 | 1.6.1 | 1.5 | 1.4.1 | 1.3.2 | 1.2.2 | 提供详细的会话和对象审计日志记录。 |
| [pgcrypto](https://www.postgresql.org/docs/14/pgcrypto.html) | 1.4 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 为 PostgreSQL 提供了密码函数。 |
| [pgl_ddl_deploy](https://github.com/enova/pgl_ddl_deploy) | 无 | 无 | 2.2 | 2.2 | 2.2 | 2.1 | 无 | 无 | 无 | 使 PostgreSQL 支持透明逻辑 DDL 复制。 |
| [pglogical](use-the-pglogical-extension-for-logical-streaming-replication.md) | 2.4.6 | 2.4.5 | 2.4.5 | 2.4.4 | 2.4.4 | 2.4.2 | 2.4.2 | 2.4.0 | 2.4.0 | 提供逻辑流复制发布和订阅的功能。 |
| [pgrouting](https://docs.pgrouting.org/) | 无 | 3.4.2 | 3.4.2 | 3.4.2 | 3.4.2 | 3.4.2 | 3.4.2 | 3.4.2 | 3.4.2 | 提供空间几何网络的计算分析功能。 |
| [pgrowlocks](https://www.postgresql.org/docs/14/pgrowlocks.html) | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 提供一个函数来显示指定表的行锁定信息。 |
| [pgsql-gzip](https://github.com/pramsey/pgsql-gzip) | 1.0 | 1.0.0 | 1.0.0 | 无 | 无 | 无 | 无 | 无 | 无 | 在 PostgreSQL 数据库中实现数据的 Gzip 压缩和解压缩功能。 |
| [pgsql-http](https://github.com/pramsey/pgsql-http) | 1.6 | 1.6 | 1.6 | 无 | 无 | 无 | 无 | 无 | 无 | 允许用户在 PostgreSQL 数据库中直接发起 HTTP 请求。 |
| [pgstattuple](https://www.postgresql.org/docs/14/pgstattuple.html) | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 提供多种函数来获得元组层的统计信息。 |
| [pgvector](pgvector-use-guide.md) | 0.8.1 | 0.8.0 | 0.8.0 | 0.8.0 | 0.8.0 | 无 | 无 | 无 | 无 | 高维向量相似度搜索插件。 |
| [pldebugger](use-the-pldebugger-extension-to-debug-stored-procedures.md) | 无 | 1.8 | 1.8 | 1.8 | 1.8 | 1.1 | 1.1 | 1.1 | 1.1 | 存储过程调试插件。 |
| [plperl](https://www.postgresql.org/docs/14/plperl.html) | 无 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 提供 Perl 过程语言。 |
| [plpgsql](https://www.postgresql.org/docs/14/plpgsql.html) | 无 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 提供 SQL 过程语言。 |
| [plproxy](use-the-pl-or-proxy-plug-in-for-horizontal-sharding.md) | 2.11.0 | 无 | 2.11.0 | 2.10.0 | 2.10.0 | 2.10.0 | 2.9.0 | 2.9.0 | 2.8.0 | 包含 CLUSTER 模式和 CONNECT 模式，可以帮助您用不同方式访问数据库。 |
| [pltcl](https://www.postgresql.org/docs/14/pltcl.html) | 无 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 提供 tcl 过程语言。 |
| [plv8](https://plv8.github.io/) | 无 | 无 | 无 | 无 | 2.3.15 | 2.3.15 | 2.3.15 | 2.3.15 | 2.3.15 | 可信 JavaScript 语言扩展。 |
| [postgis](https://postgis.net/docs/) | 3.3.7 | 3.3.7 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.2 | PostGIS 空间地理信息相关扩展。 |
| [postgis_sfcgal](https://postgis.net/docs/reference.html#reference_sfcgal) | 3.3.7 | 3.3.7 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.2 | PostGIS SFCGAL 空间地理信息相关扩展。 |
| [postgis_tiger_geocoder](https://postgis.net/docs/Extras.html) | 3.3.7 | 3.3.7 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.2 | PostGIS TIGER 数据空间地理信息相关扩展。 |
| [postgis_topology](https://postgis.net/docs/Topology.html) | 3.3.7 | 3.3.7 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.2 | PostGIS 拓扑数据空间地理信息相关扩展。 |
| [postgres_fdw](use-the-dblink-and-postgres-fdw-extensions-for-cross-database-operations.md) | 1.2 | 1.1 | 1.1 | 1.1 | 1.1 | 1.0 | 1.0 | 1.0 | 1.0 | 跨库操作表。 |
| [postgresql_anonymizer](https://gitlab.com/dalibo/postgresql_anonymizer/) | 无 | 1.1.0 | 无 | 1.1.0 | 1.1.0 | 无 | 无 | 无 | 无 | 对数据库中的敏感数据进行匿名化或脱敏处理。 |
| [q3c](https://github.com/segasai/q3c) | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 1.5.0 | 用于在球体上进行空间索引。 |
| [rdkit](use-the-rdkit-plug-in.md) | 无 | 无 | 无 | 无 | 无 | 无 | 3.8 | 无 | 无 | 支持化学分子计算、化学分子检索等功能。 |
| [rds_ai](ai-rds-ai.md) | 1.0 | 1.0.0 | 1.0.0 | 1.0.0 | 1.0.0 | 无 | 无 | 无 | 无 | 集成了阿里云百炼的先进模型，包括千问、通用文本向量 和通用文本排序 等。通过该插件，您可以在 RDS PostgreSQL 数据库中轻松实现包括大模型问答、文本向量转换、 文本排序、 Top N 相似向量检索以及 RAG 问答等多种应用场景。 |
| [rds_ccl](use-the-rds-ccl-extension-to-perform-sql-throttling-on-an-apsaradb-rds-for-postgresql-instance.md) | 1.3 | 1.2 | 1.2 | 1.2 | 1.2 | 无 | 无 | 无 | 无 | 支持 SQL 限流。 |
| [rds_duckdb](how-to-use-duckdb-to-speed-up-queries.md) | 1.3.2.3 | 1.1 | 1.2 | 1.3 | 1.1 | 1.1 | 1.1 | 无 | 无 | 复杂查询加速。 |
| [rds_embedding](rds-embedding.md) | 无 | 1.0 | 1.0 | 1.0 | 1.0 | 无 | 无 | 无 | 无 | 提供自定义模型配置、模型调用的能力，可以在数据库端实现文本到向量的转换。 |
| [rds_encdb](use-the-rds-encdb-extension-to-encrypt-sensitive-columns.md) | 无 | 无 | 1.0 | 无 | 无 | 无 | 无 | 无 | 无 | 用于对查询结果集的敏感列进行加密。同时，通过对数据库账户权限进行设置，相关账户在访问敏感列信息时，仅能获得密文格式的查询结果。 |
| [rds_online_ddl](use-the-rds-online-ddl-extension-to-modify-column-data-type-online.md) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 无 | 无 | 支持在线修改列类型，在不影响业务连续性的前提下完成表结构变更。 |
| [rds_tde_utils](use-the-rds-tde-utils-extension-to-encrypt-and-decrypt-multiple-data-records-at-a-time.md) | 1.1 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | TDE 批量加解密插件。 |
| [roaringbitmap](use-the-roaringbitmap-extension.md) | 0.5.4 | 0.5.4 | 0.5.4 | 0.5 | 0.5 | 0.5 | 0.5 | 无 | 无 | 使用位图功能，提高查询性能。 |
| [rum](use-the-rum-extension.md) | 1.3.15 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 高速全文检索。 |
| [sequential-uuids](use-the-sequential-uuids-extension-to-generate-sequential-uuids.md) | 1.0.3 | 无 | 1.0.2 | 1.0.2 | 1.0.2 | 1.0.2 | 1.0.2 | 1.0.2 | 1.0.2 | 具有顺序模式的 UUID 生成器。 |
| [smlar](use-the-smlar-plug-in.md) | 无 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 计算两个相同类型数组的相似度。 |
| [snowflake](https://github.com/pgEdge/snowflake) | 2.2 | 2.2 | 2.2 | 2.2 | 无 | 无 | 无 | 无 | 无 | 提供了一种基于 int8 和序列的唯一 ID 解决方案，以选择性替代 PostgreSQL 内置的 bigserial 数据类型。 |
| [sslinfo](https://www.postgresql.org/docs/14/sslinfo.html) | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 提供当前客户端提供的 SSL 证书的有关信息。 |
| [tablefunc](https://www.postgresql.org/docs/14/tablefunc.html) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 包括多个返回表的函数。 |
| [tds_fdw](use-the-tds-fdw-extension-to-query-data-of-sql-server-instances.md) | 无 | 2.0.4 | 2.0.3 | 2.0.3 | 2.0.3 | 2.0.3 | 2.0.3 | 2.0.3 | 无 | 查询其他类型数据库的数据。 |
| [timescaledb](use-the-timescaledb-extension.md) | 无 | 2.24.0 | 2.24.0 | 2.9.2 | 2.9.2 | 2.5.0 | 1.7.1 | 1.7.1 | 1.3.0 | 支持时序数据的自动分片、高效写入、检索、准实时聚合等。 |
| [tsm_system_rows](https://www.postgresql.org/docs/14/tsm-system-rows.html) | 1.0 | 无 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 提供表采样方法 SYSTEM_ROWS。 |
| [tsm_system_time](https://www.postgresql.org/docs/14/tsm-system-time.html) | 1.0 | 无 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 提供了表采样方法 SYSTEM_TIME。 |
| [unaccent](https://www.postgresql.org/docs/14/unaccent.html) | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 文本搜索字典，它能从词位中移除重音（附加符号）。 |
| [uuid-ossp](https://www.postgresql.org/docs/14/uuid-ossp.html) | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 提供函数使用几种标准算法之一产生通用唯一标识符（UUID）。 |
| [varbitx](use-the-varbitx-plug-in.md) | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 1.0 | 1.0 | 支持多种 BIT 操作。 |
| [wal2json](use-the-wal2json-extension.md) | 2.6 | 2.6 | 2.6 | 2.6 | 2.6 | 2.3 | 2.3 | 2.2 | 2.2 | 将逻辑日志文件输出为 JSON 格式。 |
| [xml2](https://www.postgresql.org/docs/14/xml2.html) | 1.2 | 无 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 提供 XPath 查询和 XSLT 功能。 |
| [zhparser](use-the-zhparser-extension-to-segment-chinese-text.md) | 2.1 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 中文全文搜索。 |
| [zombodb](use-the-zombodb-extension-to-integrate-with-elasticsearch.md) | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 4.0 | 无 | 强大的文本索引和分析功能。 |
## 倚天版规格
| 插件名 | 18 | 17 | 16 | 15 | 14 | 13 | 描述 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [rds_online_migrate](use-the-rds-online-migrate-extension-to-partition-tables-online.md) | 无 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 提供在线分区功能 |
| [pgroonga](https://github.com/pgroonga/pgroonga) | 无 | 4.0.4 | 无 | 无 | 无 | 无 | 为 PostgreSQL 提供全文检索功能。 |
| [pg_textsearch](https://github.com/timescale/pg_textsearch) | 1.0.0 | 1.0.0 | 无 | 无 | 无 | 无 | 提供高级全文检索功能。 |
| [clickhouse_fdw](https://github.com/ildus/clickhouse_fdw) | 无 | 1.4 | 1.4 | 1.4 | 1.4 | 1.4 | 让 PostgreSQL 可以直接查询 ClickHouse 数据库中的数据，就像查询本地表一样。 |
| [pg_permissions](https://github.com/cybertec-postgresql/pg_permissions) | 无 | 1.4 | 无 | 无 | 无 | 无 | 用来查看和审计 PostgreSQL 数据库中所有对象（表、视图、函数等）的权限设置，方便进行权限管理和安全审计。 |
| [address_standardizer](https://postgis.net/docs/standardize_address.html) | 无 | 3.3.7 | 3.3.4 | 3.3.2 | 3.1.4 | 3.1.4 | 基于 [PAGC](http://www.pagcgeo.org/docs/html/pagc-11.html) 标准的地名标准化插件。 |
| [address_standardizer_data_us](https://postgis.net/docs/standardize_address.html) | 无 | 3.3.7 | 3.3.4 | 3.3.2 | 3.1.4 | 3.1.4 | 基于 [PAGC](http://www.pagcgeo.org/docs/html/pagc-11.html) 标准的地名标准化（美国）数据插件。 |
| [age](https://github.com/apache/age) | 1.6.0 | 1.6.0 | 1.6.0 | 1.6.0 | 1.6.0 | 无 | 为 PostgreSQL 提供图形数据库功能。 |
| [bloom](https://www.postgresql.org/docs/14/bloom.html) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 提供一种基于布鲁姆过滤器的索引访问方法。 |
| [btree_gin](https://www.postgresql.org/docs/14/btree-gin.html) | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 提供一个为多种数据类型和所有 enum 类型实现 B 树等价行为的 GIN 操作符类示例。 |
| [btree_gist](https://www.postgresql.org/docs/14/btree-gist.html) | 1.8 | 1.7 | 1.7 | 1.7 | 1.6 | 1.5 | 提供一个为多种数据类型和所有 enum 类型实现 B 树等价行为的 GiST 操作符类示例。 |
| [citext](https://www.postgresql.org/docs/14/citext.html) | 1.8 | 1.6 | 1.6 | 1.6 | 1.6 | 1.6 | 提供一种大小写不敏感的字符串类型。 |
| [cube](https://www.postgresql.org/docs/14/cube.html) | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 1.4 | 提供一种数据类型来表示多维立方体。 |
| [dblink](use-the-dblink-and-postgres-fdw-extensions-for-cross-database-operations.md) | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 跨库操作表。 |
| [decoderbufs](https://github.com/debezium/postgres-decoderbufs) | 无 | 无 | 无 | 无 | 无 | 0.1.0 | 根据 Protocol Buffers 协议、输出能够适配 [Debezium](http://debezium.io) 平台的数据。 |
| [dict_int](https://www.postgresql.org/docs/14/dict-int.html) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 附加全文搜索词典模板的示例。 |
| [earthdistance](https://www.postgresql.org/docs/14/earthdistance.html) | 1.2 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 提供两种不同的方法来计算地球表面的大圆距离。 |
| [fuzzystrmatch](use-the-fuzzystrmatch-extension-to-calculate-the-similarity-between-strings.md) | 1.2 | 1.2 | 1.2 | 1.1 | 1.1 | 1.1 | 判断字符串之间的相似性和距离。 |
| [ganos_address_standardizer](https://postgis.net/docs/standardize_address.html) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 基于 [PAGC](http://www.pagcgeo.org/docs/html/pagc-11.html) 标准的地名标准化插件。 |
| [ganos_address_standardizer_data_us](https://postgis.net/docs/standardize_address.html) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 基于 [PAGC](http://www.pagcgeo.org/docs/html/pagc-11.html) 标准的地名标准化美国部分数据插件。 |
| [ganos_geometry](geometry-model.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 提供空间几何类型的计算分析功能。 |
| [ganos_geometry_pyramid](data-and-hardware-requirements.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 用于二维空间几何大数据的快速显示。 |
| [ganos_geometry_sfcgal](data-and-hardware-requirements.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 提供空间几何 SFCGAL 插件扩展功能。 |
| [ganos_geometry_topology](data-and-hardware-requirements.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 提供空间几何类型的计算分析功能。 |
| [ganos_geomgrid](geomgrid-sql-reference.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 提供 H3、GeoSOT 等网格剖分、编码、索引及分析能力。 |
| [ganos_networking](path-model.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 提供空间几何网络类型的计算分析功能。 |
| [ganos_pointcloud](point-cloud-model.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 提供点云的存储、计算分析功能。 |
| [ganos_pointcloud_geometry](point-cloud-model.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 提供点云的存储、计算分析功能。 |
| [ganos_raster](terms-1.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 提供空间栅格数据的存储、计算分析功能。 |
| [ganos_spatialref](st-srequal.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 提供空间参考的计算分析功能。 |
| [ganos_tiger_geocoder](https://postgis.net/docs/Extras.html) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | 提供 USCB Tiger 数据类型支持。 |
| [ganos_trajectory](basic-concepts.md) | 无 | 7.0 | 6.9 | 6.9 | 6.9 | 6.9 | Ganos 移动对象（MOD）数据计算分析功能。 |
| [hll](use-the-hll-plug-in.md) | 2.18 | 2.19 | 2.18 | 2.18 | 2.18 | 2.15 | 快速预估 PV、UV 等业务指标。 |
| [hstore](https://www.postgresql.org/docs/14/hstore.html) | 1.8 | 1.8 | 1.8 | 1.8 | 1.8 | 1.7 | 在单一 PostgreSQL 实例中存储键值对。 |
| [hypopg](use-the-hypopg-extension-to-create-hypothetical-indexes.md) | 1.4.2 | 1.4.1 | 1.4.1 | 1.4.1 | 1.4.1 | 1.3.1 | 创建虚拟索引。 |
| [h3](https://github.com/uber/h3) | 无 | 4.2.3 | 无 | 无 | 无 | 无 | 提供 Uber 的 H3 六边形层次空间索引功能。 |
| [index_adviser](using-the-index-adviser-extension-on-an-apsaradb-rds-for-postgresql-instance.md) | 无 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 提供索引推荐。 |
| [intagg](https://www.postgresql.org/docs/14/intagg.html) | 无 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 提供一个整数聚集器和一个枚举器。 |
| [intarray](https://www.postgresql.org/docs/14/intarray.html) | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 1.3 | 提供一些有用的函数和操作符来操纵不含空值的整数数组。 |
| [ip4r](https://github.com/RhodiumToad/ip4r) | 2.4 | 2.4 | 2.4 | 2.4 | 2.4 | 2.4 | 使 PostgreSQL 支持 IP 地址范围类型。 |
| [isn](https://www.postgresql.org/docs/14/isn.html) | 1.3 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 按照一个硬编码的前缀列表对输入进行验证，也被用来在输出时连接号码。 |
| [ltree](https://www.postgresql.org/docs/14/ltree.html) | 1.3 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 用于表示存储在一个层次树状结构中的数据的标签。 |
| [mysql_fdw](use-the-mysql-fdw-extension-to-read-data-from-and-write-data-to-a-mysql-database.md) | 无 | 2.9.2 | 1.2 | 1.2 | 1.2 | 1.1 | 读写 RDS MySQL 实例或自建 MySQL 数据库里的数据。 |
| [orafce](https://github.com/orafce/orafce) | 4.15 | 无 | 4.9.2 | 4.9.2 | 4.9.2 | 无 | 提供一系列 Oracle 兼容函数。 |
| [oss_fdw](use-the-oss-fdw-extension-to-read-and-write-foreign-data-text-files.md) | 无 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 读写 OSS 里的数据。 |
| [pase](use-pase-for-efficient-vector-search.md) | 无 | 无 | 0.0.1 | 0.0.1 | 0.0.1 | 0.0.1 | 高效向量检索。 |
| [pg_bigm](use-the-pg-bigm-extension-to-perform-fuzzy-match-based-queries.md) | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 创建一个二元语法（2-gram）的 GIN 索引来加速全文搜索过程。 |
| [pg_buffercache](https://www.postgresql.org/docs/14/pgbuffercache.html) | 1.6 | 1.4 | 1.4 | 1.3 | 1.3 | 1.3 | 提供一种方法实时检查共享缓冲区。 |
| [pg_cron](use-the-pg-cron-extension-to-configure-scheduled-tasks.md) | 1.6 | 1.6 | 1.6 | 1.6 | 1.6 | 1.5 | 设置定时任务。 |
| [pg_freespacemap](https://www.postgresql.org/docs/14/pgfreespacemap.html) | 1.3 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 检查空闲空间映射（FSM）。 |
| [pg_jieba](use-the-pg-jieba-extension-on-an-apsaradb-rds-for-postgresql-instance.md) | 1.2.0 | 1.2.0 | 1.2.0 | 1.2.0 | 1.2.0 | 1.1.0 | 对中文全文实现分词。 |
| [pg_hint_plan](use-the-pg-hint-plan-extension-to-customize-query-plans.md) | 1.8.0 | 1.7.0 | 1.6.1 | 1.5.2 | 1.4.3 | 1.3.9 | 通过特殊的注释语句提示，使 PostgreSQL 改变其既定的执行计划。 |
| [pg_partman](https://github.com/pgpartman/pg_partman) | 4.7.3 | 5.2.4 | 5.1.0 | 5.1.0 | 5.0.1 | 4.7.3 | 创建和管理基于时间和基于序列的表分区集。 |
| [pg_pathman](https://help.aliyun.com/zh/polardb/polardb-for-postgresql/pg-pathman-usage#task-2311142) | 无 | 无 | 无 | 无 | 无 | 1.5 | 高性能分区表插件。 |
| [pg_prewarm](https://www.postgresql.org/docs/14/pgprewarm.html) | 1.2 | 无 | 1.2 | 1.2 | 1.2 | 1.2 | 提供一种方便的方法把数据载入到操作系统缓冲区或者 PostgreSQL 缓冲区。 |
| [pg_profile](use-the-pg-profile-extension-to-collect-statistics-on-resource-intensive-activities.md) | 无 | 无 | 4.4 | 4.4 | 4.4 | 4.1 | 资源密集活动统计。 |
| [pg_proctab](https://gitlab.com/pg_proctab/pg_proctab/-/blob/main/doc/README.pg_proctab?ref_type=heads) | 0.0.13 | 0.0.10 | 0.0.10 | 0.0.10 | 0.0.10 | 0.0.10 | 允许用户通过 SQL 查询的方式，访问操作系统层面的进程和系统资源消耗数据。 |
| [pg_repack](use-the-pg-repack-extension-to-clear-tablespaces.md) | 无 | 1.5.1 | 1.5.0 | 1.5.0 | 1.5.0 | 1.4.6 | 在线清理表空间功能。 |
| [pg_stat_kcache](use-the-pg-stat-kcache-extension-to-collect-statistics-on-system-read-and-write-operations.md) | 无 | 2.3.0 | 2.2.3 | 2.2.3 | 2.2.3 | 2.2.1 | 系统读写信息统计。 |
| [pg_stat_statements](https://www.postgresql.org/docs/14/pgstatstatements.html) | 1.12 | 1.10 | 1.10 | 1.10 | 1.9 | 1.8 | 提供一种方法追踪服务器执行的所有 SQL 语句的执行统计信息。 |
| [pg_trgm](https://www.postgresql.org/docs/14/pgtrgm.html) | 1.6 | 1.6 | 1.6 | 1.6 | 1.6 | 1.5 | 提供字母数字文本相似度的函数和操作符，以及支持快速搜索相似字符串的索引操作符类。 |
| [pg_squeeze](shrink-inflate-tables-and-indexes-pg-squeeze.md) | 1.8 | 1.7 | 1.6 | 1.6 | 1.6 | 1.6 | 在线收缩膨胀表和索引。 |
| [pg_wait_sampling](https://github.com/postgrespro/pg_wait_sampling) | 1.1 | 1.1 | 无 | 无 | 无 | 无 | 用于监控和分析数据库的等待状态。 |
| [pgaudit](use-the-pgaudit-extension-to-generate-audit-logs.md) | 无 | 17.0 | 16.0 | 1.6.1 | 1.6.1 | 1.5 | 提供详细的会话和对象审计日志记录。 |
| [pgcrypto](https://www.postgresql.org/docs/14/pgcrypto.html) | 1.4 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 为 PostgreSQL 提供了密码函数。 |
| [pgl_ddl_deploy](https://github.com/enova/pgl_ddl_deploy) | 无 | 无 | 2.2 | 2.2 | 2.2 | 2.1 | 使 PostgreSQL 支持透明逻辑 DDL 复制。 |
| [pglogical](use-the-pglogical-extension-for-logical-streaming-replication.md) | 2.4.6 | 2.4.5 | 2.4.5 | 2.4.4 | 2.4.4 | 2.4.2 | 提供逻辑流复制发布和订阅的功能。 |
| [pgrouting](https://docs.pgrouting.org/) | 无 | 3.4.2 | 3.4.2 | 3.4.2 | 3.4.2 | 3.4.2 | 提供空间几何网络的计算分析功能。 |
| [pgrowlocks](https://www.postgresql.org/docs/14/pgrowlocks.html) | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 提供一个函数来显示指定表的行锁定信息。 |
| [pgsql-gzip](https://github.com/pramsey/pgsql-gzip) | 1.0 | 1.0.0 | 1.0.0 | 无 | 无 | 无 | 在 PostgreSQL 数据库中实现数据的 Gzip 压缩和解压缩功能。 |
| [pgsql-http](https://github.com/pramsey/pgsql-http) | 1.6 | 无 | 1.6 | 无 | 无 | 无 | 允许用户在 PostgreSQL 数据库中直接发起 HTTP 请求。 |
| [pgstattuple](https://www.postgresql.org/docs/14/pgstattuple.html) | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 提供多种函数来获得元组层的统计信息。 |
| [pgvector](pgvector-use-guide.md) | 0.8.1 | 0.8.0 | 0.8.0 | 0.8.0 | 0.8.0 | 无 | 高维向量相似度搜索插件。 |
| [pldebugger](use-the-pldebugger-extension-to-debug-stored-procedures.md) | 无 | 1.8 | 1.8 | 1.8 | 1.8 | 1.1 | 存储过程调试插件。 |
| [plperl](https://www.postgresql.org/docs/14/plperl.html) | 无 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 提供 Perl 过程语言。 |
| [plpgsql](https://www.postgresql.org/docs/14/plpgsql.html) | 无 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 提供 SQL 过程语言。 |
| [plproxy](use-the-pl-or-proxy-plug-in-for-horizontal-sharding.md) | 2.11.0 | 无 | 2.11.0 | 2.10.0 | 2.10.0 | 2.10.0 | 包含 CLUSTER 模式和 CONNECT 模式，可以帮助您用不同方式访问数据库。 |
| [pltcl](https://www.postgresql.org/docs/14/pltcl.html) | 无 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 提供 tcl 过程语言。 |
| [postgis](https://postgis.net/docs/) | 无 | 3.3.7 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.4 | PostGIS 空间地理信息相关扩展。 |
| [postgis_sfcgal](https://postgis.net/docs/reference.html#reference_sfcgal) | 无 | 3.3.7 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.4 | PostGIS SFCGAL 空间地理信息相关扩展。 |
| [postgis_tiger_geocoder](https://postgis.net/docs/Extras.html) | 无 | 3.3.7 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.4 | PostGIS TIGER 数据空间地理信息相关扩展。 |
| [postgis_topology](https://postgis.net/docs/Topology.html) | 无 | 3.3.7 | 3.3.4 | 3.3.4 | 3.3.4 | 3.3.4 | PostGIS 拓扑数据空间地理信息相关扩展。 |
| [postgres_fdw](use-the-dblink-and-postgres-fdw-extensions-for-cross-database-operations.md) | 1.2 | 1.1 | 1.1 | 1.1 | 1.1 | 1.0 | 跨库操作表。 |
| [postgresql_anonymizer](https://gitlab.com/dalibo/postgresql_anonymizer/) | 无 | 1.1.0 | 无 | 1.1.0 | 1.1.0 | 无 | 对数据库中的敏感数据进行匿名化或脱敏处理。 |
| [rds_ai](ai-rds-ai.md) | 1.0 | 1.0.0 | 1.0.0 | 1.0.0 | 1.0.0 | 无 | 集成了阿里云百炼的先进模型，包括千问、通用文本向量 和通用文本排序 等。通过该插件，您可以在 RDS PostgreSQL 数据库中轻松实现包括大模型问答、文本向量转换、 文本排序、 Top N 相似向量检索以及 RAG 问答等多种应用场景。 |
| [rds_ccl](use-the-rds-ccl-extension-to-perform-sql-throttling-on-an-apsaradb-rds-for-postgresql-instance.md) | 1.3 | 1.2 | 1.2 | 1.2 | 1.2 | 无 | 支持 SQL 限流。 |
| [rds_duckdb](how-to-use-duckdb-to-speed-up-queries.md) | 1.3.2.3 | 1.1 | 1.2 | 1.3 | 1.1 | 1.1 | 复杂查询加速。 |
| [rds_embedding](rds-embedding.md) | 无 | 1.0 | 1.0 | 1.0 | 1.0 | 无 | 提供自定义模型配置、模型调用的能力，可以在数据库端实现文本到向量的转换。 |
| [rds_encdb](use-the-rds-encdb-extension-to-encrypt-sensitive-columns.md) | 无 | 无 | 1.0 | 无 | 无 | 无 | 用于对查询结果集的敏感列进行加密。同时，通过对数据库账户权限进行设置，相关账户在访问敏感列信息时，仅能获得密文格式的查询结果。 |
| [rds_online_ddl](use-the-rds-online-ddl-extension-to-modify-column-data-type-online.md) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 支持在线修改列类型，在不影响业务连续性的前提下完成表结构变更。 |
| [rds_tde_utils](use-the-rds-tde-utils-extension-to-encrypt-and-decrypt-multiple-data-records-at-a-time.md) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | TDE 批量加解密插件。 |
| [roaringbitmap](use-the-roaringbitmap-extension.md) | 0.5.4 | 0.5.4 | 0.5.4 | 0.5 | 0.5 | 0.5 | 使用位图功能，提高查询性能。 |
| [rum](use-the-rum-extension.md) | 无 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 高速全文检索。 |
| [sequential-uuids](use-the-sequential-uuids-extension-to-generate-sequential-uuids.md) | 1.0.3 | 无 | 1.0.2 | 1.0.2 | 1.0.2 | 1.0.2 | 具有顺序模式的 UUID 生成器。 |
| [smlar](use-the-smlar-plug-in.md) | 无 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 计算两个相同类型数组的相似度。 |
| [snowflake](https://github.com/pgEdge/snowflake) | 2.2 | 2.2 | 2.2 | 2.2 | 无 | 无 | 提供了一种基于 int8 和序列的唯一 ID 解决方案，以选择性替代 PostgreSQL 内置的 bigserial 数据类型。 |
| [sslinfo](https://www.postgresql.org/docs/14/sslinfo.html) | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 提供当前客户端提供的 SSL 证书的有关信息。 |
| [tablefunc](https://www.postgresql.org/docs/14/tablefunc.html) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 包括多个返回表的函数。 |
| [tds_fdw](use-the-tds-fdw-extension-to-query-data-of-sql-server-instances.md) | 无 | 2.0.4 | 2.0.3 | 2.0.3 | 2.0.3 | 2.0.3 | 查询其他类型数据库的数据。 |
| [timescaledb](use-the-timescaledb-extension.md) | 无 | 2.24.0 | 2.24.0 | 2.9.2 | 2.9.2 | 2.5.0 | 支持时序数据的自动分片、高效写入、检索、准实时聚合等。 |
| [tsm_system_rows](https://www.postgresql.org/docs/14/tsm-system-rows.html) | 1.0 | 无 | 1.0 | 1.0 | 1.0 | 1.0 | 提供表采样方法 SYSTEM_ROWS。 |
| [tsm_system_time](https://www.postgresql.org/docs/14/tsm-system-time.html) | 1.0 | 无 | 1.0 | 1.0 | 1.0 | 1.0 | 提供了表采样方法 SYSTEM_TIME。 |
| [unaccent](https://www.postgresql.org/docs/14/unaccent.html) | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 文本搜索字典，它能从词位中移除重音（附加符号）。 |
| [uuid-ossp](https://www.postgresql.org/docs/14/uuid-ossp.html) | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 提供函数使用几种标准算法之一产生通用唯一标识符（UUID）。 |
| [wal2json](use-the-wal2json-extension.md) | 2.6 | 2.6 | 2.6 | 2.6 | 2.6 | 2.3 | 将逻辑日志文件输出为 JSON 格式。 |
| [xml2](https://www.postgresql.org/docs/14/xml2.html) | 1.2 | 无 | 1.1 | 1.1 | 1.1 | 1.1 | 提供 XPath 查询和 XSLT 功能。 |
| [zhparser](use-the-zhparser-extension-to-segment-chinese-text.md) | 2.1 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 中文全文搜索。 |
## 常见问题
Q：我需要的插件在插件表中没有找到，怎么办？
A：可以采取如下措施：
本页面仅列举了常用插件，更多插件的支持情况，可在数据库内使用SELECT * FROM pg_available_extensions;命令查询。
到[阿里云聆听平台](https://connect.aliyun.com/)提交建议和需求。
Q：我需要的插件在其他大版本支持，但是我所使用的大版本不支持，怎么办？
A：可以采取如下措施：
耐心等待，各插件正逐步在各大版本中同步，可以关注[AliPG](release-notes-for-alipg.md)[内核小版本发布记录](release-notes-for-alipg.md)，可能在后续小版本更新中支持。
如果想要变更实例版本，尽快使用所需插件：
目标实例大版本高于当前实例大版本：在当前实例上执行大版本升级。具体操作，请参见[升级数据库大版本](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md)。
目标实例大版本低于当前实例大版本：购买支持所需插件的大版本实例，然后通过[数据传输服务](https://help.aliyun.com/zh/dts/product-overview/what-is-dts)[DTS](https://help.aliyun.com/zh/dts/product-overview/what-is-dts)，将当前版本数据迁移至新实例中。
到[阿里云聆听平台](https://connect.aliyun.com/)提交建议和需求。
Q：插件表中显示支持的插件，但是在实际创建时报错提示不支持，怎么办？
A：请先[升级内核小版本](update-the-minor-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md)至最新版后，再进行尝试。
Q：我创建的插件都是在public模式下，如何在其他Schema下创建插件并使用？
A：需要在创建插件时就指定Schema，例如：
CREATE EXTENSION <插件名> SCHEMA <Schema名>;
## 相关文档
RDS PostgreSQL支持在控制台管理插件，更多信息，请参见[管理插件](manage-plug-ins.md)。
各插件的使用方法可参见本文后提供的相关文档或开源插件对应的官方文档。
如果需要使用最新的插件版本，请[升级内核小版本](update-the-minor-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md)至最新版。
也可以查看[AliPG](release-notes-for-alipg.md)[内核小版本发布记录](release-notes-for-alipg.md)，确定插件在哪个小版本支持。
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
