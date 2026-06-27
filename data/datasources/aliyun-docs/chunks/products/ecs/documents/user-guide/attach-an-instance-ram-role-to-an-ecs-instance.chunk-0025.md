## 常见问题
一台ECS实例可以被授予几个RAM角色？
一台ECS实例在同一时刻最多只能被授予一个RAM角色。可通过收回后再授予的方式切换角色。
如何使用RAM用户给实例授予RAM角色？
为RAM用户授予以下权限，其他操作同[操作步骤](attach-an-instance-ram-role-to-an-ecs-instance.md)。
管理RAM角色：需要创建RAM角色并授权。
授予/回收RAM角色：需要进入实例详情页对实例做授予/回收RAM角色的操作。
允许传递角色给云产品：给云服务授予角色需要配合ram:PassRole权限。
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "ecs:Describe*", "ecs:List*", "ecs:AttachInstanceRamRole", "ecs:DetachInstanceRAMRole" ], "Resource": "*" }, { "Effect": "Allow", "Action": [ "ram:Describe*", "ram:List*", "ram:Get*", "ram:CreateRole", "ram:CreatePolicy", "ram:AttachPolicyToRole" ], "Resource": "*" }, { "Effect": "Allow", "Action": "ram:PassRole", "Resource": "*" } ] }
