# 以托管版集群为例。 resource "alicloud_cs_managed_kubernetes" "default" { # 其它参数。 # ... # addons为list结构，通过在Resource中定义addons属性，表明创建集群时安装该组件。 addons { # 组件的名称，您可以通过Data Source中的alicloud_cs_kubernetes_addons查询。 # 当前集群已经安装的，以及可以安装的组件和其对应版本信息。 name = "XXX" # 组件的自定义参数，某些集群组件开启了自定义参数配置的能力，您可以使用该字段来为组件指定其自定义参数，具体指定方法，请参见下文“修改集群组件的自定义配置参数”一节。 config = jsonencode( { .... } ) # 该参数默认值为false（布尔值类型），ACK会默认安装部分组件，方便用户管理集群。若您在创建集群时不需安装这些组件，可设置disabled=true。 disabled = XXX } }
重要
通过在集群相关Resource中指定Addons的方式安装组件，仅支持在创建集群时指定安装，集群创建完成后，不支持通过修改Addons代码块中的属性来管理组件的生命周期，比如组件升级、组件卸载、组件配置更新等操作。若您需要在创建集群后管理组件生命周期，请参见下文[在创建集群后管理组件生命周期](use-terraform-to-manage-components.md)。
ACK中组件配置方式如下表所示。
