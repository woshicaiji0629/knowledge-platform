## 操作步骤
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在时序存储>时序库页签中，在目标MetricStore下面选择数据接入>logtail配置，然后在右侧页面单击添加Logtail配置。
在快速数据接入对话框中，单击Ping 监控。
在创建机器组页签中。
如果已有可用的机器组，请单击使用现有机器组。
如果您还没有可用的机器组，请执行以下操作（以ECS为例）。
在ECS机器页签中，通过手动选择实例方式选择目标ECS实例，单击创建。
具体操作，请参见[安装](install-logtail-on-ecs-instances.md)[Logtail（ECS](install-logtail-on-ecs-instances.md)[实例）](install-logtail-on-ecs-instances.md)。
重要
如果您的服务器是与日志服务属于不同账号的ECS、其他云厂商的服务器和自建IDC时，您需要手动安装Logtail。具体操作，请参见[安装](install-logtail-on-a-linux-server.md)[Logtail（Linux](install-logtail-on-a-linux-server.md)[系统）](install-logtail-on-a-linux-server.md)。手动安装Logtail后，您必须在该服务器上手动配置用户标识。具体操作，请参见[配置用户标识](configure-a-user-identifier.md)。
安装完成后，单击确认安装完毕。
在创建机器组页面，输入名称，单击下一步。
日志服务支持创建IP地址机器组和用户自定义标识机器组，具体操作，请参见[创建机器组](manage-machine-groups.md)。
确认目标机器组已在应用机器组区域，单击下一步。
重要
创建机器组后立刻应用，可能因为连接未生效，导致心跳为FAIL，您可单击自动重试。如果还未解决，请参见[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[机器组无心跳](troubleshoot-the-errors-related-to-logtail-machine-groups.md)进行排查。
在数据源设置页签中，设置配置名称和插件配置，然后单击下一步。
重要
inputs为数据源配置，必选项。一个inputs中只允许配置一个类型的数据源。
{{ "inputs": [ { "detail": { "tcp": [ { "port": 80, "src": "192.XX.XX.103", "count": 3, "targe
