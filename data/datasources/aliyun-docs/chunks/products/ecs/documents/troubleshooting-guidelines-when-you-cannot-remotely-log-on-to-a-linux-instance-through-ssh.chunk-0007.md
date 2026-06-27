ning-virus-protection-and-handling-guide.md)；如果实例感染勒索病毒，系统文件被加密锁定，同样可能导致无法正常登录，具体请参见[提升实例防勒索能力的指南](user-guide/enhance-anti-ransomware-capabilities-for-instances.md)。
不存在CPU负载过高情况，请继续下一步排查。
排查是否存在公网带宽不足问题。
无法远程连接可能是公网带宽不足导致的，具体排查方法如下。
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
在实例列表，单击对应的实例ID，在配置信息区域，查看公网带宽。
如果服务器带宽为0 Mbps，说明购买实例时没有购买公网带宽，您可以通过升级带宽解决，具体操作，请参见[修改公网带宽峰值](user-guide/overview-of-instance-configuration-changes.md)。
排查是否存在内存不足问题。
远程连接Linux实例后，不能正常显示桌面并直接退出，也没有错误信息提示。这种情况可能是服务器内存不足导致，需要检查服务器的内存使用情况。具体操作如下。
使用VNC方式登录Linux实例。
具体操作，请参见[通过密码认证登录](user-guide/log-on-to-an-instance-by-using-vnc.md)[Linux](user-guide/log-on-to-an-instance-by-using-vnc.md)[实例](user-guide/log-on-to-an-instance-by-using-vnc.md)。
查看内存使用情况，如果存在内存不足情况，建议您升配实例规格来解决资源瓶颈问题，具体操作，请参见[升降配方式概述](user-guide/overview-of-instance-configuration-changes.md)。
