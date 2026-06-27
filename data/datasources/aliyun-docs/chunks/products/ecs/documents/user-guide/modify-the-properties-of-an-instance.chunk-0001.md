## 操作步骤
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
单击目标实例ID进入实例详情页，单击全部操作展开所有操作面板，然后搜索并单击编辑实例属性。
在弹出的编辑实例属性对话框中，根据页面提示修改实例属性，然后单击确定。
说明
Windows操作系统的主机名不能超过15位，将Linux操作系统更换为Windows操作系统时，请确保实例的主机名符合要求。更多信息，请参见[更换操作系统（更换系统盘）](replace-the-operating-system-of-an-instance.md)。
（条件必选）重启实例。
如果修改了主机名（HostName），需要重启实例使新主机名生效。在操作系统内重启无效，必须通过ECS管理控制台或者调用API[RebootInstance](../api-rebootinstance.md)重启ECS实例。具体操作，请参见[重启实例](restart-instances.md)。
警告
重启实例会造成您的实例停止工作，可能导致业务中断，建议您在非业务高峰期时执行该操作。
