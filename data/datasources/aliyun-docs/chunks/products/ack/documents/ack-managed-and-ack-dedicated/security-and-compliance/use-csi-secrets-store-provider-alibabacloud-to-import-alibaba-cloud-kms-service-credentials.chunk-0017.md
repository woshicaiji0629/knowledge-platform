### 配置模板说明
SecretProviderClass模板格式定义如下所示。
apiVersion: secrets-store.csi.x-k8s.io/v1 kind: SecretProviderClass metadata: name: <NAME> spec: provider: alibabacloud # 此处配置固定为'alibabacloud'。 parameters: objects: | - objectName: <KMS Encryption Parameter Name> # KMS 凭据名称 objectType: kms # 同步 KMS 凭据时固定为 kms
其中parameters通常包含挂载请求的三个字段：
