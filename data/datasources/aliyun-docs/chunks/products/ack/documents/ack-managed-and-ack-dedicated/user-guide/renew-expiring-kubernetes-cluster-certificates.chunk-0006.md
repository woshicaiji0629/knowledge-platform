## 手动更新Worker节点证书
任意路径下，复制以下内容，创建job-node.yml文件。
apiVersion: batch/v1 kind: Job metadata: name: ${jobname} namespace: kube-system spec: backoffLimit: 0 completions: ${nodesize} parallelism: ${nodesize} template: spec: activeDeadlineSeconds: 3600 affinity: podAntiAffinity: requiredDuringSchedulingIgnoredDuringExecution: - labelSelector: matchExpressions: - key: job-name operator: In values: - ${jobname} topologyKey: kubernetes.io/hostname containers: - command: - /renew/upgrade-k8s.sh - --role - node - --rootkey - ${key} image: registry.cn-hangzhou.aliyuncs.com/acs/cert-rotate:v1.0.0 imagePullPolicy: Always name: ${jobname} securityContext: privileged: true volumeMounts: - mountPath: /alicoud-k8s-host name: ${jobname} hostNetwork: true hostPID: true restartPolicy: Never schedulerName: default-scheduler securityContext: {} volumes: - hostPath: path: / type: Directory name: ${jobname}
说明
如果Worker节点带有Taint，需要在job-node.yml文件中增加对该Taint的tolerations，即在securityContext: {}与volumes:之间增加以下内容（若有n个带有Taint的Worker节点，请复制n次）：
tolerations: - effect: NoSchedule key: ${key} operator: Equal value: ${value}
获取${name}和${value}的方法如下：
任意路径下，复制以下内容，创建taint.tml文件。
{{printf "%-50s %-12s\n" "Node" "Taint"}} {{-
