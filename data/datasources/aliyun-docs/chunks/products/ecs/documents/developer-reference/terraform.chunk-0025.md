eger.default.result}" system_disk_description = "test_foo_system_disk_description" image_id = "aliyun_2_1903_x64_20G_alibase_20240628.vhd" instance_name = "test_ecs_${random_integer.default.result}" vswitch_id = alicloud_vswitch.vswitch.id internet_max_bandwidth_out = 10 password = "Terraform@Example" # 用户根据自己实际情况修改 }
执行如下命令，初始化Terraform运行环境。
terraform init
返回信息如下，则Terraform初始化成功。
Terraform has been successfully initialized! You may now begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All Terraform commands should now work. If you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forget, other commands will detect it and remind you to do so if necessary.
执行如下命令，开始执行代码。
terraform apply
在执行过程中，根据提示输入yes并按下Enter键，等待命令执行完成，若出现以下信息，则表示代码执行成功。
You can apply this plan to save these new output values to the Terraform state, without changing any real infrastructure. Do you want to perform these actions? Terraform will perform the actions described above. Only 'yes' will be accepted to approve. Enter a value: yes Apply complete! Resources:
