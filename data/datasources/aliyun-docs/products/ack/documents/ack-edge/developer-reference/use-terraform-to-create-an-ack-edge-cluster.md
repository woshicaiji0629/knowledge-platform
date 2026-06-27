# 使用Terraform创建ACK Edge集群-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/developer-reference/use-terraform-to-create-an-ack-edge-cluster

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

# 使用Terraform创建ACK Edge集群

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Terraform是一种开源工具，用于安全高效地预览、配置和管理云基础架构和资源，帮助开发者自动化地创建、更新阿里云基础设施资源，并进行版本管理。本文介绍如何使用Terraform创建ACK Edge集群。

说明

本教程所含示例代码支持一键运行，您可以直接运行代码。[一键运行](https://api.aliyun.com/api-tools/terraform?resource=alicloud_cs_edge_kubernetes&exampleId=201-use-case-create-ack-edge-cluster&activeTab=example)

## 前提条件

- 

已开通容器服务 Edge 版。

- 

由于阿里云账号（主账号）具有资源的所有权限，一旦发生泄露将面临重大风险。建议您使用RAM用户，并为该RAM用户创建AccessKey，具体操作方式请参见[创建](products/ram/documents/user-guide/create-a-ram-user.md)[RAM](products/ram/documents/user-guide/create-a-ram-user.md)[用户](products/ram/documents/user-guide/create-a-ram-user.md)和[创建](products/ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](products/ram/documents/user-guide/create-an-accesskey-pair.md)。

- 

为运行Terraform命令的RAM用户绑定以下最小权限策略，以获取管理本示例所涉及资源的权限。更多信息，请参见[管理](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。

该权限策略允许RAM用户进行VPC、交换机及ACK的创建、查看与删除操作。

{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "vpc:CreateVpc", "vpc:CreateVSwitch", "cs:CreateCluster", "vpc:DescribeVpcAttribute", "vpc:DescribeVSwitchAttributes", "vpc:DescribeRouteTableList", "vpc:DescribeNatGateways", "cs:DescribeTaskInfo", "cs:DescribeClusterDetail", "cs:GetClusterCerts", "cs:CheckControlPlaneLogEnable", "cs:CreateClusterNodePool", "cs:DescribeClusterNodePoolDetail", "cs:DescribeClusterNodePools", "cs:ScaleOutCluster", "cs:DescribeClusterNodes", "vpc:DeleteVpc", "vpc:DeleteVSwitch", "cs:DeleteCluster", "cs:DeleteClusterNodepool" ], "Resource": "*" } ] }

- 

准备Terraform运行环境，您可以选择以下任一方式来使用Terraform。

- 

[在](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)[Terraform Explorer](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)[中使用](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)[Terraform](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)：阿里云提供了Terraform的在线运行环境，您无需安装Terraform，登录后即可在线使用和体验Terraform。适用于零成本、快速、便捷地体验和调试Terraform的场景。

- 

[使用](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)[Terraform](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)[快速创建资源](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)：阿里云Cloud Shell中预装了Terraform的组件，并已配置好身份凭证，您可直接在Cloud Shell中运行Terraform的命令。适用于低成本、快速、便捷地访问和使用Terraform的场景。

- 

