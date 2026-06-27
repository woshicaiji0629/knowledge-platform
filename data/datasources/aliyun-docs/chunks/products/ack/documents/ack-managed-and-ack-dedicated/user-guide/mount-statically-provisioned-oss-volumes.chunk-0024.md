## kubectl
创建pvc-oss.yaml。
apiVersion: v1 kind: PersistentVolumeClaim metadata: # PVC 名称 name: pvc-oss namespace: default spec: # 配置访问模式。ReadOnlyMany表明ossfs将以只读模式挂载OSS Bucket accessModes: - ReadOnlyMany resources: requests: # 声明存储容量，不能大于存储卷总量 storage: 10Gi # 添加此行，明确指定不使用StorageClass storageClassName: "" selector: matchLabels: # 通过PV标签精确匹配PV alicloud-pvname: pv-oss
创建PVC。
kubectl create -f pvc-oss.yaml
确认PVC状态。
kubectl get pvc pvc-oss
输出中，PVC已绑定（Bound）PV。
NAME STATUS VOLUME CAPACITY ACCESS MODES STORAGECLASS VOLUMEATTRIBUTESCLASS AGE pvc-oss Bound pv-oss 10Gi ROX <unset> 6s
