## 注意事项
在开启了SSE-KMS加密的Bucket中请求上传、下载、访问文件，需确保对指定的CMK ID拥有使用权限，且请求类型不是匿名请求，否则请求失败，并返回This request is forbidden by kms。
镜像回源至Bucket中的文件默认不加密。
开启或修改Bucket加密方式不影响Bucket中已有文件的加密配置。
同一个Object在同一时间内仅可以使用一种服务端加密方式。
如果配置了存储空间加密，仍然可以在上传或拷贝Object时单独对Object配置加密方式，且以Object配置的加密方式为准。更多信息，请参见[PutObject](../developer-reference/putobject.md)。
