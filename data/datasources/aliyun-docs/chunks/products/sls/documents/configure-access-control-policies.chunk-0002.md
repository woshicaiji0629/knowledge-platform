## 自定义角色授权（同账号）
对同一个阿里云账号下的不同日志库或指标库进行告警监控时，您可以通过自定义角色实现告警监控。
[创建可信实体为阿里云服务的](../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)[RAM](../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)[角色](../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)，其中受信服务请选择日志服务。
创建一个自定义权限策略，其中在脚本编辑页签，请使用以下脚本替换配置框中的原有内容。具体操作，请参见[通过脚本编辑模式创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)。
重要
Project名称需根据实际情况替换。如果您需要更细粒度的授权，例如只允许在指定Project下创建监控规则，则可以在下述策略的Resource中指定具体的Project，例如acs:log:*:*:project/my-project。
{ "Statement": [ { "Action": [ "log:ListProject" ], "Effect": "Allow", "Resource": [ "acs:log:*:*:*" ] }, { "Action": [ "log:ListLogStores", "log:GetLogStoreLogs", "log:GetIndex" ], "Effect": "Allow", "Resource": [ "acs:log:*:*:project/Project名称/*" ] } ], "Version": "1" }
为RAM角色添加创建的自定义权限。具体操作，请参见[管理](../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色的权限](../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
