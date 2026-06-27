## 一键安装Logtail
日志服务可一键在ECS中安装Logtail，借助OOS编排能力，无需登录ECS手动执行安装步骤。如果您使用阿里云主账号登录，默认拥有所有操作权限，可直接进行相关操作。
若您使用RAM用户登录，请联系主账号授予操作OOS资源的权限，主账号可以通过系统权限或自定义权限为您[创建](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md)[RAM](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md)[用户及授权](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md)：
系统权限：
AliyunOOSFullAccess：用于管理系统运维管理（OOS）的所有权限。
AliyunECSFullAccess：管理ECS的权限。
自定义权限：若对数据安全要求高，可以[创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)实现精细化授权。如下为操作OOS资源的权限策略：
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "ecs:DescribeTagKeys", "ecs:DescribeTags", "ecs:DescribeInstances", "ecs:DescribeInvocationResults", "ecs:RunCommand", "ecs:DescribeInvocations", "ecs:InvokeCommand" ], "Resource": "*" }, { "Effect": "Allow", "Action": [ "oos:ListTemplates", "oos:StartExecution", "oos:ListExecutions", "oos:GetExecutionTemplate", "oos:ListExecutionLogs", "oos:ListTaskExecutions" ], "Resource": "*" } ] }
通过以下操作步骤，您可以实现在ECS实例中一键安装Logtail的同时，完成机器组的创建和配置：
登录[日志服务控制台](https://sls.console.aliyun.com/)，单击管理日志资源的Project查看日志库列表，单击存放日志的LogStore名称前的展开，之后单击数据接入后的，在弹框中选择文本日志接入模板，单击立即接入。
日志服务提供了正则、单行
