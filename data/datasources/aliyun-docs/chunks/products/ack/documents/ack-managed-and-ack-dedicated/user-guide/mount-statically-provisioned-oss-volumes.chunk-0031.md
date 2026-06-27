## 资源释放指引
为避免产生预期外费用并确保数据安全，请遵循以下流程释放无需使用的资源。
删除工作负载
操作：删除所有使用相关PVC的应用，如Deployment、StatefulSet等，停止Pod并卸载存储卷。
命令示例：kubectl delete deployment <your-deployment-name>
删除PVC
操作：删除应用关联的PVC。OSS静态卷的PV回收策略（persistentVolumeReclaimPolicy）仅支持Retain。因此，删除PVC后，其绑定的PV会进入Released状态，后端的OSS Bucket及其中的所有数据都会被完整保留。
命令示例：kubectl delete pvc <your-pvc-name>
删除PV
操作：删除处于Released状态的PV。此操作仅移除Kubernetes中的资源定义，不会删除后端OSS Bucket中的数据。
命令示例：kubectl delete pv <your-pv-name>
删除Secret（可选）
操作：删除为挂载OSS而创建的Secret。此操作仅移除Kubernetes中的Secret资源对象，不删除后端OSS Bucket中的数据。
命令示例：kubectl delete secret <your-secret-name>
