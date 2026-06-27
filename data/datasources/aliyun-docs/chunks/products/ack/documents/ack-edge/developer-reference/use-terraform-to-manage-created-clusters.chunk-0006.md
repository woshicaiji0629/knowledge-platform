apply) } + operation_policy { + cluster_auto_upgrade { + channel = (known after apply) + enabled = (known after apply) } } - timeouts {} + worker_nodes { + id = (known after apply) + name = (known after apply) + private_ip = (known after apply) } } Plan: 1 to add, 0 to change, 1 to destroy.
说明
为了确保资源模板与资源状态一致，需要在模板中手动补充缺失的参数定义，直到运行terraform plan时不再出现变更信息为止。
provider "alicloud" { region = "cn-hangzhou" # 导入集群所在的区域。 } resource "alicloud_cs_managed_kubernetes" "default" { worker_vswitch_ids = [ "vsw-bp1fXXXXX2nuig6h" ] deletion_protection = false load_balancer_spec = "slb.s1.small" name = "TFCESHI" new_nat_gateway = true proxy_mode = "ipvs" slb_internet_enabled = true node_cidr_mask = 26 service_cidr = "192.168.0.0/16" pod_cidr = "172.16.224.0/20" control_plane_log_components = [] enable_rrsa = false tags = {} timezone = "Asia/Shanghai" }
执行如下命令，将上一步中补充的字段导入至本地集群。
terraform apply
返回信息如下，字段导入成功。
alicloud_cs_managed_kubernetes.default: Modifying... [id=cc7c582b0XXXXXcb80ae118eef0cb12] alicloud_cs_managed_kubernetes.default: Modifications complete after 2s [id=cc7c582b0XXXXXcb80ae118eef0cb12] Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
导入节点池。
将集群的节点资源添加到main.tf文件中。
