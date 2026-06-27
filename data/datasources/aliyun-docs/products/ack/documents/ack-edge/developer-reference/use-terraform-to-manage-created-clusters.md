# 使用Terraform管理已创建的集群-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/developer-reference/use-terraform-to-manage-created-clusters

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

# 使用Terraform管理已创建的集群

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Terraform支持导入和管理ACK的存量资源，例如集群、节点池等。本文介绍如何通过Terraform管理存量ACK托管集群。

## 前提条件

已创建ACK托管版集群，其中包含一个有两个节点的节点池。具体操作，请参见[通过](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-create-an-ack-managed-cluster.md)[Terraform](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-create-an-ack-managed-cluster.md)[创建](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-create-an-ack-managed-cluster.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-create-an-ack-managed-cluster.md)[托管集群](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-create-an-ack-managed-cluster.md)。

## 操作步骤

- 

创建一个工作目录，并在工作目录中创建名为main.tf的配置文件。

provider "alicloud" { }

- 

执行以下命令，初始化Terraform运行环境。

terraform init

返回信息如下，Terraform初始化成功。

Initializing the backend... Initializing provider plugins... - Checking for available provider plugins... - Downloading plugin for provider "alicloud" (hashicorp/alicloud) 1.90.1... ... You may now begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All Terraform commands should now work. If you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forget, other commands will detect it and remind you to do so if necessary.

- 

导入集群。

- 

将集群的资源添加到main.tf文件中。

# Kubernetes托管版。 resource "alicloud_cs_managed_kubernetes" "default" { }

- 

执行以下命令，导入集群。

其中，<Cluster-ID>为待导入集群的ID。

terraform import alicloud_cs_managed_kubernetes.default <Cluster-ID>

预期输出：

alicloud_cs_managed_kubernetes.default: Importing from ID "cc7c582b0XXXXXcb80ae118eef0cb12"... alicloud_cs_managed_kubernetes.default: Import complete! Imported alicloud_cs_managed_kubernetes alicloud_cs_managed_kubernetes.default: Refreshing state... [id=cc7c582b0XXXXXcb80ae118eef0cb12] Import successful! The resources that were imported are shown above. These resources are now in your Terraform state and will henceforth be managed by Terraform.

此时，在terraform.tfstate文件中会显示类似如下导入的集群信息：

{ "mode": "managed", "type": "alicloud_cs_managed_kubernetes", "name": "default", "provider": "provider.alicloud", "instances": [ { "mode": "managed", "type": "alicloud_cs_managed_kubernetes", "name": "default", "provider": "provider.alicloud", "instances": [ ........ ] } ] }

- 

根据terraform.tfstate文件的内容，补充main.tf的必填字段。

