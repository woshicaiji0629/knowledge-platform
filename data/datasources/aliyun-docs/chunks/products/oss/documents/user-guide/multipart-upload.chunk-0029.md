## API和权限说明
阿里云主账号默认拥有全部API的操作权限。RAM用户或RAM角色使用分片上传功能需根据具体操作的API授予相应权限。更多信息请参见[RAM Policy](../ram-policy-overview.md)和[RAM Policy](../common-examples-of-ram-policies.md)[常见示例](../common-examples-of-ram-policies.md)。

| API | Action | 说明 |
| --- | --- | --- |
| InitiateMultipartUpload | oss:PutObject | 初始化分片上传任务。 |
| oss:PutObjectTagging | 初始化分片上传任务时，如果通过 x-oss-tagging 指定对象文件的标签，则需要此操作的权限。 |  |
| kms:GenerateDataKey | 上传对象文件时，如果对象文件的元数据包含 X-Oss-Server-Side-Encryption: KMS，则需要这两个操作的权限。 |  |
| kms:Decrypt |  |  |
| UploadPart | oss:PutObject | 上传分片。 |
| UploadPartCopy | oss:GetObject | 从一个已存在的对象文件中拷贝数据来上传一个分片时，需要读取源对象文件的权限。 |
| oss:PutObject | 从一个已存在的对象文件中拷贝数据来上传一个分片时，需要写入目标对象文件的权限。 |  |
| oss:GetObjectVersion | 从一个已存在的对象文件中拷贝数据来上传一个分片时，如果通过 versionId 指定对象文件的版本，需要读取源对象文件的指定版本的权限。 |  |
| CompleteMultipartUpload | oss:PutObject | 将分片合并为对象文件。 |
| oss:PutObjectTagging | 将分片合并为对象文件时，如果通过 x-oss-tagging 指定对象文件的标签，则需要此操作的权限。 |  |
| AbortMultipartUpload | oss:AbortMultipartUpload | 取消分片上传事件并删除对应的分片数据。 |
| ListMultipartUploads | oss:ListMultipartUploads | 列举所有执行中的分片上传事件，即已经初始化但尚未完成或者尚未被中止的分片上传事件。 |
| ListParts | oss:ListParts | 列举指定 Upload ID 所属的所有已经上传成功的分片。 |

该文章对您有帮助吗？
反馈
