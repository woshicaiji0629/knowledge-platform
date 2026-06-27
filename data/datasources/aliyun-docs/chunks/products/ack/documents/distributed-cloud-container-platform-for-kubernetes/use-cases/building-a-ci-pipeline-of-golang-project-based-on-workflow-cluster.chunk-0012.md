### 步骤二：在工作流集群中挂载NAS存储卷
使用NAS存储卷的目的如下：
在工作流的各任务之间共享数据，如Clone的代码仓库信息等。
存储Go mod cache，用于加速CI Pipeline中的go test和go build过程。
在工作流集群中使用NAS存储卷的步骤如下：
获取NAS文件系统的挂载点地址。具体操作，请参见[管理挂载点](https://help.aliyun.com/zh/nas/user-guide/manage-mount-targets)。
使用以下内容在工作流集群中创建PV/PVC。具体操作，请参见[使用](../user-guide/use-volumes.md)[NAS](../user-guide/use-volumes.md)[存储卷](../user-guide/use-volumes.md)。
apiVersion: v1 kind: PersistentVolume metadata: name: pv-nas labels: alicloud-pvname: pv-nas spec: capacity: storage: 100Gi accessModes: - ReadWriteMany csi: driver: nasplugin.csi.alibabacloud.com volumeHandle: pv-nas # 必须与PV Name保持一致。 volumeAttributes: server: <your nas filesystem mount point address> path: "/" mountOptions: - nolock,tcp,noresvport - vers=3 --- kind: PersistentVolumeClaim apiVersion: v1 metadata: name: pvc-nas spec: accessModes: - ReadWriteMany resources: requests: storage: 100Gi selector: matchLabels: alicloud-pvname: pv-nas
