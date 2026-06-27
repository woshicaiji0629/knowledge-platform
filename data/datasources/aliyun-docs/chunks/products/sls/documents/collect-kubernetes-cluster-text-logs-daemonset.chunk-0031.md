ments/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[并通过](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[工具连接集群](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)。
查看集群中Worker节点数。
kubectl get node | grep -v master
系统会返回如下类似结果。
NAME STATUS ROLES AGE VERSION cn-hangzhou.i-bp17enxc2us3624wexh2 Ready <none> 238d v1.10.4 cn-hangzhou.i-bp1ad2b02jtqd1shi2ut Ready <none> 220d v1.10.4
对比心跳状态为OK的节点数是否和容器集群中Worker节点数一致。根据对比结果选择排查方式。
机器组中所有节点的心跳状态均为Failed：
如果是自建集群，请检查以下参数是否配置正确：{regionId}、{aliuid}、{access-key-id}和{access-key-secret}是否已正确填写。
如果填写错误，请执行helm del --purge alibaba-log-controller命令，删除安装包，然后重新安装。
机器组心跳状态为OK的节点数量少于集群中的Worker节点数量。
判断是否已使用YAML文件手动部署DaemonSet。
执行如下命令。如果存在返回结果，则表示之前已使用YAML文件手动部署DaemonSet。
kubectl get po -n kube-system -l k8s-app=logtail
[下载最新版本](ht
