w begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All Terraform commands should now work. If you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forget, other commands will detect it and remind you to do so if necessary.
创建执行计划，并预览变更。
terraform plan
执行以下命令，创建集群。
terraform apply
在执行过程中，根据提示输入yes并按下Enter键，等待命令执行完成，若出现以下信息，则表示ACK集群创建成功。
Do you want to perform these actions? Terraform will perform the actions described above. Only 'yes' will be accepted to approve. Enter a value: yes ... alicloud_cs_managed_kubernetes.default: Creation complete after 5m48s [id=ccb53e72ec6c447c990762800********] ... Apply complete! Resources: 11 added, 0 changed, 0 destroyed.
验证结果
