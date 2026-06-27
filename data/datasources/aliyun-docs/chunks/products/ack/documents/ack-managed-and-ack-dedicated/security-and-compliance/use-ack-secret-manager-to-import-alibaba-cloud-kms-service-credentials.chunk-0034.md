### CRD 资源说明
当前提供了四种自定义资源定义（CRD），分为两类：
认证资源配置类
SecretStore: 命名空间级别资源，用于定义访问凭据（如RRSA、ClientKey、AK配置等）。
ClusterSecretStore: 集群级别资源，功能与SecretStore相同，但可被集群中任意命名空间的ExternalSecret引用，并支持访问控制配置。
数据同步配置类
ExternalSecret: 命名空间级别资源，用于定义需要同步的凭据基础信息（如凭据名称、版本等）以及指定SecretStore。
ClusterExternalSecret: 集群级别资源，用于管理和协调多个命名空间下的ExternalSecret，能够在匹配的命名空间中自动创建ExternalSecret。
集群级别资源说明
ClusterExternalSecret
集群级别资源，用于管理和协调多个命名空间下的ExternalSecret，支持使用spec.namespaceSelectors配置匹配的命名空间，在匹配的命名空间中自动创建ExternalSecret
apiVersion: "alibabacloud.com/v1alpha1" kind: ClusterExternalSecret metadata: name: cluster-kms spec: externalSecretSpec: provider: kms data: - key: test name: test versionId: v1 secretStoreRef: name: alibaba-credentials kind: ClusterSecretStore externalSecretName: kms externalSecretMetadata: labels: app: "my-app" team: "backend" annotations: annotation-key1: "annotation-value1" annotation-key2: "annotation-value2" namespaceSelectors: - matchLabels: kubernetes.io/metadata.name: default - matchExpressions: - key: kubernetes.io/metadata.name operator: In values: - test rotationInterval: 10s
spec字段说明
