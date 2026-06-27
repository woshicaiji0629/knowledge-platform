# 定义Data Source获取gatekeeper组件的可配置参数Schema。 data "alicloud_cs_kubernetes_addon_metadata" "default" { cluster_id = "ce36b7c61e126430b8b245730ca6d****" name = "gatekeeper" version = "v3.8.1.113-geb7947ef-aliyun" } # 通过Output进行输出。 output "addon_config_schema" { value = data.alicloud_cs_kubernetes_addon_metadata.default.config_schema }
执行命令terraform apply，返回的结果为JSON Schema格式，其中properties属性定义了所有支持配置的参数。根据返回的Schema，您可以任意指定Schema中支持的配置参数。可配置的参数说明如下：
default：默认值。
description：参数的描述。
pattern：正则表达式（代表允许传递的值的格式）。
type：字段类型。
展开查看详细信息
addon_config_schema = <<EOT { "$schema": "http://json-schema.org/draft-07/schema#", "properties": { "AdmissionPodCpuLimit": { "default": "1000m", "description": "cpu limit for gatekeeper", "pattern": "^(|[1-9][0-9]*(m|\\.\\d+)?)$", "type": "string" }, "AdmissionPodCpuRequest": { "default": "100m", "description": "cpu request for gatekeeper", "pattern": "^[1-9][0-9]*(m|\\.\\d+)?$", "type": "string" }, "AdmissionPodMemoryLimit": { "default": "512Mi", "description": "memory limit for gatekeeper", "pattern": "^(|[1-9][0-9]*(\\.\\d+)?(K|Ki|M|Mi|G|Gi|T|Ti)?)$", "type": "string" }, ...... }, "title": "Config", "type": "object" } EOT
