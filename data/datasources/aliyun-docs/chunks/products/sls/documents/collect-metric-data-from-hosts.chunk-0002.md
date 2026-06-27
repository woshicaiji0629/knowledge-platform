## 数据采集配置
登录[日志服务控制台](https://sls.console.aliyun.com)。
单击控制台右侧的快速接入数据卡片。
在接入数据页面，查找主机监控并单击。
选择目标Project和时序库MetricStore，单击下一步。在选择日志空间步骤中，选择已有的项目Project和时序库MetricStore，或单击右侧立即创建新建，然后单击下一步。
在创建机器组页签中。
如果已有可用的机器组，请单击使用现有机器组。选择主机场景和ECS安装环境，从源机器组列表中选择目标机器组，单击>将其移至应用机器组列表，然后单击下一步。
如果您还没有可用的机器组，请执行以下操作（以ECS为例）。
在ECS机器页签中，通过手动选择实例方式选择目标ECS实例，单击创建。
具体操作，请参见[安装](install-logtail-on-ecs-instances.md)[Logtail（ECS](install-logtail-on-ecs-instances.md)[实例）](install-logtail-on-ecs-instances.md)。
重要
如果您的服务器是与日志服务属于不同账号的ECS、其他云厂商的服务器和自建IDC时，您需要手动安装Logtail。具体操作，请参见[安装](install-logtail-on-a-linux-server.md)[Logtail（Linux](install-logtail-on-a-linux-server.md)[系统）](install-logtail-on-a-linux-server.md)。手动安装Logtail后，您必须在该服务器上手动配置用户标识。具体操作，请参见[配置用户标识](configure-a-user-identifier.md)。
安装完成后，单击确认安装完毕。
在创建机器组页面，输入名称，单击下一步。
日志服务支持创建IP地址机器组和用户自定义标识机器组，具体操作，请参见[创建机器组](manage-machine-groups.md)。
在数据源设置页签中，设置配置名称和插件配置，然后单击下一步。
重要
inputs为数据源配置，必选项。一个inputs中只允许配置一个类型的数据源。
{ "inputs": [ { "detail": { "IntervalMs": 30000 }, "type": "metric_system_v2" } ] }
