# Redis兼容版命令兼容性列表-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/commands-supported-by-tair-serverless-kv-instances

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/redis/documents/product-overview.md)

- [快速入门](products/redis/documents/getting-started.md)

- [Tair AI能力](products/redis/documents/tair-ai-ability.md)

- [操作指南](products/redis/documents/user-guide.md)

- [实践教程](products/redis/documents/use-cases.md)

- [安全合规](products/redis/documents/security-compliance.md)

- [开发参考](products/redis/documents/developer-reference.md)

- [服务支持](products/redis/documents/support.md)

- [视频专区](products/redis/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# Redis兼容版命令支持

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍TairServerless KV Redis兼容版实例的命令支持情况。

## 兼容性说明

- 

实例兼容 Redis 6.0 的绝大多数数据结构与命令。

- 

实例采用集群架构，建议使用支持Redis集群模式的客户端进行连接。

## 命令支持列表

为便于浏览和内容表达，本文的表格约定使用下述注释：

- 

✔️表示支持该命令。

- 

❌表示不支持该命令。

- 

数字标记①：该命令要求所要操作的Key都分布在同1个Slot中。

- 

数字标记②：为兼容某些客户端、框架的行为，该命令仅返回OK或空结果，不会真正执行。

说明

未出现在表格中的命令暂不支持。

不支持命令

- 

HyperLogLog 相关命令，比如：PFADD、PFCOUNT、PFMERGE。

- 

Stream 相关命令，比如：XACK、XADD、XCLAIM、XDEL、XGROUP、XLEN、XPENDING、XRANGE、XREAD、XREADGROUP、XREVRANGE、XTRIM。

- 

Pub/Sub 相关命令，比如：PSUBSCRIBE、PUBLISH、PUNSUBSCRIBE、SUBSCRIBE、UNSUBSCRIBE、SPUBLISH、SSUBSCRIBE、SUNSUBSCRIBE、PUBSUB。

- 

Function 相关命令，比如：FCALL、FCALL_RO、FUNCTION DELETE、FUNCTION FLUSH、FUNCTION LIST、FUNCTION LOAD、FUNCTION RESTORE、FUNCTION STATS。

### String

| 命令 | 是否支持 |
| --- | --- |
| APPEND | ✔️ |
| DECR | ✔️ |
| DECRBY | ✔️ |
| GET | ✔️ |
| GETDEL | ✔️ |
| GETEX | ✔️ |
| GETRANGE | ✔️ |
| GETSET | ✔️ |
| LCS | ❌ |
| INCR | ✔️ |
| INCRBY | ✔️ |
| INCRBYFLOAT | ✔️ |
| MGET① | ✔️ |
| MSET① | ✔️ |
| MSETNX① | ✔️ |
| PSETEX | ✔️ |
| SET | ✔️ |
| SETEX | ✔️ |
| SETNX | ✔️ |
| SETRANGE | ✔️ |
| STRALGO | ❌ |
| STRLEN | ✔️ |
| SUBSTR | ✔️ |


### Generic

| 命令 | 是否支持 |
| --- | --- |
| COPY | ❌ |
| DEL① | ✔️ |
| DUMP | ✔️ |
| EXISTS① | ✔️ |
| EXPIRE | ✔️ |
| EXPIREAT | ✔️ |
| EXPIRETIME | ✔️ |
| KEYS | ✔️ |
| MIGRATE | ❌ |
| MOVE | ❌ |
| OBJECT | ❌ |
| PERSIST | ✔️ |
| PEXPIRE | ✔️ |
| PEXPIREAT | ✔️ |
| PEXPIRETIME | ✔️ |
| PTTL | ✔️ |
| RANDOMKEY | ✔️ |
| RENAME① | ✔️ 说明 最大支持 16MB 的 Key。 |
| RENAMENX① | ✔️ 说明 最大支持 16MB 的 Key。 |
| RESTORE | ✔️ |
| SCAN | ✔️ |
| SORT | ❌ |
| SORT_RO | ❌ |
| TOUCH | ❌ |
| TTL | ✔️ |
| TYPE | ✔️ |
| UNLINK① | ✔️ |
| WAIT | ❌ |


### Hash

| 命令 | 是否支持 |
| --- | --- |
| HDEL | ✔️ |
| HEXISTS | ✔️ |
| HGET | ✔️ |
| HGETALL | ✔️ |
| HINCRBY | ✔️ |
| HINCRBYFLOAT | ✔️ |
| HKEYS | ✔️ |
| HLEN | ✔️ |
| HMGET | ✔️ |
| HMSET | ✔️ |
| HRANDFIELD | ❌ |
| HSCAN | ✔️ |
| HSET | ✔️ |
| HSETNX | ✔️ |
| HSTRLEN | ✔️ |
| HVALS | ✔️ |


### Set

| 命令 | 是否支持 |
| --- | --- |
| SADD | ✔️ |
| SCARD | ✔️ |
| SDIFF① | ✔️ |
| SDIFFSTORE① | ✔️ |
| SINTER① | ✔️ |
| SINTERCARD | ❌ |
| SINTERSTORE① | ✔️ |
| SISMEMBER | ✔️ |
| SMEMBERS | ✔️ |
| SMISMEMBER | ✔️ |
| SMOVE① | ✔️ |
| SPOP | ✔️ |
| SRANDMEMBER | ✔️ |
| SREM | ✔️ |
| SSCAN | ✔️ |
| SUNION① | ✔️ |
| SUNIONSTORE① | ✔️ |


### Sorted Set

| 命令 | 是否支持 |
| --- | --- |
| BZMPOP | ❌ |
| BZPOPMAX | ❌ |
| BZPOPMIN | ❌ |
| ZADD | ✔️ |
| ZCARD | ✔️ |
| ZCOUNT | ✔️ |
| ZDIFF | ❌ |
| ZDIFFSTORE① | ✔️ |
| ZINCRBY | ✔️ |
| ZINTER | ❌ |
| ZINTERCARD | ❌ |
| ZINTERSTORE① | ✔️ |
| ZLEXCOUNT | ✔️ |
| ZMPOP | ❌ |
| ZMSCORE | ✔️ |
| ZPOPMAX | ✔️ |
| ZPOPMIN | ✔️ |
| ZRANDMEMBER | ❌ |
| ZRANGE | ✔️ |
| ZRANGEBYLEX | ✔️ |
| ZRANGEBYSCORE | ✔️ |
| ZRANGESTORE | ❌ |
| ZRANK | ✔️ |
| ZREM | ✔️ |
| ZREMRANGEBYLEX | ✔️ |
| ZREMRANGEBYRANK | ✔️ |
| ZREMRANGEBYSCORE | ✔️ |
| ZREVRANGE | ✔️ |
| ZREVRANGEBYLEX | ✔️ |
| ZREVRANGEBYSCORE | ✔️ |
| ZREVRANK | ✔️ |
| ZSCAN | ✔️ |
| ZSCORE | ✔️ |
| ZUNION | ❌ |
| ZUNIONSTORE① | ✔️ |


### Lists

| 命令 | 是否支持 |
| --- | --- |
| BLPOP | ❌ |
| BLMOVE | ❌ |
| BLMPOP | ❌ |
| BRPOP | ❌ |
| BRPOPLPUSH | ❌ |
| LINDEX | ✔️ |
| LINSERT | ✔️ |
| LLEN | ✔️ |
| LMOVE① | ✔️ |
| LMPOP① | ❌ |
| LPOP | ✔️ |
| LPOS | ✔️ |
| LPUSH | ✔️ |
| LPUSHX | ✔️ |
| LRANGE | ✔️ |
| LREM | ✔️ |
| LSET | ✔️ |
| LTRIM | ✔️ |
| RPOP | ✔️ |
| RPOPLPUSH① | ✔️ |
| RPUSH | ✔️ |
| RPUSHX | ✔️ |


### Bitmap

| 命令 | 是否支持 |
| --- | --- |
| BITCOUNT | ✔️ |
| BITFIELD | ✔️ |
| BITFIELD_RO | ❌ |
| BITOP① | ✔️ |
| BITPOS | ✔️ |
| GETBIT | ✔️ |
| SETBIT | ✔️ |


### 事务

重要

必须[设置参数](products/redis/documents/user-guide/modify-the-values-of-parameters-for-an-instance.md)txn-isolation-lock的值为yes才能使用事务相关命令。

| 命令 | 是否支持 |
| --- | --- |
| EXEC | ✔️ |
| DISCARD | ✔️ |
| MULTI | ✔️ |
| UNWATCH | ✔️ |
| WATCH① | ✔️ |


### LUA

重要

- 

必须[设置参数](products/redis/documents/user-guide/modify-the-values-of-parameters-for-an-instance.md)txn-isolation-lock的值为yes才能使用LUA脚本相关命令。

- 

执行EVAL、EVALSHA、EVAL_RO、EVALSHA_RO命令，至少需要传入一个Key且numkeys参数的值大于0。

| 命令 | 是否支持 |
| --- | --- |
| EVAL① | ✔️ |
| EVALSHA① | ✔️ |
| EVAL_RO① | ✔️ |
| EVALSHA_RO① | ✔️ |
| SCRIPT | ✔️ |


### GEO

| 命令 | 是否支持 |
| --- | --- |
| GEOADD | ✔️ |
| GEODIST | ✔️ |
| GEOHASH | ✔️ |
| GEOPOS | ✔️ |
| GEORADIUS | ✔️ |
| GEORADIUS_RO | ✔️ |
| GEORADIUSBYMEMBER | ✔️ |
| GEORADIUSBYMEMBER_RO | ✔️ |
| GEOSEARCH | ✔️ |
| GEOSEARCHSTORE① | ✔️ |


### Server management

| 命令 | 是否支持 |
| --- | --- |
| ACL | ❌ |
| BGREWRITEAOF | ❌ |
| BGSAVE | ❌ |
| BKLIST | ❌ |
| COMMAND | ✔️ |
| CONFIG | ❌ |
| DBSIZE | ✔️ |
| DEBUG | ❌ |
| FLUSHALL | ✔️ |
| FLUSHDB | ✔️ 重要 仅支持 FLUSHDB 命令同步执行模式，不支持异步执行模式。在生产环境中，请谨慎执行 FLUSHDB 命令。 |
| INFO | ✔️ |
| LASTSAVE | ❌ |
| LATENCY | ❌ |
| LOLWUT | ❌ |
| MEMORY | ❌ |
| MONITOR | ❌ |
| REWRITEAOF | ❌ |
| SAVE | ❌ |
| SHUTDOWN | ❌ |
| SLOWLOG | ✔️ |
| SWAPDB | ❌ |
| TIME | ✔️ |


### Connection management

| 命令 | 是否支持 |
| --- | --- |
| AUTH | ✔️ |
| CLIENT CACHING | ❌ |
| CLIENT GETNAME | ✔️ |
| CLIENT GETREDIR | ❌ |
| CLIENT ID | ❌ |
| CLIENT INFO | ❌ |
| CLIENT KILL | ✔️ |
| CLIENT LIST | ✔️ |
| CLIENT NO-EVICT | ❌ |
| CLIENT PAUSE | ❌ |
| CLIENT REPLY | ❌ |
| CLIENT SETNAME | ✔️ |
| CLIENT TRACKING | ❌ |
| CLIENT TRACKINGINFO | ❌ |
| CLIENT UNBLOCK | ❌ |
| CLIENT UNPAUSE | ❌ |
| ECHO | ✔️ |
| HELLO | ❌ |
| PING | ✔️ |
| QUIT | ✔️ |
| RESET | ❌ |
| SELECT | ✔️ |
| SENTINEL sentinels② | ✔️ |
| SENTINEL get-master-addr-by-name ② | ✔️ |


### Cluster management

| 命令 | 是否支持 |
| --- | --- |
| CLUSTER ADDSLOTS ② | ✔️ |
| CLUSTER ADDSLOTSRANGE | ❌ |
| CLUSTER BUMPEPOCH | ❌ |
| CLUSTER COUNT-FAILURE-REPORTS | ✔️ |
| CLUSTER COUNTKEYSINSLOT | ✔️ |
| CLUSTER DELSLOTS ② | ✔️ |
| CLUSTER DELSLOTSRANGE | ❌ |
| CLUSTER FAILOVER ② | ✔️ |
| CLUSTER FLUSHSLOTS | ❌ |
| CLUSTER FORGET ② | ✔️ |
| CLUSTER GETKEYSINSLOT ② | ✔️ |
| CLUSTER INFO | ✔️ |
| CLUSTER KEYSLOT | ✔️ |
| CLUSTER LINKS | ❌ |
| CLUSTER MEET ② | ✔️ |
| CLUSTER MYID | ❌ |
| CLUSTER NODES | ✔️ |
| CLUSTER REPLICAS | ❌ |
| CLUSTER REPLICATE ② | ✔️ |
| CLUSTER RESET ② | ✔️ |
| CLUSTER SAVECONFIG ② | ✔️ |
| CLUSTER SET-CONFIG-EPOCH ② | ✔️ |
| CLUSTER SETSLOT ② | ✔️ |
| CLUSTER SHARDS | ❌ |
| CLUSTER SLAVES | ✔️ |
| CLUSTER SLOTS | ✔️ |
| READONLY ② | ✔️ |
| READWRITE ② | ✔️ |


[上一篇：Redis兼容版](products/redis/documents/product-overview/tair-serverless-kv-redis-compatible-edition.md)[下一篇：连接Redis兼容版实例](products/redis/documents/product-overview/connect-to-a-tair-serverless-kv-instance.md)

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
