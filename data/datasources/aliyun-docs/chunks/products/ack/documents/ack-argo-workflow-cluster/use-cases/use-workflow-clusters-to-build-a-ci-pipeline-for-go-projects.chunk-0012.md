## 步骤二：在工作流集群中挂载NAS存储卷
使用NAS存储卷在工作流的各任务之间共享数据，如Clone的代码仓库信息等，并存储Go mod cache，用于加速CI Pipeline中的go test和go build过程。
登录[NAS](https://nasnext.console.aliyun.com/)[控制台](https://nasnext.console.aliyun.com/)。
在左侧导航栏，选择文件系统>文件系统列表。
在页面左侧顶部，选择目标文件系统所在的资源组和地域。
在文件系统列表页面，单击目标文件系统操作列的管理。
在文件系统详情页面，单击左侧的挂载使用页签，然后在挂载点区域，查看并记录NAS的挂载点。
将下方示例保存到pv-nas.yaml，将MOUNT_POINT替换为NAS挂载点地址，然后执行kubectl apply -f pv-nas.yaml创建存储卷。
apiVersion:v1kind:PersistentVolumemetadata:name:pv-naslabels:alicloud-pvname:pv-nasspec:capacity:storage:100GiaccessModes:-ReadWriteManycsi:driver:nasplugin.csi.alibabacloud.comvolumeHandle:pv-nas# 必须与PV Name保持一致。volumeAttributes:server:MOUNT_POINTpath:"/"mountOptions:-nolock,tcp,noresvport-vers=3---kind:PersistentVolumeClaimapiVersion:v1metadata:name:pvc-nasspec:accessModes:-ReadWriteManyresources:requests:storage:100Giselector:matchLabels:alicloud-pvname:pv-nas
