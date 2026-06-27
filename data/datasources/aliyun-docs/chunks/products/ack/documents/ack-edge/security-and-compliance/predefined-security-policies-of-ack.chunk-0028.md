示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPVSizeConstraint metadata: name: limit-pv-size annotations: description: "Limit the pv storage capacity size within a specified maximum amount." spec: enforcementAction: deny match: kinds: - apiGroups: [ "" ] kinds: [ "PersistentVolume" ] parameters: maxSize: "50Gi"
Allowed：
apiVersion: v1 kind: PersistentVolume metadata: name: pv-oss-csi labels: alicloud-pvname: pv-oss spec: capacity: storage: 25Gi accessModes: - ReadWriteMany persistentVolumeReclaimPolicy: Retain csi: driver: ossplugin.csi.alibabacloud.com volumeHandle: pv-oss nodePublishSecretRef: name: oss-secret namespace: default volumeAttributes: bucket: "oss" url: "oss-cn-beijing.aliyuncs.com" otherOpts: "-o max_stat_cache_size=0 -o allow_other" path: "/"
Disallowed：
apiVersion: v1 kind: PersistentVolume metadata: name: pv-oss-csi-bad labels: alicloud-pvname: pv-oss spec: capacity: storage: 500Gi accessModes: - ReadWriteMany persistentVolumeReclaimPolicy: Retain csi: driver: ossplugin.csi.alibabacloud.com volumeHandle: pv-oss nodePublishSecretRef: name: oss-secret namespace: default volumeAttributes: bucket: "oss" url: "oss-cn-beijing.aliyuncs.com" other
