# 资源所在的地域 variable "region" { default = "cn-chengdu" } provider "alicloud" { region = var.region }
定义专有网络VPC及其子网。
VPC是一种专有的云上私有网络，允许用户在公共云上配置和管理一个逻辑隔离的网络区域。
variable "instance_name" { default = "tf-sample" } # ecs实例规格 variable "instance_type" { default = "ecs.e-c1m2.large" } # 查询满足条件的可用区 data "alicloud_zones" "default" { available_disk_category = "cloud_essd" available_resource_creation = "VSwitch" available_instance_type = var.instance_type } # 创建VPC resource "alicloud_vpc" "vpc" { vpc_name = var.instance_name cidr_block = "172.16.0.0/12" } # 创建交换机 resource "alicloud_vswitch" "vsw" { vpc_id = alicloud_vpc.vpc.id cidr_block = "172.16.0.0/21" zone_id = data.alicloud_zones.default.zones.0.id }
定义安全组。
安全组是一种虚拟防火墙，能够控制ECS实例的出入方向流量。
