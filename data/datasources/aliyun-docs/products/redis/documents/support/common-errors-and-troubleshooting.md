# 连接Tair的常见报错与解决方案-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/support/common-errors-and-troubleshooting

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

# 常见报错

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍访问云数据库 Tair（兼容 Redis）时的常见报错与解决方法。

## 报错概览

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 分类 | 报错项 |
| --- | --- |
| Redis 通用异常 | [ERR illegal address](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR sentinel compatibility mode is disabled](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR max number of clients reached](products/redis/documents/support/common-errors-and-troubleshooting.md) [NOAUTH Authentication required](products/redis/documents/support/common-errors-and-troubleshooting.md) [WRONGPASS invalid username-password pair](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR invalid password](products/redis/documents/support/common-errors-and-troubleshooting.md) [Connection reset by peer](products/redis/documents/support/common-errors-and-troubleshooting.md) [UnknownHostException](products/redis/documents/support/common-errors-and-troubleshooting.md) [OOM command not allowed when used memory > 'maxmemory'](products/redis/documents/support/common-errors-and-troubleshooting.md) [WRONGTYPE Operation against a key holding the wrong kind of value](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR unknown command 'xxx'](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR command 'xxx' not support for your account](products/redis/documents/support/common-errors-and-troubleshooting.md) [NOPERM this user has no permissions to run the 'xxx'](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR FLUSHDB is not allowed in migrating mode](products/redis/documents/support/common-errors-and-troubleshooting.md) [CROSSSLOT Keys in request don't hash to the same slot](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR READONLY you can't write against a read only instance](products/redis/documents/support/common-errors-and-troubleshooting.md) [Filed to connect to any host resolved for DNS name](products/redis/documents/support/common-errors-and-troubleshooting.md) |
| redis-cli | [Connection reset by peer](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR must use ssl connection in ssl port](products/redis/documents/support/common-errors-and-troubleshooting.md) |
| Proxy（代理模式）通用异常 | [ERR client ip is not in whitelist](products/redis/documents/support/common-errors-and-troubleshooting.md) [NOWRITE You can't write against a non-write redis](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR syntax error](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR no such db node](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR 'xxx' command keys must in same slot](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR for redis cluster, eval/evalsha number of keys can't be negative or zero](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR request refused, too many pending request, now count xxx, beyond threshold xxx](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR redis temporary failure](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR redis temporary failure (ErrorCode 7002)](products/redis/documents/support/common-errors-and-troubleshooting.md) |
| Lua 脚本与事务（Transaction） | [NOSCRIPT No matching script. Please use EVAL.](products/redis/documents/support/common-errors-and-troubleshooting.md) [BUSY Redis is busy running a script. You can only call SCRIPT KILL or SHUTDOWN NOSAVE.](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR command eval not support for normal user](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR eval/evalsha command keys must be in same slot](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR bad lua script for redis cluster, all the keys that the script uses should be passed using the KEYS array](products/redis/documents/support/common-errors-and-troubleshooting.md) [EXECABORT Transaction discarded because of previous errors](products/redis/documents/support/common-errors-and-troubleshooting.md) [UNKILLABLE Sorry the script already executed write commands against the dataset.](products/redis/documents/support/common-errors-and-troubleshooting.md) [UNKILLABLE The busy script was sent by a master instance in the context of replication and cannot be killed.](products/redis/documents/support/common-errors-and-troubleshooting.md) [NOTBUSY No scripts in execution right now.](products/redis/documents/support/common-errors-and-troubleshooting.md) |
| Jedis 客户端 | [Could not get a resource from the pool](products/redis/documents/support/common-errors-and-troubleshooting.md) [java.net.SocketTimeoutException: connect timed out](products/redis/documents/support/common-errors-and-troubleshooting.md) [java.net.SocketTimeoutException: Read timed out](products/redis/documents/support/common-errors-and-troubleshooting.md) [No reachable node in cluster](products/redis/documents/support/common-errors-and-troubleshooting.md) [Caused by: java.lang.NumberFormatException: For input string: "6379@13028"](products/redis/documents/support/common-errors-and-troubleshooting.md) [No more cluster attempts left](products/redis/documents/support/common-errors-and-troubleshooting.md) [Unexpected end of stream](products/redis/documents/support/common-errors-and-troubleshooting.md) [java.lang.Long cannot be cast to java.util.List](products/redis/documents/support/common-errors-and-troubleshooting.md) [Broken pipe (Write failed)](products/redis/documents/support/common-errors-and-troubleshooting.md) [No way to dispatch this command to Redis Cluster because keys have different slots](products/redis/documents/support/common-errors-and-troubleshooting.md) |
| Lettuce 客户端 | [Connection to xxx not allowed. This Partition is not known in the cluster view.](products/redis/documents/support/common-errors-and-troubleshooting.md) [io.lettuce.core.RedisConnectionException: Unable to connect xxx](products/redis/documents/support/common-errors-and-troubleshooting.md) [java.nio.channels.UnresolvedAddressException](products/redis/documents/support/common-errors-and-troubleshooting.md) [ERR Unknown sentinel subcommand 'master'](products/redis/documents/support/common-errors-and-troubleshooting.md) [部分实例版本不支持](products/redis/documents/support/common-errors-and-troubleshooting.md) [RESP3](products/redis/documents/support/common-errors-and-troubleshooting.md) [协议，报错](products/redis/documents/support/common-errors-and-troubleshooting.md) [unknown command](products/redis/documents/support/common-errors-and-troubleshooting.md) |
| Redisson 客户端 | [org.redisson.client.RedisConnectionException: Unable to connect to Redis server xxx](products/redis/documents/support/common-errors-and-troubleshooting.md) [No enum constant org.redisson.cluster.ClusterNodeInfo.Flag.NOFAILOVER](products/redis/documents/support/common-errors-and-troubleshooting.md) |
| Spring Data Redis 客户端 | [NOPERM this user has no permissions to run the 'config|get' command](products/redis/documents/support/common-errors-and-troubleshooting.md) |
| StackExchange.Redis 客户端 | [Multiple databases are not supported on this server; cannot switch to database](products/redis/documents/support/common-errors-and-troubleshooting.md) |
| Predis 客户端 | [Error while reading line from the server.](products/redis/documents/support/common-errors-and-troubleshooting.md) |
| phpredis 客户端 | [Cannot assign requested address](products/redis/documents/support/common-errors-and-troubleshooting.md) [redis protocol error, got ' ' as reply type byte](products/redis/documents/support/common-errors-and-troubleshooting.md) [php_network_getaddresses: getaddrinfo failed: Temporary failure in name resolution](products/redis/documents/support/common-errors-and-troubleshooting.md) |
| Go-redis 客户端 | [panic: got 4 elements in cluster info address, expected 2 or 3](products/redis/documents/support/common-errors-and-troubleshooting.md) |
| node-redis 客户端 | [SCAN](products/redis/documents/support/common-errors-and-troubleshooting.md) [命令死循环或者返回数据为空](products/redis/documents/support/common-errors-and-troubleshooting.md) |


