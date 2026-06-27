# 通过Terraform添加并配置CDN域名的操作步骤及前提条件-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/developer-reference/add-and-configure-a-cdndcdn-domain-name-by-using-terraform

# 通过Terraform添加并配置CDN域名
阿里云CDN产品已经接入Terraform，可以通过Terraform实现添加与配置等操作。此教程演示如何通过Terraform添加CDN加速域名，并且为该加速域名配置IP白名单。
说明
本教程所含示例代码支持一键运行，您可以直接运行代码。[一键运行](https://api.aliyun.com/api-tools/terraform?resource=alicloud_cdn_domain_config&exampleId=&activeTab=example&provider=1.233.0&product=CDN&example=101-use-case-configure-cdn-domain-name)
## 前提条件
在初次使用CDN之前，您需要先开通CDN服务，请参见[开通](../activate-alibaba-cloud-cdn.md)[CDN](../activate-alibaba-cloud-cdn.md)[服务](../activate-alibaba-cloud-cdn.md)。
为了降低信息安全风险，建议使用最小权限的RAM用户完成此教程的操作。请参见[创建](../../../ram/documents/user-guide/create-a-ram-user.md)[RAM](../../../ram/documents/user-guide/create-a-ram-user.md)[用户](../../../ram/documents/user-guide/create-a-ram-user.md)与[管理](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)，完成此教程所需最小权限的权限策略如下：
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "cdn:AddCdnDomain", "cdn:DescribeCdnDomainDetail", "cdn:DescribeDomainCertificateInfo", "cdn:ListTagResources", "cdn:DeleteCdnDomain", "cdn:BatchSetCdnDomainConfig", "cdn:DescribeCdnDomainConfigs", "cdn:DeleteSpecificConfig" ], "Resource": "*" } ] }
准备Terraform运行环境，您可以选择以下任一方式来使用Terraform。
[Explorer](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)：阿里云提供了Terraform的在线运行环境，您无需安装Terraform，登录后即可在线使用和体验Terraform。适用于零成本、快速、便捷地体验和调试Terraform的场景。
[使用](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)[Terraform](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)[快速创建资源](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources)：阿里云Cloud Shell中预装了Terraform的组件，并已配置好身份凭证，您可直接在Cloud Shell中运行Terraform的命令。适用于低成本、快速、便捷地访问和使用Terraform的场景。
[在本地安装和配置](https://help.aliyun.com/zh/terraform/install-and-configure-terraform-locally)[Terraform](https://help.aliyun.com/zh/terraform/install-and-configure-terraform-locally)：适用于网络连接较差或需要自定义开发环境的场景。
拥有已完成归属权验证的待添加域名。添加加速域名前，您需要完成域名归属权验证，具体操作请参见[验证域名归属权](../verify-domain-name-ownership.md)。
## 使用的资源
说明
本教程示例包含的部分资源会产生一定费用，请在不需要时及时进行释放或退订。
[alicloud_cdn_domain_new](https://help.aliyun.com/zh/terraform/alicloud-cdn-domain-new)：添加CDN加速域名。
[alicloud_cdn_domain_config](https://help.aliyun.com/zh/terraform/alicloud-cdn-domain-config)：配置CDN加速域名规则。
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
You can apply this plan to save these new output values to the Terraform state, without changing any real infrastructure. Do you want to perform these actions? Terraform will perform the actions described above. Only 'yes' will be accepted to approve. Enter a value: yes Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
## 步骤二：为加速域名配置规则
在main.tf文件中增加以下代码。
# 为加速域名配置一个访问IP白名单 resource "alicloud_cdn_domain_config" "config-ip" { domain_name = alicloud_cdn_domain_new.domain.domain_name function_name = "ip_allow_list_set" function_args { arg_name = "ip_list" arg_value = "192.168.0.1" } }
创建执行计划，并预览变更。
terraform plan
执行如下命令执行计划，为加速域名配置访问IP白名单。
terraform apply
在执行过程中，根据提示输入yes并按下Enter键，等待命令执行完成，若出现以下信息，则表示配置规则完成。
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
## 验证结果
## 执行terrafrom show 命令
您可以使用以下命令查询Terraform已创建的资源详细信息：
terraform showshell@Alicloud:~/cdn$ terraform show # alicloud_cdn_domain_config.config-ip: resource "alicloud_cdn_domain_config" "config-ip" { config_id = "394085720977408" domain_name = "xxx" function_name = "ip_allow_list_set" id = "xxx:ip_allow_list_set:394085720977408" parent_id = "0" status = "success" function_args { arg_name = "ip_list" arg_value = "192.168.0.1" } } # alicloud_cdn_domain_new.domain: resource "alicloud_cdn_domain_new" "domain" { cdn_type = "download" cname = "xxx.com.w.cdngslb.com" domain_name = "xxx.com" id = "xxx.com" resource_group_id = "rg-acfmykd63gtpfpa" scope = "overseas" status = "online" certificate_config { cert_type = "cas" server_certificate_status = "off" } sources { content = "xxx.oss-rg-china-mainland.aliyuncs.com" port = 80 priority = 20 type = "oss" weight = 15 } }
## 登录CDN控制台
登录[CDN](https://cdn.console.aliyun.com/domain/list)[控制台](https://cdn.console.aliyun.com/domain/list)，查看已添加域名的IP黑/白名单。
在目标域名的域名管理页面，单击左侧导航栏访问控制，选择IP黑/白名单页签，可查看当前IP黑/白名单类型为IP白名单，白名单中已添加IP地址192.168.0.1。
## 清理资源
当您不再需要上述通过Terraform创建或管理的资源时，请运行以下命令以释放资源。关于terraform destroy的更多信息，请参见[Terraform](https://help.aliyun.com/zh/terraform/terraform-common-commands)[常用命令](https://help.aliyun.com/zh/terraform/terraform-common-commands)。
terraform destroy
## 完整示例
说明
本教程所含示例代码支持一键运行，您可以直接运行代码。[一键运行](https://api.aliyun.com/api-tools/terraform?resource=alicloud_cdn_domain_config&exampleId=&activeTab=example&provider=1.233.0&product=CDN&example=101-use-case-configure-cdn-domain-name)
### 示例代码
resource "random_integer" "default" { min = 10000 max = 99999 } # 添加一个加速域名 resource "alicloud_cdn_domain_new" "domain" { domain_name = "mycdndomain-${random_integer.default.result}.alicloud-provider.cn" cdn_type = "download" scope = "overseas" sources { content = "myoss-${random_integer.default.result}.oss-rg-china-mainland.aliyuncs.com" type = "oss" priority = "20" port = 80 weight = "15" } } # 为加速域名配置一个访问IP白名单 resource "alicloud_cdn_domain_config" "config-ip" { domain_name = alicloud_cdn_domain_new.domain.domain_name function_name = "ip_allow_list_set" function_args { arg_name = "ip_list" arg_value = "192.168.0.1" } }
如果您想体验更多完整示例，请前往[更多完整示例](https://github.com/alibabacloud-automation/landing-with-terraform/tree/main/quickstarts)中对应产品的文件夹查看。
## 相关文档
Terrafrom介绍，请参见[了解阿里云](https://help.aliyun.com/zh/terraform/what-is-terraform)[Terraform](https://help.aliyun.com/zh/terraform/what-is-terraform)。
当您遇到由于网络延迟等原因造成的 terraform init 超时，导致无法正常下载 Provider 等情况时，请参见[Terraform Init 加速方案配置](https://help.aliyun.com/zh/terraform/terraform-init-acceleration-solution-configuration)。
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
