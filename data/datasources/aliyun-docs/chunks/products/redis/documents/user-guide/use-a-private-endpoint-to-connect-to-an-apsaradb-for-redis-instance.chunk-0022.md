## 常见问题
Q：为什么会报错MOVED 4578 172.18.xx.xxx:6379？
A：报错MOVED <slot> <IP:Port>表示当前查询的Key位于其他节点中，通常是使用不支持Redis Cluster的客户端导致的。例如以下情况（其他客户端也类似）。
使用redis-cli连接实例时没加-c。
使用Python时，使用普通的redis-py客户端，其并不支持自动重定向，应该使用redis-cluster客户端。
说明
更多报错请参见[常见报错](../support/common-errors-and-troubleshooting.md)。
该文章对您有帮助吗？
反馈
