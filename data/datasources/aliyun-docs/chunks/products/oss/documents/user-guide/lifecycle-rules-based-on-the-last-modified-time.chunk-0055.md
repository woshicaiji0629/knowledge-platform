## 相关文档
默认情况下，OSS会将Object的上传时间置为其最后一次修改时间。通过生命周期转换文件存储类型的操作不会更新Object的最后一次修改时间。具体哪些操作会影响Object的LastModified，请参见[哪些操作会更新](what-are-the-operations-that-affect-the-lastmodified-attribute-of-oss-objects.md)[Object](what-are-the-operations-that-affect-the-lastmodified-attribute-of-oss-objects.md)[的](what-are-the-operations-that-affect-the-lastmodified-attribute-of-oss-objects.md)[LastModified？](what-are-the-operations-that-affect-the-lastmodified-attribute-of-oss-objects.md)。
当低频访问、归档、冷归档或者深度冷归档存储类型Object在存储不足规定时长时转换了存储类型并提前删除时，需要收取不足规定时长容量费用。更多信息，请参见[Object](../billing-method-for-objects-whose-storage-duration-is-less-than-the-minimum-storage-duration.md)[在存储不足规定时长时如何计费？](../billing-method-for-objects-whose-storage-duration-is-less-than-the-minimum-storage-duration.md)。
生命周期规则仅支持对整个Bucket或与前缀匹配的数据进行批量转储或者删除，如果您希望批量删除指定后缀的数据，您可以使用[ossutil rm](../developer-reference/rm.md)[命令](../developer-reference/rm.md)。
如果您希望OSS自动监测数据的访问模式并识别冷数据，然后转换其存储类型以降低存储成本，请配置[基于最后一次访问时间的生命周期规则](lifecycle-rules-based-on-the-last-access-time.md)。
如果您希望查看Bucket内所有Object的存储类型，请参见[列举文件](list-objects-18.md)。
该文章对您有帮助吗？
反馈
