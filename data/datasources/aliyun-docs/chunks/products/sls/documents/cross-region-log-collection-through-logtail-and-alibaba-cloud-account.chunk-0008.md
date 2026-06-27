## 步骤四：在地域B的日志服务Project中创建Logtail采集配置
重要
安装Logtail的主机需要在出口方向开放80（HTTP）端口和443（HTTPS）端口。ECS实例的端口由安全组规则控制，添加安全组规则的步骤请参见[添加安全组规则](../../ecs/documents/user-guide/add-a-security-group-rule.md)。
服务器日志的内容持续新增。Logtail只采集增量日志，如果下发Logtail配置后日志文件无更新，则Logtail不会采集该文件中的日志。更多信息，请参见[读取日志](log-collection-process-of-logtail.md)。
如需采集历史数据，请参见[导入历史日志文件](import-historical-logs.md)。
