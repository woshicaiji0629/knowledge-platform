# Terraform管理组件配置与生命周期-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/developer-reference/use-terraform-to-manage-components

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-edge/product-overview.md)

- [快速入门](products/ack/documents/ack-edge/quick-start.md)

- [操作指南](products/ack/documents/ack-edge/user-guide.md)

- [实践教程](products/ack/documents/ack-edge/use-cases.md)

- [安全合规](products/ack/documents/ack-edge/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-edge/developer-reference.md)

- [服务支持](products/ack/documents/ack-edge/support.md)

[首页](https://help.aliyun.com/zh)

# 使用Terraform管理组件

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

容器服务 Kubernetes 版提供丰富的组件，用于扩展集群功能。本文介绍如何在Terraform中配置组件，以帮助您在多场景下完成业务的管理。

## 组件类型

容器服务ACK管理的集群组件类型包括系统组件和可选组件。更多组件信息，请参见[组件](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/component-overview.md)。

### 系统组件

系统组件是运行ACK集群所依赖的基础组件，创建集群时会默认安装。例如：

- 

kube-apiserver

- 

kube-controller-manager

- 

cloud-controller-manager

- 

kube-proxy

- 

CoreDNS

### 可选组件

可选组件是ACK提供的非必需部署的组件，您可选择性地安装组件，用于扩展集群功能。可选组件在类型上可划分为应用管理组件、日志与监控管理组件、存储组件、网络组件及安全组件等。

## 通过控制台生成管理组件Terraform调用参数

您可以通过控制台生成Terraform调用组件参数配置，帮助您在实践中提升组件管理的效率和操作性。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。

- 

在组件管理页面，您可以搜索并定位目标组件，在组件卡片上按需单击安装或配置。

- 

在弹框中，单击同等代码，然后在右侧面板，单击Terraform页签，将显示您安装或配置组件的相关参数，您可以复制使用。

## 组件管理实践

通过Terraform，您可以在创建集群时指定需要安装的组件，并在集群创建结束后对组件进行全生命周期管理，下面将介绍如何管理集群中的组件生命周期，以及一些场景下的最佳实践。

### 在创建集群时指定需要安装的组件

您可以在创建集群时，指定集群需要安装的组件，创建集群涉及的Resource如下：

- 

Kubernetes托管版集群：alicloud_cs_managed_kubernetes

- 

Kubernetes专有版集群：alicloud_cs_kubernetes

- 

ACK Edge集群：alicloud_cs_edge_kubernetes

- 

ACK Serverless集群：alicloud_cs_serverless_kubernetes

以上Resource均可以通过addons属性定义创建集群时需要安装的组件，addons属性定义如下：

# 以托管版集群为例。 resource "alicloud_cs_managed_kubernetes" "default" { # 其它参数。 # ... # addons为list结构，通过在Resource中定义addons属性，表明创建集群时安装该组件。 addons { # 组件的名称，您可以通过Data Source中的alicloud_cs_kubernetes_addons查询。 # 当前集群已经安装的，以及可以安装的组件和其对应版本信息。 name = "XXX" # 组件的自定义参数，某些集群组件开启了自定义参数配置的能力，您可以使用该字段来为组件指定其自定义参数，具体指定方法，请参见下文“修改集群组件的自定义配置参数”一节。 config = jsonencode( { .... } ) # 该参数默认值为false（布尔值类型），ACK会默认安装部分组件，方便用户管理集群。若您在创建集群时不需安装这些组件，可设置disabled=true。 disabled = XXX } }

重要

通过在集群相关Resource中指定Addons的方式安装组件，仅支持在创建集群时指定安装，集群创建完成后，不支持通过修改Addons代码块中的属性来管理组件的生命周期，比如组件升级、组件卸载、组件配置更新等操作。若您需要在创建集群后管理组件生命周期，请参见下文[在创建集群后管理组件生命周期](products/ack/documents/ack-edge/developer-reference/use-terraform-to-manage-components.md)。

ACK中组件配置方式如下表所示。

| 组件名称 | 组件类型 | 组件描述 | Terraform 中配置组件 |
| --- | --- | --- | --- |
| appcenter | 应用管理 | 提供统一管理多集群应用部署和应用生命周期的应用中心组件。 | addon { name = "appcenter" } |
| progressive-delivery-tool | 应用管理 | 提供应用渐进式灰度发布的组件。 | addon { name = "progressive-delivery-tool" } |
| alicloud-monitor-controller | 日志与监控 | ACK 提供对接云监控的系统组件。 | addon { name = "alicloud-monitor-controller" } |
| metrics-server | 日志与监控 | ACK 基于社区开源监控组件进行改造和增强的监控采集和离线组件，并提供 Metrics API 进行数据消费，提供 HPA 的能力。 | addon { name = "metrics-server" } |
| ack-node-problem-detector | 日志与监控 | ACK 基于社区开源项目进行改造和增强的集群节点异常事件监控组件，以及对接第三方监控平台功能的组件。 | addons { name = "ack-node-problem-detector" } |
| ags-metrics-collector | 日志与监控 | 为基因计算客户使用的监控服务组件，可以通过该组件监控基因工作流中各个节点资源使用的详细信息。 | addons { name = "ags-metrics-collector" } |
| ack-arms-prometheus | 日志与监控 | 使用 阿里云 Prometheus 实现容器服务集群监控。 | addons { name = "arms-prometheus" } |
| loongcollector | 日志与监控 | 使用日志服务采集 Kubernetes 容器日志。 | ​ addons { name = "loongcollector" } |
| csi-plugin | 存储组件 | 支持数据卷的挂载、卸载功能。创建集群时，如果选择 CSI 插件实现阿里云存储的接入能力，则默认安装该组件。 | addons { name = "csi-plugin" } |
| csi-provisioner | 存储组件 | 支持数据卷的自动创建能力。创建集群时，如果选择 CSI 插件实现阿里云存储的接入能力的话，默认安装该组件。 | addons { name = "csi-plugin" } |
| storage-operator | 存储组件 | 用于管理存储组件的生命周期。 | addons { name = "storage-operator" } |
| alicloud-disk-controller | 存储组件 | 支持自动创建云盘卷。 | addons { name = "alicloud-disk-controller" } |
| flexvolume | 存储组件 | Kubernetes 社区较早实现的存储卷扩展机制。Flexvolume 支持数据卷的挂载、卸载功能。创建集群时，如果选择 Flexvolume 插件实现阿里云存储的接入能力的话，默认安装该组件。 | addons { name = "flexvolume" } |
| nginx-ingress-controller | 网络组件 | Nginx Ingress Controller 解析 Ingress 的转发规则。Ingress Controller 收到请求，匹配 Ingress 转发规则转发到后端 Service。 | ​ addons { name = "nginx-ingress-controller" } |
| terway-eniip | 网络组件 | 阿里云开源的基于专有网络 VPC 的容器网络接口 CNI（Container Network Interface）插件，支持基于 Kubernetes 标准的网络策略来定义容器间的访问策略。您可以通过使用 Terway 网络组件实现 Kubernetes 集群内部的网络互通。创建集群时，如果选择 Terway 网络插件实现集群内部网络互通的话，默认安装该组件。 | addons { name = "terway-eniip" } |
| ack-node-local-dns | 网络组件 | 基于社区开源项目 NodeLocal DNSCache 的一套 DNS 本地缓存解决方案。 | ​ addons { name = "ack-node-local-dns" } |
| aliyun-acr-credential-helper | 安全组件 | 可以在 ACK 集群中免密拉取 ACR 默认版或企业版私有镜像的组件。 | addons { name = "aliyun-acr-credential-helper" } |
| gatekeeper | 安全组件 | 帮助管理和应用集群内的 Open Policy Agent（OPA）策略，实现命名空间标签管理等功能。 | addons { name = "gatekeeper" } |
| kritis-validation-hook | 安全组件 | 部署可信容器环节中进行容器镜像签名验证的关键组件。 | addons { name = "kritis-validation-hook" } ​ |
| security-inspector | 安全组件 | 实现安全巡检功能的关键组件。 | addons { name = "security-inspector" } |
| ack-kubernetes-webhook-injector | 安全组件 | 一款可以从多种阿里云产品白名单中动态加入或移出 Pod IP 的 K8s 组件，免去手动配置 Pod IP 到云产品白名单的操作。 | addons { name = "ack-kubernetes-webhook-injector" } |
| ack-arena | 其他 | 对开源 Arena 的安装做进一步简化，能够实现在控制台一键安装 Arena 的目标。 | addons { name = "ack-arena" } |
| ack-cost-exporter | 其他 | 容器服务 ACK 成本分析功能进行数据处理的插件。 | addons { name = "ack-cost-exporter" } |
| ack-kubernetes-cronhpa-controller | 其他 | 使用 ack-kubernetes-cronhpa-controller 实现应用负载定时伸缩。 | addons { name = "ack-kubernetes-cronhpa-controller" } |
| ack-virtual-node | 其他 | 基于社区开源项目 Virtual Kubelet，扩展了对 Aliyun Provider 的支持，并做了大量优化，实现 Kubernetes 与弹性容器实例 ECI 的无缝连接。 | addons { name = "ack-virtual-node" } |
| aesm | 其他 | Intel® SGX Architectural Enclave Service Manager (Intel® SGX AESM) 是 Intel® SGX 的系统组件，主要提供了 SGX Enclave 启动支持，密钥配置、远程认证等服务。 | addons { name = "aesm" } |
| aliyun-acr-acceleration-suite | 其他 | 提供镜像按需加载加速能力的客户端插件，以 DaemonSet 形式部署在 Worker 节点上。 | addons { name = "aliyun-acr-acceleration-suite" } |
| migrate-controller | 其他 | 基于开源项目 Velero 开发的一个 Kubernetes 应用迁移的组件。 | addons { name = "migrate-controller" } |
| resource-controller | 其他 | 实现动态控制 Pod 资源的关键组件，使用 ACK Pro 集群的 CPU 拓扑感知调度需要安装此组件。 | addons { name = "resource-controller" } |
| sandboxed-container-controller | 其他 | 安全沙箱运行时提供的专用控制器组件，旨在增强和扩展安全沙箱的基本功能。 | addons { name = "sandboxed-container-controller" } |
| sandboxed-container-helper | 其他 | 为安全沙箱提供诊断和运维的组件。 | addons { name = "sandboxed-container-helper" } |
| sgx-device-plugin | 其他 | 由阿里云容器服务团队和蚂蚁金服安全计算团队针对 Intel SGX 联合开发的 Kubernetes Device Plugin，可以让您更方便地在容器中使用 SGX。 | addons { name = "sgx-device-plugin" } |


### 在创建集群后管理组件生命周期

管理组件的生命周期前提是您已经创建了一个Kubernetes集群，如果您还没有创建Kubernetes集群，请先创建集群。

对于集群中的组件，您可以通过Resource中的alicloud_cs_kubernetes_addon来管理组件的生命周期，包括组件的安装、升级、卸载、自定义配置的修改。alicloud_cs_kubernetes_addon的属性和定义如下：

resource "alicloud_cs_kubernetes_addon" "addon-example" { # 集群ID。 cluster_id = "XXXX" # 组件的名称，可以通过Data Source中的alicloud_cs_kubernetes_addons，查询当前集群所有已安装的以及可以安装的组件和其对应版本信息。 name = "XXXX" # 组件的版本信息。 version = "XXXX" # 组件的自定义参数，为JSON格式的字符串，可以使用Terraform自带的jsonencode方法进行配置，也可以直接使用JSON字符串进行配置（需要注意转义），某些集群组件开启了自定义参数配置的能力，您可以使用该字段来为组件指定其自定义参数，具体指定方法，请参见下文“修改集群组件的自定义配置参数”一节 。 config = jsonencode( { .... } ) }

您可以通过直接写入JSON字符串的方式配置组件自定义参数，但是需要注意转义。例如对于nginx-ingress-controller组件，有以下两种配置方法：

- 

通过jsonencode配置参数：

config = jsonencode( { IngressSlbNetworkType="internet" IngressSlbSpec="slb.s2.small" } )

- 

通过直接使用字符串的方式配置参数：

config = "{\"IngressSlbNetworkType\":\"internet\",\"IngressSlbSpec\":\"slb.s2.small\"}"

### 将集群已安装的组件导入Terraform管理

对于集群已经安装的组件，您可以通过terraform import的方式，将组件导入Terraform进行管理。下面以nginx-ingress-controller组件为例说明如何将集群已安装的组件导入Terraform管理。

- 

新建一个后缀名为.tf的文件或使用您已创建的.tf文件，并定义一个Resource。

Resource中的alicloud_cs_kubernetes_addon用于管理集群的Addon，其中不需要填写任何内容。

resource "alicloud_cs_kubernetes_addon" "nginx-ingress-controller" { }

- 

执行以下命令，导入集群已安装的nginx-ingress-controller组件。

Terraform会拉取集群内的nginx-ingress-controller组件配置，并写入到后缀名为.state的文件中。

terraform import alicloud_cs_kubernetes_addon.nginx-ingress-controller <cluster_id>:nginx-ingress-controller

- 

执行命令terraform plan，根据其得到的结果，您可以看到集群内nginx-ingress-controller组件配置和定义的Resource之间的差异。

根据差异的结果，以及.state后缀的文件内容，补充您在[步骤](products/ack/documents/ack-edge/developer-reference/use-terraform-to-manage-components.md)[1](products/ack/documents/ack-edge/developer-reference/use-terraform-to-manage-components.md)中写入的Resource信息。直到执行指令terraform plan，显示本地的配置与集群中的组件配置没有任何差异后，即完成了组件的导入。

resource "alicloud_cs_kubernetes_addon" "nginx-ingress-controller" { cluster_id = "XXXXX" name = "nginx-ingress-controller" version = "v1.2.1-aliyun.1" config = jsonencode( { IngressSlbNetworkType = "internet" IngressSlbSpec = "slb.s2.small" } ) }

### 安装集群组件

您可以通过Resource中的alicloud_cs_kubernetes_addon在已有集群中安装组件，下面以gatekeeper组件为例说明。

- 

在.tf文件中定义待安装组件的信息，需要指定以下信息。

- 

集群ID。

- 

组件名称和组件版本：

集群可安装的组件名称和组件版本可以通过Data Source中的alicloud_cs_kubernetes_addons查询，查询结果仅返回每个组件最新的可安装版本。如果您需要安装组件的历史版本，请查看对应组件的Release日志，并指定对应的组件版本号。

- 

（可选）组件的自定义配置：

修改config字段进行组件自定义配置，可以使用Terraform内置的jsonencode方法来构建您需要的配置。组件的可配置参数可以通过Data Source中的alicloud_cs_kubernetes_addon_metadata进行查询，具体操作，请参见[修改集群组件的自定义配置参数](products/ack/documents/ack-edge/developer-reference/use-terraform-to-manage-components.md)。

展开查看详细信息

resource "alicloud_cs_kubernetes_addon" "gatekeeper" { cluster_id = "ce36b7c61e126430b8b245730ca6d****" name = "gatekeeper" version = "v3.8.1.113-geb7947ef-aliyun" config = jsonencode( { AdmissionPodCpuLimit = "1000m" AdmissionPodCpuRequest = "100m" AdmissionPodMemoryLimit = "512Mi" AdmissionPodMemoryRequest = "256Mi" AdmissionPodNumber = 3 AuditInterval = 1800 AuditPodCpuLimit = "1000m" AuditPodCpuRequest = "100m" AuditPodMemoryLimit = "512Mi" AuditPodMemoryRequest = "256Mi" EnableAuditPod = false EnableMutatingWebhook = false } ) }

- 

执行以下命令，在集群中安装组件。

terraform apply

预期输出：

Plan: 1 to add, 0 to change, 0 to destroy. Do you want to perform these actions? Terraform will perform the actions described above. Only 'yes' will be accepted to approve. Enter a value: yes alicloud_cs_kubernetes_addon.gatekeeper: Creating... alicloud_cs_kubernetes_addon.gatekeeper: Still creating... [10s elapsed] alicloud_cs_kubernetes_addon.gatekeeper: Creation complete after 16s [id=XXXXX:gatekeeper] Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

直到显示Apply complete!，说明组件安装完成。

### 升级集群组件

您可以通过Data Source中的alicloud_cs_kubernetes_addons来查询组件可升级的版本，如果发现有新版本的组件可升级，可以通过直接修改版本号的方式进行升级，下面以gatekeeper组件为例说明。

展开查看详细信息

resource "alicloud_cs_kubernetes_addon" "gatekeeper" { cluster_id = "ce36b7c61e126430b8b245730ca6d****" name = "gatekeeper" # 修改Version为指定的可升级版本。 version = "XXXXXXXXX" config = jsonencode( { AdmissionPodCpuLimit = "1000m" AdmissionPodCpuRequest = "100m" AdmissionPodMemoryLimit = "512Mi" AdmissionPodMemoryRequest = "256Mi" AdmissionPodNumber = 3 AuditInterval = 1800 AuditPodCpuLimit = "1000m" AuditPodCpuRequest = "100m" AuditPodMemoryLimit = "512Mi" AuditPodMemoryRequest = "256Mi" EnableAuditPod = false EnableMutatingWebhook = false } ) }

执行命令terraform apply，进行组件升级，显示成功即完成了组件的升级。

### 修改集群组件的自定义配置参数

ACK的某些组件开启了用户自定义参数的配置能力，您可以通过Resource中的alicloud_cs_kubernetes_addons修改更新您的组件配置，以gatekeeper组件为例，您可以通过修改config字段来修改组件配置。

展开查看详细信息

resource "alicloud_cs_kubernetes_addon" "gatekeeper" { cluster_id = "ce36b7c61e126430b8b245730ca6d****" name = "gatekeeper" version = "v3.8.1.113-geb7947ef-aliyun" # 您可以修改Config中的属性并应用，来修改集群组件配置。 }

如果您需要查看组件支持的全部可配置参数，可以通过Data Source中的alicloud_cs_kubernetes_addon_metadata进行查询，查询结果的返回值为JSON Schema格式，以gatekeeper组件为例，您可以将以下内容添加到.tf文件中。

# 定义Data Source获取gatekeeper组件的可配置参数Schema。 data "alicloud_cs_kubernetes_addon_metadata" "default" { cluster_id = "ce36b7c61e126430b8b245730ca6d****" name = "gatekeeper" version = "v3.8.1.113-geb7947ef-aliyun" } # 通过Output进行输出。 output "addon_config_schema" { value = data.alicloud_cs_kubernetes_addon_metadata.default.config_schema }

执行命令terraform apply，返回的结果为JSON Schema格式，其中properties属性定义了所有支持配置的参数。根据返回的Schema，您可以任意指定Schema中支持的配置参数。可配置的参数说明如下：

- 

default：默认值。

- 

description：参数的描述。

- 

pattern：正则表达式（代表允许传递的值的格式）。

- 

type：字段类型。

展开查看详细信息

addon_config_schema = <<EOT { "$schema": "http://json-schema.org/draft-07/schema#", "properties": { "AdmissionPodCpuLimit": { "default": "1000m", "description": "cpu limit for gatekeeper", "pattern": "^(|[1-9][0-9]*(m|\\.\\d+)?)$", "type": "string" }, "AdmissionPodCpuRequest": { "default": "100m", "description": "cpu request for gatekeeper", "pattern": "^[1-9][0-9]*(m|\\.\\d+)?$", "type": "string" }, "AdmissionPodMemoryLimit": { "default": "512Mi", "description": "memory limit for gatekeeper", "pattern": "^(|[1-9][0-9]*(\\.\\d+)?(K|Ki|M|Mi|G|Gi|T|Ti)?)$", "type": "string" }, ...... }, "title": "Config", "type": "object" } EOT

## 配置网络组件

在ACK中，您可以通过Terway网络模式实现上述容器网络的能力。更多信息，请参见[网络](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/network.md)。

下面展示如何通过Terraform配置网络组件。

展开查看详细信息

# 使用Terway作为网络组件，并且使用Pod独占弹性网卡模式，默认此方式。 # 该模式下，节点Pod数量将受到ECS弹性网卡配额限制。 resource "alicloud_cs_managed_kubernetes" "default" { # 其它参数。 # ... addons { name = "terway-eni" } } # 使用Terway作为网络组件，并且使用IPVlan模式。 # 采用IPVlan + ebpf作为网卡共享模式虚拟化技术，只能使用Alibaba Cloud Linux 2系统。 resource "alicloud_cs_managed_kubernetes" "default" { # 其它参数。 # ... addons { name = "terway-eniip", config = "{\"IPVlan\":\"true\",\"NetworkPolicy\":\"false\"}" } } # 使用Terway作为网络组件，并且IPVlan模式下启用NetworkPolicy策略支持。 # 采用IPVlan + ebpf作为网卡共享模式虚拟化技术，只能使用Alibaba Cloud Linux 2系统。 # IPVlan模式下，提供了基于策略的网络控制。 resource "alicloud_cs_managed_kubernetes" "default" { # 其它参数。 # ... addons { name = "terway-eniip", config = "{\"IPVlan\":\"true\",\"NetworkPolicy\":\"true\"}" } }

## 配置存储组件

ACK提供的存储组件，支持Flexvolume和CSI两种。Flexvolume已经停止维护，ACK主要维护CSI存储组件。如果通过Terraform创建集群时，不指定任何存储组件，默认会安装CSI。在Terraform中通过以下方式进行存储组件定义。

展开查看详细信息

# 使用CSI作为存储组件时，CSI包含csi-plugin、csi-provisioner；如果还想启用创建默认的NAS文件系统和CNFS容器网络文件系统动态存储类型，还需要安装storage-operator组件。 resource "alicloud_cs_managed_kubernetes" "default" { # 其它参数。 # ... addons { name = "csi-plugin" } addons { name = "csi-provisioner" } addons { name = "storage-operator" config = "{\"CnfsOssEnable\":\"false\",\"CnfsNasEnable\":\"true\"}" } }

## 配置日志组件

ACK提供的日志采集组件，是将采集到的日志存储在SLS中。ACK提供的日志组件支持以下两种日志存储方式：

- 

支持指定已有SLS Project作为日志存储。

- 

支持创建集群时自动创建新的SLS Project作为日志存储。

两种不同场景下的配置也有区别，下面通过一个Terraform示例说明：

展开查看详细信息

# 使用自动创建SLS Project作为日志存储。 resource "alicloud_cs_managed_kubernetes" "default" { # 其它参数。 # ... addons { name = "loongcollector" } } # 使用自动创建SLS Project做日志存储。同时开启自动创建Ingress看板。 resource "alicloud_cs_managed_kubernetes" "default" { # 其它参数。 # ... addons { name = "loongcollector" config = "{\"IngressDashboardEnabled\":\"true\"}" } } # 使用已有SLS Project做日志存储。同时开启自动创建Ingress看板。 resource "alicloud_cs_managed_kubernetes" "default" { # 其它参数。 # ... addons { name = "loongcollector" config = "{\"IngressDashboardEnabled\":\"true\",\"sls_project_name\":\"k8s-log-c55c35ff493df47b88783bea48827****\"}" } } # 安装配置node-problem-detector事件中心。 # 使用自动创建SLS Project作为事件中心的日志存储。 resource "alicloud_cs_managed_kubernetes" "default" { # 其它参数。 # ... addons { name = "ack-node-problem-detector" config = "{\"sls_project_name\":\"\"}" } } # 安装配置node-problem-detector事件中心。 # 使用已有SLS Project作为事件中心的日志存储。可以和loongcollector共用同一个日志库。 resource "alicloud_cs_managed_kubernetes" "default" { # 其它参数。 # ... addons { name = "ack-node-problem-detector" config = "{\"sls_project_name\":\"k8s-log-c55c35ff493df47b88783bea48827****\"}" } }

## 配置监控组件

ACK提供的监控组件包括ECS节点上安装的云监控插件和Prometheus监控服务。在Terraform中安装ECS节点上安装的云监控插件是通过参数install_cloud_monitor来控制的。

展开查看详细信息

# 安装Prometheus监控。 resource "alicloud_cs_managed_kubernetes" "default" { # 其它参数。 # ... addons { name = "arms-prometheus" } } # 安装ECS节点上安装的云监控插件。 resource "alicloud_cs_kubernetes_node_pool" "default" { # 其它参数。 # ... install_cloud_monitor = true }

## 配置Ingess路由组件

ACK提供的流量接入方案，包括Nginx Ingress和ALB Ingress。

- 

Nginx Ingress组件：基于社区版的ingress-nginx进行了优化，为您的Kubernetes集群提供灵活可靠的路由服务。更多信息，请参见[Nginx Ingress](products/ack/documents/serverless-kubernetes/user-guide/overview-2.md)[概述](products/ack/documents/serverless-kubernetes/user-guide/overview-2.md)。

- 

ALB Ingress组件：是全托管并且高可靠的ALB Ingress组件，为您的Kubernetes集群提供灵活可靠的路由服务。更多信息，请参见[通过](products/ack/documents/serverless-kubernetes/user-guide/access-services-by-using-an-alb-ingress-2.md)[ALB Ingress](products/ack/documents/serverless-kubernetes/user-guide/access-services-by-using-an-alb-ingress-2.md)[访问服务](products/ack/documents/serverless-kubernetes/user-guide/access-services-by-using-an-alb-ingress-2.md)。

通过Terraform配置路由组件的示例如下：

展开查看详细信息

# 使用nginx-ingress-controller路由。 # 如果使用公网的SLB，需要在Config中设置IngressSlbNetworkType值为internet。 # 如果使用私网的SLB，需要在Config中设置IngressSlbNetworkType值为intranet。 resource "alicloud_cs_managed_kubernetes" "default" { # 其它参数。 # ... addons { name = "nginx-ingress-controller", config = "{\"IngressSlbNetworkType\":\"internet\",\"IngressSlbSpec\":\"slb.s2.small\"}" } } # 使用ALB Ingress路由。 resource "alicloud_cs_managed_kubernetes" "default" { # 其它参数。 # ... addons { name = "alb-ingress-controller", config = "{\"albIngress\":{\"CreateDefaultALBConfig\":false}}" # 暂不创建。 # config = "{\"albIngress\":{\"LoadBalancerId\":\"alb-vl8uiXXXXXxdr\",\"CreateDefaultALBConfig\":true}}" # 指定已有ALB实例。 # config = "{\"albIngress\":{\"AddressType\":\"Internet\",\"ZoneMappings\":{\"cn-hangzhou-l\":[\"vsw-uf6XXXXXoyb4qe\"],\"cn-hangzhou-m\":[\"vsw-uf6XXXX0rlkiq\"]},\"CreateDefaultALBConfig\":true}}" # 新建，至少需要选择两个及以上的可用区。 } }

## 禁用默认安装的组件

ACK会默认安装部分组件，方便您管理集群，如果您在创建集群的时候，不需要安装这些组件，可以通过设置字段为disabled = true来禁用这些组件。下面以禁用nginx-ingress-controller为例说明：

# 禁止安装nginx-ingress-controller组件。 resource "alicloud_cs_managed_kubernetes" "default" { # 其它参数。 # ... addons { name = "nginx-ingress-controller", disabled = true } }

## 未指定Addons的情况下默认安装的组件

如果集群创建时，没有指定任何Addons，会默认安装以下组件。

| 集群类型 | 组件类型 | 默认安装组件名称 | 组件描述 |
| --- | --- | --- | --- |
| ACK 集群 | 系统组件 | kube-scheduler | 使用 Kube Scheduler 进行集群资源调度。 |
| cloud-controller-manager | 使用 Cloud Controller Manager 为 K8s 应用创建负载均衡，管理节点路由条目。 |  |  |
| kube-apiserver | APIServer 是 K8s 集群的总线和入口网关。 |  |  |
| kube-controller-manager | KCM 是 K8s 集群内部资源的管理器。 |  |  |
| 日志与监控 | alicloud-monitor-controller | 监控应用容器的生命周期和状态变化。 |  |
| metrics-server | Metrics Server 为集群的自动伸缩机制提供应用容器的资源监控指标。 |  |  |
| 存储 | csi-plugin | 使用 csi-plugin 插件实现存储卷生命周期管理（推荐）。 |  |
| csi-provisioner | 使用 csi-provisioner 插件实现存储卷创建和删除（推荐）。 |  |  |
| storage-operator | 使用 storage-operator 插件实现存储运维管理（推荐）。 |  |  |
| 网络 | CoreDNS | Kubernetes 集群域名解析服务器。 |  |
| Gateway API | Gateway API 网关资源模型。 |  |  |
| terway-eniip | Terway 网络插件。 |  |  |
| nginx-ingress-controller（Pro 版默认安装） | 基于 Nginx 流量转发的 Ingress 控制器。 |  |  |
| ACK Serverless 集群 | 系统组件 | kube-scheduler | 使用 Kube Scheduler 进行集群资源调度。 |
| ack-virtual-node | 使用虚拟节点和 ECI 弹性能力。 |  |  |
| cloud-controller-manager | 使用 Cloud Controller Manager 为 K8s 应用创建负载均衡，管理节点路由条目。 |  |  |
| kube-apiserver | APIServer 是 K8s 集群的总线和入口网关。 |  |  |
| kube-controller-manager | KCM 是 K8s 集群内部资源的管理器。 |  |  |
| 网络 | CoreDNS | K8s 集群域名解析服务器。 |  |
| ACK Edge 集群 | 系统组件 | kube-scheduler | 使用 Kube Scheduler 进行集群资源调度 |
| cloud-controller-manager | 使用 Cloud Controller Manager 为 K8s 应用创建负载均衡，管理节点路由条目。 |  |  |
| kube-apiserver | APIServer 是 K8s 集群的总线和入口网关。 |  |  |
| kube-controller-manager | KCM 是 K8s 集群内部资源的管理器。 |  |  |
| 日志与监控 | alicloud-monitor-controller | 监控应用容器的生命周期和状态变化。 |  |
| metrics-server | Metrics Server 为集群的自动伸缩机制提供应用容器的资源监控指标 |  |  |
| 网络 | CoreDNS | Kubernetes 集群域名解析服务器。 |  |
| terway-eniip | Terway 网络插件。 |  |  |
| 其他 | edge-controller-manager | - |  |
| edge-tunnel-agent | Edge-tunnel 采用 C/S 架构，构建云边反向运维通道。 |  |  |
| edge-tunnel-server | Edge-tunnel 采用 C/S 架构，构建云边反向运维通道。 |  |  |
| yurt-app-manager | 使用 yurt-app-manager 为 ACK@Edge 提供节点池和单元化部署的功能。 |  |  |


## 常用配置示例

以下列出了部分通用示例，供参考使用。

- 

网络组件选择Terway。

- 

存储组件CSI和Flexvolume选择一个即可，由于Flexvolume已停止维护，建议使用CSI作为存储组件。

- 

路由组件Nginx-Ingress和ALB Ingress选择一个即可，根据业务需求进行合理选择。

- 

其他组件可以根据业务需求选择性安装，可以自由组合。

示例一：不配置任何组件

# 集群创建不配置任何组件，则仅安装默认组件。 # 一个集群的最简配置，变量请替换为您自定义的变量。 resource "alicloud_cs_managed_kubernetes" "default" { name = var.name cluster_spec = "ack.pro.small" is_enterprise_security_group = true pod_cidr = "172.20.0.0/16" service_cidr = "172.21.0.0/20" worker_vswitch_ids = [var.vswitch_id] }

示例二：使用Terway网络

# 创建Terway网络集群。 # 使用Pod独占弹性网卡模式。 resource "alicloud_cs_managed_kubernetes" "default" { name = var.name cluster_spec = "ack.pro.small" is_enterprise_security_group = true pod_vswitch_ids = [var.vswitch_id] service_cidr = "172.21.0.0/20" worker_vswitch_ids = [var.vswitch_id] addons { name = "terway-eni" } } # 创建Terway网络集群。 # 同时使用IPVlan模式，并且开启网络策略。 resource "alicloud_cs_managed_kubernetes" "default" { name = var.name cluster_spec = "ack.pro.small" is_enterprise_security_group = true service_cidr = "172.21.0.0/20" pod_vswitch_ids = [var.vswitch_id] worker_vswitch_ids = [var.vswitch_id] addons { name = "terway-eniip" config = "{\"IPVlan\":\"true\",\"NetworkPolicy\":\"true\"}" } }

示例三：使用Terway、CSI和nginx-ingress的通用模板

# Terway + CSI + nginx-ingress通用模板。 resource "alicloud_cs_managed_kubernetes" "default" { name = var.name cluster_spec = "ack.pro.small" is_enterprise_security_group = true service_cidr = "172.21.0.0/20" pod_vswitch_ids = [var.vswitch_id] worker_vswitch_ids = [var.vswitch_id] addons { name = "terway-eniip", config = "{\"IPVlan\":\"true\",\"NetworkPolicy\":\"false\"}" } addons { name = "csi-plugin" } addons { name = "csi-provisioner" } addons { name = "storage-operator" config = "{\"CnfsOssEnable\":\"false\",\"CnfsNasEnable\":\"true\"}" } addons { name = "loongcollector" config = "{\"IngressDashboardEnabled\":\"true\"}" } addons { name = "ack-node-problem-detector" config = "{\"sls_project_name\":\"\"}" } addons { name = "nginx-ingress-controller" config = "{\"IngressSlbNetworkType\":\"internet\",\"IngressSlbSpec\":\"slb.s2.small\"}" } addons { name = "ack-node-local-dns" } addons { name = "arms-prometheus" } addons { name = "alicloud-monitor-controller" config = "{\"group_contact_ids\":\"[10619]\"}" } }

[上一篇：通过Terraform创建具备自动伸缩功能的节点池](products/ack/documents/ack-edge/developer-reference/use-terraform-to-create-an-auto-scaling-node-pool.md)[下一篇：服务支持](products/ack/documents/ack-edge/support.md)

该文章对您有帮助吗？

反馈

### 为什么选择阿里云

[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)

### 大模型

[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)

### 产品和定价

[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)

### 技术内容

[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)

### 权益

[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)

### 服务

[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)

### 关注阿里云

关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务

联系我们：4008013260

[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)

### 友情链接

[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)

© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )

[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
