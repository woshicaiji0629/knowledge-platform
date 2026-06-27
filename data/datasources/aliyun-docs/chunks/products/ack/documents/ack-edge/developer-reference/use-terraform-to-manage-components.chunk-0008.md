{ name = "csi-plugin" } |
| csi-provisioner | 存储组件 | 支持数据卷的自动创建能力。创建集群时，如果选择 CSI 插件实现阿里云存储的接入能力的话，默认安装该组件。 | addons { name = "csi-plugin" } |
| storage-operator | 存储组件 | 用于管理存储组件的生命周期。 | addons { name = "storage-operator" } |
| alicloud-disk-controller | 存储组件 | 支持自动创建云盘卷。 | addons { name = "alicloud-disk-controller" } |
| flexvolume | 存储组件 | Kubernetes 社区较早实现的存储卷扩展机制。Flexvolume 支持数据卷的挂载、卸载功能。创建集群时，如果选择 Flexvolume 插件实现阿里云存储的接入能力的话，默认安装该组件。 | addons { name = "flexvolume" } |
| nginx-ingress-controller | 网络组件 | Nginx Ingress Controller 解析 Ingress 的转发规则。Ingress Controller 收到请求，匹配 Ingress 转发规则转发到后端 Service。 | ​ addons { name = "nginx-ingress-controller" } |
| terway-eniip | 网络组件 | 阿里云开源的基于专有网络 VPC 的容器网络接口 CNI（Container Network Interface）插件，支持基于 Kubernetes 标准的网络策略来定义容器间的访问策略。您可以通过使用 Terway 网络组件实现 Kubernetes 集群内部的网络互通。创建集群时，如果选择 Terway 网络插件实现集群内部网络互通的话，默认安装该组件。 | addons { name = "terway-eniip" } |
| ack-node-local-dns | 网络组件 | 基于社区开源项目 NodeLocal DNSCache 的一套 DNS 本地缓存解决方案。 | ​ addons { name = "ack-node-local-dns" } |
| aliyun-acr-credential-helper | 安全组件 | 可以在 ACK 集群中免密拉取 ACR 默认版或企业版私有镜像的组件。 | addons { name = "aliyun-acr-credential-helper" } |
| gatekeeper | 安全组件 | 帮助管理和应用集群内的 Open Policy
