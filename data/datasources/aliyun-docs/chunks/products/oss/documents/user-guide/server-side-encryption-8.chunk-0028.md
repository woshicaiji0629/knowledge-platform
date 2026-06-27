## 使用KMS托管密钥进行加解密
使用KMS托管的用户主密钥CMK生成加密密钥加密数据，通过信封加密机制，可进一步防止未经授权的数据访问。借助KMS，您可以专注于数据加解密、电子签名验签等业务功能，无需花费大量成本来保障密钥的保密性、完整性和可用性。
SSE-KMS加密方式的逻辑示意图如下。
使用SSE-KMS加密方式时，可使用如下密钥：
使用OSS默认托管的KMS密钥
OSS使用默认托管的KMS CMK生成不同的密钥来加密不同的Object，并且在Object被下载时自动解密。首次使用时，OSS会在KMS平台创建一个OSS托管的CMK。
配置方式如下：
配置Bucket加密方式
配置Bucket加密方式为KMS，指定加密算法为AES256或SM4，但不指定具体的CMK ID。此后，所有上传至此Bucket的Object都会被加密。
为目标Object配置加密方式
上传Object或修改Object的meta信息时，在请求中携带x-oss-server-side-encryption参数，并设置参数值为KMS。此时，OSS将使用默认托管的KMS CMK，并通过AES256加密算法加密Object。如需修改加密算法为SM4，您还需增加x-oss-server-side-data-encryption参数，并设置参数值为SM4。更多信息，请参见[PutObject](../developer-reference/putobject.md)。
使用自带密钥BYOK（Bring Your Own Key）
您在KMS控制台使用BYOK材料生成CMK后，OSS可使用指定的KMS CMK生成不同的密钥来加密不同的Object，并将加密Object的CMK ID记录到Object的元数据中，只有具有解密权限的用户下载Object时才会自动解密。
BYOK材料来源有两种：
由阿里云提供的BYOK材料：在KMS平台创建密钥时，选择密钥材料来源为阿里云KMS。
使用用户自有的BYOK材料：在KMS平台创建密钥时，选择密钥材料来源为外部，并按照要求导入外部密钥材料。关于导入外部密钥的具体操作，请参见[导入密钥材料](../../../kms/documents/key-management-service/support/import-key-material.md)。
配置方式如下：
配置Bucket加密方式
配置Bucket加密方式为KMS，指定加密算法为AES256或SM4，并指定具体的CMK ID。此后，所有上传至此Bucket的Object都会被加密。
为目标Object配置加密方式
上传Object或修改Object的meta信息时，在请求中携带x-oss-server-side-encryption参数，并设置参数值为KMS；携带x-oss-server-side
