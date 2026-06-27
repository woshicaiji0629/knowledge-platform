### ECS安全组引用
配置安全组入方向或出方向规则时，您可以引用前缀列表。
控制台
以添加安全组入方向规则为例，前往ECS控制台目标安全组详情页面，在访问规则的入方向页签下，单击增加规则进行配置：
访问来源：左侧下拉列表选择前缀列表，右侧选择目标前缀列表。
其他配置项：请按需配置。
API
调用[AuthorizeSecurityGroup](../../ecs/documents/developer-reference/api-ecs-2014-05-26-authorizesecuritygroup.md)增加安全组入方向规则时，SourcePrefixListId参数填入前缀列表ID。
调用[AuthorizeSecurityGroupEgress](../../ecs/documents/developer-reference/api-ecs-2014-05-26-authorizesecuritygroupegress.md)增加安全组出方向规则时，DestPrefixListId参数填入前缀列表ID。
TerraformResources：[alicloud_security_group](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/security_group)、[alicloud_security_group_rule](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/security_group_rule)# 指定地域 provider "alicloud" { region = "cn-hangzhou" } # 指定安全组 resource "alicloud_security_group" "sg_example" { security_group_name = "sg_example_name" vpc_id = "vpc-bp1d00iurwfx3pcxxxxx" # VPC ID } # 创建安全组规则时，引用前缀列表 resource "alicloud_security_group_rule" "sg_rule_pl_example" { security_group_id = alicloud_security_group.sg_example.id type = "ingress" ip_protocol = "tcp" policy = "accept" port_range = "8080/8080" prefix_list_id = "pl-bp1fnjzxkk2m6qrxxxxxx" # VP
