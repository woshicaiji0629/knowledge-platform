# 使用Terraform创建ecs-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/developer-reference/create-and-use-an-ecs-instance-by-using-terraform

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 通过Terraform创建并使用ECS实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Terraform是一款IaC工具（Infrastructure as Code），旨在帮助开发人员和运维团队自动化基础设施的创建、部署和管理。您可以通过编写简洁的代码来定义和配置云端基础设施，而不必手动操作和配置。本文为您介绍如何通过Terraform创建ECS实例。

说明

如需了解更多Terraform相关内容，请参见[了解阿里云](https://help.aliyun.com/zh/terraform/what-is-terraform)[Terraform](https://help.aliyun.com/zh/terraform/what-is-terraform)。

## 准备工作

### 1. 安装Terraform

本文以在Linux或Windows系统中使用程序包安装Terraform为例，更多安装方式，请参见[Terraform 安装](https://help.aliyun.com/zh/terraform/terraform-installation)。

说明

阿里云提供了两种Terraform在线环境，无需手动安装Terraform即可实现对Terraform命令的执行：

- 

Terraform Explorer：点击[一键运行](https://api.aliyun.com/terraform?resource=alicloud_instance&exampleId=&activeTab=example&provider=1.238.0&product=ECS&example=201-use-case-create-ecs-instance-quickstart)，自动运行本文所提供的Terraform代码。

- 

Cloud Shell：复制本文所提供的代码，在[使用](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)[Terraform](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)[快速创建资源](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)中直接执行Terraform命令。

- 

进入[Terraform](https://www.terraform.io/downloads.html)[官网](https://www.terraform.io/downloads.html)下载适用于您的操作系统的程序包。

- 

配置Terraform运行环境。

## Linux

执行以下命令将程序包解压到/usr/local/bin。

# 将{your_zip_path}替换为程序包所在路径，若系统不支持unzip命令，请先安装。 sudo unzip {your_zip_path} -d /usr/local/bin

## Windows

- 

解压程序包，例如解压后的目录为D:\tool\terraform。

- 

在桌面右键单击此电脑，选择属性>高级系统设置>环境变量>系统变量/用户变量。

- 

在系统变量/用户变量中单击Path，选择编辑 > 新建，输入Terraform的解压目录（如D:\tool\terraform），单击确定完成配置。

- 

运行terraform验证路径配置。

terraform

命令运行后将显示可用的Terraform选项的列表，如下所示，表示安装完成。

➜ ~ terraform Usage: terraform [global options] <subcommand> [args] The available commands for execution are listed below. The primary workflow commands are given first, followed by less common or more advanced commands. Main commands: init Prepare your working directory for other commands validate Check whether the configuration is valid plan Show changes required by the current configuration apply Create or update infrastructure destroy Destroy previously-created infrastructure All other commands: console Try Terraform expressions at an interactive command prompt fmt Reformat your configuration in the standard style force-unlock Release a stuck lock on the current workspace get Install or upgrade remote Terraform modules graph Generate a Graphviz graph of the steps in an operation import Associate existing infrastructure with a Terraform resource login Obtain and save credentials for a remote host logout Remove locally-stored credentials for a remote host metadata Metadata related commands output Show output values from your root module providers Show the providers required for this configuration refresh Update the state to match remote systems show Inspect Terraform state or plan state Advanced state management taint Mark a resource instance as not fully functional test Execute integration tests for Terraform modules untaint Remove the 'tainted' state from a resource instance version Show the current Terraform version workspace Workspace management Global options (use these before the subcommand, if any): -chdir=DIR Switch to a different working directory before executing the given subcommand. -help Show this message, or the help for a given subcommand. -version An alias for the "version" subcommand. show Show the current state or a saved plan state Advanced state management taint Mark a resource instance as not fully functional test Experimental support for module integration testing untaint Remove the 'tainted' state from a resource instance version Show the current Terraform version workspace Workspace management Global options (use these before the subcommand, if any): -chdir=DIR Switch to a different working directory before executing the given subcommand. -help Show this help output, or the help for a specified subcommand. -version An alias for the "version" subcommand.

### 2. 配置Terraform身份认证

Terraform身份认证是指在通过Terraform操作阿里云基础设施之前，对阿里云Terraform Provider进行身份验证。只有在身份认证成功后，才能与阿里云API进行通信，并创建和管理阿里云的基础设施资源。阿里云Terraform Provider提供多种身份认证方式，有关更多身份认证信息，请参见相关文档[Terraform 身份认证](https://help.aliyun.com/zh/terraform/terraform-authentication)。

说明

您如果使用Terraform Explorer或者Cloud Shell，则无需手动配置身份认证信息，只需确保所登录的账号具有操作VPC和ECS的权限即可。

本文以在环境变量中使用RAM用户AccessKey配置身份认证为例：

- 

由于阿里云账号（主账号）拥有资源的所有权限，其AccessKey一旦泄露风险巨大，所以建议您使用RAM用户的AccessKey。如何创建RAM用户的AccessKey，请参见[创建](products/ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](products/ram/documents/user-guide/create-an-accesskey-pair.md)。

- 

在为RAM用户授予操作云服务器ECS及专有网络VPC相关资源的权限时，建议所授予的权限应遵循最小权限原则。有关如何为RAM用户进行授权的详细信息，请参见[管理](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。本文提供的示例代码需要创建ECS、VPC、交换机等资源，为便于执行本文中的示例，您可以为授予RAM用户以下权限：

| 云产品 | 授予权限 |
| --- | --- |
| 专有网络 VPC | 本示例选择系统策略：AliyunVPCFullAccess |
| 云服务器 ECS | 本示例选择系统策略：AliyunECSFullAccess |


- 

创建环境变量，存放身份认证信息。

## Linux

重要

使用export命令配置的临时环境变量仅对当前会话有效，当会话退出之后所设置的环境变量将会丢失。若需长期保留环境变量，可将export命令配置到对应操作系统的启动配置文件中。

# AccessKey Id export ALICLOUD_ACCESS_KEY="yourAccessKeyID" # AccessKey Secret export ALICLOUD_SECRET_KEY="yourAccessKeySecret" # 资源将要部署的地域 export ALICLOUD_REGION="cn-beijing"

## Windows

- 

在桌面右键单击此电脑，选择属性>高级系统设置>环境变量>系统变量/用户变量。

- 

在系统变量/用户变量中，单击新建，创建以下环境变量。

| 变量名 | 变量描述 | 变量值 |
| --- | --- | --- |
| ALICLOUD_ACCESS_KEY | AccessKey Id | yourAccessKeyID |
| ALICLOUD_SECRET_KEY | AccessKey Secret | yourAccessKeySecret |
| ALICLOUD_REGION | 资源将要部署的地域 | 示例：cn-beijing |


## 涉及的Terraform资源

本文所提供的示例代码中，所涉及到的Terraform资源信息。

说明

本教程示例包含的部分资源会产生一定费用，请在不需要时及时进行释放或退订。

Resource

- 

[alicloud_vpc](https://help.aliyun.com/zh/terraform/alicloud-vpc)：创建专有网络VPC。

- 

[alicloud_vswitch](https://help.aliyun.com/zh/terraform/alicloud-vswitch)：创建vSwitch。

- 

[alicloud_security_group](https://help.aliyun.com/zh/terraform/alicloud-security-group)：创建安全组。

- 

[alicloud_security_group_rule](https://help.aliyun.com/zh/terraform/alicloud-security-group-rule)：创建安全组规则。

- 

[alicloud_instance](https://help.aliyun.com/zh/terraform/alicloud-instance)：创建ECS实例。

Data Source

[alicloud_zones](https://help.aliyun.com/zh/terraform/alicloud-zones)：动态查询可以创建特定实例规格的可用区。

## 编写Terraform配置文件

在main.tf中定义创建ECS所需的基础设施资源，例如ECS、VPC等。您可以直接复制下方[完整示例](products/ecs/documents/developer-reference/create-and-use-an-ecs-instance-by-using-terraform.md)中的代码到配置文件中

- 

创建配置文件。

Terraform的基础设施资源是在配置文件中进行定义的，因此必须首先创建一个配置文件。

## Linux

# 创建工作目录 mkdir terraform-projects && cd terraform-projects mkdir ecs-quickstart && cd ecs-quickstart # 创建配置文件并编辑 touch main.tf && vim main.tf

## Windows

创建一个新的文件夹，例如命名为ecs-quickstart，并在该文件夹内创建一个Terraform配置文件，例如配置文件名称为main.tf。

- 

定义Provider配置。

配置阿里云资源部署的地域。

# 资源所在的地域 variable "region" { default = "cn-chengdu" } provider "alicloud" { region = var.region }

- 

定义专有网络VPC及其子网。

VPC是一种专有的云上私有网络，允许用户在公共云上配置和管理一个逻辑隔离的网络区域。

variable "instance_name" { default = "tf-sample" } # ecs实例规格 variable "instance_type" { default = "ecs.e-c1m2.large" } # 查询满足条件的可用区 data "alicloud_zones" "default" { available_disk_category = "cloud_essd" available_resource_creation = "VSwitch" available_instance_type = var.instance_type } # 创建VPC resource "alicloud_vpc" "vpc" { vpc_name = var.instance_name cidr_block = "172.16.0.0/12" } # 创建交换机 resource "alicloud_vswitch" "vsw" { vpc_id = alicloud_vpc.vpc.id cidr_block = "172.16.0.0/21" zone_id = data.alicloud_zones.default.zones.0.id }

- 

定义安全组。

安全组是一种虚拟防火墙，能够控制ECS实例的出入方向流量。

# 创建安全组 resource "alicloud_security_group" "default" { name = var.instance_name vpc_id = alicloud_vpc.vpc.id } # 为安全组入方向添加规则 resource "alicloud_security_group_rule" "allow_tcp_22" { type = "ingress" ip_protocol = "tcp" nic_type = "intranet" policy = "accept" port_range = "22/22" priority = 1 security_group_id = alicloud_security_group.default.id cidr_ip = "0.0.0.0/0" }

- 

定义ECS实例。

使用ECS，您可以快速部署和运行应用程序，灵活调整资源以应对业务变化，同时享受高性能、高安全性和低成本的计算能力，适用于网站托管、应用开发、数据处理等多种场景。

# ecs实例镜像ID variable "image_id" { default = "ubuntu_18_04_64_20G_alibase_20190624.vhd" } # ecs实例公网带宽 variable "internet_bandwidth" { default = "10" } # ecs实例登录密码 variable "password" { default = "Test@12345" } # 指定创建ECS的数量，默认值是 1 variable "ecs_count" { default = 1 } # 创建ECS实例 resource "alicloud_instance" "instance" { count = var.ecs_count availability_zone = data.alicloud_zones.default.zones.0.id security_groups = alicloud_security_group.default.*.id password = var.password instance_type = var.instance_type system_disk_category = "cloud_essd" image_id = var.image_id instance_name = var.instance_name vswitch_id = alicloud_vswitch.vsw.id internet_max_bandwidth_out = var.internet_bandwidth } output "public_ip" { value = alicloud_instance.instance.*.public_ip }

### 完整示例

说明

当前示例代码支持一键运行，您可以直接运行代码。[一键运行](https://api.aliyun.com/terraform?resource=alicloud_instance&exampleId=&activeTab=example&provider=1.238.0&product=ECS&example=201-use-case-create-ecs-instance-quickstart)

variable "region" { default = "cn-chengdu" } provider "alicloud" { region = var.region } variable "instance_name" { default = "tf-sample" } variable "instance_type" { default = "ecs.e-c1m2.large" } data "alicloud_zones" "default" { available_disk_category = "cloud_essd" available_resource_creation = "VSwitch" available_instance_type = var.instance_type } resource "alicloud_vpc" "vpc" { vpc_name = var.instance_name cidr_block = "172.16.0.0/12" } resource "alicloud_vswitch" "vsw" { vpc_id = alicloud_vpc.vpc.id cidr_block = "172.16.0.0/21" zone_id = data.alicloud_zones.default.zones.0.id } resource "alicloud_security_group" "default" { name = var.instance_name vpc_id = alicloud_vpc.vpc.id } resource "alicloud_security_group_rule" "allow_tcp_22" { type = "ingress" ip_protocol = "tcp" nic_type = "intranet" policy = "accept" port_range = "22/22" priority = 1 security_group_id = alicloud_security_group.default.id cidr_ip = "0.0.0.0/0" } variable "image_id" { default = "ubuntu_18_04_64_20G_alibase_20190624.vhd" } variable "internet_bandwidth" { default = "10" } variable "password" { default = "Test@12345" } variable "ecs_count" { default = 1 } resource "alicloud_instance" "instance" { count = var.ecs_count availability_zone = data.alicloud_zones.default.zones.0.id security_groups = alicloud_security_group.default.*.id password = var.password instance_type = var.instance_type system_disk_category = "cloud_essd" image_id = var.image_id instance_name = var.instance_name vswitch_id = alicloud_vswitch.vsw.id internet_max_bandwidth_out = var.internet_bandwidth } output "public_ip" { value = [for i in range(var.ecs_count) : alicloud_instance.instance[i].public_ip] }

## 运行Terraform命令创建资源

在完成Terraform配置文件编写后，运行Terraform命令来完成ECS实例的自动创建。

### 1. 初始化Terraform

terraform init命令用于下载并安装阿里云提供商的插件到当前文件夹中，同时还会生成各类记录文件。

## Linux

terraform init

## Windows

打开命令提示符cmd，在cmd中切换到Terraform配置文件所在文件夹，然后执行terraform init命令进行初始化。

# 例如配置文件路径 D:/ecs-quickstart # 切换到 D盘 d: # 切换到配置文件所在文件夹路径的命令，ecs-quickstart是配置文件所在文件夹路径，您可根据实际路径替换。 cd ecs-quickstart # 执行初始化命令 terraform init

说明

当您因网络延迟等原因导致terraform init超时，无法正常下载Provider等情况时，可通过配置阿里云镜像站解决，具体操作步骤，请参见[Terraform Init 加速方案配置](https://help.aliyun.com/zh/terraform/terraform-init-acceleration-solution-configuration)。

如下所示的信息表示初始化成功。

Terraform has been successfully initialized! You may now begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All Terraform commands should now work. If you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forget, other commands will detect it and remind you to do so if necessary.

### 2. 预览Terraform代码

运行terraform plan实现如下功能：

- 

验证main.tf中Terraform代码的语法是否正确。

- 

显示当前Terraform代码将要创建的资源的预览结果。

terraform plan

如果显示如下所示的信息表示Terraform文件无语法错误，可以执行terraform apply命令创建资源。若出现其他报错提示，请根据提示修改Terraform配置文件。

... Plan: 5 to add, 0 to change, 0 to destroy.

### 3. 执行Terraform代码

运行terraform apply以完成ECS实例及其依赖资源的自动创建和Python的自动安装。在创建过程中，需要按照提示输入yes，以允许Terraform创建所有定义的资源。

terraform apply

如下所示的信息表示ECS及所依赖资源均已创建成功。

... Do you want to perform these actions? Terraform will perform the actions described above. Only 'yes' will be accepted to approve. Enter a value: yes alicloud_vpc.vpc: Creating... alicloud_vpc.vpc: Creation complete after 6s [id=vpc-2vcsghlpznz74XXXXXXXX] alicloud_security_group.default: Creating... alicloud_vswitch.vsw: Creating... alicloud_security_group.default: Creation complete after 1s [id=sg-2vcdz6b8h9c3XXXXXXXX] alicloud_security_group_rule.allow_tcp_22: Creating... alicloud_security_group_rule.allow_tcp_22: Creation complete after 0s [id=sg-2vcdz6b8h9c3XXXXXXXX:ingress:tcp:22/22:intranet:0.0.0.0/0:accept:1] alicloud_vswitch.vsw: Creation complete after 4s [id=vsw-2vc50dknug30bXXXXXXXX] alicloud_instance.instance: Creating... alicloud_instance.instance: Still creating... [10s elapsed] alicloud_instance.instance: Creation complete after 15s [id=i-2vc3rf151bwcXXXXXXXX] Apply complete! Resources: 5 added, 0 changed, 0 destroyed. Outputs: public_ip = [ "4XX.XXX.XXX.XX7", ]

## 连接ECS实例

当ECS实例成功创建后，您可以通过SSH协议远程登录到指定公网IP的ECS。更多远程连接方式，请参见[连接方式概述](products/ecs/documents/user-guide/connect-to-instance.md)。

ssh <用户名>@<公网IP>

## 查看结果

## 使用Terraform命令

您可以通过以下命令查看已创建的ECS实例信息。

# 命令格式：terraform state show <资源类型>.<资源别名>[索引] terraform state show alicloud_instance.instance[0]

## 登录控制台查看

您可以登录[ECS](https://ecs.console.aliyun.com)[管理控制台](https://ecs.console.aliyun.com)查看已创建的ECS实例。执行Terraform代码后，在ECS控制台的实例列表中，名为tf-sample的实例已创建并处于运行中状态。该实例可用区为西南1（成都）A，实例规格为ecs.e-c1m2.large（2核 4 GiB），私网IP为172.16.0.100，付费方式为按量付费，网络类型为专有网络。

## 资源变更

当您需要调整配置时，可以通过直接修改配置文件中的资源定义来实现，例如添加新的安全组入方向的放行规则。

- 

若您希望在安全组入方向规则中添加443端口的放行规则，您可以在配置文件中添加以下代码。

resource "alicloud_security_group_rule" "allow_tcp_443" { type = "ingress" ip_protocol = "tcp" nic_type = "intranet" policy = "accept" port_range = "443/443" priority = 1 security_group_id = alicloud_security_group.default.id cidr_ip = "0.0.0.0/0" }

- 

执行terraform plan命令预览所做的变更。如下所示的信息表示将要为安全组ID是sg-2vcdz6b8h9c3XXXXXXXX的安全组增加一条安全组规则。

... Terraform will perform the following actions: # alicloud_security_group_rule.allow_tcp_443 will be created + resource "alicloud_security_group_rule" "allow_tcp_443" { + cidr_ip = "0.0.0.0/0" + id = (known after apply) + ip_protocol = "tcp" + nic_type = "intranet" + policy = "accept" + port_range = "443/443" + prefix_list_id = (known after apply) + priority = 1 + security_group_id = "sg-2vcdz6b8h9c3XXXXXXXX" + type = "ingress" } Plan: 1 to add, 0 to change, 0 to destroy.

- 

如果变更符合预期，执行terraform apply命令将变更应用到您的基础设施。在执行该命令时，Terraform将要求您确认是否进行变更，请键入yes并按回车键确认。如下所示的信息表示已为安全组ID是sg-2vcdz6b8h9c3XXXXXXXX的安全组新增规则成功。

... Do you want to perform these actions? Terraform will perform the actions described above. Only 'yes' will be accepted to approve. Enter a value: yes alicloud_security_group_rule.allow_tcp_443: Creating... alicloud_security_group_rule.allow_tcp_443: Creation complete after 0s [id=sg-2vcdz6b8h9c3XXXXXXXX:ingress:tcp:443/443:intranet:0.0.0.0/0:accept:1] Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

## 释放资源

当您不再需要上述通过Terraform创建或管理的资源时，运行下面的命令释放资源。

terraform destroy

显示如下信息，表示资源释放完成。

... Do you really want to destroy all resources? Terraform will destroy all your managed infrastructure, as shown above. There is no undo. Only 'yes' will be accepted to confirm. Enter a value: yes alicloud_security_group_rule.allow_tcp_443: Destroying... [id=sg-2vcdz6b8h9c3XXXXXXXX:ingress:tcp:443/443:intranet:0.0.0.0/0:accept:1] alicloud_security_group_rule.allow_tcp_22: Destroying... [id=sg-2vcdz6b8h9c3XXXXXXXX:ingress:tcp:22/22:intranet:0.0.0.0/0:accept:1] alicloud_instance.instance: Destroying... [id=i-2vc3rf151bwcXXXXXXXX] alicloud_security_group_rule.allow_tcp_22: Destruction complete after 0s alicloud_security_group_rule.allow_tcp_443: Destruction complete after 0s alicloud_instance.instance: Still destroying... [id=i-2vc3rf151bwcXXXXXXXX, 10s elapsed] alicloud_instance.instance: Destruction complete after 10s alicloud_security_group.default: Destroying... [id=sg-2vcdz6b8h9c3XXXXXXXX] alicloud_vswitch.vsw: Destroying... [id=vsw-2vc50dknug30bXXXXXXXX] alicloud_security_group.default: Destruction complete after 1s alicloud_vswitch.vsw: Destruction complete after 8s alicloud_vpc.vpc: Destroying... [id=vpc-2vcsghlpznz74XXXXXXXX] alicloud_vpc.vpc: Destruction complete after 6s Destroy complete! Resources: 6 destroyed.

## 相关文档

- 

ECS支持的Resource和Data Source请参考[支持的资源列表](products/ecs/documents/developer-reference/terraform.md)。

- 

在[Terraform Explorer](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)中使用Terraform，无需安装和配置Terraform即可对Terraform代码进行调试。

- 

在[使用](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)[Terraform](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)[快速创建资源](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)中使用Terraform，无需安装和配置Terraform即可手动执行Terraform命令。

[上一篇：Terraform参考](products/ecs/documents/developer-reference/terraform.md)[下一篇：通过Terraform为弹性网卡绑定EIP](products/ecs/documents/developer-reference/bind-an-eip-to-an-eni-using-terraform.md)

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
