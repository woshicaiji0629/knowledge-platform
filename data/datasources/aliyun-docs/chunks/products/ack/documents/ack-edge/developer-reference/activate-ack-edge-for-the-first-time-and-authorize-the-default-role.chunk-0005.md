## 步骤二：授权角色
首次登录容器服务ACK Edge集群时，需要为服务账号授予系统默认角色，步骤如下。
在main.tf配置文件中添加如下代码。
说明
由于Terraform本身限制，无法自动检测角色是否存在，且无法自动授权不存在的角色，因此需要您手动查询角色信息，并为账号手动授权需要的角色。
// 判断角色是否存在。 data "alicloud_ram_roles" "roles" { policy_type = "System" } // 列举出账号已被完整授权角色信息。 output "exist_role" { value = data.alicloud_ram_roles.roles }
执行如下命令查询账号中是否存在已授权的角色。
terraform apply
返回信息如下。
No changes. Your infrastructure matches the configuration. Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed. Apply complete! Resources: 0 added, 0 changed, 0 destroyed. Outputs: ... exist_role = { "id" = "1788****59" "ids" = tolist([ "3009617019****1438", "3023233020****0278", "3302003419****4675", "3178548808****5924", "3371411011****5177", "3475619590****3519", ]) "name_regex" = tostring(null) "names" = tolist([ "AliyunCASDefaultRole", "AliyunContainerRegistryDefaultRole", "AliyunCSDefaultRole", "AliyunCSKubernetesAuditRole", "AliyunCSManagedArmsRole", "AliyunCSManagedCmsRole", "AliyunCSManagedCsiRole", "AliyunCSManagedKubernetesRole", "AliyunCSManagedLogRole", "AliyunCSManagedNetworkRole", "AliyunCSServerlessKubernetesRole", "AliyunServiceRoleForCSB", "Aliy
