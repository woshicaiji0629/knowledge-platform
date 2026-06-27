lue大小为64字节，测试时长20秒：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 -s 20 "LPUSH {key uniform 1000} {value 64}"
LINDEX
该指标代表LINDEX命令的性能。
构造数据，Key范围为0-1000，每个Key包含10000条数据，数据大小为64字节：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 --load -c 256 -P 10 -n 10000000 "LPUSH {key sequence 1000} {value 64}"
测试LINDEX命令，测试时长20秒：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 -s 20 "LINDEX {key uniform 1000} {rand 10000}"
SADD
该指标代表SADD命令的性能。
测试SADD命令，Key范围为0-1000，Value大小为64字节，测试时长20秒：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 -s 20 "SADD {key uniform 1000} {value 64}"
SISMEMBER
该指标代表SISMEMBER命令的性能。
构造数据，Key范围为0-1000，每个Key包含10007条数据，数据大小为64字节：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 --load -c 256 -P 10 -n 10007000 "SADD {key sequence 1000} {key sequence 10007}"
测试SISMEMBER命令，测试时长20秒：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 -s 20 "SISMEMBER {key uniform 1000} {key uniform 10007}"
EVALSHA
该指标代表在EVALSHA中执行SET命令的性能，其中SET命令的Key范围为0-10000000，Value大小为64字节。
载入Lua脚本：
redis-cli -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 SCRIPT LOAD "retur
