Seconds(TCP_USER_TIMEOUT)) .build()) .build(); client = RedisClient.create(uri); client.setOptions(ClientOptions.builder() .socketOptions(socketOptions) .build()); connection = client.connect(); RedisCommands<String, String> commands = connection.sync(); System.out.println(commands.set("foo", "bar")); System.out.println(commands.get("foo")); // 当应用退出，需销毁资源时，调用此方法。此方法会断开连接、释放资源。 connection.close(); client.shutdown(); } }
执行上述代码，预期会返回如下结果：
OK bar
