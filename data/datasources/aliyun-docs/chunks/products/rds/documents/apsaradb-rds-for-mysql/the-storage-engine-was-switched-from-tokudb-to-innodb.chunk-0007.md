## 方案三
此方案使用阿里云的数据传输服务DTS（Data Transmission Service）实时同步原表数据到临时表，在业务低峰期锁原表并交换表名。该方案可以大量的表同时操作。
[通过](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[DMS](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[登录](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[RDS](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[数据库](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)。
在上方选择SQL操作>SQL窗口。
使用如下命令创建临时表。
CREATE TABLE `testfs_tmp` ( `id` int(11) NOT NULL AUTO_INCREMENT, `vc` varchar(8000) DEFAULT NULL, PRIMARY KEY (`id`) ) ENGINE=innodb DEFAULT CHARSET=utf8
[购买数据同步作业](https://help.aliyun.com/zh/dts/getting-started/purchase-a-dts-instance)。
说明
数据同步作业为计费项，详细价格请参见[数据传输](https://cn.aliyun.com/price/product#/dts/detail)。
在数据传输控制台左侧单击数据同步。
找到已购买的数据同步实例，在右侧单击配置同步链路。
配置如下参数。
