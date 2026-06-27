件采集容器内文本日志 - Type: service_docker_stdout Stdout: true Stderr: true # 配置容器信息过滤条件，多个选项之间为“且”的关系。 # 指定待采集容器所在 Pod 所属的命名空间，支持正则匹配。 K8sNamespaceRegex: "^(default)$" # 启用容器元数据预览 CollectContainersFlag: true # 采集Pod标签符合条件的容器。多个条目之间为或的关系 IncludeK8sLabel: app: ^(.*test.*)$ # 配置多行切分配置，单行日志采集无效配置 # 配置行首正则表达式 BeginLineRegex: \d+-\d+-\d+.* # 定义输出插件 flushers: # 使用flusher_sls插件输出到指定Logstore。 - Type: flusher_sls # 需要确保该 Logstore 存在 Logstore: k8s-stdout # 需要确保 endpoint 正确 Endpoint: cn-hangzhou.log.aliyuncs.com Region: cn-hangzhou TelemetryType: logs
CRD-AliyunLogConfig
您只需要创建AliyunLogConfig自定义资源即可创建采集配置，创建完成后自动生效。
重要
对于通过自定义资源创建的采集配置，其修改只能通过更新相应的自定义资源来实现，在日志服务控制台上对采集配置的修改不会同步到自定义资源中。
登录[容器服务管理控制台](https://cs.console.aliyun.com)。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>自定义资源。
在自定义资源页面，单击资源定义（CustomResourceDefinition）页签，然后单击使用YAML创建资源。
根据实际情况修改以下示例YAML的参数，将其复制并粘贴到模板中，然后单击创建完成操作。
该YAML脚本将创建名为simple-stdout-example的采集配置，并对集群内名称开头为app的所有容器，以多行模式采集标准输出，发送到名为k8s-log-<YOUR_CLUSTER_ID>的Project中的名为k8s-stdout的Logstore。
有关YAML文件中的logtailConfig项提供的详情，如支持的输入，输出，处理插件类型与容器过滤方式等，请参见[AliyunLogConfigDetail](../../../../sls/documents/use-aliyunlogconfig-to-manage-collection-configurations.md)，完整的YAML参数详情请参见[CR](../../../../sls
