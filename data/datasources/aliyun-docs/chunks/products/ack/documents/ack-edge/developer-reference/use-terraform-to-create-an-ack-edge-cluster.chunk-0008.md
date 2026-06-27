ue # 节点的系统磁盘类别。其有效值为cloud_ssd和cloud_efficiency。默认为cloud_efficiency。 system_disk_category = "cloud_efficiency" system_disk_size = 100 # 操作系统类型。 image_type = "AliyunLinux" # 节点数据盘配置。 data_disks { # 节点数据盘种类。 category = "cloud_efficiency" # 节点数据盘大小。 size = 120 } lifecycle { ignore_changes = [ labels ] } }
执行以下命令，初始化Terraform运行环境。
terraform init
返回信息如下，Terraform初始化成功。
Terraform has been successfully initialized! You may now begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All Terraform commands should now work. If you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forget, other commands will detect it and remind you to do so if necessary.
创建执行计划，并预览变更。
terraform plan
返回以下信息，表示资源执行计划已成功生成，您可以查看相关资源信息。
Refreshing Terraform state in-memory prior to plan... The refreshed state will be used to calculate this plan, but will not be persisted to local or remote state storage. ... Plan: 4 to add, 0 to change, 0 to destroy. ...
执行以下命令，创建ACK Edge集群。
terraform apply
在执行过程中，根据提示输入yes并按下Enter键，等待命令执行完成，若出现以下信息，则表示集群创建成功。
... Do you want to perfo
