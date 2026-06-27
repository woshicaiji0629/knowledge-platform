## 使用NAS存储卷
使用以下示例代码，创建静态NAS共享卷。
展开查看使用NAS共享卷的YAML示例代码
apiVersion: v1 kind: PersistentVolume metadata: name: pv-nas labels: alicloud-pvname: pv-nas spec: capacity: storage: 100Gi accessModes: - ReadWriteMany csi: driver: nasplugin.csi.alibabacloud.com volumeHandle: pv-nas # 必须与PV Name保持一致。 volumeAttributes: server: "<your nas filesystem id>.cn-beijing.nas.aliyuncs.com" path: "/" mountOptions: - nolock,tcp,noresvport - vers=3 --- kind: PersistentVolumeClaim apiVersion: v1 metadata: name: pvc-nas spec: accessModes: - ReadWriteMany resources: requests: storage: 100Gi selector: matchLabels: alicloud-pvname: pv-nas
使用以下示例代码，在工作流中挂载和使用NAS。
展开查看在工作流中挂载使用NAS共享卷的YAML示例代码
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: volumes-existing- namespace: default spec: entrypoint: volumes-existing-example volumes: # Pass my-existing-volume as an argument to the volumes-existing-example template. # Same syntax as k8s Pod spec. - name: workdir persistentVolumeClaim: claimName: pvc-nas templates: - name: volumes-existing-example steps: - - name: generate template: whalesay - - name: print template: print-message - name: whalesay container: image: docker/whalesay:latest command:
