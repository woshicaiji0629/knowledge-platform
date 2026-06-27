netes容器内部操作审计。
在Kubernetes容器内部操作审计报表页面，单击告警>创建告警。
在告警监控规则页面，分别配置Kubernetes进入容器告警和Kubernetes进入容器后执行风险程序告警的告警规则。配置完成后，单击确定。
以下配置项均为示例值，请根据实际需求设置。
Kubernetes进入容器告警

| 配置项 | 描述 |
| --- | --- |
| 规则名称 | Kubernetes 进入容器告警 |
| 检查频率 | 固定间隔 ：1 分钟。 |
| 查询统计 | 单击右侧 添加 ，然后单击 高级配置 页签，配置如下信息。配置完成后，单击 确认 。 日志库 ：搜索并选中 advaudit-${cluster_id} ，例如 advaudit-c76da730c08ca45adb90fad86fb****** 。 查询区间 ：本示例选中 1 分钟（相对） 。 查询 ：设置 日志库 后，会显示该字段。代码配置为： kind: Kubernetes and kubeObject.operation.kind: PodExec | select "clusterid", "time", "traceId", "eventId", "k8s.user.aliuid", "k8s.user.username", json_extract(k8s, '$.user.groups') as "k8s.user.groups", "host.hostip", "host.nodename", "k8s.pod.namespace", "k8s.pod.name", json_extract(k8s, '$.pod.labels') as "k8s.pod.labels", "kubeobject.operation.podexecoptions.container", json_extract(kubeobject, '$.operation.podExecOptions.command') as "kubeobject.operation.podexecoptions.command", "kubeobject.operation.podexecoptions.commandstr" from log |
| 触发条件 | 选择当 有数据 时，严重程度： 报告 。 |
| 输出目标 | 选择 SLS 通知 。 |
| 开启 | 打开开关。 |
| 告警策略 | 选择 极简模式 ，并配置如下信息。 渠道 ：选择 钉钉 。 选择 Webhook ：选择 Kubernetes 容器内部操作审计告警 。 提醒方式 ：选择 不提醒 。 内容模板 ：搜索并选择 Kubernetes 进入容器告警 。 发送时段 ：选择 任意 。 |
