roject", "log:CreateProject" ], "Resource": [ "acs:log:*:*:project/sls-alert-*" ] }, { "Effect": "Allow", "Action": [ "log:GetLogStoreLogs", "log:ListLogStores", "log:GetIndex", "log:GetDashboard", "log:CreateDashboard", "log:UpdateDashboard", "log:ListDashboard" ], "Resource": [ "acs:log:*:*:project/Project名称/*", "acs:log:*:*:project/sls-alert-*/*" ] }, { "Effect": "Allow", "Action": [ "log:*" ], "Resource": [ "acs:log:*:*:resource/*" ] } ] }
为RAM用户添加创建的自定义权限策略。具体操作，请参见[为](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
该文章对您有帮助吗？
反馈
