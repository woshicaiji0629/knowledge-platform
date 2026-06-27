## 为已有集群创建开启自动伸缩功能的节点池
在已有集群中创建开启自动伸缩功能的节点池，配置示例如下。
provider "alicloud" { } # 为已有集群创建开启自动伸缩功能的节点池。 resource "alicloud_cs_kubernetes_node_pool" "at1" { # 目标集群ID。 cluster_id = "" name = "np-test" # 节点池内节点使用的vswitch，至少提供一个。 vswitch_ids = ["vsw-bp1mdigyhmilu2h4v****"] instance_types = ["ecs.e3.medium"] password = "Hello1234" scaling_config { # 最小节点数。 min_size = 1 # 最大节点数。 max_size = 5 } }
