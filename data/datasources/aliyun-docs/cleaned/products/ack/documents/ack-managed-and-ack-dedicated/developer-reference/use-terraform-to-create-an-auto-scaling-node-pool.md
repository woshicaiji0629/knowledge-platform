# 使用Terraform创建具备自动伸缩功能的节点池-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-create-an-auto-scaling-node-pool

# 使用Terraform创建具备自动伸缩功能的节点池
ACK的节点池及托管节点池中的节点默认不具备自动伸缩能力，您也可以通过使用Terraform工具创建开启自动伸缩功能的节点池。本文介绍如何通过Terraform创建开启自动伸缩功能的节点池。
说明
本教程所含示例代码支持一键运行，您可以直接运行代码。[一键运行](https://api.aliyun.com/api-tools/terraform?resource=alicloud_cs_managed_kubernetes&exampleId=201-use-case-create-auto-scaling-node-pool&activeTab=example)
## 前提条件
自动伸缩功能依赖弹性伸缩（Auto Scaling，旧称ESS）服务。启动节点自动伸缩前，您需要开通弹性伸缩服务，并完成默认角色授权。具体操作，请参见[开通弹性伸缩服务](../user-guide/auto-scaling-of-nodes.md)。
说明
如果您之前已经使用了alicloud_cs_kubernetes_autoscaler组件，默认已开通弹性伸缩服务。
已为系统运维管理 OOS（CloudOps Orchestration Service）服务授权。您可以通过创建AliyunOOSLifecycleHook4CSRole角色，为OOS服务授权。
单击[AliyunOOSLifecycleHook4CSRole](https://ram.console.aliyun.com/role/authorize?spm=5176.2020520152.0.0.5b4716ddI6QevL&request=%7B%22ReturnUrl%22%3A%22https%3A%2F%2Fram.console.aliyun.com%22%2C%22Services%22%3A%5B%7B%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunOOSLifecycleHook4CSRole%22%2C%22TemplateId%22%3A%22AliyunOOSLifecycleHook4CSRole%22%7D%5D%2C%22Service%22%3A%22OOS%22%7D%5D%7D)。
说明
如果当前账号是阿里云账号，单击AliyunOOSLifecycleHook4CSRole即可授权。
如果当前账号是RAM用户，请先确保对应的阿里云账号已授权AliyunOOSLifecycleHook4CSRole，并为RAM用户授予AliyunRAMReadOnlyAccess系统策略。具体操作，请参见[管理](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
在访问控制快速授权页面，单击确认授权。
准备Terraform运行环境，您可以选择以下任一方式来使用Terraform。
[在](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)[Terraform Explorer](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)[中使用](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)[Terraform](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)：阿里云提供了Terraform的在线运行环境，您无需安装Terraform，登录后即可在线使用和体验Terraform。适用于零成本、快速、便捷地体验和调试Terraform的场景。
[使用](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)[Terraform](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)[快速创建资源](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)：阿里云Cloud Shell中预装了Terraform的组件，并已配置好身份凭证，您可直接在Cloud Shell中运行Terraform的命令。适用于低成本、快速、便捷地访问和使用Terraform的场景。
[在本地安装和配置](https://help.aliyun.com/zh/terraform/install-and-configure-terraform-locally)[Terraform](https://help.aliyun.com/zh/terraform/install-and-configure-terraform-locally)：适用于网络连接较差或需要自定义开发环境的场景。
## 背景信息
Terraform是一种开源工具，通过Provider来支持新的基础架构，用于安全高效地预览、配置和管理云基础架构和资源。更多信息，请参见[了解阿里云](https://help.aliyun.com/zh/terraform/what-is-terraform#concept-vhk-wpc-rfb)[Terraform](https://help.aliyun.com/zh/terraform/what-is-terraform#concept-vhk-wpc-rfb)。
在[Alibaba Cloud Provider](https://registry.terraform.io/providers/aliyun/alicloud/latest)的老版本中，ACK提供了一个名为[alicloud_cs_kubernetes_autoscaler](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cs_kubernetes_autoscaler)的组件。alicloud_cs_kubernetes_autoscaler组件可以实现节点的弹性伸缩，但是其能力受限：
配置复杂，使用成本高。
伸缩的节点都会被放置到默认节点池，自动伸缩的节点未单独维护。
部分配置参数不可更改。
Alibaba Cloud Provider从1.111.0版本开始可通过组件[alicloud_cs_kubernetes_node_pool](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cs_kubernetes_node_pool)创建开启自动伸缩功能的节点池，优势如下：
配置简单，您只需要配置伸缩组内节点数的上下限。
针对非必须配置，ACK使用默认值的配置，以防误操作带来的基础环境不一致的问题，例如：操作系统镜像。
在ACK控制台中可以直观地观察节点池内节点的变化。
## 使用的资源
说明
本教程示例包含的部分资源会产生一定费用，请在不需要时及时进行释放或退订。
[alicloud_instance_types](https://help.aliyun.com/zh/terraform/alicloud-instance-types)：根据条件查询符合要求的ECS实例类型。
[alicloud_vpc](https://help.aliyun.com/zh/terraform/alicloud-vpc)：创建专有网络VPC。
[alicloud_vswitch](https://help.aliyun.com/zh/terraform/alicloud-vswitch)：创建虚拟交换机（vSwitch）为VPC划分一个或多个子网。
[alicloud_cs_managed_kubernetes](https://help.aliyun.com/zh/terraform/alicloud-cs-managed-kubernetes)：创建ACK托管版集群。
[alicloud_cs_kubernetes_node_pool](https://help.aliyun.com/zh/terraform/alicloud-cs-kubernetes-node-pool)：为ACK托管集群创建节点池。
## 通过控制台生成Terraform请求参数
如果由于请求参数组合不正确或以下示例中没有您需要的配置，您可以通过控制台生成创建节点池所需的请求参数组合。具体操作如下：
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点池。
在创建节点池弹窗中，配置节点池信息后，单击确认配置，然后单击左下角的同等代码。
在侧边栏中单击Terraform页签，页签中的代码块将展示您创建节点池时所需的参数组合，您可以单击代码块右上方的复制使用。
## 使用Terraform创建开启自动伸缩功能的节点池
### 使用过alicloud_cs_kubernetes_autoscaler组件
如果您的集群之前已经使用alicloud_cs_kubernetes_autoscaler组件，在完成上述为当前集群添加弹性伸缩服务授权后，您需要执行以下步骤平滑切换alicloud_cs_kubernetes_autoscaler至alicloud_cs_kubernetes_node_pool，以创建开启自动伸缩功能的节点池。
修改集群的autoscaler-meta配置项。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择配置管理>配置项。
在配置项页面左上角的命名空间下拉框中，选择kube-system，然后在autoscaler-meta配置项右侧操作列下，单击编辑。
在编辑面板中，修改autoscaler-meta配置项的值。
您需将taints值的String类型改成数组类型，即在值文本框中，修改"taints":""为"taints":[]。
单击确定。
同步节点池。
在集群管理页左侧导航栏，选择节点管理>节点池。
在节点池页面右上方，单击同步节点池。
### 未使用过alicloud_cs_kubernetes_autoscaler组件
您可以使用Terraform创建开启自动伸缩功能的节点池。
创建节点池的配置文件。
## 为已有集群创建开启自动伸缩功能的节点池
在已有集群中创建开启自动伸缩功能的节点池，配置示例如下。
provider "alicloud" { } # 为已有集群创建开启自动伸缩功能的节点池。 resource "alicloud_cs_kubernetes_node_pool" "at1" { # 目标集群ID。 cluster_id = "" name = "np-test" # 节点池内节点使用的vswitch，至少提供一个。 vswitch_ids = ["vsw-bp1mdigyhmilu2h4v****"] instance_types = ["ecs.e3.medium"] password = "Hello1234" scaling_config { # 最小节点数。 min_size = 1 # 最大节点数。 max_size = 5 } }
## 创建新的具备自动伸缩功能的节点池集群
创建一个包含自动伸缩节点池的集群，配置示例如下。
provider "alicloud" { region = var.region_id } variable "region_id" { type = string default = "cn-shenzhen" } variable "cluster_spec" { type = string description = "The cluster specifications of kubernetes cluster,which can be empty. Valid values:ack.standard : Standard managed clusters; ack.pro.small : Professional managed clusters." default = "ack.pro.small" } # 指定虚拟交换机（vSwitches）的可用区。 variable "availability_zone" { description = "The availability zones of vswitches." default = ["cn-shenzhen-c", "cn-shenzhen-e", "cn-shenzhen-f"] } # 用于创建新vSwitches的CIDR地址块列表。 variable "node_vswitch_cidrs" { type = list(string) default = ["172.16.0.0/23", "172.16.2.0/23", "172.16.4.0/23"] } # 用于创建Terway使用的vSwitch的CIDR地址块。 variable "terway_vswitch_cidrs" { type = list(string) default = ["172.16.208.0/20", "172.16.224.0/20", "172.16.240.0/20"] } # 定义了用于启动工作节点的ECS实例类型。 variable "worker_instance_types" { description = "The ecs instance types used to launch worker nodes." default = ["ecs.g6.2xlarge", "ecs.g6.xlarge"] } # 设置工作节点的密码 variable "password" { description = "The password of ECS instance." default = "Test123456" } # 指定创建ACK托管集群名称的前缀。 variable "k8s_name_prefix" { description = "The name prefix used to create managed kubernetes cluster." default = "tf-ack-shenzhen" } # 指定ACK集群安装的组件。包括Terway（网络组件）、csi-plugin（存储组件）、csi-provisioner（存储组件）、logtail-ds（日志组件）、Nginx Ingress Controller、ack-arms-prometheus（监控组件）以及ack-node-problem-detector（节点诊断组件）。 variable "cluster_addons" { type = list(object({ name = string config = string })) default = [ { "name" = "terway-eniip", "config" = "", }, { "name" = "logtail-ds", "config" = "{\"IngressDashboardEnabled\":\"true\"}", }, { "name" = "nginx-ingress-controller", "config" = "{\"IngressSlbNetworkType\":\"internet\"}", }, { "name" = "arms-prometheus", "config" = "", }, { "name" = "ack-node-problem-detector", "config" = "{\"sls_project_name\":\"\"}", }, { "name" = "csi-plugin", "config" = "", }, { "name" = "csi-provisioner", "config" = "", } ] } # 默认资源名称。 locals { k8s_name_terway = "k8s_name_terway_${random_integer.default.result}" vpc_name = "vpc_name_${random_integer.default.result}" autoscale_nodepool_name = "autoscale-node-pool-${random_integer.default.result}" } # 节点ECS实例配置。将查询满足CPU、Memory要求的ECS实例类型。 data "alicloud_instance_types" "default" { cpu_core_count = 8 memory_size = 32 availability_zone = var.availability_zone[0] kubernetes_node_role = "Worker" } resource "random_integer" "default" { min = 10000 max = 99999 } # 专有网络。 resource "alicloud_vpc" "default" { vpc_name = local.vpc_name cidr_block = "172.16.0.0/12" } # Node交换机。 resource "alicloud_vswitch" "vswitches" { count = length(var.node_vswitch_cidrs) vpc_id = alicloud_vpc.default.id cidr_block = element(var.node_vswitch_cidrs, count.index) zone_id = element(var.availability_zone, count.index) } # Pod交换机。 resource "alicloud_vswitch" "terway_vswitches" { count = length(var.terway_vswitch_cidrs) vpc_id = alicloud_vpc.default.id cidr_block = element(var.terway_vswitch_cidrs, count.index) zone_id = element(var.availability_zone, count.index) } # Kubernetes托管版。 resource "alicloud_cs_managed_kubernetes" "default" { name = local.k8s_name_terway # Kubernetes集群名称。 cluster_spec = var.cluster_spec # 创建Pro版集群。 worker_vswitch_ids = split(",", join(",", alicloud_vswitch.vswitches.*.id)) # 节点池所在的vSwitch。指定一个或多个vSwitch的ID，必须在availability_zone指定的区域中。 pod_vswitch_ids = split(",", join(",", alicloud_vswitch.terway_vswitches.*.id)) # Pod虚拟交换机。 new_nat_gateway = true # 是否在创建Kubernetes集群时创建新的NAT网关。默认为true。 service_cidr = "10.11.0.0/16" # Pod网络的CIDR块。当cluster_network_type设置为flannel，你必须设定该参数。它不能与VPC CIDR相同，并且不能与VPC中的Kubernetes集群使用的CIDR相同，也不能在创建后进行修改。集群中允许的最大主机数量：256。 slb_internet_enabled = true # 是否为API Server创建Internet负载均衡。默认为false。 enable_rrsa = true control_plane_log_components = ["apiserver", "kcm", "scheduler", "ccm"] # 控制平面日志。 dynamic "addons" { # 组件管理。 for_each = var.cluster_addons content { name = lookup(addons.value, "name", var.cluster_addons) config = lookup(addons.value, "config", var.cluster_addons) } } } # 创建自动伸缩节点池，节点池最多可以扩展到 10 个节点，最少保持 1 个节点。 resource "alicloud_cs_kubernetes_node_pool" "autoscale_node_pool" { cluster_id = alicloud_cs_managed_kubernetes.default.id node_pool_name = local.autoscale_nodepool_name vswitch_ids = split(",", join(",", alicloud_vswitch.vswitches.*.id)) scaling_config { min_size = 1 max_size = 10 } instance_types = var.worker_instance_types password = var.password # SSH登录集群节点的密码。 install_cloud_monitor = true # 是否为kubernetes的节点安装云监控。 system_disk_category = "cloud_efficiency" system_disk_size = 100 image_type = "AliyunLinux3" data_disks { # 节点数据盘配置。 category = "cloud_essd" # 节点数据盘种类。 size = 120 # 节点数据盘大小。 } }
执行如下命令，初始化Terraform运行环境。
terraform init
返回信息如下，Terraform初始化成功。
Terraform has been successfully initialized! You may now begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All Terraform commands should now work. If you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forget, other commands will detect it and remind you to do so if necessary.
执行terraform apply命令完成创建。
验证结果。
完成创建节点池后，在节点池列表中可以看到新建的节点池，该节点池名称下会标注已开启自动伸缩。在节点池页面，np-test节点池名称下方显示已开启自动伸缩标签，表示自动弹性伸缩配置已生效。
## 清理资源
当您不再需要上述通过Terraform创建或管理的资源时，请运行terraform destroy命令以释放资源。关于terraform destroy的更多信息，请参见[Terraform](https://help.aliyun.com/zh/terraform/terraform-common-commands)[常用命令](https://help.aliyun.com/zh/terraform/terraform-common-commands)。
terraform destroy
## 完整示例
说明
本教程所含示例代码支持一键运行，您可以直接运行代码。[一键运行](https://api.aliyun.com/api-tools/terraform?resource=alicloud_cs_managed_kubernetes&exampleId=201-use-case-create-auto-scaling-node-pool&activeTab=example)
### 示例代码
provider "alicloud" { region = var.region_id } variable "region_id" { type = string default = "cn-shenzhen" } variable "cluster_spec" { type = string description = "The cluster specifications of kubernetes cluster,which can be empty. Valid values:ack.standard : Standard managed clusters; ack.pro.small : Professional managed clusters." default = "ack.pro.small" } # 指定虚拟交换机（vSwitches）的可用区。 variable "availability_zone" { description = "The availability zones of vswitches." default = ["cn-shenzhen-c", "cn-shenzhen-e", "cn-shenzhen-f"] } # 用于创建新vSwitches的CIDR地址块列表。 variable "node_vswitch_cidrs" { type = list(string) default = ["172.16.0.0/23", "172.16.2.0/23", "172.16.4.0/23"] } # 用于创建Terway使用的vSwitch的CIDR地址块。 variable "terway_vswitch_cidrs" { type = list(string) default = ["172.16.208.0/20", "172.16.224.0/20", "172.16.240.0/20"] } # 定义了用于启动工作节点的ECS实例类型。 variable "worker_instance_types" { description = "The ecs instance types used to launch worker nodes." default = ["ecs.g6.2xlarge", "ecs.g6.xlarge"] } # 设置工作节点的密码 variable "password" { description = "The password of ECS instance." default = "Test123456" } # 指定创建ACK托管集群名称的前缀。 variable "k8s_name_prefix" { description = "The name prefix used to create managed kubernetes cluster." default = "tf-ack-shenzhen" } # 指定ACK集群安装的组件。包括Terway（网络组件）、csi-plugin（存储组件）、csi-provisioner（存储组件）、logtail-ds（日志组件）、Nginx Ingress Controller、ack-arms-prometheus（监控组件）以及ack-node-problem-detector（节点诊断组件）。 variable "cluster_addons" { type = list(object({ name = string config = string })) default = [ { "name" = "terway-eniip", "config" = "", }, { "name" = "logtail-ds", "config" = "{\"IngressDashboardEnabled\":\"true\"}", }, { "name" = "nginx-ingress-controller", "config" = "{\"IngressSlbNetworkType\":\"internet\"}", }, { "name" = "arms-prometheus", "config" = "", }, { "name" = "ack-node-problem-detector", "config" = "{\"sls_project_name\":\"\"}", }, { "name" = "csi-plugin", "config" = "", }, { "name" = "csi-provisioner", "config" = "", } ] } # 默认资源名称。 locals { k8s_name_terway = "k8s_name_terway_${random_integer.default.result}" vpc_name = "vpc_name_${random_integer.default.result}" autoscale_nodepool_name = "autoscale-node-pool-${random_integer.default.result}" } # 节点ECS实例配置。将查询满足CPU、Memory要求的ECS实例类型。 data "alicloud_instance_types" "default" { cpu_core_count = 8 memory_size = 32 availability_zone = var.availability_zone[0] kubernetes_node_role = "Worker" } resource "random_integer" "default" { min = 10000 max = 99999 } # 专有网络。 resource "alicloud_vpc" "default" { vpc_name = local.vpc_name cidr_block = "172.16.0.0/12" } # Node交换机。 resource "alicloud_vswitch" "vswitches" { count = length(var.node_vswitch_cidrs) vpc_id = alicloud_vpc.default.id cidr_block = element(var.node_vswitch_cidrs, count.index) zone_id = element(var.availability_zone, count.index) } # Pod交换机。 resource "alicloud_vswitch" "terway_vswitches" { count = length(var.terway_vswitch_cidrs) vpc_id = alicloud_vpc.default.id cidr_block = element(var.terway_vswitch_cidrs, count.index) zone_id = element(var.availability_zone, count.index) } # Kubernetes托管版。 resource "alicloud_cs_managed_kubernetes" "default" { name = local.k8s_name_terway # Kubernetes集群名称。 cluster_spec = var.cluster_spec # 创建Pro版集群。 worker_vswitch_ids = split(",", join(",", alicloud_vswitch.vswitches.*.id)) # 节点池所在的vSwitch。指定一个或多个vSwitch的ID，必须在availability_zone指定的区域中。 pod_vswitch_ids = split(",", join(",", alicloud_vswitch.terway_vswitches.*.id)) # Pod虚拟交换机。 new_nat_gateway = true # 是否在创建Kubernetes集群时创建新的NAT网关。默认为true。 service_cidr = "10.11.0.0/16" # Pod网络的CIDR块。当cluster_network_type设置为flannel，你必须设定该参数。它不能与VPC CIDR相同，并且不能与VPC中的Kubernetes集群使用的CIDR相同，也不能在创建后进行修改。集群中允许的最大主机数量：256。 slb_internet_enabled = true # 是否为API Server创建Internet负载均衡。默认为false。 enable_rrsa = true control_plane_log_components = ["apiserver", "kcm", "scheduler", "ccm"] # 控制平面日志。 dynamic "addons" { # 组件管理。 for_each = var.cluster_addons content { name = lookup(addons.value, "name", var.cluster_addons) config = lookup(addons.value, "config", var.cluster_addons) } } } # 创建自动伸缩节点池，节点池最多可以扩展到 10 个节点，最少保持 1 个节点。 resource "alicloud_cs_kubernetes_node_pool" "autoscale_node_pool" { cluster_id = alicloud_cs_managed_kubernetes.default.id node_pool_name = local.autoscale_nodepool_name vswitch_ids = split(",", join(",", alicloud_vswitch.vswitches.*.id)) scaling_config { min_size = 1 max_size = 10 } instance_types = var.worker_instance_types password = var.password # SSH登录集群节点的密码。 install_cloud_monitor = true # 是否为kubernetes的节点安装云监控。 system_disk_category = "cloud_efficiency" system_disk_size = 100 image_type = "AliyunLinux3" data_disks { # 节点数据盘配置。 category = "cloud_essd" # 节点数据盘种类。 size = 120 # 节点数据盘大小。 } }
如果您想体验更多完整示例，请前往[更多完整示例](https://github.com/alibabacloud-automation/landing-with-terraform/tree/main/quickstarts)中对应产品的文件夹查看。
## 相关文档
[节点池](../user-guide/node-pool-overview.md)
[启用节点自动伸缩](../user-guide/auto-scaling-of-nodes.md)
[通过](use-terraform-to-create-an-ack-managed-cluster.md)[Terraform](use-terraform-to-create-an-ack-managed-cluster.md)[创建](use-terraform-to-create-an-ack-managed-cluster.md)[ACK](use-terraform-to-create-an-ack-managed-cluster.md)[托管集群](use-terraform-to-create-an-ack-managed-cluster.md)
[alicloud_cs_kubernetes_node_pool](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cs_kubernetes_node_pool)
[alicloud_cs_kubernetes_autoscaler](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cs_kubernetes_autoscaler)
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
