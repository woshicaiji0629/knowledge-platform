## 卸载ack-kubernetes-webhook-injector
如果您不再使用ack-kubernetes-webhook-injector，可以在ACK发布功能中将其删除。具体操作，请参见[基于](../../manage-releases-by-using-helm.md)[Helm](../../manage-releases-by-using-helm.md)[的发布管理](../../manage-releases-by-using-helm.md)。同时，请执行以下命令清理配置信息。
kubectl -n kube-system delete secret kubernetes-webhook-injector-certs kubectl delete mutatingwebhookconfigurations.admissionregistration.k8s.io kubernetes-webhook-injector
该文章对您有帮助吗？
反馈
