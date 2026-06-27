## 高安全白名单模式IP白名单
说明
云盘实例不支持高安全白名单模式，[高性能本地盘存储类型已停止售卖](premium-local-ssds-are-no-longer-available-for-purchase-for-rds-for-postgresql-instances-since-september-1-2023.md)。
高安全白名单模式区分经典网络和专有网络，白名单分组需指定网络隔离模式，例如，经典网络的白名单IP地址不可从专有网络访问RDS实例，反之亦然。
如果高性能本地盘实例已经是高安全白名单模式，参见下文进行设置即可。如果需要切换为高安全白名单模式，请参见[切换为高安全白名单模式](switch-an-apsaradb-rds-for-postgresql-instance-to-the-enhanced-whitelist-mode.md)。
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏单击白名单与安全组。
单击添加白名单分组，选择网络隔离模式。
填写分组名称。
在组内白名单中，填写需要访问该实例的IP地址或IP段，然后单击确定。
重要
用英文逗号隔开多个IP地址或IP段，且逗号前后不能有空格，例如192.168.0.1,172.16.213.9。
单个实例最多添加1000个IP地址或IP段。当IP地址较多时，建议将零散的IP合并为IP段，例如10.10.10.0/24。
（可选）如果当前实例包含只读实例，可以通过参数白名单同步到只读实例配置白名单同步，将主实例的白名单同步至指定的只读实例。当有多个只读实例时，支持多选。
（可选）单击加载ECS内网IP，将显示您当前阿里云账号下所有ECS实例的IP地址，可快速将ECS私有IP地址添加到白名单中。
说明
高安全白名单模式请注意选择网络隔离模式。
