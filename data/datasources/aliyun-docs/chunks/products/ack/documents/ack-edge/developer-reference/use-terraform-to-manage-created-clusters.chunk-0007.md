# Kubernetes托管版。 resource "alicloud_cs_kubernetes_node_pool" "default" { }
执行以下命令，导入节点池。
其中，<Cluster-ID>为待导入集群的ID，此处为上一步中导入集群的ID，<Nodepool-ID>为待导入节点池的ID，两者通过英文半角冒号（:）分隔。
terraform import alicloud_cs_kubernetes_node_pool.default <Cluster-ID>:<Nodepool-ID>
预期输出：
alicloud_cs_kubernetes_node_pool.default: Importing from ID "cc7c582b0XXXXXcb80ae118eef0cb12*:np0f8f219XXXXX5d4aa503c3d24ca****"... alicloud_cs_kubernetes_node_pool.default: Import complete! Imported alicloud_cs_kubernetes_node_pool alicloud_cs_kubernetes_node_pool.default: Refreshing state... [id=cc7c582b0XXXXXcb80ae118eef0cb12:np651662XXXXXd9979360b24b1a009] Import successful! The resources that were imported are shown above. These resources are now in your Terraform state and will henceforth be managed by Terraform.
此时，在terraform.tfstate文件中会显示如下导入的节点池信息：
..... "resources": [ { "mode": "managed", "type": "alicloud_cs_kubernetes_node_pool", "name": "default", "provider": "provider.alicloud", "instances": [ ..... ] } ]
根据terraform.tfstate文件的内容，补充main.tf的必填字段。
provider "alicloud" { } # 节点池。 resource "alicloud_cs_kubernetes_node_pool" "default" { name = .... # 节点池的名称。 instance_types = .... # 节点池的实例类型。 vswitch_ids = .... # 节点使用交
