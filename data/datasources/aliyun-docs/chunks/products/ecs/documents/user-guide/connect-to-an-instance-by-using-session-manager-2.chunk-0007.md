## 相关权限管理
如果RAM用户需要通过会话管理连接实例，相关操作的权限及说明如下：
操作（Action）列对应RAM权限策略中的操作（Action）。

| 操作（Action） | 说明 |
| --- | --- |
| ecs:StartTerminalSession | 通过会话管理功能连接到 ECS 实例。 （必须） |
| ecs:DescribeCloudAssistantStatus | 查询 ECS 实例是否安装云助手 Agent，该权限用于控制台在连接前进行校验。 |
| ecs:DescribeUserBusinessBehavior | 查询会话管理是否开启，该权限用于控制台在连接前进行校验。 |
| ecs:ModifyCloudAssistantSettings | 开启或关闭会话管理，如果当前阿里云账号已经开启会话管理功能，无需分配该权限。 |
