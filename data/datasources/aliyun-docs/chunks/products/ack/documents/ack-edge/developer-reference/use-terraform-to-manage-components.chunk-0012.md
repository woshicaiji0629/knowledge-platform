### 将集群已安装的组件导入Terraform管理
对于集群已经安装的组件，您可以通过terraform import的方式，将组件导入Terraform进行管理。下面以nginx-ingress-controller组件为例说明如何将集群已安装的组件导入Terraform管理。
新建一个后缀名为.tf的文件或使用您已创建的.tf文件，并定义一个Resource。
Resource中的alicloud_cs_kubernetes_addon用于管理集群的Addon，其中不需要填写任何内容。
resource "alicloud_cs_kubernetes_addon" "nginx-ingress-controller" { }
执行以下命令，导入集群已安装的nginx-ingress-controller组件。
Terraform会拉取集群内的nginx-ingress-controller组件配置，并写入到后缀名为.state的文件中。
terraform import alicloud_cs_kubernetes_addon.nginx-ingress-controller <cluster_id>:nginx-ingress-controller
执行命令terraform plan，根据其得到的结果，您可以看到集群内nginx-ingress-controller组件配置和定义的Resource之间的差异。
根据差异的结果，以及.state后缀的文件内容，补充您在[步骤](use-terraform-to-manage-components.md)[1](use-terraform-to-manage-components.md)中写入的Resource信息。直到执行指令terraform plan，显示本地的配置与集群中的组件配置没有任何差异后，即完成了组件的导入。
resource "alicloud_cs_kubernetes_addon" "nginx-ingress-controller" { cluster_id = "XXXXX" name = "nginx-ingress-controller" version = "v1.2.1-aliyun.1" config = jsonencode( { IngressSlbNetworkType = "internet" IngressSlbSpec = "slb.s2.small" } ) }
