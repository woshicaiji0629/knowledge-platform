h。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| restrictedRole | object | 限制使用的 Clusterrole 或 Role。 |
| allowedSubjects | array | 允许挂载的 Subjects 白名单列表。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKRestrictRoleBindings metadata: name: restrict-clusteradmin-rolebindings annotations: description: "Restricts use of sensitive role in specific rolebinding." spec: match: kinds: - apiGroups: ["rbac.authorization.k8s.io"] kinds: ["RoleBinding"] parameters: restrictedRole: apiGroup: "rbac.authorization.k8s.io" kind: "ClusterRole" name: "cluster-admin" allowedSubjects: - apiGroup: "rbac.authorization.k8s.io" kind: "Group" name: "system:masters"
Allowed：
kind: RoleBinding apiVersion: rbac.authorization.k8s.io/v1 metadata: name: good-2 namespace: test-gatekeeper subjects: - kind: Group name: 'system:masters' roleRef: kind: ClusterRole name: cluster-admin apiGroup: rbac.authorization.k8s.io
Disallowed：
kind: RoleBinding apiVersion: rbac.authorization.k8s.io/v1 metadata: name: bad-1 namespace: test-gatekeeper subjects: - kind: ServiceAccount name: policy-template-controller roleRef: kind: ClusterRole name: cluster-admin apiGroup: rbac.authorization.k8s.io
