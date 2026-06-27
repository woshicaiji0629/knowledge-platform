n-readable选项，对字节、数量数据，提供了以人类可读方式输出信息。即字节数据转成Ki|Mi|Gi|Ti|Pi后缀格式（1024 base），数量数据转成k|m|g|t|p后缀格式(1000 base)。
例如：原始模式
ossutil stat oss://bucketexample ACL : private AccessMonitor : Disabled ArchiveObjectCount : 2 ArchiveRealStorage : 10 ArchiveStorage : 131072 ... StandardObjectCount : 119212 StandardStorage : 66756852803 Storage : 66756852813 StorageClass : Standard TransferAcceleration : Disabled
友好模式
ossutil stat oss://bucketexample --human-readable ACL : private AccessMonitor : Disabled ArchiveObjectCount : 2 ArchiveRealStorage : 10 ArchiveStorage : 131.072k ... StandardObjectCount : 119.212k StandardStorage : 66.757G Storage : 66.757G StorageClass : Standard TransferAcceleration : Disabled
