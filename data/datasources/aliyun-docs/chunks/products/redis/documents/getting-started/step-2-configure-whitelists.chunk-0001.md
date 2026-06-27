## 操作步骤
本示例的客户端在ECS上，且ECS与实例为同一专有网络（VPC）。
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击白名单设置。
在default默认安全组，单击修改。
添加方式选择加载ECS私网IP，页面将展示该实例同一地域的ECS私网IP。
鼠标指针悬浮在IP地址上，可查看该IP地址所属ECS ID和名称。
选中需要的IP地址，将其移至右侧。
单击确定。
下一步，您可以在客户端上连接云数据库 Tair（兼容 Redis）实例，更多信息请参见[步骤](step-3-connect-to-an-apsaradb-for-redis-instance.md)[3：连接实例](step-3-connect-to-an-apsaradb-for-redis-instance.md)。
