### Unexpected end of stream
可能原因：Jedis缓冲区异常，您可以从如下几个方面进行排查。
多个线程使用一个Jedis连接
通常情况下，一个线程使用一个Jedis连接。例如下面代码就是两个线程共用了一个Jedis连接：
new Thread(new Runnable() { public void run() { for (int i = 0; i < 100; i++) { jedis.get("hello"); } } }).start(); new Thread(new Runnable() { public void run() { for (int i = 0; i < 100; i++) { jedis.hget("haskey", "f"); } } }).start();
为避免出现这种情况，您可以使用JedisPool管理Jedis连接，实现线程安全。
长时间闲置连接
长时间闲置连接会被服务端主动断开，请查询实例的timeout参数配置、Jedis连接池配置，确定是否需要进行空闲超时检测。
说明
默认设置下，即使某个客户端已经空闲了很长时间，Tair也不会主动断开与该客户端的连接，若您调整过timeout参数，则可能会遇到该问题。更多信息请参见[设置客户端连接的空闲时间](../user-guide/specify-a-timeout-period-for-client-connections.md)。
解决方法：检查是否有多线程共用Jedis代码或由于长时间闲置连接造成服务端断开连接。
