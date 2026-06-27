# 为加速域名配置一个访问IP白名单 resource "alicloud_cdn_domain_config" "config-ip" { domain_name = alicloud_cdn_domain_new.domain.domain_name function_name = "ip_allow_list_set" function_args { arg_name = "ip_list" arg_value = "192.168.0.1" } }
创建执行计划，并预览变更。
terraform plan
执行如下命令执行计划，为加速域名配置访问IP白名单。
terraform apply
在执行过程中，根据提示输入yes并按下Enter键，等待命令执行完成，若出现以下信息，则表示配置规则完成。
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
