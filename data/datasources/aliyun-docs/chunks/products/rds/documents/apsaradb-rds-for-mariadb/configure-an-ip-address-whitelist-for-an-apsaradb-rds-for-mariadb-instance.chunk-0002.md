## 设置IP白名单
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏中单击白名单与安全组。
在白名单设置页签中，单击default白名单分组中的修改。
说明
您也可以单击添加白名单分组新建自定义分组。
在修改白名单分组对话框中，填写需要访问该实例的IP地址或IP段，然后单击确定。
说明
当您在default分组中添加新的IP地址或IP段后，系统自动删除默认地址127.0.0.1。
若您需要添加多个IP地址或IP段，请用英文逗号隔开（逗号前后都不能有空格），例如192.168.0.1,172.16.213.9。
单击加载ECS内网IP后，将显示您当前阿里云账号下所有ECS实例的IP地址，可快速添加ECS内网IP地址到白名单中。
当应用程序部署在ACK集群的容器中时，需要根据[容器网络插件](../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)添加不同的IP地址。
当ACK集群的容器网络插件为Flannel时，添加应用程序所在的节点IP。
当ACK集群的容器网络插件为Terway时，添加应用程序所在的Pod IP。
您在目标ACK集群的[容器组](../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/manage-pods.md)页面，查Pod IP和节点IP。
