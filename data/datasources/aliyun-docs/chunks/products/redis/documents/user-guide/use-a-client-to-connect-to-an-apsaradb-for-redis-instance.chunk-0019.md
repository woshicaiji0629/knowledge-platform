### .NET
请下载并安装[StackExchange.Redis](https://github.com/StackExchange/StackExchange.Redis?spm=5176.100239.blogcont272212.10.IsQwET&file=StackExchange.Redis)2.7.20及以上版本客户端，更多信息请参见[StackExchange.Redis](../product-overview/notice-suggestions-for-upgrading-stackexchange-redis-clients.md)[升级公告](../product-overview/notice-suggestions-for-upgrading-stackexchange-redis-clients.md)。
重要
不推荐使用ServiceStack.Redis或CSRedis客户端：
若使用ServiceStack.Redis客户端时遇到客户端的相关问题，您需要向该公司购买相关技术支持服务。
CSRedis客户端的原开发者已停止维护。
在StackExchange.Redis编辑器中输入下述代码，然后根据注释提示修改下述示例代码。
本示例的StackExchange.Redis版本为2.7.20。
using StackExchange.Redis; // 分别设置实例的连接地址、端口号和密码。 private static ConfigurationOptions configurationOptions = ConfigurationOptions.Parse("r-bp10noxlhcoim2****.redis.rds.aliyuncs.com:6379,password=testaccount:Rp829dlwa,connectTimeout=2000"); //the lock for singleton private static readonly object Locker = new object(); //singleton private static ConnectionMultiplexer redisConn; //singleton public static ConnectionMultiplexer getRedisConn() { if (redisConn == null) { lock (Locker) { if (redisConn == null || !redisConn.IsConnected) { redisConn = ConnectionMultiplexer.Connect(configurationOptions); } } } return redisConn;
