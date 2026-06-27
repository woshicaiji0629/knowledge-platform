"127.0.0.1", 6379); // 向JedisPool借用8次连接，但是没有执行归还操作。 for (int i = 0; i < 8; i++) { Jedis jedis = null; try { jedis = jedisPool.getResource(); jedis.ping(); } catch (Exception e) { logger.error(e.getMessage(), e); } } jedisPool.getResource().ping();
推荐使用如下规范代码。
Jedis jedis = null; try { jedis = jedisPool.getResource(); // 具体的命令。 jedis.executeCommand() } catch (Exception e) { // 如果命令有Key，建议在错误日志中把Key打印出来，对于集群架构来说，可通过Key定位到具体节点。 logger.error(e.getMessage(), e); } finally { // 注意：这里不是关闭连接，在JedisPool模式下，Jedis会被归还给资源池。 if (jedis != null) jedis.close(); }
maxTotal值设置得过小
当业务并发量大时，可能会由于maxTotal值设置的过小导致异常。例如，一次命令运行时间的平均耗时约为1ms（Borrow|Return resource+ Jedis执行命令 + 网络时间），一个连接的QPS大约为1000，业务期望的QPS为50000，则理论上需要的maxTotal值为50000 / 1000 = 50。
在该情况下，您可以在客户端所在的机器上执行下述命令，该命令返回的结果为连接客户端的连接数，您可以根据该数值对maxTotal值进行调整。
netstat -an | grep 6379 | grep EST | wc -l
Jedis连接阻塞
当Tair实例发生阻塞时（例如慢查询等原因），所有连接会在超时时间范围内等待，当并发量较大时，会造成连接池资源不足，更多信息请参见[connect timed out](common-errors-and-troubleshooting.md)。
Jedis连接被拒绝
从JedisPool中获取连接时，由于没有空闲连接，需要重新生成一个Jedis连接，但是连接被拒绝，异常示例如下：
redis.clients.jedis.exceptions.JedisConnectionException: Could not get a resource from the pool at redis.clients.util.Pool.getResource(Pool.java:50) at
