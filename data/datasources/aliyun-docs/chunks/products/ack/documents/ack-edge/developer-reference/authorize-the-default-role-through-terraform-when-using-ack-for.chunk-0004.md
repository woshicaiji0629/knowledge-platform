## 步骤一：开通容器服务ACK
在创建ACK集群前您需要开通容器服务。
创建一个工作目录，并在该工作目录中创建名为main.tf的配置文件，然后将以下代码复制到main.tf中。
// 开通容器服务ACK。 data "alicloud_ack_service" "open" { enable = "On" type = "propayasgo" }
执行如下命令，初始化Terraform运行环境。
terraform init
返回信息如下，Terraform初始化成功。
Terraform has been successfully initialized! You may now begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All Terraform commands should now work. If you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forget, other commands will detect it and remind you to do so if necessary.
执行如下命令，开通容器服务ACK。
terraform apply
在执行过程中，根据提示输入yes并按下Enter键，等待命令执行完成，若出现以下信息，则表示容器服务ACK开通成功。
You can apply this plan to save these new output values to the Terraform state, without changing any real infrastructure. Do you want to perform these actions? Terraform will perform the actions described above. Only 'yes' will be accepted to approve. Enter a value: yes Apply complete! Resources: 0 added, 0 changed, 0 destroyed.
