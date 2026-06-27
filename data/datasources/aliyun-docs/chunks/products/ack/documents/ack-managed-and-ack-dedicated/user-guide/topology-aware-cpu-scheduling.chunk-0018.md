## 费用说明
ack-koordinator组件本身的安装和使用免费，但在以下场景中可能产生额外费用。
ack-koordinator是非托管组件，安装后将占用Worker节点资源。您可以在安装组件时配置各模块的资源申请量。
ack-koordinator默认会将资源画像、精细化调度等功能的监控指标以Prometheus的格式对外透出。若您配置组件时开启了ACK-Koordinator开启Prometheus监控指标选项并使用了阿里云Prometheus服务，这些指标将被视为[自定义指标](../../../../arms/documents/prometheus-monitoring/basic-metrics.md)并产生相应费用。具体费用取决于您的集群规模和应用数量等因素。建议您在启用此功能前，仔细阅读阿里云Prometheus[Prometheus 实例计费](../../../../arms/documents/prometheus-monitoring/product-overview/billing-description.md)，了解自定义指标的免费额度和收费策略。您可以通过[用量查询](../../../../arms/documents/prometheus-monitoring/product-overview/billing-and-usage-query.md)，监控和管理您的资源使用情况。
