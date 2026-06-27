## API
如果需要通过API查询实例云助手Agent状态，请参见[查询云助手安装状态](../developer-reference/api-ecs-2014-05-26-describecloudassistantstatus.md)。
准备用于使用会话管理的RAM用户的凭证
在使用ali-instance-cli工具时，配置阶段要求设置RAM用户的AccessKey、STS Token。当通过会话管理操作连接实例时，系统会验证此凭证对应的RAM用户是否拥有ecs:StartTerminalSession权限，这是允许通过会话管理建立与ECS实例连接的必要权限。
此外，在自定义权限策略时，可以通过指定Resource字段来限定RAM用户能够通过会话管理连接的具体ECS实例。权限策略示例如下：
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "ecs:StartTerminalSession", "Resource": "*" } ] }
关于CredentialsURI、STS Token的更多说明，请参见[创建](../../../ram/documents/create-an-accesskey-pair-1.md)[AccessKey](../../../ram/documents/create-an-accesskey-pair-1.md)、[什么是](../../../ram/documents/user-guide/what-is-sts.md)[STS](../../../ram/documents/user-guide/what-is-sts.md)。
为RAM用户授权，请参见[为](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
