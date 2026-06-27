"Allow", "Action": [ "log:GetProject" ], "Resource": [ "acs:log:*:*:project/${projectName}" ] }, { "Effect": "Allow", "Action": [ "log:ListLogStores", "log:GetLogStore", "log:GetLogStoreHistogram", "log:GetIndex", "log:CreateIndex", "log:UpdateIndex", "log:ListShards", "log:GetCursorOrData", "log:ListSavedSearch", "log:GetLogStoreLogs", "log:ListDashboard", "log:GetLogStoreContextLogs" ], "Resource": [ "acs:log:*:*:project/${projectName}/*" ] }, { "Effect": "Allow", "Action": [ "log:*" ], "Resource": [ "acs:log:*:*:project/${projectName}/logtailconfig/*", "acs:log:*:*:project/${projectName}/machinegroup/*" ] } ] }
创建Project
若您无可用Project，请参考此处步骤创建一个基础Project，如需详细了解创建配置请参见[管理](manage-a-project.md)[Project](manage-a-project.md)。
登录[日志服务控制台](https://sls.console.aliyun.com)，单击创建Project完成下述基础配置，其他配置保持默认即可：
所属地域：请根据日志来源等信息选择合适的阿里云地域，创建后不可修改。
Project名称：设置名称，名称在阿里云地域内全局唯一，创建后不可修改。
创建LogStore
若您无可用LogStore，请参考此处步骤创建一个基础LogStore，如需详细了解创建配置请参见[管理](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表中单击目标Project。
在日志存储的日志库页签中，单击+图标。
填写Logstore名称，其余配置保持默认无需修改。
服务器网络要求
安装LoongCollector的机器需在出口方向开放80（HTTP）端口和443（HTTPS）端口，供LoongCollector上传数据。
