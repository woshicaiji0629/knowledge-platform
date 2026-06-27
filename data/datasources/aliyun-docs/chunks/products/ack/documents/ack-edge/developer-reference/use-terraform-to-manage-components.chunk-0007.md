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
| storage-operator
