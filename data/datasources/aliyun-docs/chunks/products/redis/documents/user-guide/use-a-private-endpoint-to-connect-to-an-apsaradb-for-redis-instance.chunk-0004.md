## redis-cli
使用集群架构直连地址连接实例。
重要
使用直连地址连接时必须添加-c参数，否则会导致连接失败。
./redis-cli -h r-bp1zxszhcgatnx****.redis.rds.aliyuncs.com -p 6379 -c
完成密码验证。
AUTH testaccount:Rp829dlwa
关于redis-cli的更多介绍请参见[通过](use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)[redis-cli](use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)[连接实例](use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)。
