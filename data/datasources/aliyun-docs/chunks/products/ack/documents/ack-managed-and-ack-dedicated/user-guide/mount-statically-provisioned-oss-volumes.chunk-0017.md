## kubectl
创建oss-secret.yaml，将[步骤一](mount-statically-provisioned-oss-volumes.md)获取的AccessKey存储为Secret，供PV使用。
apiVersion: v1 kind: Secret metadata: name: oss-secret # 需与应用所在的命令空间保持一致 namespace: default stringData: # 替换为此前获取的AccessKey ID akId: <your AccessKey ID> # 替换为此前获取的AccessKey Secret akSecret: <your AccessKey Secret>
创建Secret。
kubectl create -f oss-secret.yaml
创建pv-oss-ram.yaml。
apiVersion: v1 kind: PersistentVolume metadata: # PV 名称 name: pv-oss # PV 标签 labels: alicloud-pvname: pv-oss spec: capacity: storage: 10Gi accessModes: - ReadOnlyMany persistentVolumeReclaimPolicy: Retain csi: driver: ossplugin.csi.alibabacloud.com # 需与PV名称（metadata.name）保持一致 volumeHandle: pv-oss # 指定通过Secret对象来获取AccessKey信息 nodePublishSecretRef: name: oss-secret namespace: default volumeAttributes: # 替换为实际Bucket名称 bucket: "your-bucket-name" url: "http://oss-cn-hangzhou-internal.aliyuncs.com" otherOpts: "-o umask=022 -o max_stat_cache_size=100000 -o allow_other" path: "/"
