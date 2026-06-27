## 测试示例
重要
每次测试时建议先清空数据库，避免已有数据存在干扰。
resp-benchmark在未指定连接数时会自动选择相对合适的连接数，为测得极限负载下的数据建议手动调整连接数，比如设置为128，可以通过增加参数-c 128实现。连接数过低时，测试压力不足，导致QPS数据偏低；连接数过高时，测试压力可能会超过DB的处理能力，数据包会在网络链路中排队较长时间，导致延迟数据偏高。因为影响因素较多，难以在下文中给出固定的连接数配置，常见的连接数设置为32、64、128、192和256，可根据实际测试情况自行调整。
以下为各命令的测试实例：
SET
该指标代表SET命令的性能。
测试SET命令，Key范围为0-10000000（表示生成的Key名称为key_0000000000~key_0009999999），Value大小为64字节，测试时长20秒：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 -s 20 "SET {key uniform 10000000} {value 64}"
GET
该指标代表GET命令的性能。
构造数据，Key范围为0-10000000，Value大小为64字节：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 --load -c 256 -P 10 -n 10000000 "SET {key sequence 10000000} {value 64}"
测试GET命令，测试时长20秒：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 -s 20 "GET {key uniform 10000000}"
ZADD
该指标代表ZADD命令的性能。
测试ZADD的写性能，Key范围为0-1000，Score范围为0-70000，每个Key最多10000个Field，测试时长20秒：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 -s 20 "ZADD {key uniform 1000} {rand 70000} {key uniform 10000}"
ZSCORE
该指标代表ZSCORE命令的性能。
构造数据，Key范围为0-1000，Score范围为0-70000，每个Key最多10007个Field：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 --load -
