### 使用kubectl操作工作流
KubeConfig设置完成后，您可以通过kubectl操作工作流集群，但不同于普通的Kubernetes集群，部分操作会受限。相关权限说明如下。

| 资源 | 权限说明 |
| --- | --- |
| priorityclasses | 可以管理 priorityclasses，并在工作流中制定 priorityclasses，达到通过 Pod 优先级控制调度顺序的目的。 |
| namespaces | 可以创建 Namespaces，拥有自建 Namespaces 的全部权限，并可访问自建 Namespaces 下的资源。不能访问系统 Namespaces 下的资源。系统 Namespaces 即以 kube- 开头的 Namespaces。 重要 以集群 ID 命名的命名空间为 Argo 的系统命名空间，您可以操作此系统命名空间，例如，修改 workflow-controller-configmap 配置 Argo Workflow 的运行参数。 |
| persistentvolumes | 全部权限。 |
| persistentvolumeclaims | 自建 Namespaces 下的全部权限。 |
| secretsconfigmapsserviceaccounts | 自建 Namespaces 下的全部权限。 |
| pods | 自建 Namespaces 下的读权限。 |
| pods/logevents | 自建 Namespaces 下的读权限。 |
| pods/exec | 自建 Namespaces 下的创建权限。 |
| Argo: workflows workflowtasksets workflowtemplates cronworkflows | 自建 Namespaces 下的全部权限。 |
