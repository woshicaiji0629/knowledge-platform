## Lettuce
警告
Lettuce 默认配置可能导致实例变更时应用延迟增加和无法访问等问题。请仔细阅读[Lettuce](use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)[相关参数说明](use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)，以正确配置 Lettuce。
Lettuce 的版本应大于等于 6.3.0.RELEASE，更多信息请参见[【通知】Lettuce](../product-overview/notice-on-lettuce-update.md)[客户端升级建议](../product-overview/notice-on-lettuce-update.md)。
添加下述Maven依赖。
<dependency> <groupId>io.lettuce</groupId> <artifactId>lettuce-core</artifactId> <version>6.3.0.RELEASE</version> </dependency> <dependency> <groupId>io.netty</groupId> <artifactId>netty-transport-native-epoll</artifactId> <version>4.1.65.Final</version> <classifier>linux-x86_64</classifier> </dependency>
添加下述代码，并根据注释提示修改代码。
import io.lettuce.core.RedisURI; import io.lettuce.core.SocketOptions; import io.lettuce.core.cluster.ClusterClientOptions; import io.lettuce.core.cluster.ClusterTopologyRefreshOptions; import io.lettuce.core.cluster.RedisClusterClient; import io.lettuce.core.cluster.api.StatefulRedisClusterConnection; import java.time.Duration; public class ClusterDemo { /** * TCP_KEEPALIVE 打开，并且配置三个参数分别为： * TCP_KEEPIDLE = 30 * TCP_KEEPINTVL = 10 * TCP_KEEPCNT = 3 */ private stat
