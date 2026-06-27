# 使用Terraform首次开通ACK Edge并授权默认角色-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/developer-reference/activate-ack-edge-for-the-first-time-and-authorize-the-default-role

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-edge/product-overview.md)

- [快速入门](products/ack/documents/ack-edge/quick-start.md)

- [操作指南](products/ack/documents/ack-edge/user-guide.md)

- [实践教程](products/ack/documents/ack-edge/use-cases.md)

- [安全合规](products/ack/documents/ack-edge/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-edge/developer-reference.md)

- [服务支持](products/ack/documents/ack-edge/support.md)

[首页](https://help.aliyun.com/zh)

# 使用Terraform首次开通ACK Edge并授权默认角色

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

首次使用容器服务ACK Edge集群时，需要为服务账号授予系统默认角色。只有在该角色正确授权后，ACK Edge集群才能正常调用相关服务（如 ECS、OSS、NAS、SLB 等）、创建集群并保存日志。本文将介绍如何通过Terraform为容器服务授权默认角色。

## 前提条件

- 

已开通容器服务 Kubernetes 版ACK。若需要使用Terraform开通，请参见[通过](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-assign-default-roles-to-ack-when-you-use-ack-for-the-first-time.md)[Terraform](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-assign-default-roles-to-ack-when-you-use-ack-for-the-first-time.md)[开通](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-assign-default-roles-to-ack-when-you-use-ack-for-the-first-time.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-assign-default-roles-to-ack-when-you-use-ack-for-the-first-time.md)[并授权角色](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-assign-default-roles-to-ack-when-you-use-ack-for-the-first-time.md)。

- 

由于阿里云账号（主账号）具有资源的所有权限，一旦发生泄露将面临重大风险。建议您使用RAM用户，并为该RAM用户创建AccessKey，具体操作方式请参见[创建](products/ram/documents/user-guide/create-a-ram-user.md)[RAM](products/ram/documents/user-guide/create-a-ram-user.md)[用户](products/ram/documents/user-guide/create-a-ram-user.md)和[创建](products/ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](products/ram/documents/user-guide/create-an-accesskey-pair.md)。

- 

为运行Terraform命令的RAM用户绑定以下最小权限策略，以获取管理本示例所涉及资源的权限。更多信息，请参见[为](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。

该权限策略允许RAM用户进行VPC、交换机、安全组及ACK的创建、查看与删除操作。

{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "vpc:CreateVpc", "vpc:CreateVSwitch", "vpc:DescribeVpcAttribute", "vpc:DescribeRouteTableList", "vpc:DescribeVSwitchAttributes", "ecs:CreateSecurityGroup", "ecs:ModifySecurityGroupPolicy", "ecs:DescribeSecurityGroups", "ecs:DescribeSecurityGroupAttribute", "ecs:ListTagResources", "cs:CreateCluster", "cs:DescribeTaskInfo", "cs:DescribeClusterDetail", "vpc:DeleteVpc", "vpc:DeleteVSwitch", "cs:DeleteCluster", "ecs:DeleteSecurityGroup" ], "Resource": "*" } ] }

- 

准备Terraform运行环境，您可以选择以下任一方式来使用Terraform。

- 

[在](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)[Terraform Explorer](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)[中使用](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)[Terraform](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)：阿里云提供了Terraform的在线运行环境，您无需安装Terraform，登录后即可在线使用和体验Terraform。适用于零成本、快速、便捷地体验和调试Terraform的场景。

- 

[Cloud Shell](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)：阿里云Cloud Shell中预装了Terraform的组件，并已配置好身份凭证，您可直接在Cloud Shell中运行Terraform的命令。适用于低成本、快速、便捷地访问和使用Terraform的场景。

- 

