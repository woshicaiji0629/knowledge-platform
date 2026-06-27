.11.2 [root@xxx ~]#
执行以下命令，当Master节点对应的COMPLETIONS均为1，Worker节点对应的COMPLETIONS为集群Worker节点数时，所有证书完成更新。
kubectl -n kube-system get job[root@ ~]# kubectl get job -nkube-system NAME COMPLETIONS DURATION AGE aliyun-cert-renew-master-1 1/1 46s 4m49s aliyun-cert-renew-master-2 1/1 28s 4m19s aliyun-cert-renew-master-3 1/1 26s 3m48s aliyun-cert-renew-worker 6/6 46s 3m18s ingress-nginx-admission-create 1/1 29s 3d ingress-nginx-admission-patch 1/1 43s 3d kube-eventer-init-1.5-5e0e7cl-aliyun 1/1 31s 3d
