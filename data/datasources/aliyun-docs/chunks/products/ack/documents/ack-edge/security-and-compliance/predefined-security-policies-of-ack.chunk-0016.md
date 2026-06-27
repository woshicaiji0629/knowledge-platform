### ACKResourceDeletionProtection
规则说明：防止集群中带有自定义标签的资源被删除。支持Service、Namespace、Ingress、Deployment、StatefulSet、DaemonSet、Job、CronJob等资源类型。可定义多组键值对，资源只要满足其中任意一对即可受到保护。
重要等级：high。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| labels | array | 自定义标签，用于识别需要被保护的节点。 |
| labels.labelName | string | 自定义标签的键。 |
| labels.labelValue | string | 自定义标签的值。 |
