stom-policy.md)。
重要
将配置框中的原有脚本替换为如下内容。其中，Project名称需根据实际情况替换。如果您想要更细粒度的授权，例如只允许在指定Project下创建监控规则，则可以在下述策略的Resource中指定具体的Project，例如acs:log:*:*:project/my-project。
{ "Statement": [ { "Action": [ "log:ListProject" ], "Effect": "Allow", "Resource": [ "acs:log:*:*:*" ] }, { "Action": [ "log:ListLogStores", "log:GetLogStoreLogs", "log:GetIndex" ], "Effect": "Allow", "Resource": [ "acs:log:*:*:project/Project名称/*" ] } ], "Version": "1" }
为RAM角色添加创建的自定义权限。具体操作，请参见[管理](../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色的权限](../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
获取RAM角色标识（ARN），具体操作，请参见[查看](../../ram/documents/user-guide/view-the-information-about-a-ram-role.md)[RAM](../../ram/documents/user-guide/view-the-information-about-a-ram-role.md)[角色](../../ram/documents/user-guide/view-the-information-about-a-ram-role.md)。
