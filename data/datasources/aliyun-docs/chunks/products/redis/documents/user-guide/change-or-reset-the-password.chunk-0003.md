## 常见问题
Q：云数据库 Tair（兼容 Redis）实例的密码可以为空吗？
A：当实例开启[专有网络免密访问](enable-password-free-access.md)时，在同一专有网络下无需密码即可连接Tair实例。除此之外，连接实例均需要使用账号密码进行鉴权验证，您需要为实例配置账号、密码。
Q：修改密码后，为什么在DMS中报错“WRONGPASS invalid username-password pair”？
A：修改密码后，您需要在DMS的数据库列表中，右键单击目标实例，选择编辑实例，重新填写账号密码。
