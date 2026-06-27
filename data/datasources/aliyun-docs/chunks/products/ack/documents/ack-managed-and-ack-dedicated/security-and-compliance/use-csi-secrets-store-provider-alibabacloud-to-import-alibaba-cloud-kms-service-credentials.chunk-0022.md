### 将 KMS 凭据同步为 Kubernetes Secret
Secrets Store CSI Driver 支持将从外部密钥管理服务（如阿里云KMS、OOS）中获取的密钥，自动同步并创建为集群内原生的 Kubernetes Secret。应用无需修改代码，就能以标准方式使用这些外部密钥。
配置方法：SecretProviderClass
您可以在SecretProviderClass资源的spec中添加secretObjects可选字段来启用此功能。
apiVersion: secrets-store.csi.x-k8s.io/v1 kind: SecretProviderClass metadata: name: <NAME> spec: provider: alibabacloud # 此处配置固定为alibabacloud，请勿修改。 parameters: objects: | - objectName: <KMS Encryption Parameter Name> # KMS 凭据名称 objectType: kms # 同步 KMS 凭据时固定为 kms secretObjects: - secretName: <Kubernetes Secret Name> # Kubernetes Secret 名称 type: <Kubernetes Secret Type> # Kubernetes Secret 类型 data: - objectName: <parameters.objects.objectName> # parameters.objects.objectName 名称，当指定别名时，使用别名 key: <Kubernetes Secret Data Key> # Kubernetes Secret Data Key 字段名称
secretObjects通常包含以下三个参数：
