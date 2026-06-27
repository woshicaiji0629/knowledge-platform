# 通过客户端程序连接Tair-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance

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

# 客户端程序连接教程

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库 Tair（兼容 Redis）实例与原生Redis完全兼容，支持所有原生Redis支持的客户端，连接数据库的方式也基本相同，您可以根据自身应用特点选用任何兼容Redis协议的客户端程序。

## 免费试用

阿里云免费试用面向符合条件的新用户，提供一定时间段的免费试用阿里云产品的权益，更多信息请参见[免费试用](https://free.aliyun.com/?searchKey=redis)。

## 前提条件

根据客户端程序的部署位置，完成下述操作：

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

| 客户端程序部署位置 | 需完成的操作 |
| --- | --- |
| [ECS](products/ecs/documents/user-guide/what-is-ecs.md) [实例](products/ecs/documents/user-guide/what-is-ecs.md) （推荐） | 确保 ECS 实例与实例属于同一专有网络（即实例基本信息中的专有网络 ID 一致）。 说明 如果专有网络不同，您可以 [更换](products/ecs/documents/user-guide/change-the-vpc-of-an-ecs-instance.md) [ECS](products/ecs/documents/user-guide/change-the-vpc-of-an-ecs-instance.md) [实例所属的专有网络](products/ecs/documents/user-guide/change-the-vpc-of-an-ecs-instance.md) 。 如果网络类型不同，例如 ECS 实例为经典网络，实例为专有网络。如何连接，请参见 [ECS](products/redis/documents/connect-an-ecs-instance-to-an-apsaradb-for-redis-instance-in-different-types-of-networks.md) [实例与](products/redis/documents/connect-an-ecs-instance-to-an-apsaradb-for-redis-instance-in-different-types-of-networks.md) [Redis](products/redis/documents/connect-an-ecs-instance-to-an-apsaradb-for-redis-instance-in-different-types-of-networks.md) [实例的网络类型不同时如何连接](products/redis/documents/connect-an-ecs-instance-to-an-apsaradb-for-redis-instance-in-different-types-of-networks.md) 。 [获取](products/ecs/documents/user-guide/network-faq.md) [ECS](products/ecs/documents/user-guide/network-faq.md) [实例的内网](products/ecs/documents/user-guide/network-faq.md) [IP](products/ecs/documents/user-guide/network-faq.md) [地址](products/ecs/documents/user-guide/network-faq.md) 。 将 ECS 实例的内网 IP 地址 [添加至实例的白名单](products/redis/documents/user-guide/configure-whitelists.md) 中。 |
| 本地 | 获取本地设备公网 IP 地址。以下是不同系统通过命令方式获取本地设备公网 IP 地址的参考方法： Linux 操作系统：打开终端，输入 curl ifconfig.me 命令后回车。 Windows 操作系统：打开命令提示符，输入 curl ip.me 命令后回车。 macOS 操作系统：打开终端，输入 curl ifconfig.me 命令后回车。 将本地客户端的公网 IP 地址 [添加至实例的白名单](products/redis/documents/user-guide/configure-whitelists.md) 中。 实例默认仅提供内网连接地址，通过公网连接时您需要手动 [申请公网连接地址](products/redis/documents/user-guide/apply-for-a-public-endpoint-for-an-apsaradb-for-redis-instance.md) 。 |


## 注意事项

- 

如果您的实例为[集群架构](products/redis/documents/product-overview/cluster-master-replica-instances.md)或[读写分离架构](products/redis/documents/product-overview/read-or-write-splitting-instances-1.md)，实例默认会提供Proxy（代理）节点的连接地址，连接方式与连接标准架构的实例相同。

说明

集群架构的实例通过[直连地址](products/redis/documents/user-guide/enable-the-direct-connection-mode.md)连接时，连接方式与连接开源Redis Cluster相同。

- 

如果实例开启了[专有网络免密访问](products/redis/documents/user-guide/enable-password-free-access.md)，同一专有网络下的客户端程序无需设置密码即可连接实例。

## 如何获取连接信息

在使用客户端程序连接Tair（以及Redis开源版）实例时，通常您需要获取以下信息并设置在代码中：

- 

- 

- 

- 

| 需获取的信息 | 获取方式 |
| --- | --- |
| 实例的连接地址 | 访问 [实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou) ，在上方选择地域，然后单击目标实例 ID。 在 连接信息 区域，可查看到各连接类型的地址和端口号。 说明 实例支持多种连接地址，推荐使用专有网络连接，可获得更高的安全性和更低的网络延迟。更多信息，请参见 [查看连接地址](products/redis/documents/user-guide/view-endpoints.md) 。 |
| 端口号 | 端口号默认为 6379，您也可以自定义端口号。具体操作，请参见 [修改连接地址或端口](products/redis/documents/user-guide/change-the-endpoint-or-port-number-of-an-instance.md) 。 |
| 实例的账号（部分客户端程序无需设置） | 实例默认会创建一个以实例 ID 命名的账号（例如 r-bp10noxlhcoim2****），您也可以创建一个新的账号并赋予权限。更多信息，请参见 [创建与管理账号](products/redis/documents/user-guide/create-and-manage-database-accounts.md) 。 |
| 账号的密码 | 根据选取账号的不同，密码的填写格式有一定区别： 默认账号（以实例 ID 命名的账号）：直接填写密码即可。 新创建的账号：密码格式为 <user>:<password> 。例如自定义账号为 testaccount ，密码为 Rp829dlwa ，密码需填写为 testaccount:Rp829dlwa 。 说明 如果通过第三方数据库管理工具（例如 RDM 等）连接实例，请在密码框中输入 user:password 进行连接。 如果忘记密码，您可以重置密码。具体操作，请参见 [修改或重置密码](products/redis/documents/user-guide/change-or-reset-the-password.md) 。 |


## 常见客户端示例

关于Tair（以及Redis开源版）支持的客户端列表请参见[Redis Clients](http://redis.io/clients)。

重要

本文仅列举常见客户端程序的代码示例，帮助您快速连接。

### Jedis

本示例使用Maven方式进行构建，您也可以手动下载[Jedis](https://github.com/redis/jedis/releases)客户端。

- 

打开编译器，新建项目。

- 

在pom.xml文件中添加下述代码。

本示例的Jedis版本为4.3.0。

<dependency> <groupId>redis.clients</groupId> <artifactId>jedis</artifactId> <version>4.3.0</version> </dependency>

- 

在编辑器中输入下述代码，然后根据注释提示修改代码。

import redis.clients.jedis.Jedis; import redis.clients.jedis.JedisPool; import redis.clients.jedis.JedisPoolConfig; public class JedisExample { public static void main(String[] args) { JedisPoolConfig config = new JedisPoolConfig(); // 最大空闲连接数，需自行评估，不超过Redis实例的最大连接数。 config.setMaxIdle(200); // 最大连接数，需自行评估，不超过Redis实例的最大连接数。 config.setMaxTotal(300); config.setTestOnBorrow(false); config.setTestOnReturn(false); // 分别将host和password的值替换为实例的连接地址、密码。 String host = "r-bp1s1bt2tlq3p1****pd.redis.rds.aliyuncs.com"; // 默认账号password可直接填写密码；新建账号password填写格式为 账号:密码，例如新建账号testaccount，密码Rp829dlwa，password填写testaccount:Rp829dlwa。 String password = "r-bp1s1bt2tlq3p1****:Database123"; JedisPool pool = new JedisPool(config, host, 6379, 3000, password); Jedis jedis = null; try { jedis = pool.getResource(); // 执行相关操作，示例如下。 jedis.set("foo10", "bar"); System.out.println(jedis.get("foo10")); jedis.zadd("sose", 0, "car"); jedis.zadd("sose", 0, "bike"); System.out.println(jedis.zrange("sose", 0, -1)); } catch (Exception e) { // 超时或其他异常处理。 e.printStackTrace(); } finally { if (jedis != null) { jedis.close(); } } pool.destroy(); // 当应用退出，需销毁资源时，调用此方法。此方法会断开连接、释放资源。 } }

- 

运行上述Project，预期会返回如下结果：

bar [bike, car]

重要

在使用Jedis的过程中，如果设置了一些不合理的参数或错误使用某些功能可能会引起报错，关于如何排查，请参见[常见报错](products/redis/documents/support/common-errors-and-troubleshooting.md)。

### PhpRedis

- 

下载并安装[PhpRedis](https://github.com/phpredis/phpredis)客户端。

- 

在PHP编辑器中输入下述代码，然后根据注释提示修改代码。

本示例的PHP版本为8.2.1、PhpRedis版本为5.3.7。

<?php /* 分别将host和port的值替换为实例的连接地址、端口号。 */ $host = "r-bp10noxlhcoim2****.redis.rds.aliyuncs.com"; $port = 6379; /* 分别将user和pwd的值替换为实例的账号和密码 */ $user = "testaccount"; $pwd = "Rp829dlwa"; $redis = new Redis(); if ($redis->connect($host, $port) == false) { die($redis->getLastError()); } if ($redis->auth([$user, $pwd]) == false) { die($redis->getLastError()); } /* 完成认证后可执行数据库操作，下述代码为您提供SET与GET的使用示例。 */ if ($redis->set("foo", "bar") == false) { die($redis->getLastError()); } $value = $redis->get("foo"); echo $value; ?>

- 

执行上述代码。

说明

常见报错与解决方法：

- 

Cannot assign requested address，原因分析及排查方法，请参见[Cannot assign requested address](products/redis/documents/support/what-do-i-do-if-the-cannot-assign-requested-address-error-is-returned-when-i-access-apsaradb-for-redis-over-short-lived-connections.md)[报错](products/redis/documents/support/what-do-i-do-if-the-cannot-assign-requested-address-error-is-returned-when-i-access-apsaradb-for-redis-over-short-lived-connections.md)。

- 

redis protocol error, got ' ' as reply type byte，请升级您的PhpRedis客户端版本，参见[phpredis/phpredis#1585](https://github.com/phpredis/phpredis/issues/1585)。

### redis-py

- 

下载并安装[redis-py](https://github.com/andymccurdy/redis-py)客户端。

- 

在Python编辑器中输入下述代码，然后根据注释提示修改代码。

本示例的Python版本为3.9、redis-py版本为4.4.1。

#!/usr/bin/env python #-*- coding: utf-8 -*- import redis # 分别将host和port的值替换为实例的连接地址、端口号。 host = 'r-bp10noxlhcoim2****.redis.rds.aliyuncs.com' port = 6379 # 将pwd的值替换为实例的密码。 # 默认账号password可直接填写密码；新建账号password填写格式 账号:密码，例如新建账号testaccount，密码Rp829dlwa，password填写testaccount:Rp829dlwa。 pwd = 'testaccount:Rp829dlwa' r = redis.Redis(host=host, port=port, password=pwd) # 连接建立后即可执行数据库操作，下述代码为您提供SET与GET的使用示例。 r.set('foo', 'bar') print(r.get('foo'))

- 

执行上述代码。

### Spring Data Redis

本示例使用Maven方式进行构建，您也可以手动下载[Lettuce](https://github.com/lettuce-io/lettuce-core/releases)或[Jedis](https://github.com/redis/jedis/releases)客户端。

- 

打开编译器，新建项目。

- 

添加下述pom文件，并下载Lettuce或Jedis。

重要

若使用Lettuce，为避免Lettuce客户端黑洞问题带来的影响，建议使用6.3.0.RELEASE及以上版本，并设置TCP_USER_TIMEOUT参数。

<?xml version="1.0" encoding="UTF-8"?> <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd"> <modelVersion>4.0.0</modelVersion> <parent> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-starter-parent</artifactId> <version>2.4.2</version> <relativePath/> <!-- lookup parent from repository --> </parent> <groupId>com.aliyun.tair</groupId> <artifactId>spring-boot-example</artifactId> <version>0.0.1-SNAPSHOT</version> <name>spring-boot-example</name> <description>Demo project for Spring Boot</description> <properties> <java.version>1.8</java.version> </properties> <dependencies> <dependency> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-starter-web</artifactId> </dependency> <dependency> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-starter-test</artifactId> <scope>test</scope> </dependency> <dependency> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-starter-data-redis</artifactId> </dependency> <dependency> <groupId>redis.clients</groupId> <artifactId>jedis</artifactId> </dependency> <dependency> <groupId>io.lettuce</groupId> <artifactId>lettuce-core</artifactId> <version>6.3.0.RELEASE</version> </dependency> <dependency> <groupId>io.netty</groupId> <artifactId>netty-transport-native-epoll</artifactId> <version>4.1.100.Final</version> <classifier>linux-x86_64</classifier> </dependency> </dependencies> <build> <plugins> <plugin> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-maven-plugin</artifactId> </plugin> </plugins> </build> </project>

- 

在Spring Data Redis编辑器中输入下述代码，然后根据注释提示修改代码。

本示例的Spring Data Redis版本为2.4.2。

- 

Spring Data Redis With Jedis

@Bean JedisConnectionFactory redisConnectionFactory() { RedisStandaloneConfiguration config = new RedisStandaloneConfiguration("host", port); JedisPoolConfig jedisPoolConfig = new JedisPoolConfig(); // 最大连接数, 根据业务需要设置，不能超过实例规格规定的最大连接数。 jedisPoolConfig.setMaxTotal(30); // 最大空闲连接数, 根据业务需要设置，不能超过实例规格规定的最大连接数。 jedisPoolConfig.setMaxIdle(20); // 关闭 testOn[Borrow|Return]，防止产生额外的PING。 jedisPoolConfig.setTestOnBorrow(false); jedisPoolConfig.setTestOnReturn(false); JedisClientConfiguration jedisClientConfiguration = JedisClientConfiguration.builder().usePooling().poolConfig( jedisPoolConfig).build(); return new JedisConnectionFactory(config, jedisClientConfiguration); }

- 

Spring Data Redis With Lettuce （包含设置TCP_USER_TIMEOUT参数）

@Configuration public class BeanConfig { /** * TCP_KEEPALIVE打开，并且配置三个参数分别为: * TCP_KEEPIDLE = 30 * TCP_KEEPINTVL = 10 * TCP_KEEPCNT = 3 */ private static final int TCP_KEEPALIVE_IDLE = 30; /** * TCP_USER_TIMEOUT参数可以避免在故障宕机场景下，Lettuce持续超时的问题。 * refer: https://github.com/lettuce-io/lettuce-core/issues/2082 */ private static final int TCP_USER_TIMEOUT = 30; @Bean LettuceConnectionFactory redisConnectionFactory() { RedisStandaloneConfiguration config = new RedisStandaloneConfiguration(); config.setHostName("r-bp1y4is8svonly****pd.redis.rds.aliyuncs.com"); config.setPort(6379); config.setUsername("r-bp1y4is8svonly****"); config.setPassword("Da****3"); // Config TCP KeepAlive SocketOptions socketOptions = SocketOptions.builder() .keepAlive(KeepAliveOptions.builder() .enable() .idle(Duration.ofSeconds(TCP_KEEPALIVE_IDLE)) .interval(Duration.ofSeconds(TCP_KEEPALIVE_IDLE / 3)) .count(3) .build()) .tcpUserTimeout(TcpUserTimeoutOptions.builder() .enable() .tcpUserTimeout(Duration.ofSeconds(TCP_USER_TIMEOUT)) .build()) .build(); LettuceClientConfiguration lettuceClientConfiguration = LettuceClientConfiguration.builder().clientOptions( ClientOptions.builder().socketOptions(socketOptions).build()).build(); return new LettuceConnectionFactory(config, lettuceClientConfiguration); } @Bean RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory connectionFactory) { RedisTemplate<String, Object> template = new RedisTemplate<>(); template.setConnectionFactory(connectionFactory); return template; } }

- 

执行上述代码。

### C或C++

- 

下载并安装[Ｃ客户端](https://github.com/redis/hiredis/releases)。

- 

在C或C++编辑器中输入下述代码，然后根据注释提示修改代码。

本示例的HiRedis版本为1.1.0。

#include <stdio.h> #include <stdlib.h> #include <string.h> #include <hiredis.h> int main(int argc, char **argv) { unsigned int j; redisContext *c; redisReply *reply; if (argc < 4) { printf("Usage: example r-bp10noxlhcoim2****.redis.rds.aliyuncs.com 6379 instance_id password\n"); exit(0); } const char *hostname = argv[1]; const int port = atoi(argv[2]); const char *instance_id = argv[3]; const char *password = argv[4]; struct timeval timeout = { 1, 500000 }; // 1.5 seconds c = redisConnectWithTimeout(hostname, port, timeout); if (c == NULL || c->err) { if (c) { printf("Connection error: %s\n", c->errstr); redisFree(c); } else { printf("Connection error: can't allocate redis context\n"); } exit(1); } /* AUTH */ reply = redisCommand(c, "AUTH %s", password); printf("AUTH: %s\n", reply->str); freeReplyObject(reply); /* PING server */ reply = redisCommand(c,"PING"); printf("PING: %s\n", reply->str); freeReplyObject(reply); /* Set a key */ reply = redisCommand(c,"SET %s %s", "foo", "hello world"); printf("SET: %s\n", reply->str); freeReplyObject(reply); /* Set a key using binary safe API */ reply = redisCommand(c,"SET %b %b", "bar", (size_t) 3, "hello", (size_t) 5); printf("SET (binary API): %s\n", reply->str); freeReplyObject(reply); /* Try a GET and two INCR */ reply = redisCommand(c,"GET foo"); printf("GET foo: %s\n", reply->str); freeReplyObject(reply); reply = redisCommand(c,"INCR counter"); printf("INCR counter: %lld\n", reply->integer); freeReplyObject(reply); /* again ... */ reply = redisCommand(c,"INCR counter"); printf("INCR counter: %lld\n", reply->integer); freeReplyObject(reply); /* Create a list of numbers, from 0 to 9 */ reply = redisCommand(c,"DEL mylist"); freeReplyObject(reply); for (j = 0; j < 10; j++) { char buf[64]; snprintf(buf,64,"%d",j); reply = redisCommand(c,"LPUSH mylist element-%s", buf); freeReplyObject(reply); } /* Let's check what we have inside the list */ reply = redisCommand(c,"LRANGE mylist 0 -1"); if (reply->type == REDIS_REPLY_ARRAY) { for (j = 0; j < reply->elements; j++) { printf("%u) %s\n", j, reply->element[j]->str); } } freeReplyObject(reply); /* Disconnects and frees the context */ redisFree(c); return 0; }

- 

编译上述代码。

gcc -o example -g example.c -I /usr/local/include/hiredis -lhiredis

- 

测试运行，完成连接。

./example r-bp10noxlhcoim2****.redis.rds.aliyuncs.com 6379 r-bp10noxlhcoim2**** password

### .NET

- 

请下载并安装[StackExchange.Redis](https://github.com/StackExchange/StackExchange.Redis?spm=5176.100239.blogcont272212.10.IsQwET&file=StackExchange.Redis)2.7.20及以上版本客户端，更多信息请参见[StackExchange.Redis](products/redis/documents/product-overview/notice-suggestions-for-upgrading-stackexchange-redis-clients.md)[升级公告](products/redis/documents/product-overview/notice-suggestions-for-upgrading-stackexchange-redis-clients.md)。

重要

不推荐使用ServiceStack.Redis或CSRedis客户端：

- 

若使用ServiceStack.Redis客户端时遇到客户端的相关问题，您需要向该公司购买相关技术支持服务。

- 

CSRedis客户端的原开发者已停止维护。

- 

在StackExchange.Redis编辑器中输入下述代码，然后根据注释提示修改下述示例代码。

本示例的StackExchange.Redis版本为2.7.20。

using StackExchange.Redis; // 分别设置实例的连接地址、端口号和密码。 private static ConfigurationOptions configurationOptions = ConfigurationOptions.Parse("r-bp10noxlhcoim2****.redis.rds.aliyuncs.com:6379,password=testaccount:Rp829dlwa,connectTimeout=2000"); //the lock for singleton private static readonly object Locker = new object(); //singleton private static ConnectionMultiplexer redisConn; //singleton public static ConnectionMultiplexer getRedisConn() { if (redisConn == null) { lock (Locker) { if (redisConn == null || !redisConn.IsConnected) { redisConn = ConnectionMultiplexer.Connect(configurationOptions); } } } return redisConn; }

说明

- 

ConfigurationOptions是StackExchange.Redis的核心，它被整个应用程序共享和重用，应该设置为单例，相关参数设置说明，请参见[ConfigurationOptions](https://stackexchange.github.io/StackExchange.Redis/Configuration#configuration-options)。

- 

由于GetDatabase()返回的对象是轻量级的，每次用的时候从ConnectionMultiplexer对象中获取即可。

redisConn = getRedisConn(); var db = redisConn.GetDatabase();

- 

通过客户端程序操作常见的数据结构，示例如下：

String//set get string strKey = "hello"; string strValue = "world"; bool setResult = db.StringSet(strKey, strValue); Console.WriteLine("set " + strKey + " " + strValue + ", result is " + setResult); //incr string counterKey = "counter"; long counterValue = db.StringIncrement(counterKey); Console.WriteLine("incr " + counterKey + ", result is " + counterValue); //expire db.KeyExpire(strKey, new TimeSpan(0, 0, 5)); Thread.Sleep(5 * 1000); Console.WriteLine("expire " + strKey + ", after 5 seconds, value is " + db.StringGet(strKey)); //mset mget KeyValuePair<RedisKey, RedisValue> kv1 = new KeyValuePair<RedisKey, RedisValue>("key1", "value1"); KeyValuePair<RedisKey, RedisValue> kv2 = new KeyValuePair<RedisKey, RedisValue>("key2", "value2"); db.StringSet(new KeyValuePair<RedisKey, RedisValue>[] {kv1,kv2}); RedisValue[] values = db.StringGet(new RedisKey[] {kv1.Key, kv2.Key}); Console.WriteLine("mget " + kv1.Key.ToString() + " " + kv2.Key.ToString() + ", result is " + values[0] + "&&" + values[1]);

Hashstring hashKey = "myhash"; //hset db.HashSet(hashKey,"f1","v1"); db.HashSet(hashKey,"f2", "v2"); HashEntry[] values = db.HashGetAll(hashKey); //hgetall Console.Write("hgetall " + hashKey + ", result is"); for (int i = 0; i < values.Length;i++) { HashEntry hashEntry = values[i]; Console.Write(" " + hashEntry.Name.ToString() + " " + hashEntry.Value.ToString()); } Console.WriteLine();

List//list key string listKey = "myList"; //rpush db.ListRightPush(listKey, "a"); db.ListRightPush(listKey, "b"); db.ListRightPush(listKey, "c"); //lrange RedisValue[] values = db.ListRange(listKey, 0, -1); Console.Write("lrange " + listKey + " 0 -1, result is "); for (int i = 0; i < values.Length; i++) { Console.Write(values[i] + " "); } Console.WriteLine();

Set//set key string setKey = "mySet"; //sadd db.SetAdd(setKey, "a"); db.SetAdd(setKey, "b"); db.SetAdd(setKey, "c"); //sismember bool isContains = db.SetContains(setKey, "a"); Console.WriteLine("set " + setKey + " contains a is " + isContains );

Sorted Setstring sortedSetKey = "myZset"; //sadd db.SortedSetAdd(sortedSetKey, "xiaoming", 85); db.SortedSetAdd(sortedSetKey, "xiaohong", 100); db.SortedSetAdd(sortedSetKey, "xiaofei", 62); db.SortedSetAdd(sortedSetKey, "xiaotang", 73); //zrevrangebyscore RedisValue[] names = db.SortedSetRangeByRank(sortedSetKey, 0, 2, Order.Ascending); Console.Write("zrevrangebyscore " + sortedSetKey + " 0 2, result is "); for (int i = 0; i < names.Length; i++) { Console.Write(names[i] + " "); } Console.WriteLine();

### node-redis

- 

下载并安装[node-redis](https://github.com/redis/node-redis)客户端。

- 

在node-redis客户端中输入下述代码，然后根据注释提示修改代码。

本示例的Node.js版本为19.4.0、node-redis版本为4.5.1。

import { createClient } from 'redis'; // 分别设置实例的端口号、连接地址、账号、密码 const host = 'r-bp10noxlhcoim2****.redis.rds.aliyuncs.com'; const port = 6379; const username = 'testaccount'; // 如果密码中包含特殊字符（!@#$%^&*()+-=_）建议用encodeURIComponent进行编码:password = encodeURIComponent(password) const password = 'Rp829dlwa'; const client = createClient({ // redis://[[username]:[password]@[host][:port]/[db-number] url: `redis://${username}:${password}@${host}:${port}/0` }); client.on('error', (err) => console.log('Redis Client Error', err)); await client.connect(); await client.set('foo', 'bar'); const value = await client.get('foo'); console.log("get foo: %s", value); await client.disconnect();

说明

若提示SyntaxError: Cannot use import statement outside a module，请将.js文件的后缀改为.mjs，并在调用时增加--experimental-modules选项，例如node --experimental-modules redis.mjs。

- 

执行上述代码。

### Go-redis

- 

下载并安装[Go-Redis](https://github.com/redis/go-redis)客户端。

- 

在Go-redis编辑器中输入下述代码，然后根据注释提示修改代码。

本示例的Go版本为1.21、Go-redis版本为9.18.0。代码中已加入连接池配置示例（PoolSize、MinIdleConns等），生产环境建议根据业务并发量与实例规格的最大连接数调整。

package main import ( "context" "fmt" "time" "github.com/redis/go-redis/v9" ) var ctx = context.Background() func ExampleClient() { client := redis.NewClient(&redis.Options{ // 替换为实例的连接地址和端口。 Addr: "r-bp10noxlhcoim2****.redis.rds.aliyuncs.com:6379", // 替换为实例的账号:密码。 Password: "testaccount:Rp829dlwa", DB: 0, // 使用默认DB。 // 连接池配置（请根据业务并发量调整，且不能超过实例规格的最大连接数）。 PoolSize: 20, // 最大连接数。建议值：业务峰值QPS / 单连接QPS，或参考10 × CPU核数。 MinIdleConns: 5, // 最小空闲连接数。预热连接，避免突发流量频繁建连。 PoolTimeout: 4 * time.Second, // 从连接池获取连接的等待超时，建议略大于ReadTimeout。 ConnMaxIdleTime: 5 * time.Minute, // 空闲连接关闭时间，需小于实例的连接空闲超时（默认600秒）。 // 网络与重试配置。 DialTimeout: 5 * time.Second, // 建立TCP连接的超时时间。 ReadTimeout: 3 * time.Second, // 读超时，-1表示不超时，0使用默认值。 WriteTimeout: 3 * time.Second, // 写超时。 MaxRetries: 3, // 命令失败重试次数，-1表示不重试。 }) defer client.Close() // 下述代码为您提供SET与GET的使用示例。 if err := client.Set(ctx, "foo", "bar", 0).Err(); err != nil { panic(err) } val, err := client.Get(ctx, "foo").Result() if err != nil { panic(err) } fmt.Println("set : foo -> ", val) } func main() { ExampleClient() }

- 

执行上述代码。

### Lettuce

本示例使用Maven方式进行构建，您也可以手动下载[Lettuce](https://github.com/lettuce-io/lettuce-core/releases)客户端。

- 

打开编译器，新建项目。

- 

添加下述pom.xml文件，并下载Lettuce 6.3.0，不建议使用Lettuce 6.3.0以下的版本。

本示例的Lettuce版本为6.3.0。

<<dependencies> <dependency> <groupId>io.lettuce</groupId> <artifactId>lettuce-core</artifactId> <version>6.3.0.RELEASE</version> </dependency> <dependency> <groupId>io.netty</groupId> <artifactId>netty-transport-native-epoll</artifactId> <version>4.1.100.Final</version> <classifier>linux-x86_64</classifier> </dependency> </dependencies>

- 

在编辑器中输入下述代码，然后根据注释提示修改代码。

import io.lettuce.core.ClientOptions; import io.lettuce.core.RedisClient; import io.lettuce.core.RedisURI; import io.lettuce.core.SocketOptions; import io.lettuce.core.SocketOptions.KeepAliveOptions; import io.lettuce.core.SocketOptions.TcpUserTimeoutOptions; import io.lettuce.core.api.StatefulRedisConnection; import io.lettuce.core.api.sync.RedisCommands; import java.time.Duration; public class LettuceExample { /** * TCP_KEEPALIVE打开，并且配置三个参数分别为: * TCP_KEEPIDLE = 30 * TCP_KEEPINTVL = 10 * TCP_KEEPCNT = 3 */ private static final int TCP_KEEPALIVE_IDLE = 30; /** * TCP_USER_TIMEOUT参数可以避免在故障宕机场景下，Lettuce持续超时的问题。 * refer: https://github.com/lettuce-io/lettuce-core/issues/2082 */ private static final int TCP_USER_TIMEOUT = 30; private static RedisClient client = null; private static StatefulRedisConnection<String, String> connection = null; public static void main(String[] args) { // 分别将host、user、password和port的值替换为实际的实例信息。 String host = "r-bp1s1bt2tlq3p1****.redis.rds.aliyuncs.com"; String user = "r-bp1s1bt2tlq3p1****"; String password = "Da****3"; int port = 6379; // Config RedisURI RedisURI uri = RedisURI.Builder .redis(host, port) .withAuthentication(user, password) .build(); // Config TCP KeepAlive SocketOptions socketOptions = SocketOptions.builder() .keepAlive(KeepAliveOptions.builder() .enable() .idle(Duration.ofSeconds(TCP_KEEPALIVE_IDLE)) .interval(Duration.ofSeconds(TCP_KEEPALIVE_IDLE/3)) .count(3) .build()) .tcpUserTimeout(TcpUserTimeoutOptions.builder() .enable() .tcpUserTimeout(Duration.ofSeconds(TCP_USER_TIMEOUT)) .build()) .build(); client = RedisClient.create(uri); client.setOptions(ClientOptions.builder() .socketOptions(socketOptions) .build()); connection = client.connect(); RedisCommands<String, String> commands = connection.sync(); System.out.println(commands.set("foo", "bar")); System.out.println(commands.get("foo")); // 当应用退出，需销毁资源时，调用此方法。此方法会断开连接、释放资源。 connection.close(); client.shutdown(); } }

- 

执行上述代码，预期会返回如下结果：

OK bar

## 相关文档

- 

[常见报错](products/redis/documents/support/common-errors-and-troubleshooting.md)

- 

[Tair](products/redis/documents/support/how-do-i-troubleshoot-connection-issues-in-apsaradb-for-redis.md)[连接问题排查流程](products/redis/documents/support/how-do-i-troubleshoot-connection-issues-in-apsaradb-for-redis.md)

- 

[客户端重试指南](products/redis/documents/use-cases/retry-mechanisms-for-redis-clients.md)

- 

[报警设置](products/redis/documents/user-guide/alert-settings.md)

- 

[查看监控数据](products/redis/documents/user-guide/view-monitoring-data.md)

[上一篇：通过redis-cli连接实例](products/redis/documents/user-guide/use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)[下一篇：通过DMS连接实例](products/redis/documents/user-guide/log-on-to-an-apsaradb-for-redis-instance-by-using-dms.md)

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
