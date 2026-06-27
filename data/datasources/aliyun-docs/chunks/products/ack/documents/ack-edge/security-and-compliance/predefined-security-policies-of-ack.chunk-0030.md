### ACKPVCConstraint
规则说明：限制能够部署PVC实例的命名空间白名单列表以及限制PVC实例中能够申请的最大磁盘容量。
重要等级：medium
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| maxSize | string | PV 实例中能申请的最大磁盘容量，默认为 50 GiB。 |
| allowNamespaces | array | 能够部署 PVC 实例的命名空间白名单列表。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPVCConstraint metadata: name: limit-pvc-size-and-ns annotations: description: "Limit the maximum pvc storage capacity size and the namespace whitelists that can be deployed." spec: enforcementAction: deny match: kinds: - apiGroups: [ "" ] kinds: [ "PersistentVolumeClaim" ] parameters: maxSize: "50Gi" allowNamespaces: - "test-gatekeeper"
Allowed：
apiVersion: v1 kind: PersistentVolumeClaim metadata: name: disk-pvc namespace: test-gatekeeper spec: accessModes: - ReadWriteOnce resources: requests: storage: 20Gi
Disallowed：
apiVersion: v1 kind: PersistentVolumeClaim metadata: name: bad-disk-pvc namespace: test-gatekeeper spec: accessModes: - ReadWriteOnce resources: requests: storage: 200Gi --- apiVersion: v1 kind: PersistentVolumeClaim metadata: name: bad-namespace-pvc namespace: test-gatekeeper-bad spec: accessModes: - ReadWriteOnce resources: requests: storage: 20Gi
