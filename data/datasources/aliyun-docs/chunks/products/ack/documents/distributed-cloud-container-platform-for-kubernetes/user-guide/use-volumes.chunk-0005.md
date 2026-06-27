## 使用CPFS2.0存储卷
执行以下命令，创建CPFS2.0共享卷。
展开查看使用CPFS2.0共享卷的YAML示例代码
cat << EOF | kubectl apply -f - apiVersion: v1 kind: PersistentVolume metadata: name: pv-cpfs labels: alicloud-pvname: pv-cpfs spec: accessModes: - ReadWriteOnce capacity: storage: 1000Gi csi: driver: nasplugin.csi.alibabacloud.com volumeAttributes: mountProtocol: cpfs-nfs # 挂载时，使用NFS协议进行挂载。 path: "/share" # 挂载目录必须以/share为前缀。 volumeAs: subpath server: "<your cpfs id, e.g cpfs-****>.<regionID>.cpfs.aliyuncs.com" # 为挂载点前面的域名。 volumeHandle: pv-cpfs # 必须与PV Name保持一致。 mountOptions: - rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport - vers=3 --- apiVersion: v1 kind: PersistentVolumeClaim metadata: name: pvc-cpfs spec: accessModes: - ReadWriteOnce resources: requests: storage: 1000Gi selector: matchLabels: alicloud-pvname: pv-cpfs EOF
使用以下示例代码，在工作流中挂载和使用CPFS2.0。
展开查看在工作流中挂载使用CPFS2.0共享卷的YAML示例代码
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: volumes-existing- namespace: default spec: entrypoint: volumes-existing-example volumes: # Pass my-existing-volume as an argument to the volumes-existing-example template. # Same syntax as k8s Pod spec. - name: workdir persistentVolumeClaim: claimName
