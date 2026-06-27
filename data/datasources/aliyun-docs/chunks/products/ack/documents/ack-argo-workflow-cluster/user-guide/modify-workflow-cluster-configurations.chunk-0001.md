## 配置workflow-controller-configmap
可以通过配置workflow-controller-configmap定制Argo Workflow。例如，将大型工作流的状态数据从 etcd 转存（offload）到 PostgreSQL 或 MySQL，将工作流归档到外部数据库，或修改 Pod GC 的配置。ConfigMap的详细配置方式，请参见开源项目文档：[Workflow Controller ConfigMap](https://argo-workflows.readthedocs.io/en/latest/workflow-controller-configmap/)。
将下方命令中的CLUSTER_ID替换为集群ID，然后执行命令，编辑ConfigMap。
kubectl edit configmap -nCLUSTER_IDworkflow-controller-configmap
重要
容器Argo工作流集群在运行中需要使用ConfigMap中的podMetadata配置块，请勿删除。
... podMetadata: labels: workflow.xflow.aliyun: xflow alibabacloud.com/compute-class: general-purpose alibabacloud.com/acs: "true"
