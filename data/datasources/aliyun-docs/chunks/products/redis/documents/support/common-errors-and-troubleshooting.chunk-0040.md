### Could not get a resource from the pool
可能原因：无法从连接池获取到Jedis连接。
当blockWhenExhausted参数为true（默认）时，若连接池没有可用的Jedis连接，客户端通常会等待一段时间（等待时间由maxWaitMillis参数决定，单位为毫秒），若长时间没有获取到可用的Jedis连接，会出现如下异常：
redis.clients.jedis.exceptions.JedisConnectionException: Could not get a resource from the pool … Caused by: java.util.NoSuchElementException: Timeout waiting for idle object at org.apache.commons.pool2.impl.GenericObjectPool.borrowObject(GenericObjectPool.java:449)
当blockWhenExhausted参数为false时，若连接池没有可用的Jedis连接，则会立即出现如下异常：
redis.clients.jedis.exceptions.JedisConnectionException: Could not get a resource from the pool … Caused by: java.util.NoSuchElementException: Timeout waiting for idle object at org.apache.commons.pool2.impl.GenericObjectPool.borrowObject(GenericObjectPool.java:449)
解决方法：您可以从如下几个方面进行排查。
连接泄露
JedisPool默认maxTotal值为8，从如下代码得知，从JedisPool中获取了8个Jedis资源，但没有归还资源。因此，在第9次尝试获取Jedis资源时，无法调用jedisPool.getResource().ping()。
GenericObjectPoolConfig poolConfig = new GenericObjectPoolConfig(); JedisPool jedisPool = new JedisPool(poolConfig, "127.0.0.1", 6379); // 向JedisPool借用8次连接，但是没有执行归还操作。 for (int i = 0; i < 8; i++) { Jedis jedis = null; try { jedis = jedisPool.getResource(); jedis.ping(); } cat
