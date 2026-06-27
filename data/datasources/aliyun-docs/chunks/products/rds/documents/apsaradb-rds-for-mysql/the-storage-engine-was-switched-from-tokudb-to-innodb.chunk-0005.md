## 方案二
此方案为使用第三方工具进行转换。支持Online DDL的第三方工具很多，例如Percona开发的[pt-osc](https://www.percona.com/doc/percona-toolkit/LATEST/pt-online-schema-change.html)、Git-hub开发的[gh-ost](https://github.com/github/gh-ost)等，这里以gh-ost为例进行转换说明，详细说明请参见[gh-ost](https://github.com/github/gh-ost/blob/master/README.md)。
原理说明
gh-ost进行转换的基本原理是新建一个与原表结构相同的临时表，然后同步原表数据，全量完成后通过模拟Slave进程读取Binlog，实时同步数据到临时表。最后在业务低峰时间段重命名表进行切换。此方案主要压力来自全量数据初始化时的IO，但是可以通过修改参数限制IO。
优点：机动性强，可以自定义时间，同步过程可控。
缺点：每一个表都要用命令同步一次，如果表很多的话操作比较繁琐。
参数说明

| 参数 | 说明 |
| --- | --- |
| --initially-drop-old-table | 检查并删除已经存在的旧表。 |
| --initially-drop-ghost-table | 检查并删除已经存在的 ghost 中间表。 |
| --aliyun-rds | 在阿里云 RDS 上执行。 |
| --assume-rbr | 设置 gh-ost 为 rbr binlog 模式。 |
| --allow-on-master | 在主库上执行 gh-ost。 |
| --assume-master-host | 主库的地址。 |
| --user | 数据库账号名称。 |
| --password | 数据库密码。 |
| --host | 连接地址，与主库地址相同即可。 |
| --database | 数据库名称。 |
| --table | 表名。 |
| --alter | 操作语句。 |
| --chunk-size | 行拷贝的 batch 大小。 |
| --postpone-cut-over-flag-file | 切换文件。指定时间删除此文件立刻进行表切换。 |
| --panic-flag-file | 生成此文件，ghost 进程立刻停止。 |
| --serve-socket-file | 用于接收交互命令。 |
| --execute | 直接执行。 |
