### 云盘实例升级内核小版本
说明
如果当前实例为主实例，拥有只读实例，可以通过两种方式进行升级。
对主实例发起内核小版本升级，该主实例下的所有只读实例都会先立即进行并发升级，然后再升级主实例。
如果您不希望所有只读实例立即升级，请先逐个升级所有只读实例，然后再升级主实例。
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在配置信息区域中单击升级内核小版本。
在弹出的对话框中，选择可升级到版本和升级时间，单击确定。
可升级到版本中各字段含义：
rds：RDS实例。
postgres：PostgreSQL数据库。
1200：PostgreSQL大版本为12。
20220830：AliPG内核小版本。各小版本的具体信息，请参见[AliPG](release-notes-for-alipg.md)[内核小版本发布记录（PostgreSQL 14~18）](release-notes-for-alipg.md)。
12.11：PostgreSQL社区小版本号。
