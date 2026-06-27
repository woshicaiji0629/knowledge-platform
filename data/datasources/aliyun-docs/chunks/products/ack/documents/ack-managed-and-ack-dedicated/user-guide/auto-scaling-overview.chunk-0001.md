## 使用前说明
本文面向集群运维人员、开发人员等介绍ACK集群的弹性伸缩方案（工作负载伸缩和节点伸缩）。建议您已了解社区工作负载伸缩方案（例如[HPA](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)、[VPA](https://github.com/kubernetes/autoscaler/tree/vpa-release-0.8/vertical-pod-autoscaler)等）和节点伸缩方案（例如[Cluster Autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/cluster-autoscaling/)）的相关内容等。
如果您的集群为大规模集群（通常为超过500个节点或者10,000个Pod的集群），请参见[规划集群资源弹性速率](suggestions-on-how-to-work-with-large-ack-pro-clusters.md)了解相关使用建议，以确保集群和控制面的稳定性。
