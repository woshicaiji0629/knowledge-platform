or r in local.complement_roles : r.name => r } name = each.value.name document = each.value.policy_document description = each.value.description force = true } // 角色关联系统权限。 resource "alicloud_ram_role_policy_attachment" "attach" { for_each = { for r in local.complement_roles : r.name => r } policy_name = each.value.policy_name policy_type = "System" role_name = each.value.name depends_on = [alicloud_ram_role.role] }
说明
在示例中，variable表示作为参数提供给Terraform使用的输入变量，关于参数如何传值，请参见[Variable](https://help.aliyun.com/zh/terraform/variable-introduction)。本示例中参数值请参见[附录](use-terraform-to-assign-default-roles-to-ack-when-you-use-ack-for-the-first-time.md)，其中，服务角色是必选参数，可选角色请根据实际情况选择。
创建执行计划，并预览变更。
terraform plan
执行如下命令应用执行计划，为您的账号进行角色授权。
terraform apply
在执行过程中，根据提示输入yes并按下Enter键，等待命令执行完成，若出现以下信息，则表示授权完成。
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
验证结果。