## Redis通用异常

### ERR illegal address

可能原因：未将客户端的IP地址添加至Tair实例的白名单中。

解决方法：将客户端的IP地址添加入至Tair实例的白名单中，具体操作请参见[连接诊断](products/redis/documents/user-guide/perform-diagnostics-on-connections.md)。

### ERR sentinel compatibility mode is disabled

可能原因：未开启Tair实例的Sentinel兼容。

解决方法：在控制台开启Sentinel兼容，具体操作请参见[开启](products/redis/documents/user-guide/enable-the-sentinel-compatible-mode.md)[Sentinel](products/redis/documents/user-guide/enable-the-sentinel-compatible-mode.md)[兼容](products/redis/documents/user-guide/enable-the-sentinel-compatible-mode.md)。

### ERR max number of clients reached

可能原因：客户端的连接数超过了Tair实例的最大连接数。

解决方法：

- 

检查客户端是否出现连接泄露，例如在Jedis客户端中，使用连接池后未调用close函数。

- 

通过[实例会话](products/redis/documents/user-guide/instance-sessions.md)查看当前连接实例的会话是否符合预期，您可以根据业务需求终止异常会话，或者通过[升级实例配置](products/redis/documents/user-guide/change-the-configurations-of-an-instance.md)，扩大连接数。

### NOAUTH Authentication required

可能原因：Tair实例设置了密码鉴权，但客户端没有提供密码或提供了错误的密码。

解决方法：请使用正确的账号密码进行访问，更多信息请参见[实例的登录方式](products/redis/documents/user-guide/logon-methods.md)。

说明

