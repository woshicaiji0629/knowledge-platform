# 例如配置文件路径 D:/ecs-quickstart # 切换到 D盘 d: # 切换到配置文件所在文件夹路径的命令，ecs-quickstart是配置文件所在文件夹路径，您可根据实际路径替换。 cd ecs-quickstart # 执行初始化命令 terraform init
说明
当您因网络延迟等原因导致terraform init超时，无法正常下载Provider等情况时，可通过配置阿里云镜像站解决，具体操作步骤，请参见[Terraform Init 加速方案配置](https://help.aliyun.com/zh/terraform/terraform-init-acceleration-solution-configuration)。
如下所示的信息表示初始化成功。
Terraform has been successfully initialized! You may now begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All Terraform commands should now work. If you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forget, other commands will detect it and remind you to do so if necessary.
