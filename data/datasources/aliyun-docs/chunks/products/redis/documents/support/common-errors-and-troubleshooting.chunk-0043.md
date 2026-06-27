lainSocketImpl.socketConnect(Native Method) at java.net.AbstractPlainSocketImpl.doConnect(AbstractPlainSocketImpl.java:339) at java.net.AbstractPlainSocketImpl.connectToAddress(AbstractPlainSocketImpl.java:200) at java.net.AbstractPlainSocketImpl.connect(AbstractPlainSocketImpl.java:182) at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:392) at java.net.Socket.connect(Socket.java:579) at redis.clients.jedis.Connection.connect(Connection.java:158) ... 9 more
可以从at redis.clients.jedis.Connection.connect(Connection.java:158)中看出，实际是在创建一个Socket连接，并调用connect函数，但是被拒绝连接，如下为Jedis源码。
socket.setSoLinger(true, 0); 158: socket.connect(new InetSocketAddress(host, port), connectionTimeout);
通常情况下，该问题需要排查Tair的域名配置是否正确、该段时间网络是否正常。
