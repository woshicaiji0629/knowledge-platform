s_node_pool" "autoscale_node_pool" { cluster_id = alicloud_cs_managed_kubernetes.default.id node_pool_name = local.autoscale_nodepool_name vswitch_ids = split(",", join(",", alicloud_vswitch.vswitches.*.id)) scaling_config { min_size = 1 max_size = 10 } instance_types = var.worker_instance_types password = var.password # SSH登录集群节点的密码。 install_cloud_monitor = true # 是否为kubernetes的节点安装云监控。 system_disk_category = "cloud_efficiency" system_disk_size = 100 image_type = "AliyunLinux3" data_disks { # 节点数据盘配置。 category = "cloud_essd" # 节点数据盘种类。 size = 120 # 节点数据盘大小。 } }
执行如下命令，初始化Terraform运行环境。
terraform init
返回信息如下，Terraform初始化成功。
Terraform has been successfully initialized! You may now begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All Terraform commands should now work. If you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forget, other commands will detect it and remind you to do so if necessary.
执行terraform apply命令完成创建。
验证结果。
完成创建节点池后，在节点池列表中可以看到新建的节点池，该节点池名称下会标注已开启自动伸缩。在节点池页面的节点池列表中，np-test节点池名称下方显示已开启自动伸缩标签，表示自动弹性伸缩功能已成功开启。
