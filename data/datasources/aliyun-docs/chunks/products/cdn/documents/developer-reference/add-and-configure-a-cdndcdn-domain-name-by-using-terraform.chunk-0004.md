## 步骤一：添加加速域名
创建一个工作目录，并在该工作目录中创建名为main.tf的配置文件，在main.tf中增加以下代码：
重要
以下示例代码中的域名（如mydcdndomain-xxx.alicloud-provider.cn、mycdndomain-xxx.alicloud-provider.cn）仅用于一键运行托管环境，普通用户无法通过这些域名的归属权验证。如果您在本地环境执行此教程，请将domain_name参数的值替换为您已拥有并完成归属权验证的域名。
resource "random_integer" "default" { min = 10000 max = 99999 } # 添加一个加速域名 resource "alicloud_cdn_domain_new" "domain" { domain_name = "mycdndomain-${random_integer.default.result}.alicloud-provider.cn" cdn_type = "download" scope = "overseas" sources { content = "myoss-${random_integer.default.result}.oss-rg-china-mainland.aliyuncs.com" type = "oss" priority = "20" port = 80 weight = "15" } }
执行如下命令，初始化Terraform运行环境。
terraform init
返回信息如下，Terraform初始化成功。
Initializing the backend... Initializing provider plugins... ... Terraform has been successfully initialized!
执行如下命令执行计划，添加加速域名。
terraform apply
在执行过程中，根据提示输入yes并按下Enter键，等待命令执行完成，若出现以下信息，则表示添加加速域名成功。
说明
如果提示错误“code: 400, Owner verification of the root domain failed.”，表示该域名是首次添加到CDN系统中，需要完成域名归属权验证，请参见[验证域名归属权](../verify-domain-name-ownership.md)。
You can apply this plan to save these new output values to the Terraform state, without changing any real infrastructure. Do you want to perform these act
