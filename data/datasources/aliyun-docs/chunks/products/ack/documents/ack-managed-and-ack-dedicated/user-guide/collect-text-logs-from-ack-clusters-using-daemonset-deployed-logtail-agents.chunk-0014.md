ocuments/use-aliyunlogconfig-to-manage-collection-configurations.md)。
apiVersion: log.alibabacloud.com/v1alpha1 kind: AliyunLogConfig metadata: # 设置资源名，在当前Kubernetes集群内唯一。 name: example-k8s-file # 设置资源所在命名空间。 namespace: kube-system spec: # 设置目标project名称（可不填写，默认为k8s-log-<your_cluster_id>） # project: k8s-log-test # 设置Logstore名称。如果您所指定的Logstore不存在，日志服务会自动创建。 logstore: k8s-file # 设置采集配置。 logtailConfig: # 设置采集的数据源类型。采集文本日志时，需设置为file。 inputType: file # 设置采集配置的名称，必须与metadata.name一致。 configName: example-k8s-file inputDetail: # 指定通过极简模式采集文本日志。 logType: common_reg_log # 设置日志文件所在路径。 logPath: /data/logs/app_1 # 设置日志文件的名称。支持通配符星号（*）和半角问号（?），例如log_*.log。 filePattern: test.LOG # 采集容器的文本日志时，需设置dockerFile为true。 dockerFile: true # 开启多行日志采集。单行日志采集删除该配置 # 行首正则表达式，以该正则表示一行日志的开始。 logBeginRegex: \d+-\d+-\d+.* #设置容器过滤条件。 advanced: k8s: K8sPodRegex: '^(app.*)$'
日志服务控制台
说明
此方式适合少量采集配置的创建和管理，无需登录Kubernetes集群，操作步骤简单但无法批量配置。
登录[日志服务控制台](https://sls.console.aliyun.com)。
选择Project列表中您在安装日志采集组件时所使用的Project，如k8s-log-<YOUR_CLUSTER_ID>。在Project页面中单击目标Logstore的Logtail配置，添加采集配置，并单击Kubernetes-文件的立即接入。
在机器组配置页面K8s场景的ACK Daemonset方式下勾选k8s-group-${your_k8s_cluster_id}机器组并单击添加到应用机器组，单击下一步。
创建采集配置，按下文填写必须配置后单击下一步即可，采集配置生效大概
