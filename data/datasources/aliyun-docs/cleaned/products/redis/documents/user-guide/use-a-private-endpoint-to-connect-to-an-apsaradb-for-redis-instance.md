# 使用多种客户端通过直连模式连接Tair实例-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance

# 使用直连模式连接实例
若您购买或开通了云数据库 Tair（兼容 Redis）直连模式集群，您可以将原生Redis集群架构无缝迁移到该实例中。云数据库 Tair（兼容 Redis）的直连地址支持原生Redis Cluster协议，在该模式下，客户端将直接与数据服务器进行连接，服务的响应速度非常快。
## 前提条件
[开通直连访问](enable-the-direct-connection-mode.md)。
将客户端地址加入[实例白名单](../getting-started/step-2-configure-whitelists.md)。
使用[Jedis](https://github.com/xetorthio/jedis/wiki/Getting-started)、[PhpRedis](https://github.com/phpredis/phpredis)等支持Redis Cluster的客户端。
说明
使用不支持Redis Cluster的客户端，可能因客户端无法重定向请求到正确的分片而获取不到需要的数据。
您可以在Redis官网的[客户端列表](https://redis.io/clients)里查找更多支持Redis Cluster的客户端。
客户端所在的ECS与实例在同一VPC网络（相同VPC ID）。
## 背景信息
[开启直连模式](enable-the-direct-connection-mode.md)时，云数据库 Tair（兼容 Redis）会为该集群中所有数据分片的master节点分配一个虚拟IP（VIP）地址。客户端在首次向直连地址发送请求前会通过DNS服务器解析直连地址，解析结果会是集群中一个随机数据分片的VIP。获取到VIP后，客户端即可通过Redis Cluster协议操作该集群中的数据。下图展示了直连模式下集群的服务架构。
## 注意事项
由于部署架构的不同，相对标准架构来说，集群架构的实例在原生Redis命令的支持上有一定的区别（例如Lua存在使用限制等）。更多信息，请参见[集群架构实例的命令限制](../developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。
直连模式下，如果执行[变更实例配置](change-the-configurations-of-an-instance.md)，系统会采用Slot（槽）迁移的方式来完成，此场景下，客户端可能因访问到正在迁移的Slot而提示MOVED、TRYAGAIN等错误信息。如需确保请求的成功执行，请为客户端设计重试机制。更多信息，请参见[客户端重试指南](../use-cases/retry-mechanisms-for-redis-clients.md)。
直连模式支持使用SELECT命令切换DB，但部分Redis Cluster客户端（例如stackExchange.redis）不支持SELECT命令，如果使用该类客户端则只能使用DB0。
直连地址仅支持通过阿里云内网访问，且同时支持[VPC](enable-password-free-access.md)[免密](enable-password-free-access.md)和[账号密码认证](create-and-manage-database-accounts.md)。
## redis-cli
使用集群架构直连地址连接实例。
重要
使用直连地址连接时必须添加-c参数，否则会导致连接失败。
./redis-cli -h r-bp1zxszhcgatnx****.redis.rds.aliyuncs.com -p 6379 -c
完成密码验证。
AUTH testaccount:Rp829dlwa
关于redis-cli的更多介绍请参见[通过](use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)[redis-cli](use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)[连接实例](use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)。
## Jedis
本示例的Jedis版本为4.3.0，更多信息请参见[Jedis](https://github.com/xetorthio/jedis/wiki/Getting-started)。
使用自定义连接池（推荐）
import redis.clients.jedis.*; import java.util.HashSet; import java.util.Set; public class DirectTest { private static final int DEFAULT_TIMEOUT = 2000; private static final int DEFAULT_REDIRECTIONS = 5; private static final ConnectionPoolConfig config = new ConnectionPoolConfig(); public static void main(String args[]) { // 最大连接数，由于直连模式为客户端直接连接某个数据库分片，需要保证：业务机器数 * MaxTotal < 单个数据库分片的最大连接数。 config.setMaxTotal(30); // 最大空闲连接数, 根据业务需要设置。 config.setMaxIdle(20); config.setMinIdle(15); // 开通直连访问时申请到的直连地址。 String host = "r-bp1xxxxxxxxxxxx.redis.rds.aliyuncs.com"; int port = 6379; // 实例的密码。 String password = "xxxxx"; Set<HostAndPort> jedisClusterNode = new HashSet<HostAndPort>(); jedisClusterNode.add(new HostAndPort(host, port)); JedisCluster jc = new JedisCluster(jedisClusterNode, DEFAULT_TIMEOUT, DEFAULT_TIMEOUT, DEFAULT_REDIRECTIONS, password, "clientName", config); jc.set("key", "value"); jc.get("key"); jc.close(); // 当应用退出，需销毁资源时，调用此方法。此方法会断开连接、释放资源。 } }
使用默认连接池
import redis.clients.jedis.ConnectionPoolConfig; import redis.clients.jedis.HostAndPort; import redis.clients.jedis.JedisCluster; import java.util.HashSet; import java.util.Set; public class DirectTest{ private static final int DEFAULT_TIMEOUT = 2000; private static final int DEFAULT_REDIRECTIONS = 5; private static final ConnectionPoolConfig DEFAULT_CONFIG = new ConnectionPoolConfig(); public static void main(String args[]){ // 开通直连访问时申请到的直连地址。 String host = "r-bp1xxxxxxxxxxxx.redis.rds.aliyuncs.com"; int port = 6379; String password = "xxxx"; Set<HostAndPort> jedisClusterNode = new HashSet<HostAndPort>(); jedisClusterNode.add(new HostAndPort(host, port)); JedisCluster jc = new JedisCluster(jedisClusterNode, DEFAULT_TIMEOUT, DEFAULT_TIMEOUT, DEFAULT_REDIRECTIONS,password, "clientName", DEFAULT_CONFIG); jc.set("key","value"); jc.get("key"); jc.close(); // 当应用退出，需销毁资源时，调用此方法。此方法会断开连接、释放资源。 } }
## PhpRedis
本示例的PhpRedis版本为5.3.7，更多信息请参见[PhpRedis](https://github.com/phpredis/phpredis)。
<?php // 直连地址和连接端口。 $array = ['r-bp1xxxxxxxxxxxx.redis.rds.aliyuncs.com:6379']; // 连接密码。 $pwd = "xxxx"; // 使用密码连接集群。 $obj_cluster = new RedisCluster(NULL, $array, 1.5, 1.5, true, $pwd); // 输出连接结果。 var_dump($obj_cluster); if ($obj_cluster->set("foo", "bar") == false) { die($obj_cluster->getLastError()); } $value = $obj_cluster->get("foo"); echo $value; ?>
## redis-py
本示例的Python版本为3.9、redis-py版本为4.4.1，更多信息请参见[redis-py](https://github.com/redis/redis-py)。
# !/usr/bin/env python # -*- coding: utf-8 -*- from redis.cluster import RedisCluster # 分别将host和port的值替换为实例的连接地址、端口号。 host = 'r-bp10noxlhcoim2****.redis.rds.aliyuncs.com' port = 6379 # 分别将user和pwd的值替换为实例的账号和密码。 user = 'testaccount' pwd = 'Rp829dlwa' rc = RedisCluster(host=host, port=port, username=user, password=pwd) # 连接建立后即可执行数据库操作，下述代码为您提供SET与GET的使用示例。 rc.set('foo', 'bar') print(rc.get('foo'))
## Spring Data Redis
本示例使用Maven方式进行构建，您也可以手动下载[Lettuce](https://github.com/lettuce-io/lettuce-core/releases)或[Jedis](https://github.com/redis/jedis/releases)客户端。
添加下述Maven依赖。
<?xml version="1.0" encoding="UTF-8"?> <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd"> <modelVersion>4.0.0</modelVersion> <parent> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-starter-parent</artifactId> <version>2.4.2</version> <relativePath/> <!-- lookup parent from repository --> </parent> <groupId>com.aliyun.tair</groupId> <artifactId>spring-boot-example</artifactId> <version>0.0.1-SNAPSHOT</version> <name>spring-boot-example</name> <description>Demo project for Spring Boot</description> <properties> <java.version>1.8</java.version> </properties> <dependencies> <dependency> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-starter-web</artifactId> </dependency> <dependency> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-starter-test</artifactId> <scope>test</scope> </dependency> <dependency> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-starter-data-redis</artifactId> </dependency> <dependency> <groupId>redis.clients</groupId> <artifactId>jedis</artifactId> </dependency> <dependency> <groupId>io.lettuce</groupId> <artifactId>lettuce-core</artifactId> <version>6.3.0.RELEASE</version> </dependency> <dependency> <groupId>io.netty</groupId> <artifactId>netty-transport-native-epoll</artifactId> <version>4.1.100.Final</version> <classifier>linux-x86_64</classifier> </dependency> </dependencies> <build> <plugins> <plugin> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-maven-plugin</artifactId> </plugin> </plugins> </build> </project>
在Spring Data Redis编辑器中输入下述代码，然后根据注释提示修改代码。
本示例的Spring Data Redis版本为2.4.2。
（推荐）Spring Data Redis With Jedis
@Bean JedisConnectionFactory redisConnectionFactory() { List<String> clusterNodes = Arrays.asList("r-bp10noxlhcoim2****.redis.rds.aliyuncs.com:6379"); RedisClusterConfiguration redisClusterConfiguration = new RedisClusterConfiguration(clusterNodes); redisClusterConfiguration.setUsername("user"); redisClusterConfiguration.setPassword("password"); JedisPoolConfig jedisPoolConfig = new JedisPoolConfig(); // 最大空闲连接数，由于直连模式为客户端直接连接某个数据库分片，需要保证：业务机器数 * MaxTotal < 单个数据库分片的最大连接数。 jedisPoolConfig.setMaxTotal(30); // 最大空闲连接数, 根据业务需要设置。 jedisPoolConfig.setMaxIdle(20); // 关闭 testOn[Borrow|Return]，防止产生额外的 PING jedisPoolConfig.setTestOnBorrow(false); jedisPoolConfig.setTestOnReturn(false); return new JedisConnectionFactory(redisClusterConfiguration, jedisPoolConfig); }
Spring Data Redis With Lettuce
警告
Lettuce 默认配置可能导致实例变更时应用延迟增加和无法访问等问题。请仔细阅读[Lettuce](use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)[相关参数说明](use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)，以正确配置 Lettuce。
Lettuce 的版本应大于等于 6.3.0.RELEASE，更多信息请参见[【通知】Lettuce](../product-overview/notice-on-lettuce-update.md)[客户端升级建议](../product-overview/notice-on-lettuce-update.md)。
/** * TCP_KEEPALIVE打开，并且配置三个参数分别为: * TCP_KEEPIDLE = 30 * TCP_KEEPINTVL = 10 * TCP_KEEPCNT = 3 */ private static final int TCP_KEEPALIVE_IDLE = 30; /** * TCP_USER_TIMEOUT参数可以避免在故障宕机场景下，Lettuce持续超时的问题。 * refer: https://github.com/lettuce-io/lettuce-core/issues/2082 */ private static final int TCP_USER_TIMEOUT = 30; @Bean public LettuceConnectionFactory redisConnectionFactory() { List<String> clusterNodes = Arrays.asList("r-bp10noxlhcoim2****.redis.rds.aliyuncs.com:6379"); RedisClusterConfiguration redisClusterConfiguration = new RedisClusterConfiguration(clusterNodes); redisClusterConfiguration.setUsername("user"); redisClusterConfiguration.setPassword("password"); // Config TCP KeepAlive SocketOptions socketOptions = SocketOptions.builder() .keepAlive(KeepAliveOptions.builder() .enable() .idle(Duration.ofSeconds(TCP_KEEPALIVE_IDLE)) .interval(Duration.ofSeconds(TCP_KEEPALIVE_IDLE / 3)) .count(3) .build()) .tcpUserTimeout(TcpUserTimeoutOptions.builder() .enable() .tcpUserTimeout(Duration.ofSeconds(TCP_USER_TIMEOUT)) .build()) .build(); ClusterTopologyRefreshOptions topologyRefreshOptions = ClusterTopologyRefreshOptions.builder() .enablePeriodicRefresh(Duration.ofSeconds(60)) .dynamicRefreshSources(false) .enableAllAdaptiveRefreshTriggers() .adaptiveRefreshTriggersTimeout(Duration.ofSeconds(15)).build(); LettuceClientConfiguration lettuceClientConfiguration = LettuceClientConfiguration.builder(). clientOptions(ClusterClientOptions.builder() .socketOptions(socketOptions) .validateClusterNodeMembership(false) .topologyRefreshOptions(topologyRefreshOptions).build()).build(); return new LettuceConnectionFactory(redisClusterConfiguration, lettuceClientConfiguration); }
## .Net
本示例的.Net版本为6.0，StackExchange.Redis版本为2.6.90。
using StackExchange.Redis; class RedisConnSingleton { // 分别设置实例的连接地址、端口号和用户名、密码。 private static ConfigurationOptions configurationOptions = ConfigurationOptions.Parse("r-bp10noxlhcoim2****.redis.rds.aliyuncs.com:6379,user=testaccount,password=Rp829dlwa,connectTimeout=2000"); //the lock for singleton private static readonly object Locker = new object(); //singleton private static ConnectionMultiplexer redisConn; //singleton public static ConnectionMultiplexer getRedisConn() { if (redisConn == null) { lock (Locker) { if (redisConn == null || !redisConn.IsConnected) { redisConn = ConnectionMultiplexer.Connect(configurationOptions); } } } return redisConn; } } class Program { static void Main(string[] args) { ConnectionMultiplexer cm = RedisConnSingleton.getRedisConn(); var db = cm.GetDatabase(); db.StringSet("key", "value"); String ret = db.StringGet("key"); Console.WriteLine("get key: " + ret); } }
## node-redis
本示例的Node.js版本为19.4.0、node-redis版本为4.5.1。
import { createCluster } from 'redis'; // 分别设置实例的端口号、连接地址、账号、密码， // 注意，在url中配置用户和密码之后，还需要在defaults中设置全局用户和密码， // 用于其余节点的认证，否则将出现NOAUTH的错误。 const cluster = createCluster({ rootNodes: [{ url: 'redis://testaccount:Rp829dlwa@r-bp10noxlhcoim2****.redis.rds.aliyuncs.com:6379' }], defaults: { username: 'testaccount', password: 'Rp829dlwa' } }); cluster.on('error', (err) => console.log('Redis Cluster Error', err)); await cluster.connect(); await cluster.set('key', 'value'); const value = await cluster.get('key'); console.log('get key: %s', value); await cluster.disconnect();
## Go-redis
本示例的Go版本为1.19.7、Go-redis版本为9.5.1。
重要
请使用Go-redis v9.0及以上版本，否则在使用直连模式地址时，可能会产生[不兼容报错](../support/common-errors-and-troubleshooting.md)。
package main import ( "context" "fmt" "github.com/go-redis/redis/v9" ) var ctx = context.Background() func main() { rdb := redis.NewClusterClient(&redis.ClusterOptions{ Addrs: []string{"r-bp10noxlhcoim2****.redis.rds.aliyuncs.com:6379"}, Username: "testaccount", Password: "Rp829dlwa", }) err := rdb.Set(ctx, "key", "value", 0).Err() if err != nil { panic(err) } val, err := rdb.Get(ctx, "key").Result() if err != nil { panic(err) } fmt.Println("key", val) }
## Lettuce
警告
Lettuce 默认配置可能导致实例变更时应用延迟增加和无法访问等问题。请仔细阅读[Lettuce](use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)[相关参数说明](use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)，以正确配置 Lettuce。
Lettuce 的版本应大于等于 6.3.0.RELEASE，更多信息请参见[【通知】Lettuce](../product-overview/notice-on-lettuce-update.md)[客户端升级建议](../product-overview/notice-on-lettuce-update.md)。
添加下述Maven依赖。
<dependency> <groupId>io.lettuce</groupId> <artifactId>lettuce-core</artifactId> <version>6.3.0.RELEASE</version> </dependency> <dependency> <groupId>io.netty</groupId> <artifactId>netty-transport-native-epoll</artifactId> <version>4.1.65.Final</version> <classifier>linux-x86_64</classifier> </dependency>
添加下述代码，并根据注释提示修改代码。
import io.lettuce.core.RedisURI; import io.lettuce.core.SocketOptions; import io.lettuce.core.cluster.ClusterClientOptions; import io.lettuce.core.cluster.ClusterTopologyRefreshOptions; import io.lettuce.core.cluster.RedisClusterClient; import io.lettuce.core.cluster.api.StatefulRedisClusterConnection; import java.time.Duration; public class ClusterDemo { /** * TCP_KEEPALIVE 打开，并且配置三个参数分别为： * TCP_KEEPIDLE = 30 * TCP_KEEPINTVL = 10 * TCP_KEEPCNT = 3 */ private static final int TCP_KEEPALIVE_IDLE = 30; /** * TCP_USER_TIMEOUT可以避免在故障宕机场景下Lettuce持续超时的问题。 * refer: https://github.com/lettuce-io/lettuce-core/issues/2082 */ private static final int TCP_USER_TIMEOUT = 30; public static void main(String[] args) throws Exception { // 分别将host、port和password的值替换为实际的实例信息。 String host = "r-bp1ln3c4kopj3l****.redis.rds.aliyuncs.com"; int port = 6379; String password = "Da****3"; RedisURI redisURI = RedisURI.Builder.redis(host) .withPort(port) .withPassword(password) .build(); ClusterTopologyRefreshOptions refreshOptions = ClusterTopologyRefreshOptions.builder() .enablePeriodicRefresh(Duration.ofSeconds(60)) .dynamicRefreshSources(false) .enableAllAdaptiveRefreshTriggers() .adaptiveRefreshTriggersTimeout(Duration.ofSeconds(15)).build(); // Config TCP KeepAlive SocketOptions socketOptions = SocketOptions.builder() .keepAlive(SocketOptions.KeepAliveOptions.builder() .enable() .idle(Duration.ofSeconds(TCP_KEEPALIVE_IDLE)) .interval(Duration.ofSeconds(TCP_KEEPALIVE_IDLE/3)) .count(3) .build()) .tcpUserTimeout(SocketOptions.TcpUserTimeoutOptions.builder() .enable() .tcpUserTimeout(Duration.ofSeconds(TCP_USER_TIMEOUT)) .build()) .build(); RedisClusterClient redisClient = RedisClusterClient.create(redisURI); redisClient.setOptions(ClusterClientOptions.builder() .socketOptions(socketOptions) .validateClusterNodeMembership(false) .topologyRefreshOptions(refreshOptions).build()); StatefulRedisClusterConnection<String, String> connection = redisClient.connect(); connection.sync().set("key", "value"); System.out.println(connection.sync().get("key")); } }
执行上述代码，预期会返回如下结果：
value
Lettuce 相关参数说明如下：
| 参数 | 默认配置 | 说明 | 修改配置 |
| --- | --- | --- | --- |
| enablePeriodicRefresh(Duration refreshPeriod) | 关闭 | 启用后将进行周期性集群拓扑刷新。 | 建议配置为 60s。 开启此配置可以使不活跃的长连接也能及时更新本地拓扑。 |
| dynamicRefreshSources(boolean dynamicRefreshSources) | true | 为 true 时，使用 Cluster Nodes 命令返回的所有节点进行集群拓扑刷新；为 false 时，使用指定节点地址。 | 如无特殊需求，应配置为 false。 启用此选项会向所有节点发送 CLUSTER NODES 命令，增加服务端压力。此外，在变配期间，使用 endpoint 地址更新拓扑通常更为迅速可靠。 |
| enableAllAdaptiveRefreshTriggers() | 关闭 | 启用后，当收到 MOVED 消息时，会自动刷新集群拓扑。 | 必须启用。 启用此配置才能确保拓扑变更后 Lettuce 能及时更新本地拓扑。 |
| adaptiveRefreshTriggersTimeout(Duration timeout) | 30s | 限制集群拓扑刷新频率，在指定时间内仅允许一次刷新。 | 建议配置为 15s。 由于集群中多个节点的拓扑变更并非原子操作，Lettuce 触发的初次拓扑刷新可能会失败，因此需要快速进行后续刷新以确保拓扑正确更新。当应用数量较少时，由于不会有大量客户端同时发送 CLUSTER NODES 命令，可以适当降低该值，以实现更快的拓扑表收敛时间。 |
| validateClusterNodeMembership(boolean validateClusterNodeMembership) | true | 在拓扑变化时，Lettuce 使用 MOVED 将命令重定向到正确的节点。启用此配置后，只允许将命令重定向到 CLUSTER NODES 输出中已知的节点。 | 必须配置为 false。 配置为 false 可以防止在集群拓扑变更后，本地拓扑刷新完成前无法访问新增节点。 |
## 相关文档
直连模式适用于简化架构、快速上手的应用场景，而代理模式提供更高的可扩展性与高可用性，更多信息请参见[Tair Proxy](../product-overview/features-of-proxy-nodes.md)[特性说明](../product-overview/features-of-proxy-nodes.md)。
## 常见问题
Q：为什么会报错MOVED 4578 172.18.xx.xxx:6379？
A：报错MOVED <slot> <IP:Port>表示当前查询的Key位于其他节点中，通常是使用不支持Redis Cluster的客户端导致的。例如以下情况（其他客户端也类似）。
使用redis-cli连接实例时没加-c。
使用Python时，使用普通的redis-py客户端，其并不支持自动重定向，应该使用redis-cluster客户端。
说明
更多报错请参见[常见报错](../support/common-errors-and-troubleshooting.md)。
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
