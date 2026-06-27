### 2. 预览Terraform代码
运行terraform plan实现如下功能：
验证main.tf中Terraform代码的语法是否正确。
显示当前Terraform代码将要创建的资源的预览结果。
terraform plan
如果显示如下所示的信息表示Terraform文件无语法错误，可以执行terraform apply命令创建资源。若出现其他报错提示，请根据提示修改Terraform配置文件。
... Plan: 5 to add, 0 to change, 0 to destroy.
