## 背景信息
Terraform是一种开源工具，通过Provider来支持新的基础架构，用于安全高效地预览、配置和管理云基础架构和资源。更多信息，请参见[了解阿里云](https://help.aliyun.com/zh/terraform/what-is-terraform#concept-vhk-wpc-rfb)[Terraform](https://help.aliyun.com/zh/terraform/what-is-terraform#concept-vhk-wpc-rfb)。
在[Alibaba Cloud Provider](https://registry.terraform.io/providers/aliyun/alicloud/latest)的老版本中，ACK提供了一个名为[alicloud_cs_kubernetes_autoscaler](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cs_kubernetes_autoscaler)的组件。alicloud_cs_kubernetes_autoscaler组件可以实现节点的弹性伸缩，但是其能力受限：
配置复杂，使用成本高。
伸缩的节点都会被放置到默认节点池，自动伸缩的节点未单独维护。
部分配置参数不可更改。
Alibaba Cloud Provider从1.111.0版本开始可通过组件[alicloud_cs_kubernetes_node_pool](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cs_kubernetes_node_pool)创建开启自动伸缩功能的节点池，优势如下：
配置简单，您只需要配置伸缩组内节点数的上下限。
针对非必须配置，ACK使用默认值的配置，以防误操作带来的基础环境不一致的问题，例如：操作系统镜像。
在ACK控制台中可以直观地观察节点池内节点的变化。
