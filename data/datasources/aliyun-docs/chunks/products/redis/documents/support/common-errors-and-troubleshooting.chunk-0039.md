### UNKILLABLE The busy script was sent by a master instance in the context of replication and cannot be killed.
可能原因：当前Lua脚本已经被Master节点发给自己的replica节点，此时SCRIPT KILL命令无法生效。
解决方法：在控制台的实例列表页面，找到对应实例，单击操作列的重启，更多信息请参见[重启实例](../user-guide/restart-one-or-more-apsaradb-for-redis-instances.md)。
