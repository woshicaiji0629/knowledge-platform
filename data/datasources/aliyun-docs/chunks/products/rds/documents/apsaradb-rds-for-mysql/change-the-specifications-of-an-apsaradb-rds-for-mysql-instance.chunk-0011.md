### 连接与网络
Q：变更配置后连接地址会变吗？
A：连接地址（如rm-bpxxxxx.mysql.rds.aliyuncs.com）不变，但IP可能变更。建议在应用程序中使用连接地址，而不是IP地址。
Q：如何设置应用程序重连机制？
A：Java应用建议TTL不超过60秒，以确保在连接地址的VIP地址发生变更时，应用程序可以通过重新查询DNS来接收和使用资源的新VIP地址。Java中设置TTL的方法请参见[JDK](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/net/InetAddress.html)[官方文档](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/net/InetAddress.html)。
