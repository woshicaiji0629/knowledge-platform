## 常用处理配置
在完成[极简配置](collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)后，您可以通过添加processors插件进行处理配置，将原始日志进行结构化解析或脱敏、过滤处理。
核心配置：在[spec.config](kubernetes-cr-parameter-description.md)中添加processors，配置处理插件，支持同时启用多个插件。
此处仅介绍原生处理插件，覆盖常见日志处理场景，如需更多功能，请参考[扩展处理插件](developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md)。
重要
对于Logtail 2.0及以上版本以及LoongCollector组件，推荐遵循以下插件组合规则：
优先使用原生插件。
当原生插件无法满足需求时，可在原生插件后配置扩展插件。
原生插件只能在扩展插件之前使用。
