# 使用Terraform创建ACK托管版集群-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-create-an-ack-managed-cluster

# 使用Terraform创建ACK托管版集群
本文介绍如何使用Terraform创建ACK托管集群。
说明
本教程所含示例代码支持一键运行，您可以直接运行代码。[一键运行](https://api.aliyun.com/api-tools/terraform?resource=alicloud_cs_managed_kubernetes&exampleId=201-use-case-create-ack-managed-cluster&activeTab=example)
## 前提条件
已开通容器服务 Kubernetes 版ACK。若需要使用Terraform开通，请参见[通过](use-terraform-to-assign-default-roles-to-ack-when-you-use-ack-for-the-first-time.md)[Terraform](use-terraform-to-assign-default-roles-to-ack-when-you-use-ack-for-the-first-time.md)[开通](use-terraform-to-assign-default-roles-to-ack-when-you-use-ack-for-the-first-time.md)[ACK](use-terraform-to-assign-default-roles-to-ack-when-you-use-ack-for-the-first-time.md)[并授权角色](use-terraform-to-assign-default-roles-to-ack-when-you-use-ack-for-the-first-time.md)。
由于阿里云账号（主账号）具有资源的所有权限，一旦发生泄露将面临重大风险。建议您使用RAM用户，并为该RAM用户创建AccessKey，具体操作方式请参见[创建](../../../../ram/documents/user-guide/create-a-ram-user.md)[RAM](../../../../ram/documents/user-guide/create-a-ram-user.md)[用户](../../../../ram/documents/user-guide/create-a-ram-user.md)和[创建](../../../../ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](../../../../ram/documents/user-guide/create-an-accesskey-pair.md)。
为运行Terraform命令的RAM用户绑定以下最小权限策略，以获取管理本示例所涉及资源的权限。更多信息，请参见[为](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
该权限策略允许RAM用户进行VPC、交换机及ACK的创建、查看与删除操作。
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "vpc:CreateVpc", "vpc:CreateVSwitch", "cs:CreateCluster", "vpc:DescribeVpcAttribute", "vpc:DescribeVSwitchAttributes", "vpc:DescribeRouteTableList", "vpc:DescribeNatGateways", "cs:DescribeTaskInfo", "cs:DescribeClusterDetail", "cs:GetClusterCerts", "cs:CheckControlPlaneLogEnable", "cs:CreateClusterNodePool", "cs:DescribeClusterNodePoolDetail", "cs:ModifyClusterNodePool", "vpc:DeleteVpc", "vpc:DeleteVSwitch", "cs:DeleteCluster", "cs:DeleteClusterNodepool" ], "Resource": "*" } ] }
准备Terraform运行环境，您可以选择以下任一方式来使用Terraform。
[在](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)[Terraform Explorer](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)[中使用](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)[Terraform](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)：阿里云提供了Terraform的在线运行环境，您无需安装Terraform，登录后即可在线使用和体验Terraform。适用于零成本、快速、便捷地体验和调试Terraform的场景。
[使用](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)[Terraform](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)[快速创建资源](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)：阿里云Cloud Shell中预装了Terraform的组件，并已配置好身份凭证，您可直接在Cloud Shell中运行Terraform的命令。适用于低成本、快速、便捷地访问和使用Terraform的场景。
[在资源编排（ROS）中使用](https://help.aliyun.com/zh/ros/user-guide/create-a-terraform-template)[Terraform](https://help.aliyun.com/zh/ros/user-guide/create-a-terraform-template)：资源编排服务（ROS）为Terraform提供了托管的能力，您可以创建Terraform类型的模板，定义阿里云、AWS或Azure资源，配置资源参数和资源间的依赖关系。
[在本地安装和配置](https://help.aliyun.com/zh/terraform/install-and-configure-terraform-locally)[Terraform](https://help.aliyun.com/zh/terraform/install-and-configure-terraform-locally)：适用于网络连接较差或需要自定义开发环境的场景。
重要
请确保版本不低于v0.12.28。如需检查现有版本，请运行terraform --version命令。
## 使用的资源
说明
本教程示例包含的部分资源会产生一定费用，请在不需要时及时进行释放或退订。
[alicloud_zones](https://help.aliyun.com/zh/terraform/alicloud-zones)：查询可用区。
[alicloud_instance_types](https://help.aliyun.com/zh/terraform/alicloud-instance-types)：根据条件查询符合要求的ECS实例类型。
[alicloud_vpc](https://help.aliyun.com/zh/terraform/alicloud-vpc)：创建专有网络VPC。
[alicloud_vswitch](https://help.aliyun.com/zh/terraform/alicloud-vswitch)：创建虚拟交换机（vSwitch）为VPC划分一个或多个子网。
[alicloud_cs_managed_kubernetes](https://help.aliyun.com/zh/terraform/alicloud-cs-managed-kubernetes)：创建ACK托管版集群。
[alicloud_cs_kubernetes_node_pool](https://help.aliyun.com/zh/terraform/alicloud-cs-kubernetes-node-pool)：为ACK托管集群创建节点池。
## 通过控制台生成Terraform请求参数
如果由于请求参数组合不正确或以下示例中没有您需要的配置，您可以通过控制台生成创建集群所需的请求参数组合。具体操作如下：
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击集群模板。
在对话框，选择需要创建的集群类型，并单击创建，然后在集群配置页面配置集群信息。
配置完成后，在确认配置页面，单击右上角的同等代码。
在侧边栏中单击Terraform页签，将展示您创建集群时所需的参数组合，您可以复制使用。
## 使用Terraform创建ACK托管集群（Terway）
本示例将创建一个包含普通节点池、托管节点池及自动伸缩节点池的ACK托管集群，并为该集群默认安装一系列组件，包括Terway（网络组件）、csi-plugin（存储组件）、csi-provisioner（存储组件）、日志采集组件、Nginx Ingress Controller、ack-arms-prometheus（监控组件）以及ack-node-problem-detector（节点诊断组件）。
创建一个工作目录，并在该工作目录中创建名为main.tf的配置文件，然后将以下代码复制到main.tf中。
provider "alicloud" { region = var.region_id } variable "region_id" { type = string default = "cn-shenzhen" } variable "cluster_spec" { type = string description = "The cluster specifications of kubernetes cluster,which can be empty. Valid values:ack.standard : Standard managed clusters; ack.pro.small : Professional managed clusters." default = "ack.pro.small" } # 指定虚拟交换机（vSwitches）的可用区。 variable "availability_zone" { description = "The availability zones of vswitches." default = ["cn-shenzhen-c", "cn-shenzhen-e", "cn-shenzhen-f"] } # 指定交换机ID（vSwitch IDs）的列表。 variable "node_vswitch_ids" { description = "List of existing node vswitch ids for terway." type = list(string) default = [] } # 用于创建新vSwitches的CIDR地址块列表。 variable "node_vswitch_cidrs" { description = "List of cidr blocks used to create several new vswitches when 'node_vswitch_ids' is not specified." type = list(string) default = ["172.16.0.0/23", "172.16.2.0/23", "172.16.4.0/23"] } # 指定网络组件Terway配置。如果为空，默认会根据terway_vswitch_cidrs的创建新的terway vSwitch。 variable "terway_vswitch_ids" { description = "List of existing pod vswitch ids for terway." type = list(string) default = [] } # 当没有指定terway_vswitch_ids时，用于创建Terway使用的vSwitch的CIDR地址块。 variable "terway_vswitch_cidrs" { description = "List of cidr blocks used to create several new vswitches when 'terway_vswitch_ids' is not specified." type = list(string) default = ["172.16.208.0/20", "172.16.224.0/20", "172.16.240.0/20"] } # 定义了用于启动工作节点的ECS实例类型。 variable "worker_instance_types" { description = "The ecs instance types used to launch worker nodes." default = ["ecs.g6.2xlarge", "ecs.g6.xlarge"] } # 指定ACK集群安装的组件。包括Terway（网络组件）、csi-plugin（存储组件）、csi-provisioner（存储组件）、loongcollector（日志组件）、Nginx Ingress Controller、ack-arms-prometheus（监控组件）以及ack-node-problem-detector（节点诊断组件）。 variable "cluster_addons" { type = list(object({ name = string config = string })) default = [ { "name" = "terway-eniip", "config" = "", }, { "name" = "loongcollector", "config" = "{\"IngressDashboardEnabled\":\"true\"}", }, { "name" = "nginx-ingress-controller", "config" = "{\"IngressSlbNetworkType\":\"internet\"}", }, { "name" = "arms-prometheus", "config" = "", }, { "name" = "ack-node-problem-detector", "config" = "{\"sls_project_name\":\"\"}", }, { "name" = "csi-plugin", "config" = "", }, { "name" = "csi-provisioner", "config" = "", } ] } # 指定创建ACK托管集群名称的前缀。 variable "k8s_name_prefix" { description = "The name prefix used to create managed kubernetes cluster." default = "tf-ack-shenzhen" } # 默认资源名称。 locals { k8s_name_terway = substr(join("-", [var.k8s_name_prefix, "terway"]), 0, 63) k8s_name_flannel = substr(join("-", [var.k8s_name_prefix, "flannel"]), 0, 63) k8s_name_ask = substr(join("-", [var.k8s_name_prefix, "ask"]), 0, 63) new_vpc_name = "tf-vpc-172-16" new_vsw_name_azD = "tf-vswitch-azD-172-16-0" new_vsw_name_azE = "tf-vswitch-azE-172-16-2" new_vsw_name_azF = "tf-vswitch-azF-172-16-4" nodepool_name = "default-nodepool" managed_nodepool_name = "managed-node-pool" autoscale_nodepool_name = "autoscale-node-pool" log_project_name = "log-for-${local.k8s_name_terway}" } # 节点ECS实例配置。将查询满足CPU、Memory要求的ECS实例类型。 data "alicloud_instance_types" "default" { cpu_core_count = 8 memory_size = 32 availability_zone = var.availability_zone[0] kubernetes_node_role = "Worker" } # 专有网络。 resource "alicloud_vpc" "default" { vpc_name = local.new_vpc_name cidr_block = "172.16.0.0/12" } # Node交换机。 resource "alicloud_vswitch" "vswitches" { count = length(var.node_vswitch_ids) > 0 ? 0 : length(var.node_vswitch_cidrs) vpc_id = alicloud_vpc.default.id cidr_block = element(var.node_vswitch_cidrs, count.index) zone_id = element(var.availability_zone, count.index) } # Pod交换机。 resource "alicloud_vswitch" "terway_vswitches" { count = length(var.terway_vswitch_ids) > 0 ? 0 : length(var.terway_vswitch_cidrs) vpc_id = alicloud_vpc.default.id cidr_block = element(var.terway_vswitch_cidrs, count.index) zone_id = element(var.availability_zone, count.index) } # Kubernetes托管版。 resource "alicloud_cs_managed_kubernetes" "default" { name = local.k8s_name_terway # Kubernetes集群名称。 cluster_spec = var.cluster_spec # 创建Pro版集群。 vswitch_ids = split(",", join(",", alicloud_vswitch.vswitches.*.id)) # 节点池所在的vSwitch。指定一个或多个vSwitch的ID，必须在availability_zone指定的区域中。 pod_vswitch_ids = split(",", join(",", alicloud_vswitch.terway_vswitches.*.id)) # Pod虚拟交换机。 new_nat_gateway = true # 是否在创建Kubernetes集群时创建新的NAT网关。默认为true。 service_cidr = "10.11.0.0/16" # Pod网络的CIDR块。当cluster_network_type设置为flannel，你必须设定该参数。它不能与VPC CIDR相同，并且不能与VPC中的Kubernetes集群使用的CIDR相同，也不能在创建后进行修改。集群中允许的最大主机数量：256。 slb_internet_enabled = true # 是否为API Server创建Internet负载均衡。默认为false。 enable_rrsa = true control_plane_log_components = ["apiserver", "kcm", "scheduler", "ccm"] # 控制平面日志。 dynamic "addons" { # 组件管理。 for_each = var.cluster_addons content { name = lookup(addons.value, "name", var.cluster_addons) config = lookup(addons.value, "config", var.cluster_addons) } } } # 普通节点池。 resource "alicloud_cs_kubernetes_node_pool" "default" { cluster_id = alicloud_cs_managed_kubernetes.default.id # Kubernetes集群名称。 node_pool_name = local.nodepool_name # 节点池名称。 vswitch_ids = split(",", join(",", alicloud_vswitch.vswitches.*.id)) # 节点池所在的vSwitch。指定一个或多个vSwitch的ID，必须在availability_zone指定的区域中。 instance_types = var.worker_instance_types instance_charge_type = "PostPaid" desired_size = 2 # 节点池的期望节点数。 install_cloud_monitor = true # 是否为Kubernetes的节点安装云监控。 system_disk_category = "cloud_efficiency" system_disk_size = 100 image_type = "AliyunLinux" data_disks { # 节点数据盘配置。 category = "cloud_essd" # 节点数据盘种类。 size = 120 # 节点数据盘大小。 } } # 创建托管节点池。 resource "alicloud_cs_kubernetes_node_pool" "managed_node_pool" { cluster_id = alicloud_cs_managed_kubernetes.default.id # Kubernetes集群名称。 node_pool_name = local.managed_nodepool_name # 节点池名称。 vswitch_ids = split(",", join(",", alicloud_vswitch.vswitches.*.id)) # 节点池所在的vSwitch。指定一个或多个vSwitch的ID，必须在availability_zone指定的区域中。 desired_size = 0 # 节点池的期望节点数。 management { auto_repair = true auto_upgrade = true max_unavailable = 1 } instance_types = var.worker_instance_types instance_charge_type = "PostPaid" install_cloud_monitor = true system_disk_category = "cloud_efficiency" system_disk_size = 100 image_type = "AliyunLinux" data_disks { category = "cloud_essd" size = 120 } } # 创建自动伸缩节点池，节点池最多可以扩展到 10 个节点，最少保持 1 个节点。 resource "alicloud_cs_kubernetes_node_pool" "autoscale_node_pool" { cluster_id = alicloud_cs_managed_kubernetes.default.id node_pool_name = local.autoscale_nodepool_name vswitch_ids = split(",", join(",", alicloud_vswitch.vswitches.*.id)) scaling_config { min_size = 1 max_size = 10 } instance_types = var.worker_instance_types install_cloud_monitor = true # 是否为kubernetes的节点安装云监控。 system_disk_category = "cloud_efficiency" system_disk_size = 100 image_type = "AliyunLinux3" data_disks { # 节点数据盘配置。 category = "cloud_essd" # 节点数据盘种类。 size = 120 # 节点数据盘大小。 } }
执行以下命令，初始化Terraform运行环境。
terraform init
返回如下信息，表示Terraform初始化成功。
Terraform has been successfully initialized! You may now begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All Terraform commands should now work. If you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forget, other commands will detect it and remind you to do so if necessary.
创建执行计划，并预览变更。
terraform plan
执行以下命令，创建集群。
terraform apply
在执行过程中，根据提示输入yes并按下Enter键，等待命令执行完成，若出现以下信息，则表示ACK集群创建成功。
Do you want to perform these actions? Terraform will perform the actions described above. Only 'yes' will be accepted to approve. Enter a value: yes ... alicloud_cs_managed_kubernetes.default: Creation complete after 5m48s [id=ccb53e72ec6c447c990762800********] ... Apply complete! Resources: 11 added, 0 changed, 0 destroyed.
验证结果
## 执行terraform show命令
您可以使用以下命令查询Terraform已创建资源的详细信息。
terraform show
## 登录ACK控制台
登录[容器服务管理控制台](https://cs.console.aliyun.com)，查看已创建的集群。
## 清理资源
当您不再需要上述通过Terraform创建或管理的资源时，请运行terraform destroy命令以释放资源。关于terraform destroy的更多信息，请参见[Terraform](https://help.aliyun.com/zh/terraform/terraform-common-commands)[常用命令](https://help.aliyun.com/zh/terraform/terraform-common-commands)。
terraform destroy
## 相关文档
创建ACK托管集群时需要安装额外组件，请参见[使用](use-terraform-to-manage-plug-ins.md)[Terraform](use-terraform-to-manage-plug-ins.md)[管理组件](use-terraform-to-manage-plug-ins.md)。
关于节点池创建的更多内容，请参见[通过](use-terraform-to-create-an-auto-scaling-node-pool.md)[Terraform](use-terraform-to-create-an-auto-scaling-node-pool.md)[创建具备自动伸缩功能的节点池](use-terraform-to-create-an-auto-scaling-node-pool.md)。
当您遇到由于网络延迟等原因造成的terraform init超时，导致无法正常下载Provider等情况时，请参见[Terraform Init 加速方案配置](https://help.aliyun.com/zh/terraform/terraform-init-acceleration-solution-configuration)。
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
