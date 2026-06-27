### 部分实例版本不支持RESP3协议，报错unknown command
可能原因：Redis 6.0及以上版本支持了RESP3协议，可通过HELLO命令切换RESP协议。但部分低版本实例不支持HELLO命令，可能会存在兼容性问题。
解决方法：您可以直接在程序中指定以RESP2协议访问Tair实例，示例如下：
client.setOptions(ClientOptions.builder() .protocolVersion(ProtocolVersion.RESP2) .build());
若使用Spring-data-redis with Lettuce，示例如下：
LettuceClientConfiguration lettuceClientConfiguration = LettuceClientConfiguration.builder(). clientOptions(ClientOptions.builder().protocolVersion(ProtocolVersion.RESP2).build()).build(); return new LettuceConnectionFactory(redisClusterConfiguration, lettuceClientConfiguration);
