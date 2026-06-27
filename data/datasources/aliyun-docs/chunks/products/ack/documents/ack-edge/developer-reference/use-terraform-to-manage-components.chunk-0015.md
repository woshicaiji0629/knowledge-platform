### 升级集群组件
您可以通过Data Source中的alicloud_cs_kubernetes_addons来查询组件可升级的版本，如果发现有新版本的组件可升级，可以通过直接修改版本号的方式进行升级，下面以gatekeeper组件为例说明。
展开查看详细信息
resource "alicloud_cs_kubernetes_addon" "gatekeeper" { cluster_id = "ce36b7c61e126430b8b245730ca6d****" name = "gatekeeper" # 修改Version为指定的可升级版本。 version = "XXXXXXXXX" config = jsonencode( { AdmissionPodCpuLimit = "1000m" AdmissionPodCpuRequest = "100m" AdmissionPodMemoryLimit = "512Mi" AdmissionPodMemoryRequest = "256Mi" AdmissionPodNumber = 3 AuditInterval = 1800 AuditPodCpuLimit = "1000m" AuditPodCpuRequest = "100m" AuditPodMemoryLimit = "512Mi" AuditPodMemoryRequest = "256Mi" EnableAuditPod = false EnableMutatingWebhook = false } ) }
执行命令terraform apply，进行组件升级，显示成功即完成了组件的升级。
