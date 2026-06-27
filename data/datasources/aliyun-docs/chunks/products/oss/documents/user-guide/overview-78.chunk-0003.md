## 版本控制状态
Bucket包含三种版本控制状态，分别为未开启、开启或者暂停。
默认情况下，Bucket版本控制状态为“未开启”。如果Bucket处于“开启”版本状态，将无法返回至“未开启”状态。但是，您可以暂停Bucket的版本控制状态。
当Bucket版本控制处于“开启”状态时，OSS将为新上传的Object生成全局唯一的随机字符串版本ID。关于启用版本控制状态下Object的具体操作，请参见[开启版本控制下](manage-objects-in-a-versioning-enabled-bucket.md)[Object](manage-objects-in-a-versioning-enabled-bucket.md)[的操作](manage-objects-in-a-versioning-enabled-bucket.md)。
当Bucket版本控制处于“暂停”状态时，OSS将为新上传的Object生成特殊字符串为“null”的版本ID。关于暂停版本控制状态下Object的具体操作，请参见[暂停版本控制下](manage-objects-in-a-versioning-suspended-bucket.md)[Object](manage-objects-in-a-versioning-suspended-bucket.md)[的操作](manage-objects-in-a-versioning-suspended-bucket.md)。
说明
当Bucket版本控制处于“开启”状态时，由于Object的每个版本都被保存下来，每个版本都会占用存储空间，OSS会对Object的所有版本收取存储费用。建议结合您的使用场景通过生命周期规则，将当前版本或历史版本Object转换为低频访问或归档存储类型以及删除不再需要的历史版本，以降低您的存储费用，更多信息请参见[使用最后一次修改时间的生命周期规则结合版本控制降低存储成本](configure-lifecycle-rules-to-manage-object-versions.md)。
