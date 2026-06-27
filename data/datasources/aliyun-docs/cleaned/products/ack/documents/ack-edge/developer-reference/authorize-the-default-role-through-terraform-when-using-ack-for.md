# 使用Terraform首次开通ACK并对服务角色进行授权-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/developer-reference/authorize-the-default-role-through-terraform-when-using-ack-for

# 使用Terraform首次开通ACK并授权服务角色
本文为您介绍在首次使用ACK时，如何通过Terraform开通容器服务ACK并进行容器服务角色的授权。
说明
本教程所含示例代码支持一键运行，您可以直接运行代码。[一键运行](https://api.aliyun.com/api-tools/terraform?resource=alicloud_cs_managed_kubernetes&exampleId=201-use-case-enable-ack-and-assign-role&activeTab=example)
## 前提条件
由于阿里云账号（主账号）具有资源的所有权限，一旦发生泄露将面临重大风险。建议您使用RAM用户，并为该RAM用户创建AccessKey，具体操作方式请参见[创建](../../../../ram/documents/user-guide/create-a-ram-user.md)[RAM](../../../../ram/documents/user-guide/create-a-ram-user.md)[用户](../../../../ram/documents/user-guide/create-a-ram-user.md)和[创建](../../../../ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](../../../../ram/documents/user-guide/create-an-accesskey-pair.md)。
为运行Terraform命令的RAM用户绑定以下最小权限策略，以获取管理本示例所涉及资源的权限。更多信息，请参见[为](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
该权限策略允许RAM用户创建、查看和删除RAM角色，并支持对RAM角色权限策略的管理。
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "ram:GetRole", "ram:ListRoles", "ram:AttachPolicyToRole", "ram:ListPoliciesForRole", "ram:CreateRole", "ram:DetachPolicyFromRole", "ram:DeleteRole" ], "Resource": "*" } ] }
准备Terraform运行环境，您可以选择以下任一方式来使用Terraform。
[在](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)[Terraform Explorer](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)[中使用](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)[Terraform](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)：阿里云提供了Terraform的在线运行环境，您无需安装Terraform，登录后即可在线使用和体验Terraform。适用于零成本、快速、便捷地体验和调试Terraform的场景。
[使用](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)[Terraform](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)[快速创建资源](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)：阿里云Cloud Shell中预装了Terraform的组件，并已配置好身份凭证，您可直接在Cloud Shell中运行Terraform的命令。适用于低成本、快速、便捷地访问和使用Terraform的场景。
[在本地安装和配置](https://help.aliyun.com/zh/terraform/install-and-configure-terraform-locally)[Terraform](https://help.aliyun.com/zh/terraform/install-and-configure-terraform-locally)：适用于网络连接较差或需要自定义开发环境的场景。
## 使用的资源
[alicloud_ack_service](https://help.aliyun.com/zh/terraform/alicloud-ack-service)：自动开通容器服务ACK。
[alicloud_ram_role](https://help.aliyun.com/zh/terraform/alicloud-ram-role)：创建一个RAM角色。
[alicloud_ram_role_policy_attachment](https://help.aliyun.com/zh/terraform/alicloud-ram-role-policy-attachment)：为RAM角色绑定其他权限。
[alicloud_ram_roles](https://help.aliyun.com/zh/terraform/alicloud-ram-roles)：根据指定的过滤条件，返回阿里云账号中RAM角色的列表。
## 步骤一：开通容器服务ACK
在创建ACK集群前您需要开通容器服务。
创建一个工作目录，并在该工作目录中创建名为main.tf的配置文件，然后将以下代码复制到main.tf中。
// 开通容器服务ACK。 data "alicloud_ack_service" "open" { enable = "On" type = "propayasgo" }
执行如下命令，初始化Terraform运行环境。
terraform init
返回信息如下，Terraform初始化成功。
Terraform has been successfully initialized! You may now begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All Terraform commands should now work. If you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forget, other commands will detect it and remind you to do so if necessary.
执行如下命令，开通容器服务ACK。
terraform apply
在执行过程中，根据提示输入yes并按下Enter键，等待命令执行完成，若出现以下信息，则表示容器服务ACK开通成功。
You can apply this plan to save these new output values to the Terraform state, without changing any real infrastructure. Do you want to perform these actions? Terraform will perform the actions described above. Only 'yes' will be accepted to approve. Enter a value: yes Apply complete! Resources: 0 added, 0 changed, 0 destroyed.
## 步骤二：授权角色
首次登录容器服务 Kubernetes 版时，需要为服务账号授予系统服务角色，具体步骤如下。
在main.tf配置文件中增加如下授权模板。
// 所需RAM角色。 variable "roles" { type = list(object({ name = string policy_document = string description = string policy_name = string })) default = [ { name = "AliyunCSManagedLogRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的日志组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedLogRolePolicy" }, { name = "AliyunCSManagedCmsRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的CMS组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedCmsRolePolicy" }, { name = "AliyunCSManagedCsiRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的存储组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedCsiRolePolicy" }, { name = "AliyunCSManagedCsiPluginRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的存储组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedCsiPluginRolePolicy" }, { name = "AliyunCSManagedCsiProvisionerRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的存储组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedCsiProvisionerRolePolicy" }, { name = "AliyunCSManagedVKRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "ACK Serverless集群的VK组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedVKRolePolicy" }, { name = "AliyunCSServerlessKubernetesRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSServerlessKubernetesRolePolicy" }, { name = "AliyunCSKubernetesAuditRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群审计功能使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSKubernetesAuditRolePolicy" }, { name = "AliyunCSManagedNetworkRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群网络组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedNetworkRolePolicy" }, { name = "AliyunCSDefaultRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群操作时默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSDefaultRolePolicy" }, { name = "AliyunCSManagedKubernetesRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedKubernetesRolePolicy" }, { name = "AliyunCSManagedArmsRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群Arms插件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedArmsRolePolicy" }, { name = "AliyunCISDefaultRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "容器服务（CS）智能运维使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCISDefaultRolePolicy" }, { name = "AliyunOOSLifecycleHook4CSRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"oos.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群扩缩容节点池依赖OOS服务，OOS使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunOOSLifecycleHook4CSRolePolicy" }, { name = "AliyunCSManagedAutoScalerRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的弹性伸缩组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedAutoScalerRolePolicy" } ] } // 查询RAM角色列表 data "alicloud_ram_roles" "roles" { policy_type = "Custom" name_regex = "^Aliyun.*Role$" } locals { # 提取所有所需RAM角色name all_role_names = [for role in var.roles : role.name] # 提取已存在的RAM角色name created_role_names = [for role in data.alicloud_ram_roles.roles.roles : role.name] # 计算补集：即找出还未创建的所需RAM角色 complement_names = setsubtract(local.all_role_names, local.created_role_names) # 待创建的RAM角色 complement_roles = [for role in var.roles : role if contains(local.complement_names, role.name)] } // 创建角色。 resource "alicloud_ram_role" "role" { for_each = { for r in local.complement_roles : r.name => r } name = each.value.name document = each.value.policy_document description = each.value.description force = true } // 角色关联系统权限。 resource "alicloud_ram_role_policy_attachment" "attach" { for_each = { for r in local.complement_roles : r.name => r } policy_name = each.value.policy_name policy_type = "System" role_name = each.value.name depends_on = [alicloud_ram_role.role] }
说明
在示例中，variable表示作为参数提供给Terraform使用的输入变量，关于参数如何传值，请参见[Variable](https://help.aliyun.com/zh/terraform/variable-introduction)。本示例中参数值请参见[附录](authorize-the-default-role-through-terraform-when-using-ack-for.md)，其中，服务角色是必选参数，可选角色请根据实际情况选择。
创建执行计划，并预览变更。
terraform plan
执行如下命令应用执行计划，为您的账号进行角色授权。
terraform apply
在执行过程中，根据提示输入yes并按下Enter键，等待命令执行完成，若出现以下信息，则表示授权完成。
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
验证结果。
## 执行terraform show命令
您可以使用以下命令查询Terraform已创建的资源详细信息：
terraform show
## 登录RAM控制台
登录[RAM](https://ram.console.aliyun.com)[控制台](https://ram.console.aliyun.com)，查看已创建的角色。
## 清理资源
当您不再需要上述通过Terraform创建或管理的资源时，请运行以下命令以释放资源。关于terraform destroy的更多信息，请参见[Terraform](https://help.aliyun.com/zh/terraform/terraform-common-commands)[常用命令](https://help.aliyun.com/zh/terraform/terraform-common-commands)。
terraform destroy
## 完整示例
说明
本教程所含示例代码支持一键运行，您可以直接运行代码。[一键运行](https://api.aliyun.com/api-tools/terraform?resource=alicloud_cs_managed_kubernetes&exampleId=201-use-case-enable-ack-and-assign-role&activeTab=example)
### 示例代码
provider "alicloud" { region = var.region_id } variable "region_id" { type = string default = "cn-hangzhou" } // 开通容器服务ACK。 data "alicloud_ack_service" "open" { enable = "On" type = "propayasgo" } // 所需RAM角色。 variable "roles" { type = list(object({ name = string policy_document = string description = string policy_name = string })) default = [ { name = "AliyunCSManagedLogRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的日志组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedLogRolePolicy" }, { name = "AliyunCSManagedCmsRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的CMS组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedCmsRolePolicy" }, { name = "AliyunCSManagedCsiRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的存储组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedCsiRolePolicy" }, { name = "AliyunCSManagedCsiPluginRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的存储组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedCsiPluginRolePolicy" }, { name = "AliyunCSManagedCsiProvisionerRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的存储组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedCsiProvisionerRolePolicy" }, { name = "AliyunCSManagedVKRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "ACK Serverless集群的VK组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedVKRolePolicy" }, { name = "AliyunCSServerlessKubernetesRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSServerlessKubernetesRolePolicy" }, { name = "AliyunCSKubernetesAuditRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群审计功能使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSKubernetesAuditRolePolicy" }, { name = "AliyunCSManagedNetworkRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群网络组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedNetworkRolePolicy" }, { name = "AliyunCSDefaultRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群操作时默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSDefaultRolePolicy" }, { name = "AliyunCSManagedKubernetesRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedKubernetesRolePolicy" }, { name = "AliyunCSManagedArmsRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群Arms插件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedArmsRolePolicy" }, { name = "AliyunCISDefaultRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "容器服务（CS）智能运维使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCISDefaultRolePolicy" }, { name = "AliyunOOSLifecycleHook4CSRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"oos.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群扩缩容节点池依赖OOS服务，OOS使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunOOSLifecycleHook4CSRolePolicy" }, { name = "AliyunCSManagedAutoScalerRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的弹性伸缩组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedAutoScalerRolePolicy" } ] } // 查询RAM角色列表 data "alicloud_ram_roles" "roles" { policy_type = "Custom" name_regex = "^Aliyun.*Role$" } locals { # 提取所有所需RAM角色name all_role_names = [for role in var.roles : role.name] # 提取已存在的RAM角色name created_role_names = [for role in data.alicloud_ram_roles.roles.roles : role.name] # 计算补集：即找出还未创建的所需RAM角色 complement_names = setsubtract(local.all_role_names, local.created_role_names) # 待创建的RAM角色 complement_roles = [for role in var.roles : role if contains(local.complement_names, role.name)] } // 创建角色。 resource "alicloud_ram_role" "role" { for_each = { for r in local.complement_roles : r.name => r } name = each.value.name document = each.value.policy_document description = each.value.description force = true } // 角色关联系统权限。 resource "alicloud_ram_role_policy_attachment" "attach" { for_each = { for r in local.complement_roles : r.name => r } policy_name = each.value.policy_name policy_type = "System" role_name = each.value.name depends_on = [alicloud_ram_role.role] }
## 附录
### 服务角色
[AliyunCSManagedLogRole](../../../../ram/documents/developer-reference/aliyuncsmanagedlogrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的日志组件使用该角色访问您在SLS服务中的资源。
授权代码：
{ name = "AliyunCSManagedLogRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的日志组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedLogRolePolicy" }
[AliyunCSManagedCmsRole](../../../../ram/documents/developer-reference/aliyuncsmanagedcmsrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的监控组件使用该角色访问您在CMS、SLS服务中的资源。
授权代码：
{ name = "AliyunCSManagedCmsRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的CMS组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedCmsRolePolicy" }
[AliyunCSManagedCsiRole](../../../../ram/documents/developer-reference/aliyuncsmanagedcsirolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的存储组件使用该角色访问您在ECS、NAS、OSS等服务中的资源。
授权代码：
{ name = "AliyunCSManagedCsiRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的存储插件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedCsiRolePolicy" }
[AliyunCSManagedCsiPluginRole](../../../../ram/documents/developer-reference/aliyuncsmanagedcsipluginrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的存储组件（新版csi-plugin组件）使用该角色访问您在ECS服务中的资源。
授权代码：
{ name = "AliyunCSManagedCsiPluginRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "ACK托管集群、ACK Edge集群和ACK Serverless集群的存储组件（新版csi-plugin组件）使用该角色访问您在ECS服务中的资源。" policy_name = "AliyunCSManagedCsiPluginRolePolicy" }
[AliyunCSManagedCsiProvisionerRole](../../../../ram/documents/developer-reference/aliyuncsmanagedcsiprovisionerrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的存储组件（新版csi-provisioner组件）使用该角色访问您在ECS、NAS、OSS服务中的资源。
授权代码：
{ name = "AliyunCSManagedCsiProvisionerRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "ACK托管集群、ACK Edge集群和ACK Serverless集群的存储组件（新版csi-provisioner组件）使用该角色访问您在ECS、NAS、OSS服务中的资源。" policy_name = "AliyunCSManagedCsiProvisionerRolePolicy" }
[AliyunCSServerlessKubernetesRole](../../../../ram/documents/developer-reference/aliyuncsserverlesskubernetesrolepolicy.md)
说明：
ACK Edge集群和ACK Serverless集群使用该角色来访问您在ECS、VPC、SLB、Private Zone等服务中的资源。
授权代码：
{ name = "AliyunCSServerlessKubernetesRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSServerlessKubernetesRolePolicy" }
[AliyunCSKubernetesAuditRole](../../../../ram/documents/developer-reference/aliyuncskubernetesauditrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的审计功能组件使用该角色来访问您在SLS服务中的资源。
授权代码：
{ name = "AliyunCSKubernetesAuditRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群审计功能使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSKubernetesAuditRolePolicy" }
[AliyunCSManagedNetworkRole](../../../../ram/documents/developer-reference/aliyuncsmanagednetworkrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的网络组件使用该角色访问您在ECS、VPC服务中的资源。
授权代码：
{ name = "AliyunCSManagedNetworkRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群网络组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedNetworkRolePolicy" }
[AliyunCSDefaultRole](../../../../ram/documents/developer-reference/aliyuncsdefaultrolepolicy.md)
说明：
容器服务 Kubernetes 版在管控操作中使用该角色访问您在ECS、VPC、SLB、ROS、ESS等服务中的资源。
授权代码：
{ name = "AliyunCSDefaultRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群操作时默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSDefaultRolePolicy" }
[AliyunCSManagedKubernetesRole](../../../../ram/documents/developer-reference/aliyuncsmanagedkubernetesrolepolicy.md)
说明：
ACK托管集群和ACK Edge集群使用该角色访问您在ECS、VPC、SLB、ACR等服务中的资源。
授权代码：
{ name = "AliyunCSManagedKubernetesRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedKubernetesRolePolicy" }
[AliyunCSManagedArmsRole](../../../../ram/documents/developer-reference/aliyuncsmanagedarmsrolepolicy.md)
说明：
ACK Edge集群和ACK Serverless集群的应用实时监控组件使用该角色访问您在ARMS服务中的资源。
授权代码：
{ name = "AliyunCSManagedArmsRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群Arms插件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedArmsRolePolicy" }
- [AliyunCISDefaultRole](../../../../ram/documents/developer-reference/aliyuncisdefaultrolepolicy.md)
说明：
ACK容器智能运维平台将使用该角色访问您在ECS、VPC、SLB等服务中的资源，为您提供诊断和巡检等服务。
授权代码：
{ name = "AliyunCISDefaultRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "容器服务（CS）智能运维使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCISDefaultRolePolicy" }
### 可选角色
[AliyunCSManagedAcrRole](../../../../ram/documents/developer-reference/aliyuncsmanagedacrrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的免密组件镜像拉取使用该角色访问您在ACR容器镜像服务中的资源。
授权代码：
{ name = "AliyunCSManagedAcrRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的镜像拉取免密插件使用该角色访问您在ACR容器镜像服务中的资源。" policy_name = "AliyunCSManagedAcrRolePolicy" }
[AliyunCSManagedNlcRole](../../../../ram/documents/developer-reference/aliyuncsmanagednlcrolepolicy.md)
说明：
ACK托管集群和ACK Edge集群的节点生命周期控制器使用该角色访问您的ECS和ACK节点池资源。
授权代码：
{ name = "AliyunCSManagedNlcRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群托管节点池控制组件使用该角色访问您的ECS和ACK节点池资源。" policy_name = "AliyunCSManagedNlcRolePolicy" }
[AliyunCSManagedAutoScalerRole](../../../../ram/documents/developer-reference/aliyuncsmanagedautoscalerrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的弹性伸缩组件使用该角色访问您在ESS和ECS服务中的资源。
授权代码：
{ name = "AliyunCSManagedAutoScalerRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的弹性伸缩组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedAutoScalerRolePolicy" }
[AliyunCSManagedSecurityRole](../../../../ram/documents/developer-reference/aliyuncsmanagedsecurityrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的落盘加密和凭据管理组件使用该角色访问您在KMS服务中的资源。
授权代码：
{ name = "AliyunCSManagedSecurityRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的落盘加密插件使用该角色访问您在KMS服务中的资源。" policy_name = "AliyunCSManagedSecurityRolePolicy" }
[AliyunCSManagedCostRole](../../../../ram/documents/developer-reference/aliyuncsmanagedcostrolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的成本分析组件使用该角色访问您在账单管理API、ECS和ECI服务中的资源。
授权代码：
{ name = "AliyunCSManagedCostRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的成本分析组件使用该角色访问您在账单管理API、ECS和ECI服务中的资源。" policy_name = "AliyunCSManagedCostRolePolicy" }
[AliyunCSManagedNimitzRole](../../../../ram/documents/developer-reference/aliyuncsmanagednimitzrolepolicy.md)
说明：
ACK Edge集群的管控组件使用该角色访问您在智能接入网关、VPC和云企业网CEN服务中的资源。
授权代码：
{ name = "AliyunCSManagedNimitzRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "ACK灵骏集群的网络组件使用该角色访问您在智能计算灵骏服务中的资源。" policy_name = "AliyunCSManagedNimitzRolePolicy" }
[AliyunCSManagedBackupRestoreRole](../../../../ram/documents/developer-reference/aliyuncsmanagedbackuprestorerolepolicy.md)
说明：
ACK托管集群、ACK Edge集群和ACK Serverless集群的备份中心服务组件使用该角色访问您在云备份（Cloud Backup）服务和OSS服务中的资源。
授权代码：
{ name = "AliyunCSManagedBackupRestoreRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的备份中心组件使用该角色访问您在云备份（Cloud Backup）服务和OSS服务中的资源。" policy_name = "AliyunCSManagedBackupRestoreRolePolicy" }
[AliyunCSManagedEdgeRole](../../../../ram/documents/developer-reference/aliyuncsmanagededgerolepolicy.md)
说明：
ACK Edge集群的管控组件使用该角色访问您在智能接入网关、VPC和云企业网CEN服务中的资源。
授权代码：
{ name = "AliyunCSManagedEdgeRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "ACK Edge集群的管控组件使用该角色访问您在智能接入网关、VPC和云企业网CEN服务中的资源。" policy_name = "AliyunCSManagedEdgeRolePolicy" }
AliyunOOSLifecycleHook4CSRole
说明：
系统运维管理OOS使用该角色访问您在容器服务 Kubernetes 版、ECS、PolarDB等服务中的资源。
授权代码：
{ name = "AliyunOOSLifecycleHook4CSRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"oos.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群扩缩容节点池依赖OOS服务，OOS使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunOOSLifecycleHook4CSRolePolicy" }
## 相关文档
Terraform介绍，请参见[了解阿里云](https://help.aliyun.com/zh/terraform/what-is-terraform)[Terraform](https://help.aliyun.com/zh/terraform/what-is-terraform)。
当您遇到由于网络延迟等原因造成的 terraform init 超时，导致无法正常下载 Provider 等情况时，请参见[Terraform Init 加速方案配置](https://help.aliyun.com/zh/terraform/terraform-init-acceleration-solution-configuration)。
关于如何配置Terraform的身份认证信息，请参见[静态配置身份认证](https://help.aliyun.com/zh/terraform/terraform-authentication#75fb0fdd14jef)。
ROS提供了Terraform托管服务，因此您可以直接在[ROS](https://ros.console.aliyun.com/cn-hangzhou/welcome)[控制台](https://ros.console.aliyun.com/cn-hangzhou/welcome)部署Terraform模板。详细操作，请参见[创建](https://help.aliyun.com/zh/ros/user-guide/create-a-terraform-stack)[Terraform](https://help.aliyun.com/zh/ros/user-guide/create-a-terraform-stack)[类型资源栈](https://help.aliyun.com/zh/ros/user-guide/create-a-terraform-stack)。
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
