说明
当使用（推荐）CRD-AliyunPipelineConfig配置方式时，需要logtail-ds组件版本高于1.8.10。升级详情请参见[升级](../../../../sls/documents/install-logtail-components-in-a-kubernetes-cluster.md)[Logtail latest](../../../../sls/documents/install-logtail-components-in-a-kubernetes-cluster.md)[版本](../../../../sls/documents/install-logtail-components-in-a-kubernetes-cluster.md)。对于LoongCollector组件，则无版本限制。
CRD-AliyunPipelineConfig（推荐）
您只需要创建AliyunPipelineConfig自定义资源即可创建采集配置，资源创建完成后自动生效。
重要
对于通过自定义资源创建的采集配置，其修改只能通过更新相应的自定义资源来实现，在日志服务控制台上对采集配置的修改不会同步到自定义资源中。
登录[容器服务管理控制台](https://cs.console.aliyun.com)。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>自定义资源。
在自定义资源页面，单击资源定义（CustomResourceDefinition）页签，然后单击使用YAML创建资源。
根据实际情况修改以下示例YAML的参数，将其复制并粘贴到模板中，然后单击创建完成操作。
该示例YAML以多行文本模式采集default命名空间下，标签为app: ^(.*test.*)$的Pod中/data/logs/app_1路径下的test.LOG文件内容，并将其发送到名为k8s-log-<YOUR_CLUSTER_ID>的Project中的名为k8s-file（自动创建）的Logstore。您需根据实际情况修改YAML中的以下参数：
project，示例：k8s-log-<YOUR_CLUSTER_ID>。
登录[日志服务控制台](https://sls.console.aliyun.com)，确定您安装的日志采集组件生成的Project的名称。
IncludeK8sLabel，示例：app: ^(.*test.*)$。用于筛选目标Pod的标签，当前条件指定标签键为app，值中包含test的Pod会被采集。
说明
如果需要采集集群中名称包含test的所有Pod，可以将IncludeK8sLabel替换为K8sContainerRegex，并使用通配符配置值，如：K8sContainerRegex: ^(.test.)$。
FilePaths，示例
