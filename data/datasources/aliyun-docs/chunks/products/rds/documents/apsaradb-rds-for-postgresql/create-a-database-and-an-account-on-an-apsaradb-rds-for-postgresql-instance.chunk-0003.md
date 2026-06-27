## 创建数据库
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏单击数据库管理。
单击创建数据库。
设置如下参数。

| 参数 | 说明 |
| --- | --- |
| 数据库（DB）名称 | 最长 63 个字符。 由小写字母、数字、中划线、下划线组成。 以字母开头，以字母或数字结尾。 |
| 支持字符集 | 数据库的字符集。 重要 RDS PostgreSQL 数据库的字符集在数据库创建后不支持修改。 |
| Collate | 字符串排序规则。 |
| Ctype | 字符分类。 |
| 授权账号 | 设置数据库的所有者，对数据库拥有 ALL 权限。 |
| 备注 | 填写备注信息。 |

单击创建。
创建成功后，即可在数据库管理中查看已创建的数据库及其相关信息。

| 参数 | 说明 |
| --- | --- |
| 限制并发量 | 指对应数据库并发请求执行的上限量，默认不限制，您也可以使用高权限账号登录数据库后，使用 ALTER DATABASE <数据库名> CONNECTION LIMIT <并发量>; 命令修改。 |
| 表空间 | 指数据库所属的表空间，默认为 pg_default ，表空间路径不支持查看和修改。 如果您使用 [一键上云](use-the-cloud-migration-feature-for-an-apsaradb-rds-for-postgresql-instance.md) 等迁移方式将本地自建数据库迁移上云时，表空间将与本地自建数据库表空间名称相同，支持将数据库和表的表空间修改为 pg_default 。 |
