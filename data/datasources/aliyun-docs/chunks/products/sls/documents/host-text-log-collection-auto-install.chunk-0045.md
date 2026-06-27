## 自定义权限策略（精细化控制）
当系统策略无法满足最小权限原则时，可通过[创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)实现精细化授权。以下为权限策略示例，包含的权限有：
查看Project：查看Project列表，查看指定Project详情。
管理日志库 (LogStore)：在Project下创建新的日志库，或修改、删除已有的日志库。
管理采集配置：创建、删除和修改采集配置。
查看日志：查询和分析指定Project下指定日志库中的数据。
替换${regionName}${uid}、${projectName}、${logstoreName}为实际的地域名称，主账号id，目标Project和LogStore。
示例策略
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "log:ListProject", "log:GetAcceleration", "log:ListDomains", "log:GetLogging", "log:ListTagResources" ], "Resource": "acs:log:${regionName}:${uid}:project/*" }, { "Effect": "Allow", "Action": "log:GetProject", "Resource": "acs:log:${regionName}:${uid}:project/${projectName}" }, { "Effect": "Allow", "Action": [ "log:ListLogStores", "log:*LogStore", "log:*Index", "log:ListShards", "log:GetCursorOrData", "log:GetLogStoreHistogram", "log:GetLogStoreContextLogs", "log:PostLogStoreLogs" ], "Resource": "acs:log:${regionName}:${uid}:project/${projectName}/*" }, { "Effect": "Allow", "Action": "log:*", "Resource": [ "acs:log:${regionName}:${uid}:project/${projectName}/logtailconfig/*", "acs:log:${regionName}:${uid}:project/${projectName}/machinegroup/*" ] }, { "Effect": "Allow", "Ac
