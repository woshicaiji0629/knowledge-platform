## Terraform
Resources：[alicloud_route_entry](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/route_entry)resource "alicloud_route_entry" "foo" { route_table_id = "rt-12345xxxx" # 填写路由表id destination_cidrblock = "172.16.1.1/32" nexthop_type = "Instance" # 填写下一跳类型 nexthop_id = "i-12345xxxx" # 填写下一跳实例id }
