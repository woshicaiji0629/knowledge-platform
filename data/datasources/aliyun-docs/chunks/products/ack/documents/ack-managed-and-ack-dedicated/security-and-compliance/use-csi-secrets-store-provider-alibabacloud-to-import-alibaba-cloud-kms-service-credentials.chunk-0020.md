### 配置使用示例
本示例以ACK托管集群同一地域下的KMS服务凭据test为例，介绍如何通过SecretProviderClass将其导入到集群应用中。
使用以下简单的SecretProviderClass示例，创建secretstore.yaml文件。
apiVersion: secrets-store.csi.x-k8s.io/v1 kind: SecretProviderClass metadata: name: test-secrets spec: provider: alibabacloud # 此处固定配置为alibabacloud。 parameters: objects: | # objectType 支持oos和kms, 默认为kms - objectName: "test-hangzhou" objectType: "kms" objectAlias: "hangzhou-public" kmsEndpoint: "kms.{region}.aliyuncs.com"
执行以下命令，部署SecretProviderClass。
kubectl apply -f secretstore.yaml
使用以下内容，创建deploy.yaml。
包含一个Nginx Deployment实例，通过CSI Inline文件系统的形式声明使用了上面示例中已经创建的SecretProviderClass，并在Pod中的/mnt/secrets-store目录下挂载凭据密钥。关于Deployment实例更多信息，请参见[Deployment](https://github.com/AliyunContainerService/secrets-store-csi-driver-provider-alibaba-cloud/tree/main/examples)[示例](https://github.com/AliyunContainerService/secrets-store-csi-driver-provider-alibaba-cloud/tree/main/examples)。
apiVersion: apps/v1 # 1.8.0之前版本请使用apps/v1beta1。 kind: Deployment metadata: name: nginx-deployment-basic labels: app: nginx spec: replicas: 2 selector: matchLabels: app: nginx template: metadata: labels: app: nginx spec: volumes: - name: secrets-store-inline csi: driver: secrets-store.csi.
