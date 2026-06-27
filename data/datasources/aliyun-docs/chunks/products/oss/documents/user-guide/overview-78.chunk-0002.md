## 注意事项
费用说明
版本控制功能本身不收取任何费用，但对当前版本和所有历史版本的文件都会收取存储费用。为避免不必要的存储费用，请通过生命周期及时删除不需要的历史版本文件。具体操作，请参见[生命周期](overview-54.md)。此外，若您对历史版本文件进行下载或恢复等操作，还会产生相应的请求费用、流量费用等。计费详情，请参见[计量项与计费项](../billing-overview.md)。
权限说明
只有Bucket的拥有者及授予了PutBucketVersioning权限的RAM用户才能配置版本控制。
功能互斥
如果Bucket版本控制状态为开启或暂停：
禁止覆盖规则将不生效。更多信息，请参见[禁止文件覆盖写](prevent-file-overwrite.md)。
上传文件时附加的覆盖同名文件请求头x-oss-forbid-overwrite将不生效。更多信息，请参见[PutObject](../developer-reference/putobject.md)。
版本控制与OSS-HDFS服务
同一Bucket禁止同时开通OSS-HDFS服务和版本控制，否则可能导致OSS-HDFS服务异常。为确保服务稳定性，请尽快暂停版本控制，并配置生命周期规则清理删除标记。
