## 通过kubectl自动更新所有节点证书
更新证书
在集群任意Master节点，执行以下命令完成集群所有节点的证书更新。
curl http://aliacs-k8s-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/public/cert-update/renew.sh | bash
结果验证需已通过kubectl连接集群，请参见[通过](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[连接](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[Kubernetes](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[集群](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)。
执行以下命令，查看集群Master和Worker节点状态。
kubectl get nodes[root@xxx ~]# kubectl get nodes NAME STATUS ROLES AGE VERSION cn-hangzhou.xxx Ready <none> 23d v1.11.2 cn-hangzhou.xxx Ready <none> 23d v1.11.2 cn-hangzhou.xxx Ready master 47d v1.11.2 cn-hangzhou.xxx Ready master 47d v1.11.2 cn-hangzhou.xxx Ready master 47d v1.11.2 cn-hangzhou.xxx Ready <none> 47d v1.11.2 cn-hangzhou.xxx Ready <none> 47d v1.11.2 [root@xxx ~]#
执行以下命令，当Master节点对应的COMPLETIONS均为1，Worker节点对应的COMPLETIONS为集群Worker节点数时，所有证书完成更新。
kubectl -n kube-system get job[root@ ~]# kubectl get job -nk
