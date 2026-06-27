### 使用命令行工具ossutil
方式一：为Bucket开启服务端加密
您可以使用命令行工具ossutil来为Bucket开启服务端加密，ossutil的安装请参见[安装](../install-ossutil2.md)[ossutil](../install-ossutil2.md)。
以下示例展示了如何为已创建的存储空间examplebucket设置服务端加密方式为AES256。
ossutil api put-bucket-encryption --bucket examplebucket --server-side-encryption-rule "{\"ApplyServerSideEncryptionByDefault\":{\"SSEAlgorithm\":\"AES256\"}}"
如果您想了解该命令的更多信息，请参见[put-bucket-encryption](../developer-reference/put-bucket-encryption.md)。
方式二：上传文件时设置服务端加密
ossutil支持在上传文件时指定文件的服务端加密方式，ossutil的安装请参见[安装](../install-ossutil2.md)[ossutil](../install-ossutil2.md)。以下示例展示了如何在上传文件时设定服务端加密方式为AES256。
ossutil cp examplefile.txt oss://examplebucket --metadata=x-oss-server-side-encryption:AES256
如果您想了解该命令的更多信息，请参见[cp（上传文件）](../developer-reference/cp-upload-file.md)。
