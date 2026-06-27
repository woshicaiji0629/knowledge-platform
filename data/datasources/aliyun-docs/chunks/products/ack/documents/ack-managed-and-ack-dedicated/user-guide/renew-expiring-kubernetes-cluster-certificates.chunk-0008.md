处设置为cert-node-2。
${nodesize}为Worker节点个数，获取方法可参见[手动更新](renew-expiring-kubernetes-cluster-certificates.md)[Worker](renew-expiring-kubernetes-cluster-certificates.md)[节点证书](renew-expiring-kubernetes-cluster-certificates.md)的步骤1。此处请将nodesize替换为集群的Worker个数。
${key}为集群的CAKey，此处请将key替换为[手动更新](renew-expiring-kubernetes-cluster-certificates.md)[Worker](renew-expiring-kubernetes-cluster-certificates.md)[节点证书](renew-expiring-kubernetes-cluster-certificates.md)步骤2获取到的CAKey。
执行以下命令创建Job。
kubectl create -f job-node2.yml
执行以下命令查看Job状态，当COMPLETIONS为集群Worker节点数时，证书完成更新。
kubectl get job -nkube-system[root@xxx ~]# kubectl get job -nkube-system NAME COMPLETIONS DURATION AGE cert-job-2 1/1 46s 1h cert-job-3 1/1 28s 47m cert-job-4 1/1 26s 46m cert-node-2 4/4 46s 1m [root@xxx ~]#
该文章对您有帮助吗？
反馈
