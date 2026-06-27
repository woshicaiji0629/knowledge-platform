## 加密方式
OSS针对不同使用场景提供了两种服务端加密方式，您可以根据实际使用场景选用。

| 加密方式 | 功能描述 | 使用场景 | 注意事项 | 费用说明 |
| --- | --- | --- | --- | --- |
| 使用 KMS 托管密钥进行加解密（SSE-KMS） | 使用 KMS 托管的默认 CMK（Customer Master Key）或指定 CMK 进行加解密操作。数据无需通过网络发送到 KMS 服务端进行加解密。 | 因安全合规的要求，需要使用自管理、可指定的密钥。 | 用于加密 Object 的密钥也会被加密，并写入 Object 的元数据中。 KMS 托管密钥的服务端加密方式仅加密 Object 数据，不加密 Object 的元数据。 | 使用 OSS 控制台默认创建的 KMS 密钥 免费。 使用自选的 KMS 密钥，会在 KMS 侧产生费用。费用详情，请参见 [KMS](../../../kms/documents/key-management-service/product-overview/kms-billing.md) [计费标准](../../../kms/documents/key-management-service/product-overview/kms-billing.md) 。 |
| 使用 OSS 完全托管密钥进行加解密（SSE-OSS） | 使用 OSS 完全托管的密钥加密每个 Object。为了提升安全性，OSS 还会使用主密钥对加密密钥本身进行加密。 | 仅需要基础的加密能力，对密钥无自管理需求。 | 无。 | 免费。 |
