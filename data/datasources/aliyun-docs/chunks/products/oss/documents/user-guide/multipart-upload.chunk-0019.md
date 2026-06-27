## 清理碎片文件
分片上传过程意外中断且未调用AbortMultipartUpload接口时，已上传的分片会作为碎片文件保留在Bucket中并持续产生存储费用。及时清理这些碎片文件可避免不必要的存储成本。
通过控制台
前往[Bucket](https://oss.console.aliyun.com/bucket)[列表](https://oss.console.aliyun.com/bucket)，单击目标Bucket。
在文件列表单击碎片管理，查看并删除碎片文件。
通过生命周期规则
配置生命周期规则可实现对过期碎片的自动清理，减少手动维护工作量并防止遗漏。具体操作参见[通过生命周期规则清理过期碎片](configuration-examples.md)。
通过工具
图形化管理工具ossbrowser
在Bucket的文件列表页面单击文件碎片，查看并删除碎片文件。
命令行工具ossutil
使用[abort-multipart-upload](../developer-reference/abort-multipart-upload.md)命令取消分片上传任务并删除对应的分片数据。命令示例如下：
ossutil api abort-multipart-upload --bucket example-bucket --key dest.jpg --upload-id D9F4****************************
通过SDK
通过调用AbortMultipartUpload接口取消分片上传任务并删除对应的分片数据。以下为常见语言的SDK取消分片上传任务代码示例，更多语言的使用示例请参见[SDK](../developer-reference/sdk-code-samples.md)[参考](../developer-reference/sdk-code-samples.md)中对应语言的示例代码。
运行代码前需安装对应语言的SDK并配置访问凭证环境变量，使用RAM用户或RAM角色时还需参考[API](multipart-upload.md)[和权限说明](multipart-upload.md)进行接口授权。
