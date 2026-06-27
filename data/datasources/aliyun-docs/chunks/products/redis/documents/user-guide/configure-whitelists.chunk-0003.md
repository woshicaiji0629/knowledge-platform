## 添加ECS私网IP到白名单
如果您的ECS与实例位于同一专有网络（VPC），推荐您通过专有网络访问。
说明
如果您的ECS与实例不属于同一专有网络，您可以更换ECS所属的专有网络。具体操作，请参见[更换](../../../ecs/documents/user-guide/change-the-vpc-of-an-ecs-instance.md)[ECS](../../../ecs/documents/user-guide/change-the-vpc-of-an-ecs-instance.md)[的](../../../ecs/documents/user-guide/change-the-vpc-of-an-ecs-instance.md)[VPC](../../../ecs/documents/user-guide/change-the-vpc-of-an-ecs-instance.md)。
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击白名单设置。
在default默认安全组，单击修改。
说明
您也可以单击添加白名单分组创建一个新的分组。分组名称长度为2~32个字符，由小写字母、数字或下划线（_）组成，需以小写字母开头，以小写字母或数字结尾。
添加方式选择加载ECS私网IP，页面将展示该实例同一地域的ECS私网IP。
鼠标指针悬浮在IP地址上，可查看该IP地址所属ECS的ID和名称
选中需要的IP地址，将其移至右侧。
单击确定。
可选：若某个白名单分组中的所有IP地址均需要移除，您可以在目标白名单分组的右侧单击删除来完成该操作。
系统默认生成的白名单分组无法删除，例如default、hdm_security_ips等。
