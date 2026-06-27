### 使用命令行工具ossutil
您可以使用命令行工具ossutil来设置生命周期规则，ossutil的安装请参见[安装](../install-ossutil2.md)[ossutil](../install-ossutil2.md)。
以下示例展示了如何为存储空间examplebucket设置生命周期信息。
ossutil api put-bucket-lifecycle --bucket examplebucket --lifecycle-configuration "{\"Rule\":{\"ID\":\"rule1\",\"Prefix\":\"tmp/\",\"Status\":\"Enabled\",\"Expiration\":{\"Days\":\"10\"},\"Transition\":{\"Days\":\"5\",\"StorageClass\":\"IA\"},\"AbortMultipartUpload\":{\"Days\":\"10\"}}}"
关于该命令的更多信息，请参见[put-bucket-lifecycle](../developer-reference/put-bucket-lifecycle.md)。
