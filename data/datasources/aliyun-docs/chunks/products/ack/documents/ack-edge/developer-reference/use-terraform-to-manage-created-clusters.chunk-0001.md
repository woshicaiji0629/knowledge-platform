## 操作步骤
创建一个工作目录，并在工作目录中创建名为main.tf的配置文件。
provider "alicloud" { }
执行以下命令，初始化Terraform运行环境。
terraform init
返回信息如下，Terraform初始化成功。
Initializing the backend... Initializing provider plugins... - Checking for available provider plugins... - Downloading plugin for provider "alicloud" (hashicorp/alicloud) 1.90.1... ... You may now begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All Terraform commands should now work. If you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forget, other commands will detect it and remind you to do so if necessary.
导入集群。
将集群的资源添加到main.tf文件中。
