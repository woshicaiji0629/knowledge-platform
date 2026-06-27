chLabels: kubernetes.io/metadata.name: default - matchExpressions: - key: kubernetes.io/metadata.name operator: In values: - test rotationInterval: 10s
spec字段说明

| crd 字段 | 描述 | 是否必选 |
| --- | --- | --- |
| externalSecretSpec | 要创建的 ExternalSecret 的规格定义 | 是 |
| externalSecretName | 要创建的 ExternalSecret 的名称，默认是 ClusterExternalSecret 的名称 | 否 |
| externalSecretMetadata | 要创建的 ExternalSecret 的元数据 | 否 |
| namespaceSelectors | 用于选择目标命名空间的标签选择器列表 | 否 |
| rotationInterval | 控制器检查命名空间标签和协调对象的时间间隔 | 否 |

externalSecretMetadata字段说明
externalSecretMetadata 字段允许您自动为 ClusterExternalSecret 创建的 ExternalSecret 资源添加额外的元数据：

| crd 字段 | 描述 | 是否必选 |
| --- | --- | --- |
| annotations | 要创建的 ExternalSecret 的注解 | 否 |
| labels | 要创建的 ExternalSecret 的标签 | 否 |

ClusterSecretStore
集群级别资源，功能与SecretStore相同，但可被集群中任意命名空间的ExternalSecret引用，并支持使用spec.conditions配置访问控制
apiVersion: alibabacloud.com/v1alpha1 kind: ClusterSecretStore metadata: name: alibaba-credentials spec: conditions: - namespaceSelector: matchLabels: kubernetes.io/metadata.name: test KMS: KMSAuth: oidcProviderARN: acs:ram::<role-name>:oidc-provider/ack-rrsa-<cluster-id> serviceAccountRef: name: test-serviceaccount-auth namespace: test
spec字段说明
