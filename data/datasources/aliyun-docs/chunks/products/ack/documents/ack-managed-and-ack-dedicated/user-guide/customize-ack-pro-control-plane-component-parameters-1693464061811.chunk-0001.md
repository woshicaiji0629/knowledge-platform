## 注意事项
为了保证控制面的稳定性，当前仅ACK托管集群Pro版、ACK Serverless集群Pro版、ACK Edge集群Pro版、ACK灵骏集群支持自定义部分控制面核心组件参数。
关于支持自定义的参数，请参见[默认参数列表](customize-ack-pro-control-plane-component-parameters-1693464061811.md)（具体请以控制台界面为准）。
部分参数仅支持特定版本的集群，如需升级集群，请参见[手动升级集群](update-the-kubernetes-version-of-an-ack-cluster.md)。
修改参数后，控制面会重启，请在业务低谷期操作。
自定义的参数会覆盖原集群的默认参数。自定义参数时，请确保输入的参数正确且完整，避免参数错误导致控制面启动失败。关于参数设置的详细信息，请根据集群版本参见Kubernetes官方文档[kube-apiserver](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/)、[kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)、[kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/)。
