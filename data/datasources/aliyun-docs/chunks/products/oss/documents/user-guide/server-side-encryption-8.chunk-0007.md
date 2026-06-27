密功能
登录[OSS](https://oss.console.aliyun.com/)[管理控制台](https://oss.console.aliyun.com/)。
单击Bucket 列表，然后单击创建 Bucket。
在创建 Bucket面板，按以下说明填写各项参数。
其中，服务端加密方式区域配置参数说明如下：

| 参数 | 说明 |
| --- | --- |
| 服务端加密方式 | 选择 Object 的加密方式。取值范围如下： 无 ：不启用服务端加密。 OSS 完全托管 ：使用 OSS 托管的密钥进行加密。OSS 会为每个 Object 使用不同的密钥进行加密，作为额外的保护，OSS 会使用主密钥对加密密钥本身进行加密。 KMS ：使用 KMS 默认托管的 CMK 或指定 CMK ID 进行加解密操作。 使用 KMS 加密方式前，需要开通 KMS 服务。具体操作，请参见 [购买专属](../../../kms/documents/key-management-service/support/purchase-a-dedicated-kms-instance.md) [KMS](../../../kms/documents/key-management-service/support/purchase-a-dedicated-kms-instance.md) [实例](../../../kms/documents/key-management-service/support/purchase-a-dedicated-kms-instance.md) 。 |
| 加密算法 | 可选择 AES256 或 SM4 加密算法。 |
| 加密密钥 | 仅当服务端加密方式选择 KMS 时，需要配置该选项。 选择加密密钥。密钥格式为 <alias>(CMK ID) 。其中 <alias> 为用户主密钥的别名，CMK ID 为用户主密钥 ID。取值范围如下： alias/acs/oss(CMK ID) ：选择该选项后，OSS 会使用默认的服务密钥加密 Bucket 内的数据，并在下载 Bucket 内的 Object 时自动进行解密处理。 alias/<cmkname>(CMK ID ) ：选择该选项后，OSS 会使用指定的服务密钥加密 Bucket 内的数据，并将加密 Object 的 CMK ID 记录到 Object 的元数据中，具有解密权限的用户下载 Object 时会自动解密。其中 <cmkname> 为创建密钥时配置的主密钥可选标识。 使用指定的 CMK ID 前，您需要在 KMS 管理控制台创建一个与 Bucket 处于相同地域的普通密钥或外部密钥。具体操作，请参见 [创建密钥](../../../kms/documents/key-management-service/support/create-a-cmk-1.md) 。 |
