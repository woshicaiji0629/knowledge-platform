## 使用限制
高性能本地盘实例只支持迁移主可用区。
暂不支持[Serverless](https://help.aliyun.com/zh/document_detail/607742.html#main-2272489)实例迁移可用区。
当实例存储类型为高性能云盘并且开启了[Buffer Pool Extension（BPE）](buffer-pool-extension-bpe.md)时，无法迁移至不支持IO加速的可用区。IO加速支持的地域及可用区请参见[支持范围](buffer-pool-extension-bpe.md)。
您可以关闭IO加速后，再进行可用区迁移。
