# 使用Terraform部署ECS-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/developer-reference/terraform

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

# Terraform参考

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Terraform是一个开源的基础设施即代码工具，允许开发人员通过声明式的语言来定义和管理基础设施的配置，提供了一种简洁的方式来创建、修改或删除ECS资源，减少手动操作的繁琐和错误，提高基础设施的可管理性和可维护性。本文为您介绍如何安装与配置Terraform、使用Terraform创建ECS实例。

## Terraform基本功能

Terraform是IT基础架构自动化编排工具，可以用代码来管理维护IT资源。更多信息，请参见[Terraform](https://help.aliyun.com/zh/terraform/what-is-terraform#concept-vhk-wpc-rfb)[产品介绍](https://help.aliyun.com/zh/terraform/what-is-terraform#concept-vhk-wpc-rfb)。

- 

Terraform的命令行接口CLI（Command Line Interface）提供一种简单机制，用于将配置文件部署到阿里云或其他任意支持的云上，并对其进行版本控制。它编写了描述云资源拓扑的配置文件中的基础结构，例如虚拟机、存储账户和网络接口。

- 

Terraform通过Provider支持新的基础架构，让您在阿里云上能够轻松使用简单模板语言来定义、预览和部署云基础结构。

- 

Terraform可以创建、修改和删除多种阿里云产品的相关资源。

关于阿里云与Terraform集成的更多信息，请参见[Alibaba Cloud Provider](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs)。

## Terraform安装

## CloudShell

阿里云Cloud Shell是一款帮助您运维的免费产品，预装了Terraform的组件，您可直接在Cloud Shell中运行Terraform的命令。

首先，确保您有一个合法的、有相关权限的阿里云账号。

其次，打开浏览器，访问Cloud Shell的地址[https://shell.aliyun.com](https://shell.aliyun.com)。

登录成功后，执行如下指令

terraform

您将看到，Terraform组件已经内置在CloudShell中，并且可以直接使用。

更多Cloud Shell使用方式，请参见[使用云命令行](https://help.aliyun.com/zh/cloud-shell/using-the-cloud-command-line#task-1958468)。

## 手动安装

## 使用预编译包

登录[Terraform](https://www.terraform.io/downloads.html)[官网](https://www.terraform.io/downloads.html)，找到对应操作系统的zip包，并下载。

在下载完成后，请将程序包解压到/usr/local/bin。其余文件在复制完成后均可删除，这并不会影响Terraform正常运行。

最后，请确保Terraform目录在PATH变量中已完成定义，不同操作系统会有所不同。

## Windows

- 

进入控制面板 -> 系统 -> 系统设置 -> 环境变量。

- 

在系统变量中向下滚动，直到找到 PATH。

- 

单击编辑并进行相应更改。

- 

请务必在前一个末尾添加分号，因为这是分隔符，即 c:\path;c:\path2

- 

启动新控制台以使设置生效。

更多信息参见：[在](https://stackoverflow.com/questions/1618280/where-can-i-set-path-to-make-exe-on-windows)[Windows](https://stackoverflow.com/questions/1618280/where-can-i-set-path-to-make-exe-on-windows)[系统定义全局路径](https://stackoverflow.com/questions/1618280/where-can-i-set-path-to-make-exe-on-windows)。

## Mac或Linux

打印您的PATH配置

echo $PATH

将Terraform二进制文件移动到列出的位置之一。此命令假定二进制文件当前位于您的Downloads文件夹中并且您的PATH包含/usr/local/bin，但如果您的位置不同，您可以自定义命令中的目录。

mv ~/Downloads/terraform /usr/local/bin/

更多信息参见：

- 

[在](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)[Linux](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)[系统定义全局路径](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)。

- 

[在](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)[Mac](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)[系统定义全局路径](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)。

## 使用源

如果您期望从源代码编译二进制文件，可以克隆[HashiCorp Terraform](https://github.com/hashicorp/terraform)[代码库](https://github.com/hashicorp/terraform)

git clone https://github.com/hashicorp/terraform.git

您将会看到如下进度提示信息，并等待其执行完成。

执行完成后，您执行命令的目录下会新增一个terraform名称的目录。通过cd指令进入该目录。

cd terraform

然后，执行install 指令，这将会编译目录并将编译后的包移动到$GOPATH/bin/terraform目录中

go install

当您看到如下提示信息，则说明正在编译中。等待完成后即可进行下一步操作。

注意：如果提示zsh: command not found: go，则您需要先[安装](https://go.dev/doc/install)[go](https://go.dev/doc/install)[的环境](https://go.dev/doc/install)。

最终，确保terraform目录在PATH中定义并可用。 PATH定义取决于您所使用的操作系统。

## Mac或Linux

打印您的PATH配置

echo $PATH

将 Terraform 二进制文件移动到列出的位置之一。此命令假定二进制文件当前位于您的Downloads文件夹中并且您的PATH包含/usr/local/bin，但如果您的位置不同，您可以自定义命令中的目录。

mv ~/Downloads/terraform /usr/local/bin/

更多信息参见：

- 

[在](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)[Linux](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)[系统定义全局路径](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)。

- 

[在](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)[Mac](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)[系统定义全局路径](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)。

## Windows

- 

进入控制面板 -> 系统 -> 系统设置 -> 环境变量。

- 

在系统变量中向下滚动，直到找到 PATH。

- 

单击编辑并进行相应更改。

- 

请务必在前一个末尾添加分号，如：c:\path;c:\path2

- 

启动新控制台以使设置生效。

更多信息参见：[在](https://stackoverflow.com/questions/1618280/where-can-i-set-path-to-make-exe-on-windows)[Windows](https://stackoverflow.com/questions/1618280/where-can-i-set-path-to-make-exe-on-windows)[系统定义全局路径](https://stackoverflow.com/questions/1618280/where-can-i-set-path-to-make-exe-on-windows)。

## macOS Homebrew

[Homebrew](https://brew.sh/)是一款在Mac系统上经常使用的包安装工具。借助Homebrew可以通过简单的指令安装Terraform。

第一步，安装HashiCorp的tap，用来定义包在Homebrew的位置。

brew tap hashicorp/tap

第二步，执行安装指令，安装Terraform

brew install hashicorp/tap/terraform

重要

安装指令将索引最新的版本并进行安装，如果在安装一段时间后希望更新到最新版本。可以通过重新执行upgrade指令进行。

更新最新版本的Terraform，首先需要更新Homebrew。

brew update

然后，运行upgrade指令更新到最新版本。

brew upgrade hashicorp/tap/terraform

## Linux

## Alibaba Cloud Liunx

yum install -y dnf-plugin-releasever-adapter yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo yum install terraform

## Windows Chocolatey

[Chocolatey](https://chocolatey.org/)是一款在Mac系统上经常使用的包安装工具。借助[Chocolatey](https://chocolatey.org/)可以通过简单的指令安装Terraform。

choco install terraform

## Terraform 身份认证

基于环境变量配置身份认证是将访问凭证保存在特定的环境变量中，当执行Terraform命令时，如果配置模板中没有显式声明访问凭证，那么将尝试从如下的环境变量中获取。具体环境变量的设置方式如下：

## Windows

- 

在桌面右键单击此电脑，选择属性>高级系统设置>环境变量>系统变量/用户变量。

- 

在系统变量/用户变量中，单击新建，创建以下环境变量。

| 变量名 | 变量描述 | 变量值 |
| --- | --- | --- |
| ALICLOUD_ACCESS_KEY | Access Key Id | yourAccessKeyID |
| ALICLOUD_SECRET_KEY | Access Key Secret | yourAccessKeySecret |
| ALICLOUD_SECURITY_TOKEN（可选） | 如果是 STS 的访问凭证，此处需要配置 Security Token | yourSTSToken |


## Linux

重要

使用export命令配置的临时环境变量仅对当前会话有效，当会话退出之后所设置的环境变量将会丢失。如需长期保留环境变量，可将export命令配置到操作系统的启动配置文件中。

# Access Key Id $ export ALICLOUD_ACCESS_KEY="<你的 Access Key ID>" # Access Key Secret $ export ALICLOUD_SECRET_KEY="<你的 Access Key Secret>" # 如果是 STS 的访问凭证，此处需要配置 security_token $ export ALICLOUD_SECURITY_TOKEN="<你的访问 Token>"

设置了环境变量之后，provider块可以不在配置模板中显式声明或者只声明地域信息：

provider "alicloud" { region = "cn-hangzhou" }

当然，region也是支持通过环境变量ALICLOUD_REGION进行配置的。如果 region 没有显式声明也没有配置环境变量，cn-beijing将是其默认配置值。

## 支持的资源列表

说明

Resource：资源，指新创建的资源，用于定义基础设施组件，例如一个ECS实例、一个虚拟机、一个网络安全组等。

Resource

[alicloud_auto_provisioning_group](https://help.aliyun.com/zh/terraform/alicloud-auto-provisioning-group)：用于ECS的自动配置组资源，它利用抢占式实例和按量付费实例快速部署集群。

[alicloud_ecs_disk_attachment](https://help.aliyun.com/zh/terraform/alicloud-ecs-disk-attachment)：用于为ECS实例挂载数据盘或系统盘。

[alicloud_ecs_activation](https://help.aliyun.com/zh/terraform/alicloud-ecs-activation)：用于创建ECS激活码，允许用户配置描述、最大注册实例数、默认实例名称前缀、允许使用激活码的主机IP地址范围及激活码的有效期等参数，以批量注册受管实例。

[alicloud_ecs_auto_snapshot_policy](https://help.aliyun.com/zh/terraform/alicloud-ecs-auto-snapshot-policy)：用于创建ECS自动快照策略，允许用户配置自动创建快照的周期（如每周的哪几天）、一天中的哪些时间点创建快照、快照保留天数等参数，同时也支持跨区域复制快照及其加密设置。

[alicloud_ecs_auto_snapshot_policy_attachment](https://help.aliyun.com/zh/terraform/alicloud-ecs-auto-snapshot-policy-attachment)：用于将自动快照策略附加到指定的磁盘上，允许用户通过指定自动快照策略ID和磁盘ID来关联两者的配置，以实现对特定磁盘应用预设的自动快照策略。

[alicloud_ecs_capacity_reservation](https://help.aliyun.com/zh/terraform/alicloud-ecs-capacity-reservation)：用于在阿里云上创建容量预留，允许用户为特定实例类型预留资源，确保在需要时能够启动指定数量的实例。

[alicloud_ecs_command](https://help.aliyun.com/zh/terraform/alicloud-ecs-command)：资源用于在阿里云ECS实例上创建命令，允许用户通过指定命令内容（Base64编码）、描述、是否启用自定义参数、命令名称、超时时间及命令类型等参数来执行预设的脚本命令。

[alicloud_ecs_dedicated_host](https://help.aliyun.com/zh/terraform/alicloud-ecs-dedicated-host)：用于在阿里云上创建专用主机，并允许用户配置如主机类型、计费方式、自动续费周期、主机名称及描述等参数。

[alicloud_ecs_dedicated_host_cluster](https://help.aliyun.com/zh/terraform/alicloud-ecs-dedicated-host-cluster)：用于在阿里云上创建专用主机集群，允许用户配置如集群名称、描述、所属可用区及标签等参数，以集中管理和组织专用主机资源。

[alicloud_ecs_deployment_set](https://help.aliyun.com/zh/terraform/alicloud-ecs-deployment-set)：用于在阿里云上创建部署集，允许用户通过指定部署策略、部署集名称和描述等参数来管理和组织ECS实例的分布，以实现高可用性或低延迟等特定部署目标。

[alicloud_ecs_disk](https://help.aliyun.com/zh/terraform/alicloud-ecs-disk)：用于在阿里云上创建云盘（数据盘），允许用户配置如磁盘类型、大小、是否加密、快照ID、性能级别及标签等参数，以满足不同应用场景下的存储需求。

[alicloud_ecs_disk_attachment](https://help.aliyun.com/zh/terraform/alicloud-ecs-disk-attachment)：用于在阿里云上实现ECS实例与磁盘的挂载和卸载操作，允许用户通过指定实例ID和磁盘ID来关联两者，支持设置是否随实例释放磁盘以及是否作为系统盘挂载等选项。

[alicloud_ecs_elasticity_assurance](https://help.aliyun.com/zh/terraform/alicloud-ecs-elasticity-assurance)：资源用于在阿里云上创建弹性保障，以确保在特定区域中为指定的实例类型预留一定的计算资源容量。

[alicloud_ecs_hpc_cluster](https://help.aliyun.com/zh/terraform/alicloud-ecs-hpc-cluster)：用于在阿里云上创建高性能计算（HPC）集群，允许用户通过指定HPC集群的名称和描述来配置集群的基础信息。

[alicloud_ecs_image_component](https://help.aliyun.com/zh/terraform/alicloud-ecs-image-component)：用于在阿里云上创建镜像组件，允许用户定义构建或测试组件的内容、类型、适用的操作系统及其他元数据，以便在创建自定义镜像时复用这些组件。

[alicloud_ecs_image_pipeline](https://help.aliyun.com/zh/terraform/alicloud-ecs-image-pipeline)：用于在阿里云上创建镜像管道，允许用户通过指定基础镜像、构建内容、实例类型及其他相关配置来自动化地创建和管理自定义镜像。

[alicloud_ecs_image_pipeline_execution](https://help.aliyun.com/zh/terraform/alicloud-ecs-image-pipeline-execution)：用于执行阿里云上的镜像管道任务，即根据已定义的镜像管道来创建自定义镜像。它通过指定镜像管道ID来触发镜像构建任务，并允许用户监控任务状态和结果。

[alicloud_ecs_invocation](https://help.aliyun.com/zh/terraform/alicloud-ecs-invocation)：用于管理和执行 ECS 实例上的命令调用（Invocation）。它允许用户在一台或多台 ECS 实例上运行指定的命令，并获取执行结果。

[alicloud_ecs_key_pair](https://help.aliyun.com/zh/terraform/alicloud-ecs-key-pair)：用于管理和创建 ECS 实例的密钥对（Key Pair）。

[alicloud_ecs_key_pair_attachment](https://help.aliyun.com/zh/terraform/alicloud-ecs-key-pair-attachment)：用于将创建的 ECS 密钥对绑定到指定的 ECS 实例。

[alicloud_ecs_launch_template](https://help.aliyun.com/zh/terraform/alicloud-ecs-launch-template)：用于管理 ECS 启动模板的资源，帮助用户通过预定义的配置快速创建和部署 ECS 实例，提升效率并确保一致性。

[alicloud_ecs_network_interface](https://help.aliyun.com/zh/terraform/alicloud-ecs-network-interface)：用于管理 ECS 网络接口的资源，帮助用户配置和管理实例的网络连接，支持灵活的私有 IP 分配策略，适用于复杂的网络环境和高可用架构设计。

[alicloud_ecs_network_interface_attachment](https://help.aliyun.com/zh/terraform/alicloud-ecs-network-interface-attachment)：允许用户将弹性网卡（ENI）附加到阿里云的ECS实例上，以灵活扩展实例的网络功能，如增加多个IP地址或实现更复杂的网络配置。

[alicloud_ecs_network_interface_permission](https://help.aliyun.com/zh/terraform/alicloud-ecs-network-interface-permission)：提供了一个ECS网络接口权限资源。

[alicloud_ecs_prefix_list](https://help.aliyun.com/zh/terraform/alicloud-ecs-prefix-list)：用于在阿里云ECS服务中创建和管理前缀列表的资源。

[alicloud_ecs_session_manager_status](https://help.aliyun.com/zh/terraform/alicloud-ecs-session-manager-status)：用于在阿里云ECS服务中管理和配置会话管理器状态的资源，允许用户启用或禁用会话管理功能，以控制对ECS实例的访问和管理方式。

[alicloud_ecs_snapshot](https://help.aliyun.com/zh/terraform/alicloud-ecs-snapshot)：个用于在阿里云中创建磁盘快照的资源，允许用户备份指定磁盘的数据以便日后恢复或存档。

[alicloud_ecs_snapshot_group](https://help.aliyun.com/zh/terraform/alicloud-ecs-snapshot-group)：用于在阿里云中为一组磁盘创建快照的资源。

[alicloud_ecs_storage_capacity_unit](https://help.aliyun.com/zh/terraform/alicloud-ecs-storage-capacity-unit)：用于在阿里云ECS服务中创建和管理存储容量单元的资源。

[alicloud_image](https://help.aliyun.com/zh/terraform/alicloud-image)：用于在阿里云上基于现有ECS实例创建自定义镜像的资源。

[alicloud_image_copy](https://help.aliyun.com/zh/terraform/alicloud-image-copy)：用于将自定义镜像从一个地域复制到另一个地域。

[alicloud_image_export](https://help.aliyun.com/zh/terraform/alicloud-image-export)： 用于将自定义镜像导出到与该自定义镜像同一地域的OSS存储桶中。

[alicloud_image_import](https://help.aliyun.com/zh/terraform/alicloud-image-import)： 用于提供ECS镜像导入功能。

[alicloud_image_share_permission](https://help.aliyun.com/zh/terraform/alicloud-image-share-permission)：用于管理镜像共享权限。

[alicloud_instance](https://help.aliyun.com/zh/terraform/alicloud-instance)：用于提供ECS实例资源

[alicloud_ecs_key_pair](https://help.aliyun.com/zh/terraform/alicloud-ecs-key-pair)：用于提供ECS密钥对资源。

[alicloud_ecs_key_pair_attachment](https://help.aliyun.com/zh/terraform/alicloud-ecs-key-pair-attachment)：用于将密钥对绑定到多个ECS实例。

[alicloud_ecs_launch_template](https://help.aliyun.com/zh/terraform/alicloud-ecs-launch-template)：用于提供ECS启动模板资源。

[alicloud_ecs_network_interface](https://help.aliyun.com/zh/terraform/alicloud-ecs-network-interface)：用于提供ECS网络接口资源。

[alicloud_ecs_network_interface_attachment](https://help.aliyun.com/zh/terraform/alicloud-ecs-network-interface-attachment)：用于提供ECS网络接口附加资源。

[alicloud_ram_role_attachment](https://help.aliyun.com/zh/terraform/alicloud-ram-role-attachment)：用于为多个ECS实例绑定RAM角色。

[alicloud_reserved_instance](https://help.aliyun.com/zh/terraform/alicloud-reserved-instance)：用于提供预留实例券资源。

[alicloud_security_group](https://help.aliyun.com/zh/terraform/alicloud-security-group)： 用于提供ECS安全组资源。

[alicloud_security_group_rule](https://help.aliyun.com/zh/terraform/alicloud-security-group-rule)：用于提供安全组规则资源。

[alicloud_ecs_snapshot](https://help.aliyun.com/zh/terraform/alicloud-ecs-snapshot)：用于提供ECS快照资源。

[alicloud_ecs_auto_snapshot_policy](https://help.aliyun.com/zh/terraform/alicloud-ecs-auto-snapshot-policy)：用于提供ECS自动快照策略资源。

## 使用Terraform创建并管理ECS

下文以创建ECS为例，介绍如何使用Terraform创建并管理ECS资源。

- 

创建一个工作目录，并在该工作目录中创建名为main.tf的配置文件。以下代码将创建一个ECS实例，以及创建ECS实例所需的VPC、安全组与交换机资源。将以下代码复制到main.tf中。

# 定义一个变量region，默认值为"cn-beijing"，用于指定阿里云区域 variable "region"{ default = "cn-beijing" } # 配置阿里云provider，使用变量region中定义的区域 provider "alicloud"{ region = var.region } # 定义一个字符串类型的变量instance_type，默认值为"ecs.e-c1m1.large"，用于指定ECS实例类型 variable "instance_type" { type = string default = "ecs.e-c1m1.large" } # 使用数据源查询可用区信息，通过指定的实例类型、资源创建类型（如VSwitch）以及磁盘种类来过滤结果 data "alicloud_zones" "default" { available_instance_type = var.instance_type available_resource_creation = "VSwitch" available_disk_category = "cloud_essd" } # 定义一个变量vpc_cidr_block，默认值为"172.16.0.0/16"，用于指定VPC的CIDR块 variable "vpc_cidr_block" { default = "172.16.0.0/16" } # 定义一个变量vsw_cidr_block，默认值为"172.16.0.0/24"，用于指定VSwitch的CIDR块 variable "vsw_cidr_block" { default = "172.16.0.0/24" } # 生成一个介于10000到99999之间的随机整数，用于确保某些资源名称的唯一性 resource "random_integer" "default" { min = 10000 max = 99999 } # 创建名为vpc-test的VPC，并使用随机整数确保名称唯一性 resource "alicloud_vpc" "vpc" { vpc_name = "vpc-test_${random_integer.default.result}" cidr_block = var.vpc_cidr_block } # 创建安全组，名称包含随机整数以保证唯一性，并关联至上述VPC resource "alicloud_security_group" "group" { security_group_name = "test_${random_integer.default.result}" # 替换了这里的字段名 vpc_id = alicloud_vpc.vpc.id } # 创建一条允许所有TCP流量进入的安全组规则，与之前创建的安全组关联 resource "alicloud_security_group_rule" "allow_all_tcp" { type = "ingress" ip_protocol = "tcp" nic_type = "intranet" # 修改了这里，将nic_type改为'intranet' policy = "accept" port_range = "1/65535" priority = 1 security_group_id = alicloud_security_group.group.id cidr_ip = "0.0.0.0/0" } # 创建VSwitch，名称中包含随机整数以确保唯一性，并与VPC、可用区关联 resource "alicloud_vswitch" "vswitch" { vpc_id = alicloud_vpc.vpc.id cidr_block = var.vsw_cidr_block zone_id = data.alicloud_zones.default.zones[0].id vswitch_name = "vswitch-test-${random_integer.default.result}" } # 创建ECS实例，设置多个参数如可用区、安全组、实例类型等，并使用随机整数保证实例名称的唯一性 resource "alicloud_instance" "instance" { availability_zone = data.alicloud_zones.default.zones[0].id security_groups = [alicloud_security_group.group.id] instance_type = var.instance_type system_disk_category = "cloud_essd" system_disk_name = "test_foo_system_disk_${random_integer.default.result}" system_disk_description = "test_foo_system_disk_description" image_id = "aliyun_2_1903_x64_20G_alibase_20240628.vhd" instance_name = "test_ecs_${random_integer.default.result}" vswitch_id = alicloud_vswitch.vswitch.id internet_max_bandwidth_out = 10 password = "Terraform@Example" # 用户根据自己实际情况修改 }

- 

执行如下命令，初始化Terraform运行环境。

terraform init

返回信息如下，则Terraform初始化成功。

Terraform has been successfully initialized! You may now begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All Terraform commands should now work. If you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forget, other commands will detect it and remind you to do so if necessary.

- 

执行如下命令，开始执行代码。

terraform apply

在执行过程中，根据提示输入yes并按下Enter键，等待命令执行完成，若出现以下信息，则表示代码执行成功。

You can apply this plan to save these new output values to the Terraform state, without changing any real infrastructure. Do you want to perform these actions? Terraform will perform the actions described above. Only 'yes' will be accepted to approve. Enter a value: yes Apply complete! Resources: 6 added, 0 changed, 0 destroyed.

- 

结果验证

## 执行terraform show命令

您可以在工作目录中，使用以下命令查询Terraform已创建资源的详细信息：

terraform show

## 登录控制台查看

登录[云服务器管理控制台](https://ecs.console.aliyun.com/server/region/cn-shanghai?instanceName=test_ecs_64914&page=1#/)，进入实例与镜像>实例页面，左上角选择地区，此例中选择华北2（北京），查看已创建的ECS实例。

## 相关文档

- 

更多实践教程，请参见[Terraform](https://help.aliyun.com/zh/terraform/terraform-tutorials)[的教程](https://help.aliyun.com/zh/terraform/terraform-tutorials)。

- 

更多Terraform的常用命令，请参见[Terraform](https://help.aliyun.com/zh/terraform/terraform-common-commands)[常用命令](https://help.aliyun.com/zh/terraform/terraform-common-commands)。

- 

当您遇到由于网络延迟等原因造成的 terraform init 超时，导致无法正常下载 Provider 等情况时，请参见[Terraform Init 加速方案配置](https://help.aliyun.com/zh/terraform/terraform-init-acceleration-solution-configuration)。

- 

ROS提供了Terraform托管服务，因此您可以直接在[ROS](https://ros.console.aliyun.com/cn-hangzhou/welcome)[控制台](https://ros.console.aliyun.com/cn-hangzhou/welcome)部署Terraform模板。详细操作，请参见[创建](https://help.aliyun.com/zh/ros/user-guide/create-a-terraform-stack)[Terraform](https://help.aliyun.com/zh/ros/user-guide/create-a-terraform-stack)[类型资源栈](https://help.aliyun.com/zh/ros/user-guide/create-a-terraform-stack)。

[上一篇：通过CLI创建并使用ECS实例](products/ecs/documents/developer-reference/cli-reference.md)[下一篇：通过Terraform创建并使用ECS实例](products/ecs/documents/developer-reference/create-and-use-an-ecs-instance-by-using-terraform.md)

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
