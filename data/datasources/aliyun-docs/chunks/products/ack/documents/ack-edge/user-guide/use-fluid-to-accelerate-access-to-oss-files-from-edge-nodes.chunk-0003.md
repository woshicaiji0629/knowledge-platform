## 步骤二：创建Dataset和JindoRuntime
在创建Dataset之前，创建一个mySecret.yaml文件。
apiVersion: v1 kind: Secret metadata: name: mysecret stringData: fs.oss.accessKeyId: xxx fs.oss.accessKeySecret: xxx
其中，fs.oss.accessKeyId和fs.oss.accessKeySecret是[步骤一](../../cloud-native-ai-suite/user-guide/use-jindofs-to-accelerate-access-to-oss.md)中用来访问OSS的AccessKey ID和AccessKey Secret。
执行以下命令，生成Secret。K8s会对已创建的Secret使用加密编码，避免将其明文暴露。
kubectl create -f mySecret.yaml
使用以下YAML文件样例创建一个名为resource.yaml的文件，里面包含两部分：
创建一个Dataset，描述远端存储数据集和UFS的信息。
创建一个JindoRuntime，启动一个JindoFS的集群来提供缓存服务。
apiVersion: data.fluid.io/v1alpha1 kind: Dataset metadata: name: hadoop spec: nodeAffinity: required: nodeSelectorTerms: - matchExpressions: - key: alibabacloud.com/nodepool-id operator: In values: - npxxxxxxxxxxxxxx mounts: - mountPoint: oss://<oss_bucket>/<bucket_dir> options: fs.oss.endpoint: <oss_endpoint> name: hadoop path: "/" encryptOptions: - name: fs.oss.accessKeyId valueFrom: secretKeyRef: name: mysecret key: fs.oss.accessKeyId - name: fs.oss.accessKeySecret valueFrom: secretKeyRef: name: mysecret key: fs.oss.accessKeySecret --- apiVersion: data.fluid.io/v1alpha1 kind: JindoRuntime metadata: name: hadoop spec: nodeSelector: alibabaclo
