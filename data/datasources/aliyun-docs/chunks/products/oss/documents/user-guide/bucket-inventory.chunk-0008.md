| 参数 | 说明 |
| --- | --- |
| 状态 | 设置清单任务的状态，选择 启动 。 |
| 规则名称 | 设置清单任务的名称。只能包含小写字母、数字、短划线（-），且不能以短划线（-）开头或结尾。 |
| 清单报告存储至 | 设置清单报告的存储路径。配置清单的 Bucket 与存放清单 Bucket 必须同账号、同地域。 若需将报告保存到存储空间 examplebucket 的 exampledir1 路径，请填写 exampledir1/ ，指定路径在 Bucket 中不存在时，OSS 会自动创建该路径。 若留空，报告将保存在根目录。 重要 为避免影响 OSS-HDFS 服务的正常使用或者引发数据污染的风险，在开通了 OSS-HDFS 服务的 Bucket 设置清单报告规则时，禁止将清单报告目录填写为 .dlsdata/ 。 |
| 清单文件扫描范围 | 扫描整个 Bucket ：扫描整个 Bucket 的所有文件。 按前缀匹配 ：用于仅扫描指定前缀下的文件，例如 exampledir1/ 。 |
| 清单报告加密选项 | 选择是否加密清单文件。 无 ：不加密。 AES256 ：使用 AES256 加密算法加密清单文件。 KMS ：使用 KMS 密钥加密清单文件，可以选择使用 OSS 托管的 KMS 密钥或在 KMS 平台 [创建一个与目标](../../../kms/documents/key-management-service/support/create-a-cmk-1.md) [Bucket](../../../kms/documents/key-management-service/support/create-a-cmk-1.md) [相同地域的](../../../kms/documents/key-management-service/support/create-a-cmk-1.md) [KMS](../../../kms/documents/key-management-service/support/create-a-cmk-1.md) [密钥](../../../kms/documents/key-management-service/support/create-a-cmk-1.md) 。 说明 使用 KMS 密钥功能时会产生少量的 KMS 密钥 API 调用费用，费用详情请参考 [KMS 1.0](../../../kms/documents/key-management-service/support/billing-of-kms.md) [计费说明](../../../kms/documents/key-management-service/support/billing-of-kms.md) 。 |
|