[在本地安装和配置](https://help.aliyun.com/zh/terraform/install-and-configure-terraform-locally)[Terraform](https://help.aliyun.com/zh/terraform/install-and-configure-terraform-locally)：适用于网络连接较差或需要自定义开发环境的场景。

重要

请确认Terraform版本不低于v0.12.28，可通过terraform --version命令查看Terraform版本。

## 使用的资源

说明

本教程示例包含的部分资源会产生一定费用，请在不需要时及时进行释放或退订。

- 

[alicloud_zones](https://help.aliyun.com/zh/terraform/alicloud-zones)：查询可用区。

- 

[alicloud_instance_types](https://help.aliyun.com/zh/terraform/alicloud-instance-types)：根据条件查询符合要求的ECS实例类型。

- 

[alicloud_vpc](https://help.aliyun.com/zh/terraform/alicloud-vpc)：创建专有网络VPC。

- 

[alicloud_vswitch](https://help.aliyun.com/zh/terraform/alicloud-vswitch)：创建虚拟交换机（vSwitch）为VPC划分一个或多个子网。

- 

[alicloud_cs_edge_kubernetes](https://help.aliyun.com/zh/terraform/alicloud-cs-edge-kubernetes)：创建ACK Edge集群。

- 

[alicloud_cs_kubernetes_node_pool](https://help.aliyun.com/zh/terraform/alicloud-cs-kubernetes-node-pool)：为ACK托管集群创建节点池。

## 使用Terraform创建ACK Edge集群

- 

创建一个工作目录，并在工作目录下创建以下名为main.tf的配置文件。

main.tf配置文件中描述了如下Terraform配置：

- 

创建一个新的VPC，并在该VPC下创建一个vSwitch。

- 

创建一个ACK Edge集群。

- 

创建一个包含两个节点的节点池。

provider "alicloud" { region = var.region_id } variable "region_id" { default = "cn-hangzhou" } variable "k8s_name_edge" { type = string description = "The name used to create edge kubernetes cluster." default = "edge-example" } variable "new_vpc_name" { type = string description = "The name used to create vpc." default = "tf-vpc-172-16" } variable "new_vsw_name" { type = string description = "The name used to create vSwitch." default = "tf-vswitch-172-16-0" } variable "nodepool_name" { type = string description = "The name used to create node pool." default = "edge-nodepool-1" } variable "k8s_login_password" { type = string default = "Test123456" } variable "k8s_version" { type = string description = "Kubernetes version" default = "1.28.9-aliyun.1" } variable "containerd_runtime_version" { type = string default = "1.6.34" } variable "cluster_spec" { type = string description = "The cluster specifications of kubernetes cluster,which can be empty. Valid values:ack.standard : Standard managed clusters; ack.pro.small : Professional managed clusters." default = "ack.pro.small" } data "alicloud_zones" "default" { available_resource_creation = "VSwitch" available_disk_category = "cloud_efficiency" } data "alicloud_instance_types" "default" { availability_zone = data.alicloud_zones.default.zones.0.id cpu_core_count = 4 memory_size = 8 kubernetes_node_role = "Worker" } resource "alicloud_vpc" "vpc" { vpc_name = var.new_vpc_name cidr_block = "172.16.0.0/12" } resource "alicloud_vswitch" "vsw" { vswitch_name = var.new_vsw_name vpc_id = alicloud_vpc.vpc.id cidr_block = cidrsubnet(alicloud_vpc.vpc.cidr_block, 8, 8) zone_id = data.alicloud_zones.default.zones.0.id } resource "alicloud_cs_edge_kubernetes" "edge" { name = var.k8s_name_edge version = var.k8s_version cluster_spec = var.cluster_spec worker_vswitch_ids = split(",", join(",", alicloud_vswitch.vsw.*.id)) worker_instance_types = [data.alicloud_instance_types.default.instance_types.0.id] password = var.k8s_login_password new_nat_gateway = true pod_cidr = "10.10.0.0/16" service_cidr = "10.12.0.0/16" load_balancer_spec = "slb.s2.small" worker_number = 1 node_cidr_mask = 24 # 运行时。 runtime = { name = "containerd" version = var.containerd_runtime_version } } # 节点池。 resource "alicloud_cs_kubernetes_node_pool" "nodepool" { # Kubernetes集群名称。 cluster_id = alicloud_cs_edge_kubernetes.edge.id # 节点池名称。 node_pool_name = var.nodepool_name # 新的Kubernetes集群将位于的vSwitch。指定一个或多个vSwitch的ID。它必须在availability_zone指定的区域中。 vswitch_ids = split(",", join(",", alicloud_vswitch.vsw.*.id)) # ECS实例类型和收费方式。 instance_types = [data.alicloud_instance_types.default.instance_types.0.id] instance_charge_type = "PostPaid" # 可选，自定义实例名称。 # node_name_mode = "customized,edge-shenzhen,ip,default" #容器运行时。 runtime_name = "containerd" runtime_version = var.containerd_runtime_version # 集群节点池的期望节点数。 desired_size = 2 # SSH登录集群节点的密码。 password = var.k8s_login_password # 是否为Kubernetes的节点安装云监控。 install_cloud_monitor = true # 节点的系统磁盘类别。其有效值为cloud_ssd和cloud_efficiency。默认为cloud_efficiency。 system_disk_category = "cloud_efficiency" system_disk_size = 100 # 操作系统类型。 image_type = "AliyunLinux" # 节点数据盘配置。 data_disks { # 节点数据盘种类。 category = "cloud_efficiency" # 节点数据盘大小。 size = 120 } lifecycle { ignore_changes = [ labels ] } }

- 

执行以下命令，初始化Terraform运行环境。

terraform init

返回信息如下，Terraform初始化成功。

Terraform has been successfully initialized! You may now begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All Terraform commands should now work. If you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forget, other commands will detect it and remind you to do so if necessary.

- 

创建执行计划，并预览变更。

terraform plan

返回以下信息，表示资源执行计划已成功生成，您可以查看相关资源信息。

Refreshing Terraform state in-memory prior to plan... The refreshed state will be used to calculate this plan, but will not be persisted to local or remote state storage. ... Plan: 4 to add, 0 to change, 0 to destroy. ...

- 

执行以下命令，创建ACK Edge集群。

terraform apply

在执行过程中，根据提示输入yes并按下Enter键，等待命令执行完成，若出现以下信息，则表示集群创建成功。

... Do you want to perform these actions? Terraform will perform the actions described above. Only 'yes' will be accepted to approve. Enter a value: yes ... alicloud_cs_edge_kubernetes.edge: Creation complete after 8m26s [id=************] Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

- 

验证结果

## 执行terraform show命令

您可以使用以下命令查询Terraform已创建的资源详细信息。

terraform show

执行命令后，返回如下资源详细信息：

# alicloud_cs_edge_kubernetes.edge: resource "alicloud_cs_edge_kubernetes" "edge" { certificate_authority = {} cluster_spec = "ack.pro.small" connections = { "api_server_internet" = "https://121.43.224.65:6443" "api_server_intranet" = "https://172.16.143.180:6443" "master_public_ip" = "12xxx5" } deletion_protection = false force_update = false id = "c8cfixxx691" install_cloud_monitor = true load_balancer_spec = "slb.s2.small" name = "edge-example-edge" name_prefix = "Terraform-Creation" nat_gateway_id = "ngw-bp1xxxoy" new_nat_gateway = true node_cidr_mask = 24 password = (sensitive value) pod_cidr = "10.10.0.0/16" proxy_mode = "ipvs" resource_group_id = "rg-aekzxxxxxxxx" runtime = { "name" = "containerd" "version" = "1.6.28" } }resource_group_id = "rg-acxxxdy" runtime = { "name" = "containerd" "version" = "1.5.13" } }`

## 登录ACK控制台

登录[容器服务管理控制台](https://cs.console.aliyun.com)，查看已创建的集群。在容器服务ACK集群详情页面，选中基本信息Tab页签，可查看集群的基本信息和网络配置。基本信息包括集群名称（edge-example）、地域（华东1杭州）、集群状态（运行中）、集群类型（ACK Edge Pro版）、K8s版本（1.22.15-aliyunedge.1）、集群删除保护（未开启）等。网络配置包括网络插件Flannel、服务转发模式IPVS、API server内网端点https://172.16.143.52:6443、API server公网端点https://101.37.69.234:6443、Service CIDR10.12.0.0/16等。

## 清理资源

当您不再需要上述通过Terraform创建或管理的资源时，请运行terraform destroy命令以释放资源。关于terraform destroy的更多信息，请参见[Terraform](https://help.aliyun.com/zh/terraform/terraform-common-commands)[常用命令](https://help.aliyun.com/zh/terraform/terraform-common-commands)。

terraform destroy

## 完整示例

说明

当前示例代码支持一键运行，您可以直接运行代码。[一键运行](https://api.aliyun.com/api-tools/terraform?resource=alicloud_cs_edge_kubernetes&exampleId=201-use-case-create-ack-edge-cluster&activeTab=example)

### 示例代码

provider "alicloud" { region = var.region_id } variable "region_id" { default = "cn-hangzhou" } variable "k8s_name_edge" { type = string description = "The name used to create edge kubernetes cluster." default = "edge-example" } variable "new_vpc_name" { type = string description = "The name used to create vpc." default = "tf-vpc-172-16" } variable "new_vsw_name" { type = string description = "The name used to create vSwitch." default = "tf-vswitch-172-16-0" } variable "nodepool_name" { type = string description = "The name used to create node pool." default = "edge-nodepool-1" } variable "k8s_login_password" { type = string default = "Test123456" } variable "k8s_version" { type = string description = "Kubernetes version" default = "1.28.9-aliyun.1" } variable "containerd_runtime_version" { type = string default = "1.6.34" } variable "cluster_spec" { type = string description = "The cluster specifications of kubernetes cluster,which can be empty. Valid values:ack.standard : Standard managed clusters; ack.pro.small : Professional managed clusters." default = "ack.pro.small" } data "alicloud_zones" "default" { available_resource_creation = "VSwitch" available_disk_category = "cloud_efficiency" } data "alicloud_instance_types" "default" { availability_zone = data.alicloud_zones.default.zones.0.id cpu_core_count = 4 memory_size = 8 kubernetes_node_role = "Worker" } resource "alicloud_vpc" "vpc" { vpc_name = var.new_vpc_name cidr_block = "172.16.0.0/12" } resource "alicloud_vswitch" "vsw" { vswitch_name = var.new_vsw_name vpc_id = alicloud_vpc.vpc.id cidr_block = cidrsubnet(alicloud_vpc.vpc.cidr_block, 8, 8) zone_id = data.alicloud_zones.default.zones.0.id } resource "alicloud_cs_edge_kubernetes" "edge" { name = var.k8s_name_edge version = var.k8s_version cluster_spec = var.cluster_spec worker_vswitch_ids = split(",", join(",", alicloud_vswitch.vsw.*.id)) worker_instance_types = [data.alicloud_instance_types.default.instance_types.0.id] password = var.k8s_login_password new_nat_gateway = true pod_cidr = "10.10.0.0/16" service_cidr = "10.12.0.0/16" load_balancer_spec = "slb.s2.small" worker_number = 1 node_cidr_mask = 24 # 运行时。 runtime = { name = "containerd" version = var.containerd_runtime_version } } # 节点池。 resource "alicloud_cs_kubernetes_node_pool" "nodepool" { # Kubernetes集群名称。 cluster_id = alicloud_cs_edge_kubernetes.edge.id # 节点池名称。 node_pool_name = var.nodepool_name # 新的Kubernetes集群将位于的vSwitch。指定一个或多个vSwitch的ID。它必须在availability_zone指定的区域中。 vswitch_ids = split(",", join(",", alicloud_vswitch.vsw.*.id)) # ECS实例类型和收费方式。 instance_types = [data.alicloud_instance_types.default.instance_types.0.id] instance_charge_type = "PostPaid" # 可选，自定义实例名称。 # node_name_mode = "customized,edge-shenzhen,ip,default" #容器运行时。 runtime_name = "containerd" runtime_version = var.containerd_runtime_version # 集群节点池的期望节点数。 desired_size = 2 # SSH登录集群节点的密码。 password = var.k8s_login_password # 是否为Kubernetes的节点安装云监控。 install_cloud_monitor = true # 节点的系统磁盘类别。其有效值为cloud_ssd和cloud_efficiency。默认为cloud_efficiency。 system_disk_category = "cloud_efficiency" system_disk_size = 100 # 操作系统类型。 image_type = "AliyunLinux" # 节点数据盘配置。 data_disks { # 节点数据盘种类。 category = "cloud_efficiency" # 节点数据盘大小。 size = 120 } lifecycle { ignore_changes = [ labels ] } }

## 相关文档

- 

若您期望通过调用API创建ACK Edge集群，请参见[通过](products/ack/documents/create-an-ack-managed-cluster.md)[OpenAPI](products/ack/documents/create-an-ack-managed-cluster.md)[创建](products/ack/documents/create-an-ack-managed-cluster.md)[ACK](products/ack/documents/create-an-ack-managed-cluster.md)[托管集群](products/ack/documents/create-an-ack-managed-cluster.md)。

- 

您可以参考[阿里云容器服务](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cs_kubernetes)[Terraform](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cs_kubernetes)[资源](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cs_kubernetes)来获取更多ACK相关的Terraform资源。

- 

若您期望获取更多Terraform相关代码，请参见[阿里云](https://github.com/hashicorp/terraform-provider-alicloud)[Terraform Provider](https://github.com/hashicorp/terraform-provider-alicloud)。

[上一篇：通过Terraform开通ACK并授权角色](products/ack/documents/ack-edge/developer-reference/authorize-the-default-role-through-terraform-when-using-ack-for.md)[下一篇：使用Terraform管理已创建的集群](products/ack/documents/ack-edge/developer-reference/use-terraform-to-manage-created-clusters.md)

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
