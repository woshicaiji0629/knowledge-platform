ffect: NoSchedule key: ${key} operator: Equal value: ${value}
获取${name}和${value}的方法如下：
任意路径下，复制以下内容，创建taint.tml文件。
{{printf "%-50s %-12s\n" "Node" "Taint"}} {{- range .items}} {{- if $taint := (index .spec "taints") }} {{- .metadata.name }}{{ "\t" }} {{- range $taint }} {{- .key }}={{ .value }}:{{ .effect }}{{ "\t" }} {{- end }} {{- "\n" }} {{- end}} {{- end}}
执行以下命令，查询带有Taint的Worker节点的${name}和${value}。
kubectl get nodes -o go-template-file="taint.tml"[root@xxx ~]# kubectl get nodes -o go-template-file="taint.tml" Node Taint cn-hangzhou.i-xxx key1=value1:NoSchedule cn-hangzhou.i-xxx node-role.kubernetes.io/master=<no value>:NoSchedule cn-hangzhou.i-xxx node-role.kubernetes.io/master=<no value>:NoSchedule cn-hangzhou.i-xxx node-role.kubernetes.io/master=<no value>:NoSchedule
执行以下命令，获取集群的CAKey。
sed '1d' /etc/kubernetes/pki/ca.key | base64 -w 0
执行以下命令替换job-node.yml文件中指定的变量${jobname}、${nodesize}和${key}。
sed 's/${jobname}/cert-node-2/g; s/${nodesize}/nodesize/g; s/${key}/key/g' job-node.yml > job-node2.yml
其中：
${jobname}为Job的名称，此处设置为cert-node-2。
${nodesize}为Worker节点个数，获取方法可参见[手动更新](renew-expiring-kubernetes-cluster-certificates.md)[Worker](renew-expiring-kubernetes-cluster-certificates.
