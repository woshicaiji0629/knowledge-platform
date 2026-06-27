| 错误码 | 错误信息 | 报错原因 | 解决方案 |
| --- | --- | --- | --- |
| AccessDenied | The bucket you are attempting to access must be addressed using the specified endpoint | srcDomain 或 destDomain 填写错误。 | 请按照 [域名列表](user-guide/regions-and-endpoints.md) 填写正确的Endpoint。 |
| SignatureDoesNotMatch | The request signature we calculated does not match the signature you provided | destAccessKey 和 destSecretKey 有误。 | 请填写正确的AK信息。 |
| 无 | The bucket name “xxx/xx” is invalid | 配置项 destBucket 填写不正确。 | 检查配置项 destBucket 是否填写正确，Bucket名称是不带正斜线（/）以及路径的。 |
| ConnectionTimeout | Connect to xxx.oss-cn-beijing-internal.aliyuncs.com:80 timed out | 这个是连接超时的报错，通常原因是迁移用的设备非ECS实例或不是与OSS同地域的ECS实例，但是配置文件使用了OSS的内网域名。OSS内网域名仅支持同地域ECS实例访问。 | 该问题可以通过以下方法解决： 修改配置文件中域名为外网Endpoint，清除任务后重新提交任务。 使用与OSS同地域的ECS实例运行迁移任务。 |
| InvalidBucketName | The specified bucket is not valid | 配置文件里的 destDomian 配置的域名是Bucket所在地域的Endpoint地址，而不是带Bucket名称的二级域名。 | 填写正确的Bucket所在地域的Endpoint地址，例如Bucket在华北2（北京），应填写oss-cn-beijing.aliyuncs.com。详情请参见 [配置文件示例](overview-36.md) 。 |
| RequestTimeTooSkewed | Unable to execute HTTP request: The Difference between … is too large | 该报错可能是以下情况导致： 本地机器时间不对，与OSS服务器时间相差15分钟以上，该情况居多。 可能是并发太高，尤其是CPU占用率很高，导致并发上传慢。 | 该问题可以通过以
