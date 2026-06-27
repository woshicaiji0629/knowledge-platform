## 组件介绍
ack-secret-manager：支持以Kubernetes Secret的形式向集群导入或同步KMS凭据信息，确保集群内应用能够安全访问敏感数据。工作负载可通过文件系统挂载指定Secret实例，以使用凭据信息。
csi-secrets-store-provider-alibabacloud：支持以Kubernetes Secret的形式向集群导入或同步KMS凭据信息，确保集群内应用能够安全访问敏感数据；还支持通过CSI Inline的形式将凭据密钥作为文件系统直接挂载到应用中，适用于通过文件系统接口（如读取文件）来获取敏感信息的应用。
ack-kms-agent-webhook-injector：将[KMS Agent](../../../../kms/documents/key-management-service/developer-reference/kms-agent-overview.md)作为Sidecar容器注入Pod，使业务应用可通过本地HTTP接口，借助KMS Agent从KMS实例获取凭据并缓存于内存中，避免敏感信息硬编码，提升数据安全性。
