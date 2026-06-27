secretstore-rrsa.yaml文件。
<NAME>：替换为指定的SecretStore实例名称。
<NAMESPACE>：替换为指定的集群命名空间名称。
<SERVICEACCOUNT_NAME>：替换为上一步中创建的ServiceAccount实例名称。
apiVersion: alibabacloud.com/v1alpha1 kind: SecretStore metadata: name: <NAME> namespace: <NAMESPACE> spec: KMS: KMSAuth: serviceAccountRef: name: <SERVICEACCOUNT_NAME>
执行以下命令，部署SecretStore。
kubectl apply -f secretstore-rrsa.yaml
