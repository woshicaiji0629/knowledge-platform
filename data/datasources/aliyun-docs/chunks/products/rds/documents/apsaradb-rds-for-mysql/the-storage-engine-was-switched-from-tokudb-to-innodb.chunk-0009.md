## 方案四
此方案使用DTS同步整个数据库至新实例，适用于有实例升级需求，或者可以接受业务停机时间相对长一些的实例。
源实例导出所有结构脚本，将脚本中关于引擎部分删除或修改。
说明
例如将create table t1(id int,name varchar(10)) engine=tokudb;修改为create table t1(id int,name varchar(10)) engine=innodb;。
[新建](../create-an-apsaradb-rds-for-mysql-instance.md)[RDS](../create-an-apsaradb-rds-for-mysql-instance.md)[实例](../create-an-apsaradb-rds-for-mysql-instance.md)，使用修改过的脚本创建库、表。
将源实例数据库使用DTS[同步至新实例](https://help.aliyun.com/zh/dts/user-guide/configure-one-way-data-synchronization-between-apsaradb-rds-for-mysql-instances)上。
说明
在同步初始化时，仅勾选全量数据初始化。
确认同步无延迟后，切换应用连接地址到新实例即可。
该文章对您有帮助吗？
反馈
