### NOPERM this user has no permissions to run the 'config|get' command
可能原因：在实例信息页确认您的实例版本为Redis 7.0。云数据库 Tair（兼容 Redis）的7.0版本禁用CONFIG命令。
应用启动时，Spring Data Redis会执行CONFIG SET命令动态设置notify-keyspace-events参数来启用KeyspaceEventMessageListener功能。因为CONFIG GET/SET命令被禁用，导致启动时报错。
解决方法：设置keyspaceNotificationsConfigParameter为空，绕过该问题，完整代码见[SpringRedisTest.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20251027/nghdhn/springredistest.zip)，更多信息请参见[Spring Data Redis](https://docs.spring.io/spring-data/data-redis/docs/current-SNAPSHOT/reference/html/)。
@EnableRedisRepositories(enableKeyspaceEvents = RedisKeyValueAdapter.EnableKeyspaceEvents.ON_STARTUP, keyspaceNotificationsConfigParameter = "")
同时，如果监听了KeyExpirationListener，需要在构造函数中设置 keyspaceNotificationsConfigParameter 为空。
public RedisKeyExpirationListener(RedisMessageListenerContainer redisMessageListenerContainer) { super(redisMessageListenerContainer); setKeyspaceNotificationsConfigParameter(""); // 重要 }
