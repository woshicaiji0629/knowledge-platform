-attempts-to-pass-the-server-and-port-disconnection.md)[ECS](troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[实例公网](troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[IP](troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[的排查方法](troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)。
步骤三：检查端口和安全组
检查安全组配置是否允许远程连接的端口。
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
在实例列表页面，单击对应的实例ID。
在安全组页签下，单击安全组操作列的管理规则。
在安全组详情页面，在访问规则区域的入方向页签下，单击增加规则，按以下参数添加规则。
授权策略：允许
优先级：1（代表安全规则中优先级最高，数字越小优先级越高）
协议：自定义 TCP
访问来源：设置为本机IP，可以访问[https://cip.cc/](https://cip.cc/)获取本机IP
访问目的(本实例)：选择SSH(22)
使用以下命令，进行端口测试，判断端口是否正常。
telnet [$IP] [$Port]
说明
[$IP]指Linux实例的IP地址。
[$Port]指Linux实例的RDP端口号。
系统显示类似如下，比如执行telnet 192.168.0.1 22命令，正常情况下返回结果类似如下。
Trying 192.168.0.1 ... Connected to 192.168.0.1. Escape character is '^]'
如果端口测试失败，请参见[能](troubleshoot-the-issue-that-an-instance-can-be-pinged-but-the-required-port-cannot.md)[ping](troubleshoot-the-issue-that-an-instance-can-be-pinged-but-the-required-port-cannot.md)[通](troubl
