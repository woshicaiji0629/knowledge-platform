); auto outcome = client.SetBucketVersioning(setrequest); if (!outcome.isSuccess()) { /* 异常处理。*/ std::cout << "SetBucketVersioning fail" << ",code:" << outcome.error().Code() << ",message:" << outcome.error().Message() << ",requestId:" << outcome.error().RequestId() << std::endl; return -1; } /* 释放网络等资源。*/ ShutdownSdk(); return 0; }
使用命令行工具ossutil
您可以使用命令行工具ossutil来设置指定存储空间的版本控制状态，ossutil的安装请参见[安装](../install-ossutil2.md)[ossutil](../install-ossutil2.md)。
以下命令用于暂停指定存储空间的版本控制功能。
ossutil api put-bucket-versioning --bucket examplebucket --versioning-configuration "{\"Status\":\"Suspended\"}"
关于该命令的更多信息，请参见[put-bucket-versioning](../developer-reference/put-bucket-versioning.md)。
