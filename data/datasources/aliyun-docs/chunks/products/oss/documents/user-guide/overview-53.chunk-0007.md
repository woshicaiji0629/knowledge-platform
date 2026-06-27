## 相关文档
默认情况下，上传到Bucket内Object的存储类型默认采用标准存储。标准存储适用于频繁访问、低延迟数据存取的场景。如果您识别到部分Object不再需要频繁访问，或者为了节省存储成本，您可以考虑将标准存储类型的Object转换为更为经济的存储类型，例如低频访问、归档类型等。具体操作，请参见[转换存储类型](convert-storage-classes.md)。
深度冷归档存储提供高持久性、低成本的存储服务，适用于需要超长时间存放的极冷数据。具体操作，请参见[深度冷归档存储使用最佳实践](deep-cold-archive-storage-usage-best-practices.md)。
如果您希望了解存储类型转换后，目标Object存储类型存储容量增加了，但是源Object存储类型容量没有减少的原因以及解决方法，请参见[为什么存储类型转换后，源](../why-does-the-storage-capacity-of-the-source-object-remain-unchanged-after-the-storage-type-conversion.md)[Object](../why-does-the-storage-capacity-of-the-source-object-remain-unchanged-after-the-storage-type-conversion.md)[存储类型容量保持不变？](../why-does-the-storage-capacity-of-the-source-object-remain-unchanged-after-the-storage-type-conversion.md)。
该文章对您有帮助吗？
反馈
