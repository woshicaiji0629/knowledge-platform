}"
ZSCORE
该指标代表ZSCORE命令的性能。
构造数据，Key范围为0-1000，Score范围为0-70000，每个Key最多10007个Field：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 --load -c 256 -P 10 -n 10007000 "ZADD {key sequence 1000} {rand 70000} {key sequence 10007}"
测试ZSCORE命令，测试时长20秒：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 -s 20 "ZSCORE {key uniform 1000} {key uniform 10007}"
HSET
该指标代表HSET命令的性能。
测试HSET命令，Key范围为0-1000，Field范围为0-10000，每个Field的Value大小为64字节，测试时长20秒：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 -s 20 "HSET {key uniform 1000} {key uniform 10000} {value 64}"
HGET
该指标代表HGET命令的性能。
构造数据，Key范围为0-1000，每个Key包含10007个Field，每个Field的Value大小为64字节：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 --load -c 256 -P 10 -n 10007000 "HSET {key sequence 1000} {key sequence 10007} {value 64}"
测试HGET命令，测试时长20秒：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 -s 20 "HGET {key uniform 1000} {key uniform 10007}"
LPUSH
该指标代表LPUSH命令的性能。
测试LPUSH命令，Key范围为0-1000，Value大小为64字节，测试时长20秒：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 -s 20 "LPUSH {key uniform 1000} {value 64}"
LINDEX
该指标代表LINDEX命令的性能。
构
