apiVersion: alibabacloud.com/v1alpha1 kind: ExternalSecret metadata: name: esdemo spec: provider: kms # 需要同步的阿里云服务类型，默认是kms，当同步KMS凭据时，可以不填写该字段或者指定字段值为 kms data: # 无需特殊处理的数据源。 - key: <KMS_SECRET_NAME> name: <KUBERNETES_SECRET_KEY> versionStage: <KMS_SECRET_VERSION_STAGE> secretStoreRef: # 组件通过Worker RAM授权时，无需配置该参数。 name: <SECRET_STORE_NAME> namespace: <SECRET_STORE_NAMESPACE> - key: <KMS_SECRET_NAME> name: <KUBERNETES_SECRET_KEY> versionStage: <KMS_SECRET_VERSION_STAGE> kmsEndpoint: <KMS_SERVICE_ENDPOINT>
执行以下命令，部署ExternalSecret。
kubectl apply -f external.yaml
执行以下命令，查看集群中是否存在对应的Kubernetes Secret。
kubectl get secret esdemo
查询存在Secret，表明Secret同步成功。
