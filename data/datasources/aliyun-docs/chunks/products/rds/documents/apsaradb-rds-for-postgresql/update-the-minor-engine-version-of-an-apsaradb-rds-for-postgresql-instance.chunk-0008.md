IS或Ganos插件，升级方法，请参见[时空引擎插件升级](how-do-i-update-the-plug-ins-of-ganos.md)。
PostGIS在升级内核小版本时有哪些兼容性问题？
兼容性差异如下表所示：
说明
内核小版本在20211031前的RDS PostgreSQL实例，可能会遇到如下兼容性问题。

| PostGIS 插件版本 | 只升级 RDS PostgreSQL 内核小版本 | 升级 RDS PostgreSQL 内核小版本 + 升级 PostGIS 插件 |
| --- | --- | --- |
| 2.5.x | 使用如下函数时，可能导致数据库崩溃 ST_ClusterKMeans ST_GeomFromKML ST_AsKML 使用如下函数时，将会报错 ST_Buffer 报错 ： Invalid buffer parameter: uad_segs (accept: 'endcap', 'join', 'mitre_limit', 'miter_limit', 'quad_segs' and 'side') 解决办法 ：将 quadsegs 参数修改为 quad_segs 。 ST_Intersects 报错 ： ERROR: GetGenericCacheCollection: Could not find upper context 解决办法： 无。 如下函数将会被删除，无法使用 ST_Force_2D ST_Locate_Along_Measure ST_Estimated_Extent 如下函数的参数值或写法将与升级前不一致 ST_GeomFromGeoJSON：升级后会默认指定 SRID=4326 。 ST_AsGeoJSON：maxdecimaldigits 从 16 修改为 9。 MutliPoint 写法不一致： 升级前： MULTIPOINT(1 1,-1 1) 升级后： MULTIPOINT((1 1),(-1 1)) | 如下函数将会被删除，无法使用 ST_Force_2D ST_Locate_Along_Measure ST_Estimated_Extent 如下函数的参数值或写法将与升级前不一致 ST_GeomFromGeoJSON：升级后会默认指定 SRID=4326 。 ST_AsGeoJSON：参数 maxdecimaldigits 从 16 修改为 9。 MutliPoint 写法不一致： 升级前： MULTIPOINT(1 1,-1 1) 升级后： MULTIPOINT((1 1),(-1 1)) |
| 3.1.x | 使用如下函数时，可能导致数据库崩溃 ST_ClusterKMeans MutliPoint 写法将与升级前不一致 升级前： MULTIPOINT(1 1,-1 1) 升级后： MULTIPOINT((1 1),(-1 1)) | MutliPoint 写法将与升级前不一致 升级前： MULTIPOINT(1 1,-1 1) 升级后： MULTIPOINT((1 1),(-1 1)) |
