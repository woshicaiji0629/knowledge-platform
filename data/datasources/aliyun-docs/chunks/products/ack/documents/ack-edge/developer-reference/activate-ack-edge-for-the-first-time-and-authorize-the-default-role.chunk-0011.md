\"Version\":\"1\"}" description = "集群的管控组件使用该角色访问您在智能接入网关、VPC和云企业网CEN服务中的资源。" policy_name = "AliyunCSManagedEdgeRolePolicy" }, { name = "AliyunOOSLifecycleHook4CSRole" policy_document = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":[\"oos.aliyuncs.com\"]}}],\"Version\":\"1\"}" description = "系统运维管理OOS使用该角色访问您在集群、ECS、PolarDB等服务中的资源" policy_name = "AliyunOOSLifecycleHook4CSRolePolicy" } ] }
执行如下命令，初始化Terraform运行环境。
terraform init
返回信息如下Terraform初始化成功。
Initializing the backend... Initializing provider plugins... ... Terraform has created a lock file .terraform.lock.hcl to record the providerselections it made above. Include this file in your version control repositoryso that Terraform can guarantee to make the same selections by default whenyou run "terraform init" in the future. Terraform has been successfully initialized! ...
执行如下命令，为您的账号进行角色授权。
terraform apply
返回信息如下，输入yes，按Enter键，表示授权成功。
Do you want to perform these actions? Terraform will perform the actions described above. Only 'yes' will be accepted to approve. Enter a value: yes alicloud_ram_role_policy_attachment.attach["AliyunCSManagedEdgeRole"]: Creating... alicloud_ram_rol
