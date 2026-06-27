Pod的标签，当前条件指定标签键为app，值中包含test的Pod会被采集。
说明
如果需要采集集群中名称包含test的所有Pod，可以将IncludeK8sLabel替换为K8sContainerRegex，并使用通配符配置值，如：K8sContainerRegex: ^(.test.)$。
FilePaths，示例：/data/logs/app_1/**/test.LOG（**：递归匹配多级子目录，仅能出现一次，且必须位于文件名前）。更多详情请参见[采集容器内文本文件](../../../../sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)。
Endpoint（[访问域名](../../../../sls/documents/developer-reference/api-sls-2020-12-30-endpoint.md)）和Region（地域ID），示例：cn-hangzhou.log.aliyuncs.com和cn-hangzhou。
有关YAML文件中config项的详情，包括支持的输入、输出、处理插件类型和容器过滤方式，请参见[PipelineConfig](../../../../sls/documents/recommend-use-aliyunpipelineconfig-to-manage-collection-configurations.md)。完整的YAML参数详情请参见[CR](../../../../sls/documents/recommend-use-aliyunpipelineconfig-to-manage-collection-configurations.md)[参数说明](../../../../sls/documents/recommend-use-aliyunpipelineconfig-to-manage-collection-configurations.md)。
apiVersion: telemetry.alibabacloud.com/v1alpha1 kind: ClusterAliyunPipelineConfig metadata: # 设置资源名，在当前Kubernetes集群内唯一。该名称也是创建出的采集配置名，如果名称重复则不会生效。 name: example-k8s-file spec: # 指定目标Project project: name: k8s-log-<YOUR_CLUSTER_ID> logstores: # 创建名为 k8s-file的Logstore - name: k8s-file # 定义采集配置 config: #
