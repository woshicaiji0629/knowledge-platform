### 没有可用机器组
单击创建机器组，在创建机器组面板设置相关参数。机器组标识分为IP地址和用户自定义标识，更多信息请参见[创建用户自定义标识机器组（推荐）](create-a-user-defined-identity-machine-group.md)或[创建](create-an-ip-address-based-machine-group.md)[IP](create-an-ip-address-based-machine-group.md)[地址机器组](create-an-ip-address-based-machine-group.md)。
重要
创建机器组后立刻应用，可能因为连接未生效，导致心跳为FAIL，您可单击自动重试。如果还未解决，请参见[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[机器组无心跳](troubleshoot-the-errors-related-to-logtail-machine-groups.md)进行排查。
在数据源设置页签中，设置配置名称和插件配置，然后单击下一步。
inputs为数据源配置，必选项。
重要
一个inputs中只允许配置一个类型的数据源。
processors为处理配置，用于解析数据。可选项，您可以配置一种或多种处理方式。
如果当前的inputs配置无法满足日志解析需求，您可以在插件配置中添加processors配置，即添加Logtail插件处理数据。例如提取字段、提取日志时间、脱敏数据、过滤日志等。更多信息，请参见[使用](overview-22.md)[Logtail](overview-22.md)[插件处理数据](overview-22.md)。
例如您要采集应用程序、系统、TerminalServices-LocalSessionManager/Operational等通道对应的日志，则可以在inputs中添加如下示例。
{ "inputs": [ { "type": "service_wineventlog", "detail": { "Name": "Application", "IgnoreOlder": 259200 } }, { "type": "service_wineventlog", "detail": { "Name": "System", "IgnoreOlder": 259200 } }, { "type": "service_wineventlog", "detail": { "Name": "Microsoft-Windows-TerminalServices-LocalSessionManager/Operational", "IgnoreOlder": 259
