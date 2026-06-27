## Secret加密介绍
在Kubernetes集群中，通常使用Secret密钥模型存储和管理业务应用涉及的敏感信息，例如应用密码、TLS证书、Docker镜像下载凭据等敏感信息。Kubernetes会将所有的Secret密钥对象数据存储在集群对应的etcd中。关于密钥的更多信息，请参见[Secrets](https://kubernetes.io/zh/docs/concepts/configuration/secret/)。
在ACK Edge集群Pro版中，您可以使用在KMS中创建的密钥加密Kubernetes Secret密钥。KMS加密过程基于Kubernetes提供的KMS Encryption Provider机制，使用信封加密的方式对存储在etcd中的Kubernetes Secret密钥进行自动加密和解密。Kubernetes Secret密钥加密和解密的过程如下。
当一个业务密钥需要通过Kubernetes Secret API存储时，数据会首先被API Server生成的一个随机的数据加密密钥加密，然后该数据密钥会被指定的KMS密钥加密为一个密文密钥存储在etcd中。
解密Kubernetes Secret密钥时，系统会首先调用KMS的解密OpenAPI进行密文密钥的解密，然后使用解密后的明文密钥对Secret数据解密，并最终返回给您。
更多信息，请参见[KMS Encryption Provider](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/)[机制](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/)、[使用](../../../../kms/documents/key-management-service/use-cases/use-envelope-encryption.md)[KMS](../../../../kms/documents/key-management-service/use-cases/use-envelope-encryption.md)[密钥进行信封加密](../../../../kms/documents/key-management-service/use-cases/use-envelope-encryption.md)。
