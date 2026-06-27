## 常见运维操作
在下述场景中，需要替换执行命令中的变量信息。变量信息和获取方式如下表。

| 变量 | 说明 | 获取方式 |
| --- | --- | --- |
| {pod-name} | 替换为要修改的 Pod 的名称。 | 在节点上执行 crictl pods 查看。 |
| {namespace} | 替换为 Pod 所在的 Namespace 名称。 |  |
| {pod-id} | 替换为该 Pod 对应的 ID。 |  |
| {configmap-name} | 替换为要修改的 ConfigMap 名称。 | 在节点上执行 ls /etc/kubernetes/cache/kubelet/configmaps.v1.core/{namespace} 查看。 |
| {secret-name} | 替换要修改的 Secret 的名称。 | 在节点上执行 ls /etc/kubernetes/cache/kubelet/secrets.v1.core/{namespace} 查看。 |
