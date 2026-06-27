## 自定义角色授权
当授权方式选择为自定义角色时，需要先配置权限策略，创建自定义角色，并为角色授权。
使用阿里云账号（主账号）或RAM管理员登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。
创建一个自定义权限策略，其中在脚本编辑页签，请使用以下脚本替换配置框中的原有内容。具体操作，请参见[通过脚本编辑模式创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)。
{ { "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "log:PostLogStoreLogs", "Resource": "*" } ] }
创建阿里云服务需要扮演的RAM角色。具体操作，请参见[创建可信实体为阿里云服务的](../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)[RAM](../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)[角色](../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)。
重要
创建RAM角色时，信任主体类型应选择云服务，且信任主体名称应选择日志服务。
请检查角色的信任策略如下，Service内容至少包含"log.aliyuncs.com"。
{ "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Principal": { "Service": [ "log.aliyuncs.com" ] } } ], "Version": "1" }
为RAM角色添加创建的自定义权限。具体操作，请参见[管理](../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色的权限](../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
