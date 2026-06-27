### ERR max number of clients reached
可能原因：客户端的连接数超过了Tair实例的最大连接数。
解决方法：
检查客户端是否出现连接泄露，例如在Jedis客户端中，使用连接池后未调用close函数。
通过[实例会话](../user-guide/instance-sessions.md)查看当前连接实例的会话是否符合预期，您可以根据业务需求终止异常会话，或者通过[升级实例配置](../user-guide/change-the-configurations-of-an-instance.md)，扩大连接数。
