| 权限 | 对应操作 | 资源 |
| --- | --- | --- |
| 只读 Project | GetAcceleration GetLogging ListProject ListDomains ListTagResources | acs:log:${regionName}:${uid}:project/* |
| 获取指定 Project | GetProject | acs:log:${regionName}:${uid}:project/${projectName} |
| 管理 LogStore | ListLogStores *LogStore *Index ListShards GetCursorOrData GetLogStoreHistogram GetLogStoreContextLogs PostLogStoreLogs | acs:log:${regionName}:${uid}:project/${projectName}/* |
| 管理 LoongCollector（Logtail）数据接入 | * | acs:log:${regionName}:${uid}:project/${projectName}/logtailconfig/* acs:log:${regionName}:${uid}:project/${projectName}/machinegroup/* |
| 查询快速查询 | ListSavedSearch | acs:log:${regionName}:${uid}:project/${projectName}/savedsearch/* |
| 查询仪表盘 | ListDashboard | acs:log:${regionName}:${uid}:project/${projectName}/dashboard/* |
| 查询指定日志库日志 | GetLogStoreLogs | acs:log:${regionName}:${uid}:project/${projectName}/logstore/${logstoreName} |
| 操作 ECS 的权限 | DescribeTagKeys DescribeTags DescribeInstances DescribeInvocationResults RunCommand DescribeInvocations InvokeCommand | * |
| 操作 OOS 的权限（ 可选） 仅在日志服务与 ECS 实例同账号同地域通过 OOS 自动化安装 LoongCollector(Logtail)时需要。 | ListTemplates StartExecution ListExecutions GetExecutionTempla
