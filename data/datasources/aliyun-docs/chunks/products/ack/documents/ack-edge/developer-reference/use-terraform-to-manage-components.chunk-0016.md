### 修改集群组件的自定义配置参数
ACK的某些组件开启了用户自定义参数的配置能力，您可以通过Resource中的alicloud_cs_kubernetes_addons修改更新您的组件配置，以gatekeeper组件为例，您可以通过修改config字段来修改组件配置。
展开查看详细信息
resource "alicloud_cs_kubernetes_addon" "gatekeeper" { cluster_id = "ce36b7c61e126430b8b245730ca6d****" name = "gatekeeper" version = "v3.8.1.113-geb7947ef-aliyun" # 您可以修改Config中的属性并应用，来修改集群组件配置。 }
如果您需要查看组件支持的全部可配置参数，可以通过Data Source中的alicloud_cs_kubernetes_addon_metadata进行查询，查询结果的返回值为JSON Schema格式，以gatekeeper组件为例，您可以将以下内容添加到.tf文件中。