[在本地安装和配置](https://help.aliyun.com/zh/terraform/install-and-configure-terraform-locally)[Terraform](https://help.aliyun.com/zh/terraform/install-and-configure-terraform-locally)：适用于网络连接较差或需要自定义开发环境的场景。

重要

请确认Terraform版本不低于v0.12.28，可通过terraform --version命令查看Terraform版本。

## 步骤一：开通ACK Edge集群

容器服务ACK Edge现已正式商用，在创建ACK Edge集群前您需要开通相应服务。

- 

创建一个工作目录，并在工作目录中创建名为main.tf的配置文件。

- 

将如下代码复制到main.tf配置文件。

展开查看本文用到的main.tf文件

provider "alicloud" { } // 开通容器服务ACK Edge。 data "alicloud_ack_service" "open" { enable = "On" type = "edgepayasgo" }

- 

执行如下命令，初始化Terraform运行环境。

terraform init

返回信息如下，Terraform初始化成功。

Initializing the backend... Initializing provider plugins... ... Terraform has been successfully initialized! ...

- 

执行如下命令，开通容器服务ACK Edge集群。

terraform apply

返回信息如下，服务开通成功。

data.alicloud_ack_service.open: Refreshing state... Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

## 步骤二：授权角色

首次登录容器服务ACK Edge集群时，需要为服务账号授予系统默认角色，步骤如下。

- 

在main.tf配置文件中添加如下代码。

说明

由于Terraform本身限制，无法自动检测角色是否存在，且无法自动授权不存在的角色，因此需要您手动查询角色信息，并为账号手动授权需要的角色。

// 判断角色是否存在。 data "alicloud_ram_roles" "roles" { policy_type = "System" } // 列举出账号已被完整授权角色信息。 output "exist_role" { value = data.alicloud_ram_roles.roles }

执行如下命令查询账号中是否存在已授权的角色。

terraform apply

返回信息如下。

No changes. Your infrastructure matches the configuration. Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed. Apply complete! Resources: 0 added, 0 changed, 0 destroyed. Outputs: ... exist_role = { "id" = "1788****59" "ids" = tolist([ "3009617019****1438", "3023233020****0278", "3302003419****4675", "3178548808****5924", "3371411011****5177", "3475619590****3519", ]) "name_regex" = tostring(null) "names" = tolist([ "AliyunCASDefaultRole", "AliyunContainerRegistryDefaultRole", "AliyunCSDefaultRole", "AliyunCSKubernetesAuditRole", "AliyunCSManagedArmsRole", "AliyunCSManagedCmsRole", "AliyunCSManagedCsiRole", "AliyunCSManagedKubernetesRole", "AliyunCSManagedLogRole", "AliyunCSManagedNetworkRole", "AliyunCSServerlessKubernetesRole", "AliyunServiceRoleForCSB", "AliyunServiceRoleForECI", "AliyunServiceRoleForGws", "AliyunServiceRoleForResourceDirectory", "AliyunServiceRoleForServiceMesh", ]) "output_file" = tostring(null) "policy_name" = tostring(null) "policy_type" = "System" "roles" = tolist([ { "arn" = "acs:ram::1848450434088535:role/aliyuncasdefaultrole" "assume_role_policy_document" = <<-EOT { "Statement": [{ "Action": "sts:AssumeRole", "Effect": "Allow", "Principal": {"Service": ["cas.aliyuncs.com"]}}], "Version": "1"} EOT "create_date" = "2023-07-17T03:27:28Z" "description" = "云盾证书服务(CAS)默认使用此角色来访问您在其他云产品中的资源" "document" = <<-EOT { "Statement": [{ "Action": "sts:AssumeRole", "Effect": "Allow", "Principal": {"Service": ["cas.aliyuncs.com"]}}], "Version": "1"} EOT "id" = "300961701980****" "name" = "AliyunCASDefaultRole" "update_date" = "2023-07-17T03:27:28Z" }, { "arn" = "acs:ram::1848450434****:role/aliyuncontainerregistrydefaultrole" "assume_role_policy_document" = <<-EOT { "Statement": [{ "Action": "sts:AssumeRole", "Effect": "Allow", "Principal": {"Service": ["cr.aliyuncs.com"]}}], "Version": "1"} "id" = "3502335964487******" "name" = "AliyunServiceRoleForServiceMesh" "update_date" = "2022-09-27T10:26:50Z" }, ]) }

- 

在main.tf配置文件中替换如下授权模板。

说明

此授权模板基于[服务角色](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-assign-default-roles-to-ack-when-you-use-ack-for-the-first-time.md)进行授权，并通过变量来指定各角色的名称、策略等属性。如需调整角色授权，可以参见[可选角色](products/ack/documents/ack-edge/developer-reference/activate-ack-edge-for-the-first-time-and-authorize-the-default-role.md)、[步骤二：授权角色](products/ack/documents/ack-edge/developer-reference/activate-ack-edge-for-the-first-time-and-authorize-the-default-role.md)查询到的角色，在模板的default = [ ]中，您可以根据需要新增新角色或删除已有角色，以确保授权不会重复或遗漏。

展开查看所有角色详细信息

provider "alicloud" { } // 创建角色。 resource "alicloud_ram_role" "role" { for_each = { for r in var.roles : r.name => r } name = each.value.name document = each.value.policy_document description = each.value.description force = true } // 角色关联系统权限。 resource "alicloud_ram_role_policy_attachment" "attach" { for_each = { for r in var.roles : r.name => r } policy_name = each.value.policy_name policy_type = "System" role_name = each.value.name depends_on = [alicloud_ram_role.role] } // 所需角色。 variable "roles" { type = list(object({ name = string policy_document = string description = string policy_name = string })) default = [ { name = "AliyunCSManagedLogRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的日志组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedLogRolePolicy" }, { name = "AliyunCSManagedCmsRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的CMS组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedCmsRolePolicy" }, { name = "AliyunCSManagedCsiRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的存储插件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedCsiRolePolicy" }, { name = "AliyunCSServerlessKubernetesRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSServerlessKubernetesRolePolicy" }, { name = "AliyunCSKubernetesAuditRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群审计功能使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSKubernetesAuditRolePolicy" }, { name = "AliyunCSManagedNetworkRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群网络组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedNetworkRolePolicy" }, { name = "AliyunCSDefaultRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群操作时默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSDefaultRolePolicy" }, { name = "AliyunCSManagedKubernetesRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedKubernetesRolePolicy" }, { name = "AliyunCSManagedArmsRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群Arms插件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedArmsRolePolicy" }, { name = "AliyunCSManagedEdgeRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的管控组件使用该角色访问您在智能接入网关、VPC和云企业网CEN服务中的资源。" policy_name = "AliyunCSManagedEdgeRolePolicy" }, { name = "AliyunOOSLifecycleHook4CSRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"oos.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "系统运维管理OOS使用该角色访问您在集群、ECS、PolarDB等服务中的资源" policy_name = "AliyunOOSLifecycleHook4CSRolePolicy" } ] }

- 

执行如下命令，初始化Terraform运行环境。

terraform init

返回信息如下Terraform初始化成功。

Initializing the backend... Initializing provider plugins... ... Terraform has created a lock file .terraform.lock.hcl to record the providerselections it made above. Include this file in your version control repositoryso that Terraform can guarantee to make the same selections by default whenyou run "terraform init" in the future. Terraform has been successfully initialized! ...

- 

执行如下命令，为您的账号进行角色授权。

terraform apply

返回信息如下，输入yes，按Enter键，表示授权成功。

Do you want to perform these actions? Terraform will perform the actions described above. Only 'yes' will be accepted to approve. Enter a value: yes alicloud_ram_role_policy_attachment.attach["AliyunCSManagedEdgeRole"]: Creating... alicloud_ram_role_policy_attachment.attach["AliyunCSManagedEdgeRole"]: Creation complete after 0s [id=role:AliyunCSManagedEdgeRolePolicy:System:AliyunCSManagedEdgeRole] ...

- 

执行如下命令，查看已存在的角色。

terraform show

返回信息如下，列举出了账号授权的所有角色信息，表示角色授权已完成。

# alicloud_ram_role.role["AliyunCSManagedEdgeRole"]: resource "alicloud_ram_role" "role" { arn = "acs:ram::10051XXXXXX30:role/aliyuncsmanagededgerole" description = "集群的管控组件使用该角色访问您在智能接入网关、VPC和云企业网CEN服务中的资源。" ...... } # alicloud_ram_role_policy_attachment.attach["AliyunCSManagedEdgeRole"]: resource "alicloud_ram_role_policy_attachment" "attach" { id = "role:AliyunCSManagedEdgeRolePolicy:System:AliyunCSManagedEdgeRole" policy_name = "AliyunCSManagedEdgeRolePolicy" policy_type = "System" role_name = "AliyunCSManagedEdgeRole" ..... }

## 服务角色

### [AliyunCSManagedLogRole](products/ram/documents/developer-reference/aliyuncsmanagedlogrolepolicy.md)

- 

说明：

ACK托管集群、ACK Edge集群和ACK Serverless集群的日志组件使用该角色访问您在SLS服务中的资源。

- 

授权代码：

{ name = "AliyunCSManagedLogRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的日志组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedLogRolePolicy" }

### [AliyunCSManagedCmsRole](products/ram/documents/developer-reference/aliyuncsmanagedcmsrolepolicy.md)

- 

说明：

ACK托管集群、ACK Edge集群和ACK Serverless集群的监控组件使用该角色访问您在CMS、SLS服务中的资源。

- 

授权代码：

{ name = "AliyunCSManagedCmsRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的CMS组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedCmsRolePolicy" }

### [AliyunCSManagedCsiRole](products/ram/documents/developer-reference/aliyuncsmanagedcsirolepolicy.md)

- 

说明：

ACK托管集群、ACK Edge集群和ACK Serverless集群的存储组件使用该角色访问您在ECS、NAS、OSS等服务中的资源。

- 

授权代码：

{ name = "AliyunCSManagedCsiRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的存储插件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedCsiRolePolicy" }

### [AliyunCSServerlessKubernetesRole](products/ram/documents/developer-reference/aliyuncsserverlesskubernetesrolepolicy.md)

- 

说明：

ACK Edge集群和ACK Serverless集群使用该角色来访问您在ECS、VPC、SLB、Private Zone等服务中的资源。

- 

授权代码：

{ name = "AliyunCSServerlessKubernetesRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSServerlessKubernetesRolePolicy" }

### [AliyunCSKubernetesAuditRole](products/ram/documents/developer-reference/aliyuncskubernetesauditrolepolicy.md)

- 

说明：

ACK托管集群、ACK Edge集群和ACK Serverless集群的审计功能组件使用该角色来访问您在SLS服务中的资源。

- 

授权代码：

{ name = "AliyunCSKubernetesAuditRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群审计功能使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSKubernetesAuditRolePolicy" }

### [AliyunCSManagedNetworkRole](products/ram/documents/developer-reference/aliyuncsmanagednetworkrolepolicy.md)

- 

说明：

ACK托管集群、ACK Edge集群和ACK Serverless集群的网络组件使用该角色访问您在ECS、VPC服务中的资源。

- 

授权代码：

{ name = "AliyunCSManagedNetworkRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群网络组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedNetworkRolePolicy" }

### [AliyunCSDefaultRole](products/ram/documents/developer-reference/aliyuncsdefaultrolepolicy.md)

- 

说明：

容器服务 Kubernetes 版在管控操作中使用该角色访问您在ECS、VPC、SLB、ROS、ESS等服务中的资源。

- 

授权代码：

{ name = "AliyunCSDefaultRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群操作时默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSDefaultRolePolicy" }

### [AliyunCSManagedKubernetesRole](products/ram/documents/developer-reference/aliyuncsmanagedkubernetesrolepolicy.md)

- 

说明：

ACK托管集群和ACK Edge集群使用该角色访问您在ECS、VPC、SLB、ACR等服务中的资源。

- 

授权代码：

{ name = "AliyunCSManagedKubernetesRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群默认使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedKubernetesRolePolicy" }

### [AliyunCSManagedArmsRole](products/ram/documents/developer-reference/aliyuncsmanagedarmsrolepolicy.md)

- 

说明：

ACK托管集群、ACK Edge集群和ACK Serverless集群的应用实时监控组件使用该角色访问您在ARMS服务中的资源。

- 

授权代码：

{ name = "AliyunCSManagedArmsRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群Arms插件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedArmsRolePolicy" }

## 可选角色

### [AliyunCISDefaultRole](products/ram/documents/developer-reference/aliyuncisdefaultrolepolicy.md)

- 

说明：

ACK容器智能运维平台将使用该角色访问您在ECS、VPC、SLB等服务中的资源，为您提供诊断和巡检等服务。

- 

授权代码：

{ name = "AliyunCISDefaultRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "容器服务（CS）智能运维使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCISDefaultRolePolicy" }

### [AliyunCSManagedAcrRole](products/ram/documents/developer-reference/aliyuncsmanagedacrrolepolicy.md)

- 

说明：

ACK托管集群、ACK Edge集群和ACK Serverless集群的免密组件镜像拉取使用该角色访问您在ACR容器镜像服务中的资源。

- 

授权代码：

{ name = "AliyunCSManagedAcrRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的镜像拉取免密插件使用该角色访问您在ACR容器镜像服务中的资源。" policy_name = "AliyunCSManagedAcrRolePolicy" }

### [AliyunCSManagedNlcRole](products/ram/documents/developer-reference/aliyuncsmanagednlcrolepolicy.md)

- 

说明：

ACK托管集群和ACK Edge集群的节点生命周期控制器使用该角色访问您的ECS和ACK节点池资源。

- 

授权代码：

{ name = "AliyunCSManagedNlcRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群托管节点池控制组件使用该角色访问您的ECS和ACK节点池资源。" policy_name = "AliyunCSManagedNlcRolePolicy" }

### [AliyunCSManagedAutoScalerRole](products/ram/documents/developer-reference/aliyuncsmanagedautoscalerrolepolicy.md)

- 

说明：

ACK托管集群、ACK Edge集群和ACK Serverless集群的弹性伸缩组件使用该角色访问您在ESS和ECS服务中的资源。

- 

授权代码：

{ name = "AliyunCSManagedAutoScalerRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的弹性伸缩组件使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunCSManagedAutoScalerRolePolicy" }

### [AliyunCSManagedSecurityRole](products/ram/documents/developer-reference/aliyuncsmanagedsecurityrolepolicy.md)

- 

说明：

ACK托管集群、ACK Edge集群和ACK Serverless集群的落盘加密和凭据管理组件使用该角色访问您在KMS服务中的资源。

- 

授权代码：

{ name = "AliyunCSManagedSecurityRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的落盘加密插件使用该角色访问您在KMS服务中的资源。" policy_name = "AliyunCSManagedSecurityRolePolicy" }

### [AliyunCSManagedCostRole](products/ram/documents/developer-reference/aliyuncsmanagedcostrolepolicy.md)

- 

说明：

ACK托管集群、ACK Edge集群和ACK Serverless集群的成本分析组件使用该角色访问您在账单管理API、ECS和ECI服务中的资源。

- 

授权代码：

{ name = "AliyunCSManagedCostRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的成本分析组件使用该角色访问您在账单管理API、ECS和ECI服务中的资源。" policy_name = "AliyunCSManagedCostRolePolicy" }

### [AliyunCSManagedNimitzRole](products/ram/documents/developer-reference/aliyuncsmanagednimitzrolepolicy.md)

- 

说明：

ACK Edge集群的管控组件使用该角色访问您在智能接入网关、VPC和云企业网CEN服务中的资源。

- 

授权代码：

{ name = "AliyunCSManagedNimitzRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "ACK灵骏集群的网络组件使用该角色访问您在智能计算灵骏服务中的资源。" policy_name = "AliyunCSManagedNimitzRolePolicy" }

### [AliyunCSManagedBackupRestoreRole](products/ram/documents/developer-reference/aliyuncsmanagedbackuprestorerolepolicy.md)

- 

说明：

ACK托管集群、ACK Edge集群和ACK Serverless集群的备份中心服务组件使用该角色访问您在云备份（Cloud Backup）服务和OSS服务中的资源。

- 

授权代码：

{ name = "AliyunCSManagedBackupRestoreRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群的备份中心组件使用该角色访问您在云备份（Cloud Backup）服务和OSS服务中的资源。" policy_name = "AliyunCSManagedBackupRestoreRolePolicy" }

### [AliyunCSManagedEdgeRole](products/ram/documents/developer-reference/aliyuncsmanagededgerolepolicy.md)

- 

说明：

ACK Edge集群的管控组件使用该角色访问您在智能接入网关、VPC和云企业网CEN服务中的资源。

- 

授权代码：

{ name = "AliyunCSManagedEdgeRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "ACK Edge集群的管控组件使用该角色访问您在智能接入网关、VPC和云企业网CEN服务中的资源。" policy_name = "AliyunCSManagedEdgeRolePolicy" }

### [AliyunCSManagedCsiProvisionerRole](products/ram/documents/developer-reference/aliyuncsmanagedcsiprovisionerrolepolicy.md)

- 

说明：

ACK托管集群、ACK Edge集群和ACK Serverless集群的存储组件（csi-provisioner托管组件）使用该角色访问您在ECS、NAS、OSS、服务中的资源。

授权代码：

{ name = "AliyunCSManagedCsiProvisionerRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"cs.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "ACK托管集群、ACK Edge集群和ACK Serverless集群的存储组件（新版csi-provisioner组件）使用该角色访问您在ECS、NAS、OSS服务中的资源。" policy_name = "AliyunCSManagedCsiProvisionerRolePolicy" }

### AliyunOOSLifecycleHook4CSRole

- 

说明：

系统运维管理OOS使用该角色访问您在容器服务 Kubernetes 版、ECS、PolarDB等服务中的资源。

- 

授权代码：

{ name = "AliyunOOSLifecycleHook4CSRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"oos.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "集群扩缩容节点池依赖OOS服务，OOS使用此角色来访问您在其他云产品中的资源。" policy_name = "AliyunOOSLifecycleHook4CSRolePolicy" }

[上一篇：Terraform概述](products/ack/documents/ack-edge/developer-reference/terraform-overview.md)[下一篇：通过Terraform开通ACK并授权角色](products/ack/documents/ack-edge/developer-reference/authorize-the-default-role-through-terraform-when-using-ack-for.md)

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
