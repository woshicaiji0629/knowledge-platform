### ACKProtectBoundingPV
规则说明：防止集群中绑定到持久化存储卷声明（PVC）的持久化存储卷（PV）被删除。
重要等级：high。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKProtectBoundingPV metadata: name: protect-pv-deletion spec: enforcementAction: deny match: kinds: - apiGroups: - "" kinds: - PersistentVolume
Allowed：
apiVersion: v1 kind: PersistentVolume metadata: name: test-pv-bound-should-be-blocked spec: accessModes: - ReadWriteOnce capacity: storage: 1Gi persistentVolumeReclaimPolicy: Retain storageClassName: manual-sc hostPath: path: /tmp/data type: DirectoryOrCreate status: phase: Released
Disallowed：
apiVersion: v1 kind: PersistentVolume metadata: name: test-pv-bound-should-be-blocked spec: accessModes: - ReadWriteOnce capacity: storage: 1Gi persistentVolumeReclaimPolicy: Retain storageClassName: manual-sc hostPath: path: /tmp/data type: DirectoryOrCreate status: phase: Bound
