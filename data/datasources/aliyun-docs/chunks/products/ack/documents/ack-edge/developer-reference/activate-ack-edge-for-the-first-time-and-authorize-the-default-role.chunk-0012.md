. Only 'yes' will be accepted to approve. Enter a value: yes alicloud_ram_role_policy_attachment.attach["AliyunCSManagedEdgeRole"]: Creating... alicloud_ram_role_policy_attachment.attach["AliyunCSManagedEdgeRole"]: Creation complete after 0s [id=role:AliyunCSManagedEdgeRolePolicy:System:AliyunCSManagedEdgeRole] ...
执行如下命令，查看已存在的角色。
terraform show
返回信息如下，列举出了账号授权的所有角色信息，表示角色授权已完成。
