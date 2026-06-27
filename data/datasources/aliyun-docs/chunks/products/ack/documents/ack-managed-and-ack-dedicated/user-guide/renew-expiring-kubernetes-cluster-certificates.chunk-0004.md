## 手动更新Master节点证书
任意路径下，复制以下内容，创建job-master.yml文件。
apiVersion: batch/v1 kind: Job metadata: name: ${jobname} namespace: kube-system spec: backoffLimit: 0 completions: 1 parallelism: 1 template: spec: activeDeadlineSeconds: 3600 affinity: nodeAffinity: requiredDuringSchedulingIgnoredDuringExecution: nodeSelectorTerms: - matchExpressions: - key: kubernetes.io/hostname operator: In values: - ${hostname} containers: - command: - /renew/upgrade-k8s.sh - --role - master image: registry.cn-hangzhou.aliyuncs.com/acs/cert-rotate:v1.0.0 imagePullPolicy: Always name: ${jobname} securityContext: privileged: true volumeMounts: - mountPath: /alicoud-k8s-host name: ${jobname} hostNetwork: true hostPID: true restartPolicy: Never schedulerName: default-scheduler securityContext: {} tolerations: - effect: NoSchedule key: node-role.kubernetes.io/master volumes: - hostPath: path: / type: Directory name: ${jobname}
获取集群Master节点个数和节点名称等信息。
方法一：通过命令行
执行以下命令：
kubectl get nodes[root@xxx ~]# kubectl get nodes NAME STATUS ROLES AGE VERSION cn-hangzhou.ixxx Ready <none> 22d v1.11.2 cn-hangzhou.ixxx Ready <none> 22d v1.11.2 cn-hangzhou.ixxx Ready master 46d v1.11.2 cn-hangzhou.ixxx Ready master 46d v1.11.2 cn-