若您使用Lettuce 6.4.0.RELEASE至6.4.1.RELEASE版本的客户端，即使提供了正确密码，仍可能会出现该报错。该问题是由于Lettuce在支持Client setinfo时引入的，并已在6.4.2.RELEASE版本中修复，详情请参见[redis/lettuce#3035](https://github.com/redis/lettuce/pull/3035)。

如遇到该问题，您可以选择[手动切换](products/redis/documents/support/common-errors-and-troubleshooting.md)[RESP](products/redis/documents/support/common-errors-and-troubleshooting.md)[协议为](products/redis/documents/support/common-errors-and-troubleshooting.md)[RESP2](products/redis/documents/support/common-errors-and-troubleshooting.md)，或者将客户端升级至Lettuce 6.4.2.RELEASE版本及以上，如果您仍在使用Spring Data Redis客户端，建议使用Spring Data Redis 3.4.2及以上版本。

### WRONGPASS invalid username-password pair

可能原因：密码错误。

解决方法：请使用正确的账号密码进行访问，更多信息请参见[实例的登录方式](products/redis/documents/user-guide/logon-methods.md)。

说明

若实例使用Sentinel模式访问，请参见[使用](products/redis/documents/user-guide/use-the-sentinel-compatible-mode-to-connect-to-an-apsaradb-for-redis-instance.md)[Sentinel](products/redis/documents/user-guide/use-the-sentinel-compatible-mode-to-connect-to-an-apsaradb-for-redis-instance.md)[兼容模式连接实例](products/redis/documents/user-guide/use-the-sentinel-compatible-mode-to-connect-to-an-apsaradb-for-redis-instance.md)。

### ERR invalid password

可能原因：密码错误。

解决方法：请使用正确的账号密码进行访问，更多信息请参见[实例的登录方式](products/redis/documents/user-guide/logon-methods.md)。

说明

若在DMS中产生该报错，则有可能是DMS保存了之前登录的账号密码，而此时密码发生了修改。您可以在DMS数据库实例列表中，右键单击目标实例，选择编辑实例，在数据库密码文本框中输入新的密码进行重试。

### Connection reset by peer

可能原因：客户端连接被关闭，通常是由于客户端缓冲区异常而关闭客户端连接。

解决方法：检查应用侧代码或调整客户端Buffer的大小，更多信息请参见[Unexpected end of stream](products/redis/documents/support/common-errors-and-troubleshooting.md)章节。

### UnknownHostException

或failed to connect: xxx.redis.rds.aliyuncs.com could not be resolved。

可能原因：客户端无法正常解析Tair实例的域名地址。

解决方案：请设置正确的DNS服务器地址，更多信息请参见[解决因域名解析失败导致的连接问题](products/redis/documents/support/troubleshoot-connection-issues-caused-by-failed-dns-resolution.md)。

### OOM command not allowed when used memory > 'maxmemory'

可能原因：Tair实例已使用的内存超过该实例的最大配置（maxmemory）。

说明

如果是Tair集群实例，可能是其中一个节点已使用的内存已超过该节点的最大配置。

解决方法：

- 

若实例的总内存使用率达到100%，建议升级实例配置，更多信息请参见[升级实例配置](products/redis/documents/user-guide/change-the-configurations-of-an-instance.md)。

- 

若集群实例仅有单个节点的内存使用率达到100%，该实例中可能存在大Key，您可以通过[离线全量](products/redis/documents/user-guide/offline-key-analysis.md)[Key](products/redis/documents/user-guide/offline-key-analysis.md)[分析](products/redis/documents/user-guide/offline-key-analysis.md)或[实例诊断](products/redis/documents/user-guide/create-a-diagnostic-report.md)进行定位分析。

### WRONGTYPE Operation against a key holding the wrong kind of value

可能原因：命令使用错误，例如对String数据类型执行HASH命令。

解决方法：修改错误代码或命令，更多信息请参[Redis Commands](https://valkey.io/commands/)。

### ERR unknown command 'xxx'

可能原因：当前的实例不支持此命令。

如出现：ERR unknown command 'WAIT'，是由于云上集群架构代理模式不支持WAIT命令，需要用直连模式。

解决方法：检查当前实例版本的命令支持情况，更多信息请参见[Tair（企业版）命令支持与限制](https://help.aliyun.com/zh/tair/developer-reference/limits-on-commands-supported-by-tair#concept-1960075)、[Redis](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持与限制](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)及[集群架构与读写分离实例的命令限制](products/redis/documents/developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。

说明

最新小版本将提供更丰富的功能与稳定的服务，建议将实例的小版本升级到最新，具体操作请参见[升级小版本与代理版本](products/redis/documents/user-guide/update-the-minor-version.md)。

### ERR command 'xxx' not support for your account

可能原因：阿里云禁止用户执行某些Tair命令，或您手动在#no_loose_disabled-commands参数中配置了禁止执行的命令。更多信息请参见[Redis](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)和[禁用高风险命令](products/redis/documents/user-guide/disable-high-risk-commands.md)。

解决方法：若需执行您禁用的命令，您可以在#no_loose_disabled-commands参数中删除对应命令。

### NOPERM this user has no permissions to run the 'xxx'

可能原因：阿里云禁止用户执行某些Tair命令，或您手动在#no_loose_disabled-commands参数中配置了禁止执行的命令。更多信息请参见[Redis](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)和[禁用高风险命令](products/redis/documents/user-guide/disable-high-risk-commands.md)。

解决方法：若需执行您禁用的命令，您可以在#no_loose_disabled-commands参数中删除对应命令。

### ERR FLUSHDB is not allowed in migrating mode

可能原因：Tair云原生版集群架构实例在执行增加或减少数据节点时，禁止使用FLUSHDB或FLUSHALL命令。

解决方法：等待Tair云原生版集群架构实例执行增加或减少数据节点结束，更多信息请参见[调整集群分片数](products/redis/documents/user-guide/adjust-the-number-of-cluster-shards.md)。

### CROSSSLOT Keys in request don't hash to the same slot

可能原因：Tair集群架构直连模式不支持跨Slot执行涉及多Key的命令，例如DEL、MSET、MGET等。

解决方法：

- 

在执行操作命令前增加确认Key Slot的逻辑（例如通过CLUSTER KEYSLOT命令），确保单个命令执行的所有Key在一个Slot中。

- 

通过改造Key名称，增加Hash tags使其保证在同一个Slot，该方案在使用过程中需避免数据倾斜。

- 

改造实例为集群架构代理（Proxy）模式，Proxy模式支持跨Slot执行DEL、MGET、MSET等涉及多Key的命令，更多信息请参见[Tair Proxy](products/redis/documents/product-overview/features-of-proxy-nodes.md)[特性说明](products/redis/documents/product-overview/features-of-proxy-nodes.md)。

### ERR READONLY you can't write against a read only instance

可能原因：Tair实例在主备切换、升降配或小版本升级时，将出现秒级的连接闪断和30秒以内的只读状态。

解决方法：属于正常现象，实例会自动恢复，您无需进行任何操作。请提前为您的应用设计重连机制和异常处理的能力，更多信息请参见[升级实例配置](products/redis/documents/user-guide/change-the-configurations-of-an-instance.md)。

### Filed to connect to any host resolved for DNS name

可能原因：未正确配置白名单。

解决方案：将客户端的IP地址添加至实例的白名单中，具体操作请参见[设置](products/redis/documents/user-guide/configure-whitelists.md)[IP](products/redis/documents/user-guide/configure-whitelists.md)[白名单](products/redis/documents/user-guide/configure-whitelists.md)。

说明

如果是公网访问请在白名单中添加出口IP（访问[https://cip.cc/](https://cip.cc/)获取）。

## redis-cli异常

### Connection reset by peer

可能原因：标准架构，开启了TLS（SSL）加密连接，未带证书访问。

解决方案：

- 

携带证书访问，参考[TLS（SSL）加密连接实例](products/redis/documents/user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance-that-has-ssl-encryption-enabled.md)。

- 

若无需使用TLS（SSL）加密，请[关闭](products/redis/documents/user-guide/enable-tls-encryption.md)[TLS](products/redis/documents/user-guide/enable-tls-encryption.md)[加密](products/redis/documents/user-guide/enable-tls-encryption.md)后重试。

### ERR must use ssl connection in ssl port

可能原因：集群架构，开启了TLS（SSL）加密连接，未带证书访问。

解决方案：

- 

携带证书访问，参考[TLS（SSL）加密连接实例](products/redis/documents/user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance-that-has-ssl-encryption-enabled.md)。

- 

若无需使用TLS（SSL）加密，请[关闭](products/redis/documents/user-guide/enable-tls-encryption.md)[TLS](products/redis/documents/user-guide/enable-tls-encryption.md)[加密](products/redis/documents/user-guide/enable-tls-encryption.md)后重试。

## Proxy（代理模式）通用异常

### ERR client ip is not in whitelist

可能原因：未将客户端的IP地址添加至Tair实例的白名单中。

解决方法：将客户端的IP地址添加入至Tair实例的白名单中，具体操作请参见[连接诊断](products/redis/documents/user-guide/perform-diagnostics-on-connections.md)。

### NOWRITE You can't write against a non-write redis

或NOREAD You can't read against a non-read redis。

可能原因：实例处于欠费或到期状态，实例状态显示为已锁定。

解决方法：对账号进行充值，或对到期的实例进行续费，更多信息请参见[到期与欠费](products/redis/documents/product-overview/expiration-and-overdue-payments.md)。

### ERR syntax error

可能原因：命令语法错误，例如需要传入4个参数，实际仅传入3个参数。

解决方法：检查命令格式是否正确，更多信息请参[Redis Commands](https://valkey.io/commands/)。

### ERR no such db node

可能原因：使用阿里云自研的Tair命令时，传入的db node错误。

解决方法：传入正确的db node，db node需小于分片数量，更多信息请参见[阿里云自研的](products/redis/documents/developer-reference/in-house-commands-for-tair-instances-in-proxy-mode.md)[Proxy](products/redis/documents/developer-reference/in-house-commands-for-tair-instances-in-proxy-mode.md)[命令](products/redis/documents/developer-reference/in-house-commands-for-tair-instances-in-proxy-mode.md)。

### ERR 'xxx' command keys must in same slot

可能原因：在Tair集群架构实例执行的事务或脚本中，存在跨Slot的Key。

解决方法：改造事务或脚本，您可以通过CLUSTER KEYSLOT命令获取目标Key的Hash Slot。

重要

Tair集群架构实例会根据CRC算法将Key均匀的写入不同Slot中。若您希望将多个Key写入到一个Slot中，您可以使用Hash Tags，但该方法若使用不当容易造成数据倾斜，请谨慎使用。

### ERR for redis cluster, eval/evalsha number of keys can't be negative or zero

可能原因：执行EVAL和EVALSHA命令未传入Key或numkeys参数的值未大于0。

解决方法：执行EVAL和EVALSHA命令时，至少需要传入一个Key且numkeys参数的值大于0，更多信息请参见[Lua](products/redis/documents/support/usage-of-lua-scripts.md)[脚本基本语法](products/redis/documents/support/usage-of-lua-scripts.md)。

### ERR request refused, too many pending request, now count xxx, beyond threshold xxx

可能原因：由于客户端使用了不合理的Pipeline，Tair后端堆积了过多未处理的Request，新请求被拒绝。

解决方法：减少Pipeline的请求数量。

### ERR redis temporary failure

可能原因：部分Tair子实例访问超时，可能是网络抖动、连接数到达上限导致断链、实例正在进行主备切换或执行慢查询等导致。

解决方法：属于正常现象，实例会自动恢复，您无需进行任何操作。请提前为您的应用设计重连机制和异常处理的能力。

### ERR redis temporary failure (ErrorCode 7002)

可能原因：部分Tair子实例访问超时，可能是实例正在变配或正在进行主备切换导致。

解决方法：属于正常现象，实例会自动恢复，您无需进行任何操作。请提前为您的应用设计重连机制和异常处理的能力。

## Lua脚本与事务（Transaction）

### NOSCRIPT No matching script. Please use EVAL.

可能原因：使用EVALSHA命令时，若SHA1值对应的脚本未缓存至Tair中。

解决方法：通过EVAL命令或SCRIPT LOAD命令将目标脚本缓存至Tair中后进行重试，更多信息请参见[NOSCRIPT](products/redis/documents/support/usage-of-lua-scripts.md)[错误](products/redis/documents/support/usage-of-lua-scripts.md)。

### BUSY Redis is busy running a script. You can only call SCRIPT KILL or SHUTDOWN NOSAVE.

可能原因：处理Lua脚本超时。

解决方法：通过SCRIPT KILL命令终止Lua脚本或等待Lua脚本执行结束，更多信息请参见[Lua](products/redis/documents/support/usage-of-lua-scripts.md)[脚本超时错误](products/redis/documents/support/usage-of-lua-scripts.md)。

### ERR command eval not support for normal user

可能原因：无法执行EVAL的相关命令。

解决方法：请将实例的小版本升级至最新，具体操作请参见[升级小版本与代理版本](products/redis/documents/user-guide/update-the-minor-version.md)。

### ERR eval/evalsha command keys must be in same slot

可能原因：Lua脚本操作的Key不在同一个Slot（槽）中，该报错通常产生于集群实例中。

解决方法：改造Lua脚本，您可以通过CLUSTER KEYSLOT命令获取目标Key的Hash Slot，更多信息请参见[集群架构特殊限制](products/redis/documents/support/usage-of-lua-scripts.md)。

### ERR bad lua script for redis cluster, all the keys that the script uses should be passed using the KEYS array

可能原因：Proxy（代理）节点的Lua脚本限制。

解决方法：所有Key都应该由KEYS数组来传递，例如EVAL "return redis.call('mget', KEYS[1], KEYS[2])" 2 foo {foo}bar，不能使用Lua变量替换KEYS，更多信息请参见[集群架构特殊限制](products/redis/documents/support/usage-of-lua-scripts.md)。

### EXECABORT Transaction discarded because of previous errors

可能原因：事务中的命令执行失败，可能是命令语法错误或运行错误等。

解决方法：检查代码逻辑，修复错误命令。

### UNKILLABLE Sorry the script already executed write commands against the dataset.

可能原因：当前Lua脚本已执行写命令，此时SCRIPT KILL命令无法生效。

解决方法：在控制台的实例列表页面，找到对应实例，单击操作列的重启，更多信息请参见[重启实例](products/redis/documents/user-guide/restart-one-or-more-apsaradb-for-redis-instances.md)。

### UNKILLABLE The busy script was sent by a master instance in the context of replication and cannot be killed.

可能原因：当前Lua脚本已经被Master节点发给自己的replica节点，此时SCRIPT KILL命令无法生效。

解决方法：在控制台的实例列表页面，找到对应实例，单击操作列的重启，更多信息请参见[重启实例](products/redis/documents/user-guide/restart-one-or-more-apsaradb-for-redis-instances.md)。

### NOTBUSY No scripts in execution right now.

可能原因：当前没有正在运行Lua脚本。

解决方法：无需处理，不要调用SCRIPT KILL命令。

## Jedis客户端

### Could not get a resource from the pool

可能原因：无法从连接池获取到Jedis连接。

- 

当blockWhenExhausted参数为true（默认）时，若连接池没有可用的Jedis连接，客户端通常会等待一段时间（等待时间由maxWaitMillis参数决定，单位为毫秒），若长时间没有获取到可用的Jedis连接，会出现如下异常：

redis.clients.jedis.exceptions.JedisConnectionException: Could not get a resource from the pool … Caused by: java.util.NoSuchElementException: Timeout waiting for idle object at org.apache.commons.pool2.impl.GenericObjectPool.borrowObject(GenericObjectPool.java:449)

- 

当blockWhenExhausted参数为false时，若连接池没有可用的Jedis连接，则会立即出现如下异常：

redis.clients.jedis.exceptions.JedisConnectionException: Could not get a resource from the pool … Caused by: java.util.NoSuchElementException: Timeout waiting for idle object at org.apache.commons.pool2.impl.GenericObjectPool.borrowObject(GenericObjectPool.java:449)

解决方法：您可以从如下几个方面进行排查。

- 

连接泄露

JedisPool默认maxTotal值为8，从如下代码得知，从JedisPool中获取了8个Jedis资源，但没有归还资源。因此，在第9次尝试获取Jedis资源时，无法调用jedisPool.getResource().ping()。

GenericObjectPoolConfig poolConfig = new GenericObjectPoolConfig(); JedisPool jedisPool = new JedisPool(poolConfig, "127.0.0.1", 6379); // 向JedisPool借用8次连接，但是没有执行归还操作。 for (int i = 0; i < 8; i++) { Jedis jedis = null; try { jedis = jedisPool.getResource(); jedis.ping(); } catch (Exception e) { logger.error(e.getMessage(), e); } } jedisPool.getResource().ping();

推荐使用如下规范代码。

Jedis jedis = null; try { jedis = jedisPool.getResource(); // 具体的命令。 jedis.executeCommand() } catch (Exception e) { // 如果命令有Key，建议在错误日志中把Key打印出来，对于集群架构来说，可通过Key定位到具体节点。 logger.error(e.getMessage(), e); } finally { // 注意：这里不是关闭连接，在JedisPool模式下，Jedis会被归还给资源池。 if (jedis != null) jedis.close(); }

- 

maxTotal值设置得过小

当业务并发量大时，可能会由于maxTotal值设置的过小导致异常。例如，一次命令运行时间的平均耗时约为1ms（Borrow|Return resource+ Jedis执行命令 + 网络时间），一个连接的QPS大约为1000，业务期望的QPS为50000，则理论上需要的maxTotal值为50000 / 1000 = 50。

在该情况下，您可以在客户端所在的机器上执行下述命令，该命令返回的结果为连接客户端的连接数，您可以根据该数值对maxTotal值进行调整。

netstat -an | grep 6379 | grep EST | wc -l

- 

Jedis连接阻塞

当Tair实例发生阻塞时（例如慢查询等原因），所有连接会在超时时间范围内等待，当并发量较大时，会造成连接池资源不足，更多信息请参见[connect timed out](products/redis/documents/support/common-errors-and-troubleshooting.md)。

- 

Jedis连接被拒绝

从JedisPool中获取连接时，由于没有空闲连接，需要重新生成一个Jedis连接，但是连接被拒绝，异常示例如下：

redis.clients.jedis.exceptions.JedisConnectionException: Could not get a resource from the pool at redis.clients.util.Pool.getResource(Pool.java:50) at redis.clients.jedis.JedisPool.getResource(JedisPool.java:99) at TestAdmin.main(TestAdmin.java:14) Caused by: redis.clients.jedis.exceptions.JedisConnectionException: java.net.ConnectException: Connection refused at redis.clients.jedis.Connection.connect(Connection.java:164) at redis.clients.jedis.BinaryClient.connect(BinaryClient.java:80) at redis.clients.jedis.BinaryJedis.connect(BinaryJedis.java:1676) at redis.clients.jedis.JedisFactory.makeObject(JedisFactory.java:87) at org.apache.commons.pool2.impl.GenericObjectPool.create(GenericObjectPool.java:861) at org.apache.commons.pool2.impl.GenericObjectPool.borrowObject(GenericObjectPool.java:435) at org.apache.commons.pool2.impl.GenericObjectPool.borrowObject(GenericObjectPool.java:363) at redis.clients.util.Pool.getResource(Pool.java:48) ... 2 more Caused by: java.net.ConnectException: Connection refused at java.net.PlainSocketImpl.socketConnect(Native Method) at java.net.AbstractPlainSocketImpl.doConnect(AbstractPlainSocketImpl.java:339) at java.net.AbstractPlainSocketImpl.connectToAddress(AbstractPlainSocketImpl.java:200) at java.net.AbstractPlainSocketImpl.connect(AbstractPlainSocketImpl.java:182) at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:392) at java.net.Socket.connect(Socket.java:579) at redis.clients.jedis.Connection.connect(Connection.java:158) ... 9 more

可以从at redis.clients.jedis.Connection.connect(Connection.java:158)中看出，实际是在创建一个Socket连接，并调用connect函数，但是被拒绝连接，如下为Jedis源码。

socket.setSoLinger(true, 0); 158: socket.connect(new InetSocketAddress(host, port), connectionTimeout);

通常情况下，该问题需要排查Tair的域名配置是否正确、该段时间网络是否正常。

### java.net.SocketTimeoutException: connect timed out

可能原因：客户端连接Tair实例超时。

解决方法：更多信息请参见[连接问题排查流程](products/redis/documents/support/how-do-i-troubleshoot-connection-issues-in-apsaradb-for-redis.md)。

### java.net.SocketTimeoutException: Read timed out

可能原因：网络不稳定、读写超时时间过短、存在慢查询或发生阻塞等原因造成Jedis API调用超时。

解决方法：适当增大超时时间，或进行[实例诊断](products/redis/documents/user-guide/create-a-diagnostic-report.md)，查看实例在对应时间点是否存在性能问题或异常。

说明

若在DMS中产生该报错，则有可能是实例专有网络的连接地址或端口被修改了。您可以在DMS数据库实例列表中，右键单击目标实例，选择编辑实例，然后选择录入方式为连接串地址，将修改后的实例连接地址填写到连接串地址文本框中进行重试。

### No reachable node in cluster

可能原因：JedisCluster地址无法访问。

解决方法：若是首次访问Tair实例，请检查是否将客户端的IP地址添加至Tair白名单中或客户端的网络情况；若不是首次访问Tair实例，可以进行[实例诊断](products/redis/documents/user-guide/create-a-diagnostic-report.md)，进行问题定位。

### Caused by: java.lang.NumberFormatException: For input string: "6379@13028"

可能原因：Jedis 2.8.0及以下版本引入了ClusterNodeInformationParser来解析cluster slots返回值，但Redis后续更改了此命令返回值类型，所以报错NumberFormatException。

解决方法：将Jedis升级至2.9.0及以上版本。

### No more cluster attempts left

可能原因：JedisCluster在API超时之后会默认重试5次（MaxAttempts，默认为5），并且在均失败之后抛出此错误。

解决方法：适当增大超时时间或进行[实例诊断](products/redis/documents/user-guide/create-a-diagnostic-report.md)。

### Unexpected end of stream

可能原因：Jedis缓冲区异常，您可以从如下几个方面进行排查。

- 

多个线程使用一个Jedis连接

通常情况下，一个线程使用一个Jedis连接。例如下面代码就是两个线程共用了一个Jedis连接：

new Thread(new Runnable() { public void run() { for (int i = 0; i < 100; i++) { jedis.get("hello"); } } }).start(); new Thread(new Runnable() { public void run() { for (int i = 0; i < 100; i++) { jedis.hget("haskey", "f"); } } }).start();

为避免出现这种情况，您可以使用JedisPool管理Jedis连接，实现线程安全。

- 

长时间闲置连接

长时间闲置连接会被服务端主动断开，请查询实例的timeout参数配置、Jedis连接池配置，确定是否需要进行空闲超时检测。

说明

默认设置下，即使某个客户端已经空闲了很长时间，Tair也不会主动断开与该客户端的连接，若您调整过timeout参数，则可能会遇到该问题。更多信息请参见[设置客户端连接的空闲时间](products/redis/documents/user-guide/specify-a-timeout-period-for-client-connections.md)。

解决方法：检查是否有多线程共用Jedis代码或由于长时间闲置连接造成服务端断开连接。

### java.lang.Long cannot be cast to java.util.List

可能原因：若多个线程操作同一个Jedis连接就会返回该报错，Jedis本身存在线程安全问题。

解决方法：Jedis的正确使用方法是一个线程操作一个Jedis。您可以使用JedisPool（非Jedis）避免该问题。

### Broken pipe (Write failed)

可能原因：在Jedis单连接模式（未使用JedisPool）下超时后，客户端关闭了Socket，此时若您继续调用读写接口写入数据，会返回该报错。

解决方法：Jedis的正确使用方法是一个线程操作一个Jedis。您可以使用JedisPool（非Jedis）避免该问题。

### No way to dispatch this command to Redis Cluster because keys have different slots

可能原因：JedisCluster操作的Key不在同一个Slot（槽）中。

解决方法：通过Hash tags对Key进行改造。

说明

您也可以使用Proxy（代理）模式屏蔽集群的限制。

## Lettuce客户端

### Connection to xxx not allowed. This Partition is not known in the cluster view.

可能原因：Lettuce客户端在默认情况下，配置为refreshOption = null , validateClusterNodeMembership = true，表示开启validateClusterNodeMembership检测。在Tair实例地址发生路由变化后，由于没有开启refreshOption，即不会更新路由表，此时validateClusterNodeMembership检测就会返回该报错。

解决方法：配置refreshOption选项，并且设置validateClusterNodeMembership为false，更多信息请参见[Lettuce](products/redis/documents/user-guide/use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)。

### io.lettuce.core.RedisConnectionException: Unable to connect xxx

可能原因：客户端连接Tair实例超时。

解决方法：更多信息请参见[连接问题排查流程](products/redis/documents/support/how-do-i-troubleshoot-connection-issues-in-apsaradb-for-redis.md)。

### java.nio.channels.UnresolvedAddressException

可能原因：大概率是Netty版本冲突。

解决方法：检查Netty依赖，建议选择较高的版本，更多信息请参见[spring-projects/spring-boot#14307](https://github.com/spring-projects/spring-boot/issues/14307)。

### ERR Unknown sentinel subcommand 'master'

可能原因：Lettuce在[master-replica](https://github.com/lettuce-io/lettuce-core/wiki/Master-Replica)Sentinel模式下会向Redis实例发送Sentinel master/slave命令，而Tair实例在Sentinel兼容模式下仅支持Sentinel get-master-addr-by-name命令，故产生该报错。

解决方法：修改代码为普通模式（非Sentinel），Tair采用自研的高可用服务HA组件，无需Sentinel。

### 部分实例版本不支持RESP3协议，报错unknown command

可能原因：Redis 6.0及以上版本支持了RESP3协议，可通过HELLO命令切换RESP协议。但部分低版本实例不支持HELLO命令，可能会存在兼容性问题。

解决方法：您可以直接在程序中指定以RESP2协议访问Tair实例，示例如下：

client.setOptions(ClientOptions.builder() .protocolVersion(ProtocolVersion.RESP2) .build());

若使用Spring-data-redis with Lettuce，示例如下：

LettuceClientConfiguration lettuceClientConfiguration = LettuceClientConfiguration.builder(). clientOptions(ClientOptions.builder().protocolVersion(ProtocolVersion.RESP2).build()).build(); return new LettuceConnectionFactory(redisClusterConfiguration, lettuceClientConfiguration);

## Redisson客户端

### org.redisson.client.RedisConnectionException: Unable to connect to Redis server xxx

可能原因：客户端连接Tair实例超时。

解决方法：更多信息请参见[连接问题排查流程](products/redis/documents/support/how-do-i-troubleshoot-connection-issues-in-apsaradb-for-redis.md)。

### No enum constant org.redisson.cluster.ClusterNodeInfo.Flag.NOFAILOVER

可能原因：Redisson低版本Bug，更多信息请参见[redisson/redisson#2399](https://github.com/redisson/redisson/issues/2399)。

解决方法：将Redisson升级至3.11.6及以上版本。

## Spring Data Redis客户端

### NOPERM this user has no permissions to run the 'config|get' command

可能原因：在实例信息页确认您的实例版本为Redis 7.0。云数据库 Tair（兼容 Redis）的7.0版本禁用CONFIG命令。

应用启动时，Spring Data Redis会执行CONFIG SET命令动态设置notify-keyspace-events参数来启用KeyspaceEventMessageListener功能。因为CONFIG GET/SET命令被禁用，导致启动时报错。

解决方法：设置keyspaceNotificationsConfigParameter为空，绕过该问题，完整代码见[SpringRedisTest.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20251027/nghdhn/springredistest.zip)，更多信息请参见[Spring Data Redis](https://docs.spring.io/spring-data/data-redis/docs/current-SNAPSHOT/reference/html/)。

@EnableRedisRepositories(enableKeyspaceEvents = RedisKeyValueAdapter.EnableKeyspaceEvents.ON_STARTUP, keyspaceNotificationsConfigParameter = "")

同时，如果监听了KeyExpirationListener，需要在构造函数中设置 keyspaceNotificationsConfigParameter 为空。

public RedisKeyExpirationListener(RedisMessageListenerContainer redisMessageListenerContainer) { super(redisMessageListenerContainer); setKeyspaceNotificationsConfigParameter(""); // 重要 }

## StackExchange.Redis客户端

### Multiple databases are not supported on this server; cannot switch to database

可能原因：集群架构不支持执行SELECT命令。

解决方法：将cluster_compat_enable参数设置为0（即关闭原生Redis Cluster语法兼容），具体操作请参见[设置参数](products/redis/documents/user-guide/modify-the-values-of-parameters-for-an-instance.md)，然后重启客户端应用后重试。

## Predis客户端

### Error while reading line from the server.

可能原因：读取超时，您可能正在执行一个慢查询。

解决方法：适当增大超时时间或将客户端的read_write_timeout参数改为0或-1，更多信息请参见[Predis questions](https://stackoverflow.com/questions/11776029/predis-is-giving-error-while-reading-line-from-server/11931651#11931651)。

## phpredis客户端

### Cannot assign requested address

可能原因：客户端通过短连接访问Tair实例时，产生该报错。

解决方法：使用pconnect替换connect的连接方式，或修改客户端所在ECS实例的tcp_max_tw_buckets内核参数，更多信息请参见[Cannot assign requested address](products/redis/documents/support/what-do-i-do-if-the-cannot-assign-requested-address-error-is-returned-when-i-access-apsaradb-for-redis-over-short-lived-connections.md)[报错](products/redis/documents/support/what-do-i-do-if-the-cannot-assign-requested-address-error-is-returned-when-i-access-apsaradb-for-redis-over-short-lived-connections.md)。

### redis protocol error, got ' ' as reply type byte

可能原因：phpredis低版本Bug，更多信息请参见[phpredis/phpredis#1585](https://github.com/phpredis/phpredis/issues/1585)。

解决方法：将phpredis升级至最新版。

### php_network_getaddresses: getaddrinfo failed: Temporary failure in name resolution

解决方案：请设置正确的DNS服务器地址，更多信息请参见[解决因域名解析失败导致的连接问题](products/redis/documents/support/troubleshoot-connection-issues-caused-by-failed-dns-resolution.md)。

可能原因：客户端无法正常解析Tair实例的域名地址。

## Go-redis客户端

### panic: got 4 elements in cluster info address, expected 2 or 3

可能原因：您的Redis版本为7.0及以上，但未使用兼容的Go-redis客户端版本导致，更多信息请参见[redis/go-redis#2085](https://github.com/go-redis/redis/issues/2085)。

解决方案：升级、使用Go-redis客户端9.0及以上版本。

## node-redis客户端

### SCAN命令死循环或者返回数据为空

可能原因：SCAN命令返回的Cursor值可能超过了JavaScript最大可精确表达的数值[Number.MAX_SAFE_INTEGER](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)，导致Cursor不准确，引发死循环，更多信息请参见[redis/node-redis#2561](https://github.com/redis/node-redis/issues/2561)。

解决方案：将node-redis客户端升级至5.0.0及以上版本。

[上一篇：服务支持](products/redis/documents/support.md)[下一篇：常见问题](products/redis/documents/support/faq.md)

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
