## 前提条件
权限须知
如果您使用阿里云主账号登录，默认拥有所有操作权限，可直接进行相关操作。
若您使用RAM用户登录，请根据需要向主账号使用者申请如下系统策略以获得管理日志服务、ECS与OOS资源的权限。
AliyunLogFullAccess：授予管理日志服务的权限。
AliyunOOSFullAccess：授予管理OOS的权限，可执行OOS自动编排安装loongcollector。
AliyunECSFullAccess：授予管理ECS的权限，可执行ECS云助手命令批量安装loongcollector。
当系统策略无法满足您的需求，您可以参考下表通过[创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)实现精细化权限管理。
请将Resource中的${projectName}替换为您需要访问的Project名称。{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "ecs:DescribeTagKeys", "ecs:DescribeTags", "ecs:DescribeInstances", "ecs:DescribeInvocationResults", "ecs:RunCommand", "ecs:DescribeInvocations", "ecs:InvokeCommand" ], "Resource": "*" }, { "Effect": "Allow", "Action": [ "oos:ListTemplates", "oos:StartExecution", "oos:ListExecutions", "oos:GetExecutionTemplate", "oos:ListExecutionLogs", "oos:ListTaskExecutions" ], "Resource": "*" }, { "Effect": "Allow", "Action": [ "log:ListProject", "log:GetAcceleration", "log:ListDomains", "log:GetLogging", "log:ListTagResources" ], "Resource": [ "acs:log:*:*:project/*" ] }, { "Effect": "Allow", "Action": [ "log:GetProject" ], "Resource": [ "acs:log:*:*:project/${projectName}" ] }, { "Effect": "Allow", "Action": [ "log:ListLogStores", "log:Get
