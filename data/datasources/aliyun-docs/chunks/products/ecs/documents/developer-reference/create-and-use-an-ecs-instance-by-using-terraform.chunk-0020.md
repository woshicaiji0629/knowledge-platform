## 资源变更
当您需要调整配置时，可以通过直接修改配置文件中的资源定义来实现，例如添加新的安全组入方向的放行规则。
若您希望在安全组入方向规则中添加443端口的放行规则，您可以在配置文件中添加以下代码。
resource "alicloud_security_group_rule" "allow_tcp_443" { type = "ingress" ip_protocol = "tcp" nic_type = "intranet" policy = "accept" port_range = "443/443" priority = 1 security_group_id = alicloud_security_group.default.id cidr_ip = "0.0.0.0/0" }
执行terraform plan命令预览所做的变更。如下所示的信息表示将要为安全组ID是sg-2vcdz6b8h9c3XXXXXXXX的安全组增加一条安全组规则。
... Terraform will perform the following actions: # alicloud_security_group_rule.allow_tcp_443 will be created + resource "alicloud_security_group_rule" "allow_tcp_443" { + cidr_ip = "0.0.0.0/0" + id = (known after apply) + ip_protocol = "tcp" + nic_type = "intranet" + policy = "accept" + port_range = "443/443" + prefix_list_id = (known after apply) + priority = 1 + security_group_id = "sg-2vcdz6b8h9c3XXXXXXXX" + type = "ingress" } Plan: 1 to add, 0 to change, 0 to destroy.
如果变更符合预期，执行terraform apply命令将变更应用到您的基础设施。在执行该命令时，Terraform将要求您确认是否进行变更，请键入yes并按回车键确认。如下所示的信息表示已为安全组ID是sg-2vcdz6b8h9c3XXXXXXXX的安全组新增规则成功。
... Do you want to perform these actions? Terraform will perform the actions described above. Only 'yes' will be accepted to approve. Enter a value:
