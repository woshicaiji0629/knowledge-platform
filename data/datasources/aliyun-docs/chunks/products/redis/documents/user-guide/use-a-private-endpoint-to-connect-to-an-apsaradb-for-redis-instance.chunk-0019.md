veOptions.builder() .enable() .idle(Duration.ofSeconds(TCP_KEEPALIVE_IDLE)) .interval(Duration.ofSeconds(TCP_KEEPALIVE_IDLE/3)) .count(3) .build()) .tcpUserTimeout(SocketOptions.TcpUserTimeoutOptions.builder() .enable() .tcpUserTimeout(Duration.ofSeconds(TCP_USER_TIMEOUT)) .build()) .build(); RedisClusterClient redisClient = RedisClusterClient.create(redisURI); redisClient.setOptions(ClusterClientOptions.builder() .socketOptions(socketOptions) .validateClusterNodeMembership(false) .topologyRefreshOptions(refreshOptions).build()); StatefulRedisClusterConnection<String, String> connection = redisClient.connect(); connection.sync().set("key", "value"); System.out.println(connection.sync().get("key")); } }
执行上述代码，预期会返回如下结果：
value
Lettuce 相关参数说明如下：
