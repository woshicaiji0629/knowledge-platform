## 相关操作
查看集群基本信息
在集群列表页面的操作列，单击详情，然后单击基本信息和连接信息页签，查看集群的基本信息和连接信息。其中：
API Server 公网端点：Kubernetes的API Server对公网提供服务的地址和端口，可以通过此服务在用户终端使用kubectl等工具管理集群。
绑定公网IP和解绑公网IP功能：
绑定公网IP：您可以选择在已有EIP列表中绑定EIP或者新建EIP。
绑定公网IP操作会导致API Server短暂重启，请避免在此期间操作集群。
解绑公网IP：解绑公网IP后您将无法通过公网访问API Server。
解绑公网IP操作会导致API Server短暂重启，请避免在此期间操作集群。
API Server 内网端点：Kubernetes的API Server对集群内部提供服务的地址和端口，此IP为负载均衡的地址。
查看集群日志信息
您可以单击操作列的更多>运维管理>查看日志，进入日志中心页面查看集群的日志信息。
查看集群节点信息
您可以[获取集群](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[KubeConfig](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[并通过](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[工具连接集群](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)，执行kubectl get node查看集群的节点信息。
