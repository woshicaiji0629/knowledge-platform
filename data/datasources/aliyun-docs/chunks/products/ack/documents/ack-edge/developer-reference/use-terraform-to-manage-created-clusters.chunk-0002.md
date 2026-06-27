# Kubernetes托管版。 resource "alicloud_cs_managed_kubernetes" "default" { }
执行以下命令，导入集群。
其中，<Cluster-ID>为待导入集群的ID。
terraform import alicloud_cs_managed_kubernetes.default <Cluster-ID>
预期输出：
alicloud_cs_managed_kubernetes.default: Importing from ID "cc7c582b0XXXXXcb80ae118eef0cb12"... alicloud_cs_managed_kubernetes.default: Import complete! Imported alicloud_cs_managed_kubernetes alicloud_cs_managed_kubernetes.default: Refreshing state... [id=cc7c582b0XXXXXcb80ae118eef0cb12] Import successful! The resources that were imported are shown above. These resources are now in your Terraform state and will henceforth be managed by Terraform.
此时，在terraform.tfstate文件中会显示类似如下导入的集群信息：
{ "mode": "managed", "type": "alicloud_cs_managed_kubernetes", "name": "default", "provider": "provider.alicloud", "instances": [ { "mode": "managed", "type": "alicloud_cs_managed_kubernetes", "name": "default", "provider": "provider.alicloud", "instances": [ ........ ] } ] }
根据terraform.tfstate文件的内容，补充main.tf的必填字段。
provider "alicloud" { } resource "alicloud_cs_managed_kubernetes" "default" { worker_vswitch_ids = [ # 补充必填字段。 ..... ] }
执行如下命令，查看本地资源与集群差异，以确保main.tf文件与导入集群资源一致。
terraform plan
请将以下带有->状态更新或+新增字段的内容添加到ma
