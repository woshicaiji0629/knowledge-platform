# 标准输出配置 apiVersion: log.alibabacloud.com/v1alpha1 kind: AliyunLogConfig metadata: # 设置资源名，在当前Kubernetes集群内唯一。 name: simple-stdout-example spec: # 设置目标project名称（可不填写，默认为k8s-log-<your_cluster_id>） # project: k8s-log-test # 设置Logstore名称。如果您所指定的Logstore不存在，日志服务会自动创建。 logstore: k8s-stdout # 设置日志采集配置。 logtailConfig: # 设置采集的数据源类型。采集标准输出时，需设置为plugin。 inputType: plugin # 设置Logtail采集配置的名称，必须与资源名(metadata.name)相同。 configName: simple-stdout-example inputDetail: plugin: inputs: - type: service_docker_stdout detail: # 指定采集stdout和stderr。 Stdout: true Stderr: true # 指定待采集容器所在 Pod 所属的命名空间，支持正则匹配。 K8sNamespaceRegex: "^(default)$" # 指定待采集容器的名称，支持正则匹配。 K8sContainerRegex: "^(app.*)$" # 配置多行切分配置 # 配置行首正则表达式 BeginLineRegex: \d+-\d+-\d+.*
日志服务控制台
登录[日志服务控制台](https://sls.console.aliyun.com)。
选择Project列表中您在安装日志采集组件时所使用的Project，如k8s-log-<YOUR_CLUSTER_ID>。在Project页面中点击目标Logstore的Logtail配置，添加采集配置，并单击K8S-标准输出-旧版的立即接入。
由于上一步骤中已为ACK集群安装日志采集组件，请单击使用现有机器组。
在机器组配置页面K8s场景的ACK Daemonset方式下勾选k8s-group-${your_k8s_cluster_id}机器组并单击>添加到应用机器组中，点击下一步。
创建Logtail采集配置，按下文填写必须配置后点击下一步即可，Logtail采集配置生效大概需要1分钟，请耐心等待。
此处仅介绍必须配置，详细配置请参见[Logtail](../../../../sls/documents/collect-container-text-logs-through-the-daemonset-console.md)
