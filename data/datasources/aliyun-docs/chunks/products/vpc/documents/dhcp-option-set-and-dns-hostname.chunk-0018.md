器IP，将自建 DNS 服务器 IP 填写在首位。
在目标 DHCP 选项集的操作列选择关联专有网络，已配置域名解析记录的 ECS 可通过主机名被关联 VPC 内的 ECS 访问。
API
依次调用如下 API，创建自定义 DHCP 选项集指定域名与自建 DNS 服务器 IP，与 VPC 关联。
[CreateDhcpOptionsSet - 创建 DHCP 选项集](developer-reference/api-vpc-2016-04-28-createdhcpoptionsset.md)
[AttachDhcpOptionsSetToVpc - 将 DHCP 选项集关联到 VPC](developer-reference/api-vpc-2016-04-28-attachdhcpoptionssettovpc.md)
TerraformResource：[alicloud_vpc_dhcp_options_set](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_dhcp_options_set)、[alicloud_vpc_dhcp_options_set_attachment](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_dhcp_options_set_attachment)# 指定VPC的地域 provider "alicloud" { region = "cn-hangzhou" } # 创建DHCP选项集 resource "alicloud_vpc_dhcp_options_set" "test_dhcp_options_set" { dhcp_options_set_name = "test_dhcp_options_set_name" domain_name = "example.com" # 指定域名 domain_name_servers = "192.168.0.10,100.100.2.136,100.100.2.138" # 指定DNS服务器IP，首位填写自建DNS服务器IP } # 关联DHCP选项集与VPC resource "alicloud_vpc_dhcp_options_set_attachment" "test_attachment_vpc" { vpc_id = "vpc-8vbg******" # 指定关联的VPC的实例ID dhcp_options_set_id = alicloud_vpc_dhcp_options_set.test_dhcp_options_set.id
