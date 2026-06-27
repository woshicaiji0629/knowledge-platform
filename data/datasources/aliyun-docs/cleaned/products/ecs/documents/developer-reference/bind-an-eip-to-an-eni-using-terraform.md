# Terraform绑定EIP至辅助弹性网卡-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/developer-reference/bind-an-eip-to-an-eni-using-terraform

# 通过Terraform为弹性网卡绑定EIP
弹性公网IP（Elastic IP Address）是可以独立购买和持有的公网IP地址资源，当EIP和云资源绑定后，云资源可以通过EIP与公网通信。例如在单个ECS实例上托管多个应用时，可以通过为每个应用分配独立的辅助弹性网卡并绑定独立的弹性公网IP（EIP），实现每个应用对外呈现一个独立的公网IP地址。本文将为您介绍如何为辅助弹性网卡绑定弹性公网IP。
说明
本教程所含示例代码支持一键运行，您可以直接运行代码。[一键运行](https://api.aliyun.com/terraform?spm=api-workbench.home.0.0.5f4de85cHYWAyq&provider=1.246.0&product=ECS&resource=alicloud_auto_provisioning_group&example=201-use-case-bind-eip-to-ecs-eni&activeTab=code)
## 所涉及资源
[alicloud_eip_address](https://help.aliyun.com/zh/terraform/alicloud-eip-address)：创建EIP。
[alicloud_eip_association](https://help.aliyun.com/zh/terraform/alicloud-eip-association)：将EIP绑定至云资源，例如将EIP绑定至ECS实例或者弹性网卡。
[alicloud_vpc](https://help.aliyun.com/zh/terraform/alicloud-vpc)：创建专有网络VPC。
[alicloud_vswitch](https://help.aliyun.com/zh/terraform/alicloud-vswitch)：创建虚拟交换机。
[alicloud_security_group](https://help.aliyun.com/zh/terraform/alicloud-security-group)：创建安全组。
[alicloud_security_group_rule](https://help.aliyun.com/zh/terraform/alicloud-security-group-rule)：为安全组添加访问控制规则。
[alicloud_ecs_network_interface](https://help.aliyun.com/zh/terraform/alicloud-ecs-network-interface)：创建弹性网卡。
## 编写配置文件
创建terraform.tf文件，输入以下内容并保存。
provider "alicloud" { region = var.region } # 资源将要创建的地域 variable "region" { default = "cn-beijing" description = "The region where the resources will be created." } # 输入已有的VPC ID，当为已有ECS实例绑定弹性网卡时，该值必填，且值为ECS实例所对应的VPC。 variable "vpc_id" { default = "" description = "When binding an ENI to an existing ECS instance, this value is required and must be the VPC associated with the ECS instance." } # 指定VPC的CIDR块，当填入vpc_id时，该值可不填。 variable "vpc_cidr_block" { default = "192.168.0.0/16" description = "Specify the CIDR block of the VPC. If the vpc_id is provided, this value can be left blank." } # 输入可用区，当为已有ECS实例绑定弹性网卡时，该值必填，且值为ECS实例所在可用区。 variable "zone_id" { default = "" description = "When binding an ENI to an existing ECS instance, this value is required and must be the zone where the ECS instance is located." } # 指定VSwitch的CIDR块，CIDR块需在VPC CIDR块的范围内 variable "vswitch_cidr_block" { default = "192.168.0.0/24" description = "Specify the CIDR block of the VSwitch. The CIDR block must be within the range of the VPC CIDR block." } # 访问弹性网卡的源地址 variable "source_ip" { description = "The IP address you used to access the ENI." type = string default = "0.0.0.0/0" } # 指定弹性网卡的私网IP地址 variable "private_ip" { description = "The primary private IP address of the ENI. The specified IP address must be available within the CIDR block of the VSwitch. If this parameter is not specified, an available IP address is assigned from the VSwitch CIDR block at random." type = string default = "" } locals { new_zone_id = var.zone_id == "" create_vpc = var.vpc_id == "" } resource "alicloud_eip" "eip" { address_name = "test_eip" } resource "alicloud_vpc" "vpc" { count = local.create_vpc ? 1 : 0 vpc_name = "test_vpc" cidr_block = var.vpc_cidr_block } data "alicloud_zones" "default" { count = local.new_zone_id ? 1 : 0 available_resource_creation = "VSwitch" } resource "alicloud_vswitch" "vswitch" { vswitch_name = "test_vswitch" cidr_block = var.vswitch_cidr_block zone_id = local.new_zone_id ? data.alicloud_zones.default[0].zones.0.id : var.zone_id vpc_id = local.create_vpc ? alicloud_vpc.vpc[0].id : var.vpc_id } resource "alicloud_security_group" "group" { security_group_name = "test_sg" vpc_id = local.create_vpc ? alicloud_vpc.vpc[0].id : var.vpc_id } # 添加允许TCP 80端口入方向流量的规则 resource "alicloud_security_group_rule" "allow_80_tcp" { type = "ingress" ip_protocol = "tcp" nic_type = "intranet" policy = "accept" port_range = "80/80" priority = 1 security_group_id = alicloud_security_group.group.id cidr_ip = var.source_ip } resource "alicloud_network_interface" "default" { network_interface_name = "test_eni" vswitch_id = alicloud_vswitch.vswitch.id security_group_ids = [alicloud_security_group.group.id] primary_ip_address = var.private_ip secondary_private_ip_address_count = 1 } resource "alicloud_eip_association" "default" { allocation_id = alicloud_eip.eip.id instance_type = "NetworkInterface" instance_id = alicloud_network_interface.default.id }
## 创建资源
以下命令需要在terraform.tf文件所在目录执行。
运行terraform init进行初始化，当返回如下信息时，表示初始化完成。
Terraform has been successfully initialized! You may now begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All Terraform commands should now work. If you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forget, other commands will detect it and remind you to do so if necessary.
运行terraform apply并根据提示输入yes创建资源，当返回如下信息时，表示资源创建完成。
Do you want to perform these actions? Terraform will perform the actions described above. Only 'yes' will be accepted to approve. Enter a value: yes alicloud_vpc.vpc: Creating... alicloud_eip.eip: Creating... ... Apply complete! Resources: 7 added, 0 changed, 0 destroyed.
说明
当您创建弹性网卡是为了绑定到已有ECS实例时，可以执行terraform apply传相应的参数，例如terraform apply -var source_ip=XX.XX.XX.XX -var vpc_id=vpc-2vc4ctyuxpq6nXXXXXXXXX -var zone_id=cn-beijing-a -var vswitch_cidr_block=XX.XX.XX.XX/XX。
运行terraform show查看已创建的资源，包括VPC、弹性公网IP、弹性网卡等。
说明
您也可以在控制台查看所创建的资源。
## 清理资源
当您不再需要上述通过Terraform创建或管理的资源时，请运行terraform destroy命令以释放资源。
terraform destroy
## 相关文档
在弹性网卡创建完成后，您可以将其绑定至同一VPC内的同一可用区的ECS实例上。具体操作，请参见[创建并使用弹性网卡](../user-guide/create-and-use-an-eni.md)。
Terraform更多命令，请参见[Terraform](https://help.aliyun.com/zh/terraform/terraform-common-commands)[常用命令](https://help.aliyun.com/zh/terraform/terraform-common-commands)。
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
