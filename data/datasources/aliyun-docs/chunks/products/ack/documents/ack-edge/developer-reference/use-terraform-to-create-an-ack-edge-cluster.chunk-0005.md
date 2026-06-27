## 使用Terraform创建ACK Edge集群
创建一个工作目录，并在工作目录下创建以下名为main.tf的配置文件。
main.tf配置文件中描述了如下Terraform配置：
创建一个新的VPC，并在该VPC下创建一个vSwitch。
创建一个ACK Edge集群。
创建一个包含两个节点的节点池。
provider "alicloud" { region = var.region_id } variable "region_id" { default = "cn-hangzhou" } variable "k8s_name_edge" { type = string description = "The name used to create edge kubernetes cluster." default = "edge-example" } variable "new_vpc_name" { type = string description = "The name used to create vpc." default = "tf-vpc-172-16" } variable "new_vsw_name" { type = string description = "The name used to create vSwitch." default = "tf-vswitch-172-16-0" } variable "nodepool_name" { type = string description = "The name used to create node pool." default = "edge-nodepool-1" } variable "k8s_login_password" { type = string default = "Test123456" } variable "k8s_version" { type = string description = "Kubernetes version" default = "1.28.9-aliyun.1" } variable "containerd_runtime_version" { type = string default = "1.6.34" } variable "cluster_spec" { type = string description = "The cluster specifications of kubernetes cluster,which can be empty. Valid values:ack.standard : Standard managed clusters; ack.pro.small : Professional
