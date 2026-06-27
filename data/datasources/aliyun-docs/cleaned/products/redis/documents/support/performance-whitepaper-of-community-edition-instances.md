# 云数据库Tair（兼容 Redis）的性能白皮书-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/support/performance-whitepaper-of-community-edition-instances

# Tair内存型、Tair 持久内存型、Redis开源版性能白皮书
本文介绍Tair内存型、Tair 持久内存型、Redis开源版的性能测试结果，以及测试环境、测试工具与测试方法。
## 测试结果
对包括SET、GET等在内的十余种Redis基础命令进行性能测试并给出测试指标。
| 命令 | Tair 内存型 | Tair 持久内存型 | Redis 开源版 |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| QPS | Average Latency | 99th Percentile Latency | QPS | Average Latency | 99th Percentile Latency | QPS | Average Latency | 99th Percentile Latency |  |
| SET | 282,656 | 0.45 | 0.86 | 135,247 | 0.93 | 1.50 | 142,376 | 0.45 | 0.72 |
| GET | 519,761 | 0.24 | 0.36 | 208,960 | 0.61 | 0.90 | 204,690 | 0.31 | 0.47 |
| ZADD | 208,169 | 0.62 | 1.14 | 96,007 | 1.29 | 1.90 | 113,135 | 0.57 | 0.78 |
| ZSCORE | 463,904 | 0.27 | 0.40 | 154,693 | 0.82 | 1.00 | 170,163 | 0.37 | 0.54 |
| HSET | 260,069 | 0.49 | 1.03 | 68,565 | 1.81 | 3.80 | 124,613 | 0.51 | 0.97 |
| HGET | 494,603 | 0.25 | 0.37 | 180,050 | 0.70 | 0.91 | 188,903 | 0.34 | 0.52 |
| LPUSH | 286,324 | 0.44 | 0.84 | 143,951 | 0.87 | 1.20 | 153,269 | 0.42 | 0.59 |
| LINDEX | 414,070 | 0.30 | 0.45 | 62,112 | 2.01 | 2.80 | 157,568 | 0.40 | 0.58 |
| SADD | 292,738 | 0.44 | 0.86 | 138,710 | 0.90 | 1.20 | 140,155 | 0.45 | 0.63 |
| SISMEMBER | 531,139 | 0.24 | 0.34 | 162,585 | 0.78 | 0.99 | 181,492 | 0.35 | 0.52 |
| EVALSHA | 214,303 | 0.60 | 1.12 | 89,726 | 1.38 | 2.10 | 101,136 | 0.63 | 0.91 |
测试指标说明：
QPS：每秒处理的读写操作数，单位为次/秒。
Average Latency：操作的平均延迟时间，单位为毫秒（ms）。
99th Percentile Latency：99%操作延迟，指99%操作的最大延迟时间，单位为毫秒（ms）。例如该指标的值为0.5毫秒，表示99%的请求可以在0.5毫秒内被处理。
说明
测试结果为在多个可用区、对多个实例、进行多次测试的平均值。
测试结果中的延迟为全链路延迟，包含数据包在DB侧及压测端排队的时延。
测试结果受到多种不可控因素的影响，存在约10%的误差属于合理范围。
测试结果仅代表新购实例进行单一命令测试的结果，而生产环境实例的压力测试请以业务压测场景为准。
测试结果反映了实例的极限性能，在生产环境中，不建议将实例维持在极限负载状态。
P99毛刺受数据结构编码转换影响，尤其是空实例首次写入数据时容易出现。
## 测试环境
### 数据库
| 测试环境信息 | 说明 |
| --- | --- |
| 地域和可用区 | 华北 2（北京）可用区 L、华东 1（杭州）可用区 K、华东 2（上海）可用区 N、华南 1（深圳）可用区 C。 说明 本测试在多个地域进行，本测试报告仅代表上述可用区的平均性能水平。 |
| 实例架构 | 标准架构（双副本），不启用集群，详情请参见 [标准架构](../product-overview/standard-master-replica-instances.md) 。 说明 其他架构的性能说明： 集群架构代理模式：当请求的 Key 分布均匀时，其性能不低于标准架构的 n 倍。 集群架构直连模式：当请求的 Key 分布均匀时，其性能等于标准架构的 n 倍。 读写分离架构：写性能略低于标准架构（因为有更多的复制流量），读性能不低于标准架构的 n 倍。 n 为集群架构的分片节点数或读写分离架构的总节点数。 |
| 实例版本 | 本次测试兼容 Redis 6.0 版本，通常测试结果受版本影响较小。 |
| 实例规格 | 本次测试以下实例规格： Tair 内存型 8 GB（tair.rdb.8g） Tair 持久内存型 8 GB（tair.scm.standard.2m.8d） Redis 开源版 8 GB（redis.shard.xlarge.ce） 测试结果受规格影响较小，更多关于规格的详情请参见 [实例规格](../product-overview/overview-4.md) 。 |
### 测试客户端
| 测试环境信息 | 说明 |
| --- | --- |
| 部署压测工具的设备 | [云服务器](../../../ecs/documents/user-guide/what-is-ecs.md) [ECS](../../../ecs/documents/user-guide/what-is-ecs.md) 实例，规格为 ecs.g7.8xlarge，详情请参见 [实例规格族](../../../ecs/documents/user-guide/overview-of-instance-families.md) 。 |
| 地域和可用区 | 与实例对应的地域及可用区。 |
| 操作系统 | Alibaba Cloud Linux 3。 |
| 网络 | 与 Tair 实例为相同专有网络（VPC），且与 Tair 实例通过专有网络连接。 |
## 测试工具
建议优先使用Tair团队开源的[resp-benchmark](https://github.com/tair-opensource/resp-benchmark)工具：
SET、GET等常规测试项与redis-benchmark保持一致，在复杂测试项中采用更贴近真实业务场景的测试模式。
默认启用了多线程能力，最大程度向服务端发送请求增压，避免压测客户端成为性能瓶颈。
若使用redis-benchmark，建议Redis 7.0及以上版本（该版本优化了基准测试工具的多线程支持）。
### 安装方法
pip install resp-benchmark==0.1.7
说明
安装完成后，您可以执行resp-benchmark --help命令获取更详细的配置项说明，或访问其[GitHub](https://github.com/tair-opensource/resp-benchmark)[主页](https://github.com/tair-opensource/resp-benchmark)。
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
redis-cli -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 SCRIPT LOAD "return redis.call('SET', KEYS[1], ARGV[1])"
测试命令时长20秒：
resp-benchmark -h r-bp1u****8qyvemv2em.redis.rds.aliyuncs.com -p 6379 -s 20 "EVALSHA d8f2fad9f8e86a53d2a6ebd960b33c4972cacc37 1 {key uniform 10000000} {value 64}"
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
