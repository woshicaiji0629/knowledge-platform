### 安装集群组件
您可以通过Resource中的alicloud_cs_kubernetes_addon在已有集群中安装组件，下面以gatekeeper组件为例说明。
在.tf文件中定义待安装组件的信息，需要指定以下信息。
集群ID。
组件名称和组件版本：
集群可安装的组件名称和组件版本可以通过Data Source中的alicloud_cs_kubernetes_addons查询，查询结果仅返回每个组件最新的可安装版本。如果您需要安装组件的历史版本，请查看对应组件的Release日志，并指定对应的组件版本号。
（可选）组件的自定义配置：
修改config字段进行组件自定义配置，可以使用Terraform内置的jsonencode方法来构建您需要的配置。组件的可配置参数可以通过Data Source中的alicloud_cs_kubernetes_addon_metadata进行查询，具体操作，请参见[修改集群组件的自定义配置参数](use-terraform-to-manage-components.md)。
展开查看详细信息
resource "alicloud_cs_kubernetes_addon" "gatekeeper" { cluster_id = "ce36b7c61e126430b8b245730ca6d****" name = "gatekeeper" version = "v3.8.1.113-geb7947ef-aliyun" config = jsonencode( { AdmissionPodCpuLimit = "1000m" AdmissionPodCpuRequest = "100m" AdmissionPodMemoryLimit = "512Mi" AdmissionPodMemoryRequest = "256Mi" AdmissionPodNumber = 3 AuditInterval = 1800 AuditPodCpuLimit = "1000m" AuditPodCpuRequest = "100m" AuditPodMemoryLimit = "512Mi" AuditPodMemoryRequest = "256Mi" EnableAuditPod = false EnableMutatingWebhook = false } ) }
执行以下命令，在集群中安装组件。
terraform apply
预期输出：
Plan: 1 to add, 0 to change, 0 to destroy. Do you want to perform these actions? Terraform will perform the actions described above. Only 'yes' wil
