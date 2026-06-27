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
