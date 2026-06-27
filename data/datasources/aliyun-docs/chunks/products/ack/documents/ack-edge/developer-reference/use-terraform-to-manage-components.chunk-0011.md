### 在创建集群后管理组件生命周期
管理组件的生命周期前提是您已经创建了一个Kubernetes集群，如果您还没有创建Kubernetes集群，请先创建集群。
对于集群中的组件，您可以通过Resource中的alicloud_cs_kubernetes_addon来管理组件的生命周期，包括组件的安装、升级、卸载、自定义配置的修改。alicloud_cs_kubernetes_addon的属性和定义如下：
resource "alicloud_cs_kubernetes_addon" "addon-example" { # 集群ID。 cluster_id = "XXXX" # 组件的名称，可以通过Data Source中的alicloud_cs_kubernetes_addons，查询当前集群所有已安装的以及可以安装的组件和其对应版本信息。 name = "XXXX" # 组件的版本信息。 version = "XXXX" # 组件的自定义参数，为JSON格式的字符串，可以使用Terraform自带的jsonencode方法进行配置，也可以直接使用JSON字符串进行配置（需要注意转义），某些集群组件开启了自定义参数配置的能力，您可以使用该字段来为组件指定其自定义参数，具体指定方法，请参见下文“修改集群组件的自定义配置参数”一节 。 config = jsonencode( { .... } ) }
您可以通过直接写入JSON字符串的方式配置组件自定义参数，但是需要注意转义。例如对于nginx-ingress-controller组件，有以下两种配置方法：
通过jsonencode配置参数：
config = jsonencode( { IngressSlbNetworkType="internet" IngressSlbSpec="slb.s2.small" } )
通过直接使用字符串的方式配置参数：
config = "{\"IngressSlbNetworkType\":\"internet\",\"IngressSlbSpec\":\"slb.s2.small\"}"
