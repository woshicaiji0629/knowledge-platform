## 删除ACK默认Pod安全策略对应的集群角色绑定
警告
在删除ACK默认的Pod安全策略对应的集群角色绑定前必须先配置好自定义的Pod安全策略及其相应的RBAC绑定，否则所有用户、控制器、服务账号都将无法创建或更新Pod。
在配置好自定义的Pod安全策略及其相应的RBAC绑定后，您可以通过删除ACK默认Pod安全策略ack.privileged的集群角色绑定的方式来启用您自定义的Pod安全策略。
重要
请不要删除或修改名为ack.privileged的Pod安全策略以及名为ack:podsecuritypolicy:privileged的集群角色，ACK集群的正常运行需要依赖这两个资源。
展开查看删除ACK默认Pod安全策略ack.privileged的集群角色绑定命令
$ cat <<EOF | kubectl delete -f - apiVersion: rbac.authorization.k8s.io/v1 kind: ClusterRoleBinding metadata: name: ack:podsecuritypolicy:authenticated annotations: kubernetes.io/description: 'Allow all authenticated users to create privileged pods.' labels: kubernetes.io/cluster-service: "true" ack.alicloud.com/component: pod-security-policy roleRef: apiGroup: rbac.authorization.k8s.io kind: ClusterRole name: ack:podsecuritypolicy:privileged subjects: - kind: Group apiGroup: rbac.authorization.k8s.io name: system:authenticated EOF
