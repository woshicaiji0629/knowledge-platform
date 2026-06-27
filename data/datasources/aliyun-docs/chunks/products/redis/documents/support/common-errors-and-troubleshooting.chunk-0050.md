### java.lang.Long cannot be cast to java.util.List
可能原因：若多个线程操作同一个Jedis连接就会返回该报错，Jedis本身存在线程安全问题。
解决方法：Jedis的正确使用方法是一个线程操作一个Jedis。您可以使用JedisPool（非Jedis）避免该问题。
