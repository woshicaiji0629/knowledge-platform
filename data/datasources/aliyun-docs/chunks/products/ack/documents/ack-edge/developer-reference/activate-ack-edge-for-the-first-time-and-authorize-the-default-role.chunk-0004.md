## 步骤一：开通ACK Edge集群
容器服务ACK Edge现已正式商用，在创建ACK Edge集群前您需要开通相应服务。
创建一个工作目录，并在工作目录中创建名为main.tf的配置文件。
将如下代码复制到main.tf配置文件。
展开查看本文用到的main.tf文件
provider "alicloud" { } // 开通容器服务ACK Edge。 data "alicloud_ack_service" "open" { enable = "On" type = "edgepayasgo" }
执行如下命令，初始化Terraform运行环境。
terraform init
返回信息如下，Terraform初始化成功。
Initializing the backend... Initializing provider plugins... ... Terraform has been successfully initialized! ...
执行如下命令，开通容器服务ACK Edge集群。
terraform apply
返回信息如下，服务开通成功。
data.alicloud_ack_service.open: Refreshing state... Apply complete! Resources: 0 added, 0 changed, 0 destroyed.
