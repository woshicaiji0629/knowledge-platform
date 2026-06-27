SHA
该指标代表在EVALSHA中执行SET命令的性能，其中SET命令的Key范围为0-10000000，Value大小为64字节。
载入Lua脚本：
redis-cli -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 SCRIPT LOAD "return redis.call('SET', KEYS[1], ARGV[1])"
测试命令时长20秒：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 -s 20 "EVALSHA d8f2fad9f8e86a53d2a6ebd960b33c4972cacc37 1 {key uniform 10000000} {value 64}"
该文章对您有帮助吗？
反馈
