"alicloud" { } # 节点池。 resource "alicloud_cs_kubernetes_node_pool" "default" { name = .... # 节点池的名称。 instance_types = .... # 节点池的实例类型。 vswitch_ids = .... # 节点使用交换机ID。 cluster_id = alicloud_cs_managed_kubernetes.default.id # 引用 cluster_id }
执行如下命令，将上一步中补充的字段导入至本地集群。
terraform apply
返回信息如下，字段导入成功。
alicloud_cs_kubernetes_node_pool.default: Refreshing state... [id=cc7c5XXXXX6dcb80ae118eef0cb12:np651662XXXXXd9979360b24b1a009] alicloud_cs_managed_kubernetes.default: Refreshing state... [id=cc7c582XXXXX6dcb80ae118eef0cb12] Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols: ~ update in-place Terraform will perform the following actions: ............ # (2 unchanged blocks hidden) } Plan: 0 to add, 1 to change, 0 to destroy.
集群导入完成后，您就可以通过main.tf文件对集群或节点池进行操作。
验证节点池的扩容操作。
通过main.tf验证节点池的扩容操作。
比如给刚导入的节点池扩容至3个节点，需要将main.tf文件新增为desired_size = 3字段。
...... # Kubernetes托管版。 resource "alicloud_cs_kubernetes_node_pool" "default" { ..... # 节点池期望节点数为3。 desired_size = 3 } .....
执行以下命令，完成变更操作。
terraform apply
返回信息如下，输入yes，按Enter键，等待变更结束。
alicloud_cs_kubernetes_node_pool.default: Refreshing state... [id=cc7c5XXXXX546dc
