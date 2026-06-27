ijing.log.aliyuncs.com Region: cn-beijing TelemetryType: logs
CRD-AliyunLogConfig
您只需要创建AliyunLogConfig自定义资源即可创建采集配置，创建完成后自动生效。
重要
对于通过自定义资源创建的采集配置，其修改只能通过更新相应的自定义资源来实现，在日志服务控制台上对采集配置的修改不会同步到自定义资源中。
登录[容器服务管理控制台](https://cs.console.aliyun.com)。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>自定义资源。
在自定义资源页面，单击资源定义（CustomResourceDefinition）页签，然后单击使用YAML创建资源。
根据实际情况修改以下示例YAML的参数，将其复制并粘贴到模板中，然后单击创建完成操作。
该示例YAML将创建名为example-k8s-file的采集配置，并对集群内名称开头为app的所有容器，以极简文本模式采集/data/logs/app_1路径下的test.LOG文件内容，发送到名为k8s-log-<YOUR_CLUSTER_ID>的Project中的名为k8s-file（自动创建）的Logstore。
您需根据实际情况修改示例中容器内文件路径，更多详情请参见[容器文件路径映射](../../../../sls/documents/collect-container-text-logs-through-the-daemonset-console.md)。
logPath：采集日志路径。示例：/data/logs/app_1。
filePattern：采集日志文件名称。示例：test.LOG。
有关YAML文件中的Config项提供的配置详情，如支持的输入，输出，处理插件类型与容器过滤方式等，请参见[AliyunLogConfigDetail](../../../../sls/documents/use-aliyunlogconfig-to-manage-collection-configurations.md)，完整的YAML参数详情请参见[CR](../../../../sls/documents/use-aliyunlogconfig-to-manage-collection-configurations.md)[参数说明](../../../../sls/documents/use-aliyunlogconfig-to-manage-collection-configurations.md)。
apiVersion: log.alibabacloud.com/v1alpha1 kind: AliyunLogConfig metadata: # 设置资源名，在当前Kuber
