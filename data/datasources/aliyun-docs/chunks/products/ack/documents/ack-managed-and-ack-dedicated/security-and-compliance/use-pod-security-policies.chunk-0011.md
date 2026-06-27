eadOnlyRootFilesystem: false --- apiVersion: rbac.authorization.k8s.io/v1 kind: ClusterRole metadata: name: podsecuritypolicy:allow-unsafe-sysctls rules: - apiGroups: - policy resourceNames: - psp.allow-unsafe-sysctls resources: - podsecuritypolicies verbs: - use --- apiVersion: rbac.authorization.k8s.io/v1 kind: ClusterRoleBinding metadata: name: podsecuritypolicy:allow-unsafe-sysctls:authenticated roleRef: apiGroup: rbac.authorization.k8s.io kind: ClusterRole name: podsecuritypolicy:allow-unsafe-sysctls subjects: - kind: Group apiGroup: rbac.authorization.k8s.io name: system:authenticated
在集群内创建相应资源。
kubectl create -f unsafe-sysctl-psp.yaml
预期输出：
podsecuritypolicy.policy/psp.allow-unsafe-sysctls created clusterrole.rbac.authorization.k8s.io/podsecuritypolicy:allow-unsafe-sysctls created clusterrolebinding.rbac.authorization.k8s.io/podsecuritypolicy:allow-unsafe-sysctls:authenticated created
自定义节点池的kubelet参数，允许使用不安全的sysctl。详见[支持自定义的](../user-guide/customize-the-kubelet-configurations-of-a-node-pool.md)[kubelet](../user-guide/customize-the-kubelet-configurations-of-a-node-pool.md)[参数](../user-guide/customize-the-kubelet-configurations-of-a-node-pool.md)。
部署一个使用不安全的sysctl的测试Pod。
可按需
