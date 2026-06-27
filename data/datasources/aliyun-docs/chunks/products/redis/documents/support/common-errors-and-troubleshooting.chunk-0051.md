### Broken pipe (Write failed)
可能原因：在Jedis单连接模式（未使用JedisPool）下超时后，客户端关闭了Socket，此时若您继续调用读写接口写入数据，会返回该报错。
解决方法：Jedis的正确使用方法是一个线程操作一个Jedis。您可以使用JedisPool（非Jedis）避免该问题。
