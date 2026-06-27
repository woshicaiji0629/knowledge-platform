## 容器Argo工作流集群中的kubectl权限
不同于普通的Kubernetes集群，kubectl在容器Argo工作流集群中部分操作会受限，权限说明如下：

| 集群资源 | 权限说明 |
| --- | --- |
| PriorityClass | 可以管理 PriorityClasse，并在工作流中指定 PriorityClass，达到通过 Pod 优先级控制调度顺序的目的。 |
| Namespace | 可以创建 Namespace，拥有自建 Namespace 的全部权限，并可访问自建 Namespace 下的资源。不能访问系统 Namespace 下的资源，即以 kube- 开头的 Namespace。 重要 以集群 ID 命名的命名空间为 Argo 的系统命名空间，您可以操作此系统命名空间，例如，修改 workflow-controller-configmap 配置 Argo Workflow 的运行参数。 |
| Persistentvolume | 全部权限。 |
| Persistentvolumeclaim | 自建 Namespaces 下的全部权限。 |
| Secret Configmap Serviceaccount | 自建 Namespaces 下的全部权限。 |
| Pod | 自建 Namespaces 下的读权限。 |
| Pods/logevents | 自建 Namespaces 下的读权限。 |
| Pods/exec | 自建 Namespaces 下的创建权限。 |
| Argo 资源： workflows workflowtasksets workflowtemplates cronworkflows | 自建 Namespaces 下的全部权限。 |

该文章对您有帮助吗？
反馈
