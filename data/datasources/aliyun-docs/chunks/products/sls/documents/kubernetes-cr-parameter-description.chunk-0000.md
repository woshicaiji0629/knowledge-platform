# AliyunPipelineConfig参数说明
当您使用[ClusterAliyunPipelineConfig](collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)创建日志采集配置时，需要通过一个结构化的YAML文件定义采集规则。本文介绍该YAML文件的整体结构及各字段的含义。
重要
CRD创建的采集配置内容请以CR为准，禁止在控制台修改，若在控制台进行修改，改动内容会被CR覆盖，可能导致数据格式异常或丢失。
