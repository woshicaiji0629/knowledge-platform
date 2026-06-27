### 添加IPv6安全组规则
IPv4和IPv6通信彼此独立，如果当前的安全组规则不能满足业务需求，为了增强网络安全性您需要为ECS实例单独配置IPv6安全组规则。
如何添加IPv6安全组规则
访问[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
找到目标安全组，在操作列中，单击管理规则。
在安全组详情页，找到访问规则区域，选择入方向或出方向。
添加安全组规则。具体操作，请参见[添加安全组规则](start-using-security-groups.md)。
说明
您需要设置访问来源为IPv6地址段，例如：2001:db8:1234:1a00::***。有关安全组规则更多信息，可参见[安全组规则](security-group-rules.md)。
