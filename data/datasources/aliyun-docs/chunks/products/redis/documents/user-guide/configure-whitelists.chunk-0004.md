## 添加公网IP到白名单
当您需要从本地设备远程访问实例或您的ECS与实例不在同一专有网络（VPC）时，请参考以下步骤添加白名单。
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击白名单设置。
在default默认安全组，单击修改。
说明
您也可以单击添加白名单分组创建一个新的分组。分组名称长度为2~32个字符，由小写字母、数字或下划线（_）组成，需以小写字母开头，以小写字母或数字结尾。
添加方式选择手动添加。
在组内白名单文本框中，输入IP地址或IP地址段。
查询本地设备公网IP和ECS公网IP的方法

| 类别 | 查询公网 IP 地址的方法 |
| --- | --- |
| [ECS](../../../ecs/documents/user-guide/what-is-ecs.md) [实例](../../../ecs/documents/user-guide/what-is-ecs.md) | [查询](../../../ecs/documents/user-guide/network-faq.md) [ECS](../../../ecs/documents/user-guide/network-faq.md) [的](../../../ecs/documents/user-guide/network-faq.md) [IP](../../../ecs/documents/user-guide/network-faq.md) [地址？](../../../ecs/documents/user-guide/network-faq.md) |
| 本地 | 查询本地设备公网 IP 地址的方式可能因您所处的网络环境或操作不同而不同。以下是不同系统通过命令方式获取本地设备公网 IP 地址的参考方法： Linux 操作系统：打开终端，输入 curl ifconfig.me 命令后回车。 Windows 操作系统：打开命令提示符，输入 curl ip.me 命令后回车。 macOS 操作系统：打开终端，输入 curl ifconfig.me 命令后回车。 |
