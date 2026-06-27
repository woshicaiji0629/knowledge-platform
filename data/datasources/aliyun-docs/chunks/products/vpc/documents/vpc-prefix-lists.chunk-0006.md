### VPC路由表引用
在VPC路由表中添加自定义路由条目时，您可以引用前缀列表。引用时需注意：
避免与VPC现有路由条目发生路由冲突，否则无法引用。如果引用后发生了冲突，请参考[处理引用后出现的条目冲突](vpc-prefix-lists.md)。
前缀列表的最大条目数（注意不是实际包含的条目数），会占用VPC路由表自定义路由条目数配额。您可尝试通过调低最大条目数、合并相邻IP段、清理无用条目等方式来降低配额超限风险。
控制台
前往路由表基本信息页面，在路由条目列表>自定义路由条目页签下，单击添加路由条目进行配置：
目标网段：左侧下拉框选择VPC前缀列表，右侧选择目标前缀列表，
下一跳类型：选择对应的类型及实例。
API
调用[CreateRouteEntry](developer-reference/api-vpc-2016-04-28-createrouteentry.md)，DestinationCidrBlock参数填入前缀列表的实例 ID。
TerraformResources：[alicloud_route_entry](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/route_entry)# 指定地域 provider "alicloud" { region = "cn-hangzhou" } # 增加1条VPC路由条目，目标网段为前缀列表 resource "alicloud_route_entry" "example" { route_table_id = "vtb-bp1pa1mwgfd6rqxfxxxxx" # VPC路由表ID destination_cidrblock = "pl-bp1fnjzxkk2m6qrwxxxxx" # 目标网段，填前缀列表ID nexthop_type = "Ecr" # 下一跳类型 nexthop_id = "ecr-assoc-stwhaft9a371nxxxxx" # 下一跳实例ID }
