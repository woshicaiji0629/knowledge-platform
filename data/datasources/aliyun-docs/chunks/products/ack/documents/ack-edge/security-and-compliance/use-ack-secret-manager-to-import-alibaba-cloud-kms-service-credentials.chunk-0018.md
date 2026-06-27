apiVersion: 'alibabacloud.com/v1alpha1' kind: ExternalSecret metadata: name: esdemo spec: provider: kms # 需要同步的阿里云服务类型，默认是kms，当同步KMS凭据时，可以不填写该字段或者指定字段值为 kms data: # 无需特殊处理的数据源。 - key: {KMS secret name} name: {Kubernetes secret key} versionStage: {KMS secret version stage} secretStoreRef: # 组件通过Worker RAM授权时，无需配置该参数。 name: {secret store name} namespace: {secret store namespace} - key: {KMS secret name} name: {Kubernetes secret key} versionStage: {KMS secret version stage} kmsEndpoint: {KMS Service endpoint address}
执行以下命令，部署ExternalSecret。
kubectl apply -f external.yaml
执行以下命令，查看集群中是否存在对应的Kubernetes Secret。
kubectl get secret esdemo
查询存在Secret，表明Secret同步成功。
