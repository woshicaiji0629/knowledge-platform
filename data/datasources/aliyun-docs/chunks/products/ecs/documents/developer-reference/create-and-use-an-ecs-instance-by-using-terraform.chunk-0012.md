# 创建安全组 resource "alicloud_security_group" "default" { name = var.instance_name vpc_id = alicloud_vpc.vpc.id } # 为安全组入方向添加规则 resource "alicloud_security_group_rule" "allow_tcp_22" { type = "ingress" ip_protocol = "tcp" nic_type = "intranet" policy = "accept" port_range = "22/22" priority = 1 security_group_id = alicloud_security_group.default.id cidr_ip = "0.0.0.0/0" }
定义ECS实例。
使用ECS，您可以快速部署和运行应用程序，灵活调整资源以应对业务变化，同时享受高性能、高安全性和低成本的计算能力，适用于网站托管、应用开发、数据处理等多种场景。
