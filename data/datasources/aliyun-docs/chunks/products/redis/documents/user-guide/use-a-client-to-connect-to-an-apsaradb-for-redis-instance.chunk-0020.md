l) { lock (Locker) { if (redisConn == null || !redisConn.IsConnected) { redisConn = ConnectionMultiplexer.Connect(configurationOptions); } } } return redisConn; }
说明
ConfigurationOptions是StackExchange.Redis的核心，它被整个应用程序共享和重用，应该设置为单例，相关参数设置说明，请参见[ConfigurationOptions](https://stackexchange.github.io/StackExchange.Redis/Configuration#configuration-options)。
由于GetDatabase()返回的对象是轻量级的，每次用的时候从ConnectionMultiplexer对象中获取即可。
redisConn = getRedisConn(); var db = redisConn.GetDatabase();
通过客户端程序操作常见的数据结构，示例如下：
String//set get string strKey = "hello"; string strValue = "world"; bool setResult = db.StringSet(strKey, strValue); Console.WriteLine("set " + strKey + " " + strValue + ", result is " + setResult); //incr string counterKey = "counter"; long counterValue = db.StringIncrement(counterKey); Console.WriteLine("incr " + counterKey + ", result is " + counterValue); //expire db.KeyExpire(strKey, new TimeSpan(0, 0, 5)); Thread.Sleep(5 * 1000); Console.WriteLine("expire " + strKey + ", after 5 seconds, value is " + db.StringGet(strKey)); //mset mget KeyValuePair<RedisKey, RedisValue> kv1 = new KeyValuePair<RedisKey, RedisValue>("key1", "value1"); KeyValuePair<RedisKey, RedisValue> kv2 = new KeyV