provider "alicloud" { } resource "alicloud_cs_managed_kubernetes" "default" { worker_vswitch_ids = [ # 补充必填字段。 ..... ] }

- 

执行如下命令，查看本地资源与集群差异，以确保main.tf文件与导入集群资源一致。

terraform plan

请将以下带有->状态更新或+新增字段的内容添加到main.tf文件中。可以忽略带有(known after apply)的字段。参数字段描述请参见[Only works for Create Operation](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cs_managed_kubernetes)。

alicloud_cs_managed_kubernetes.default: Refreshing state.. erraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols: -/+ destroy and then create replacement Terraform will perform the following actions: # 请将如下代码中，状态即将变换的字段补充至main.tf文件中。 # alicloud_cs_managed_kubernetes.default must be replaced ~ cluster_spec = "ack.pro.small" -> (known after apply) ~ connections = { - "api_server_internet" = "" - "api_server_intranet" = "https://10.XX.XX.154:6443" - "service_domain" = "*.ca28e9fbefe8647d2a21057bcf5c993e0.cn-hangzhou.alicontainer.com" } -> (known after apply) - control_plane_log_components = [] -> null + control_plane_log_project = (known after apply) + control_plane_log_ttl = (known after apply) deletion_protection = false - enable_rrsa = false -> null ~ id = "ca28e9fbeXXXXXX1057bcf5c993e0" -> (known after apply) + install_cloud_monitor = (known after apply) + is_enterprise_security_group = (known after apply) + load_balancer_spec = "slb.s1.small" ~ name = "TFCESHI" -> (known after apply) + name_prefix = "Terraform-Creation" #修改集群名称为Terraform-Creation，如果不希望修改可用name字段代替。 ~ nat_gateway_id = "ngw-bp17XXXXguwkeyj" -> (known after apply) + new_nat_gateway = true ~ node_cidr_mask = 26 -> 24 # forces replacement + node_port_range = (known after apply) + platform = (known after apply) - pod_cidr = "172.16.224.0/20" -> null # forces replacement proxy_mode = "ipvs" ~ resource_group_id = "rg-acfmwXXXXesq" -> (known after apply) ~ rrsa_metadata = [ - { - enabled = false - ram_oidc_provider_arn = "" - ram_oidc_provider_name = "" - rrsa_oidc_issuer_url = "" }, ] -> (known after apply) ~ security_group_id = "sg-bp11XXXXXX9d8rp3" -> (known after apply) - service_cidr = "192.168.0.0/16" -> null # forces replacement ~ slb_id = "lb-bp1dqXXXXXXeifbb3" -> (known after apply) + slb_internet = (known after apply) + slb_internet_enabled = true ~ slb_intranet = "10.XX.XXX.154" -> (known after apply) - tags = {} -> null - timezone = "Asia/Shanghai" -> null # forces replacement ~ version = "1.31.1-aliyun.1" -> (known after apply) ~ vpc_id = "vpc-bp1l44aXXXXXXc54ev" -> (known after apply) + worker_auto_renew_period = (known after apply) + worker_disk_size = (known after apply) + worker_instance_charge_type = (known after apply) + worker_period = (known after apply) + worker_period_unit = (known after apply) ~ worker_ram_role_name = "KubernetesWorkerRole-04d86599-xxxx-487a-b927-379e63b9d485" -> (known after apply) worker_vswitch_ids = [ "vsw-bp1fXXXXX2nuig6h", ] ~ maintenance_window { ~ duration = "3h" -> (known after apply) ~ enable = true -> (known after apply) ~ maintenance_time = "2024-10-22T16:00:00.000Z" -> (known after apply) ~ weekly_period = "Wednesday" -> (known after apply) } + operation_policy { + cluster_auto_upgrade { + channel = (known after apply) + enabled = (known after apply) } } - timeouts {} + worker_nodes { + id = (known after apply) + name = (known after apply) + private_ip = (known after apply) } } Plan: 1 to add, 0 to change, 1 to destroy.

说明

为了确保资源模板与资源状态一致，需要在模板中手动补充缺失的参数定义，直到运行terraform plan时不再出现变更信息为止。

provider "alicloud" { region = "cn-hangzhou" # 导入集群所在的区域。 } resource "alicloud_cs_managed_kubernetes" "default" { worker_vswitch_ids = [ "vsw-bp1fXXXXX2nuig6h" ] deletion_protection = false load_balancer_spec = "slb.s1.small" name = "TFCESHI" new_nat_gateway = true proxy_mode = "ipvs" slb_internet_enabled = true node_cidr_mask = 26 service_cidr = "192.168.0.0/16" pod_cidr = "172.16.224.0/20" control_plane_log_components = [] enable_rrsa = false tags = {} timezone = "Asia/Shanghai" }

- 

执行如下命令，将上一步中补充的字段导入至本地集群。

terraform apply

返回信息如下，字段导入成功。

alicloud_cs_managed_kubernetes.default: Modifying... [id=cc7c582b0XXXXXcb80ae118eef0cb12] alicloud_cs_managed_kubernetes.default: Modifications complete after 2s [id=cc7c582b0XXXXXcb80ae118eef0cb12] Apply complete! Resources: 0 added, 1 changed, 0 destroyed.

- 

导入节点池。

- 

将集群的节点资源添加到main.tf文件中。

# Kubernetes托管版。 resource "alicloud_cs_kubernetes_node_pool" "default" { }

- 

执行以下命令，导入节点池。

其中，<Cluster-ID>为待导入集群的ID，此处为上一步中导入集群的ID，<Nodepool-ID>为待导入节点池的ID，两者通过英文半角冒号（:）分隔。

terraform import alicloud_cs_kubernetes_node_pool.default <Cluster-ID>:<Nodepool-ID>

预期输出：

alicloud_cs_kubernetes_node_pool.default: Importing from ID "cc7c582b0XXXXXcb80ae118eef0cb12*:np0f8f219XXXXX5d4aa503c3d24ca****"... alicloud_cs_kubernetes_node_pool.default: Import complete! Imported alicloud_cs_kubernetes_node_pool alicloud_cs_kubernetes_node_pool.default: Refreshing state... [id=cc7c582b0XXXXXcb80ae118eef0cb12:np651662XXXXXd9979360b24b1a009] Import successful! The resources that were imported are shown above. These resources are now in your Terraform state and will henceforth be managed by Terraform.

此时，在terraform.tfstate文件中会显示如下导入的节点池信息：

..... "resources": [ { "mode": "managed", "type": "alicloud_cs_kubernetes_node_pool", "name": "default", "provider": "provider.alicloud", "instances": [ ..... ] } ]

- 

根据terraform.tfstate文件的内容，补充main.tf的必填字段。

provider "alicloud" { } # 节点池。 resource "alicloud_cs_kubernetes_node_pool" "default" { name = .... # 节点池的名称。 instance_types = .... # 节点池的实例类型。 vswitch_ids = .... # 节点使用交换机ID。 cluster_id = alicloud_cs_managed_kubernetes.default.id # 引用 cluster_id }

- 

执行如下命令，将上一步中补充的字段导入至本地集群。

terraform apply

返回信息如下，字段导入成功。

alicloud_cs_kubernetes_node_pool.default: Refreshing state... [id=cc7c5XXXXX6dcb80ae118eef0cb12:np651662XXXXXd9979360b24b1a009] alicloud_cs_managed_kubernetes.default: Refreshing state... [id=cc7c582XXXXX6dcb80ae118eef0cb12] Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols: ~ update in-place Terraform will perform the following actions: ............ # (2 unchanged blocks hidden) } Plan: 0 to add, 1 to change, 0 to destroy.

集群导入完成后，您就可以通过main.tf文件对集群或节点池进行操作。

- 

验证节点池的扩容操作。

- 

通过main.tf验证节点池的扩容操作。

比如给刚导入的节点池扩容至3个节点，需要将main.tf文件新增为desired_size = 3字段。

...... # Kubernetes托管版。 resource "alicloud_cs_kubernetes_node_pool" "default" { ..... # 节点池期望节点数为3。 desired_size = 3 } .....

- 

执行以下命令，完成变更操作。

terraform apply

返回信息如下，输入yes，按Enter键，等待变更结束。

alicloud_cs_kubernetes_node_pool.default: Refreshing state... [id=cc7c5XXXXX546dcb80ae118eef0cb12:np651662dfc3e4440d9979360b24b1a009] alicloud_cs_managed_kubernetes.default: Refreshing state... [id=cc7c582bXXXXXcb80ae118eef0cb12] Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols: ~ update in-place Terraform will perform the following actions: # alicloud_cs_kubernetes_node_pool.default will be updated in-place ~ resource "alicloud_cs_kubernetes_node_pool" "default" { ~ desired_size = 2 -> 3 # (2 unchanged blocks hidden) } Plan: 0 to add, 1 to change, 0 to destroy. Do you want to perform these actions? Terraform will perform the actions described above. Only 'yes' will be accepted to approve. Enter a value: yes alicloud_cs_kubernetes_node_pool.default: Modifying... [id=cc7c582b0XXXXXcb80ae118eef0cb12:np651662dfc3e4XXXXX360b24b1a009] alicloud_cs_kubernetes_node_pool.default: Still modifying... [id=cc7c582XXXXX6dcb80ae118eef0cb12:np651662dXXXXX0d9979360b24b1a009, 10s elapsed] alicloud_cs_kubernetes_node_pool.default: Still modifying... [id=cc7c582bXXXXX6dcb80ae118eef0cb12:np651662XXXXX0d9979360b24b1a009, 20s elapsed] alicloud_cs_kubernetes_node_pool.default: Still modifying... [id=cc7c582bXXXXXdcb80ae118eef0cb12:np65166XXXXX440d9979360b24b1a009, 30s elapsed] alicloud_cs_kubernetes_node_pool.default: Still modifying... [id=cc7c582b0XXXXXae118eef0cb12:np6516XXXXX3e4440d9979360b24b1a009, 40s elapsed] alicloud_cs_kubernetes_node_pool.default: Still modifying... [id=cc7c582b0XXXXX6dcb80ae118eef0cb12:np65166XXXXXe4440d9979360b24b1a009, 50s elapsed] alicloud_cs_kubernetes_node_pool.default: Modifications complete after 1m0s [id=cc7c582b0b2b546dcb80ae118eef0cb12:np651662dfc3e4440d9979360b24b1a009] Apply complete! Resources: 0 added, 1 changed, 0 destroyed.

您可以登录[容器服务管理控制台](https://cs.console.aliyun.com)的节点池列表页面，查看到节点池中已成功扩容一个节点。

## 相关文档

- 

当您遇到由于网络延迟等原因造成的terraform init超时，导致无法正常下载Provider等情况时，请参见[Terraform Init 加速方案配置](https://help.aliyun.com/zh/terraform/terraform-init-acceleration-solution-configuration)。

- 

ROS提供了Terraform托管服务，因此您可以直接在[ROS](https://ros.console.aliyun.com/cn-hangzhou/welcome)[控制台](https://ros.console.aliyun.com/cn-hangzhou/welcome)部署Terraform模板。详细操作，请参见[创建](https://help.aliyun.com/zh/ros/user-guide/create-a-terraform-stack)[Terraform](https://help.aliyun.com/zh/ros/user-guide/create-a-terraform-stack)[类型资源栈](https://help.aliyun.com/zh/ros/user-guide/create-a-terraform-stack)。

[上一篇：通过Terraform创建ACK Edge集群](products/ack/documents/ack-edge/developer-reference/use-terraform-to-create-an-ack-edge-cluster.md)[下一篇：通过Terraform创建具备自动伸缩功能的节点池](products/ack/documents/ack-edge/developer-reference/use-terraform-to-create-an-auto-scaling-node-pool.md)

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
