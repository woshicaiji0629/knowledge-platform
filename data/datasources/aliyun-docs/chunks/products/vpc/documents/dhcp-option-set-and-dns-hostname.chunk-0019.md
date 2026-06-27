s_set_attachment" "test_attachment_vpc" { vpc_id = "vpc-8vbg******" # 指定关联的VPC的实例ID dhcp_options_set_id = alicloud_vpc_dhcp_options_set.test_dhcp_options_set.id # 指定关联的DHCP选项集的实例ID }
