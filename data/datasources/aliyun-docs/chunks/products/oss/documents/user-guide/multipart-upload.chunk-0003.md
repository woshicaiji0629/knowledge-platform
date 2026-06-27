### 通过工具自动分片
对于日常开发、测试、运维或手动上传场景，推荐使用图形化或命令行工具，工具会自动处理分片逻辑，操作便捷。
图形化管理工具ossbrowser
使用[图形化管理工具](../developer-reference/ossbrowser-2-0-overview.md)[ossbrowser 2.0](../developer-reference/ossbrowser-2-0-overview.md)上传文件时，默认启用分片上传机制，并提供可视化的上传进度和状态监控。
命令行工具ossutil
使用[命令行工具](../developer-reference/ossutil-overview.md)[ossutil 2.0](../developer-reference/ossutil-overview.md)的[cp](../developer-reference/cp-upload-file.md)命令上传文件时，工具会自动对超过100MiB的文件启用分片上传，提高大文件上传的成功率和传输效率。如需手动控制分片上传过程，可组合使用[initiate-multipart-upload](../developer-reference/initiate-multipart-upload.md)、[upload-part](../developer-reference/upload-part.md)和[complete-multipart-upload](../developer-reference/complete-multipart-upload.md)命令。
ossutil cp example.zip oss://example-bucket
