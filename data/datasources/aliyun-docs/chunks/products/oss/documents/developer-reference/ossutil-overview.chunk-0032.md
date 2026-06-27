### 使用RAMRoleARN
如果应用程序需要授权访问OSS，例如跨阿里云账号访问OSS，可以使用RAMRoleARN初始化凭证提供者。该方式底层实现是STS Token。通过指定RAM角色的ARN（Alibabacloud Resource Name），Credentials工具会前往STS服务获取STS Token，并在会话到期前调用AssumeRole接口申请新的STS Token。此外，还可以通过为policy赋值来限制RAM角色到一个更小的权限集合。
重要
阿里云账号拥有资源的全部权限，AK一旦泄露，会给系统带来巨大风险，不建议使用。推荐使用最小化授权的RAM用户的AK。
如需创建RAM用户的AK，请直接访问[创建](../../../ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](../../../ram/documents/user-guide/create-an-accesskey-pair.md)。RAM用户的Access Key ID、Access Key Secret信息仅在创建时显示，请及时保存，如若遗忘请考虑创建新的AK进行轮换。
如需获取RAMRoleARN，请直接访问[创建角色](../../../ram/documents/developer-reference/api-ram-2015-05-01-createrole.md)。
生成如下配置文件，并保存在~/.ossutilconfig。不支持通过环境变量或者命令行选项方式设置。
[default] accessKeyID = yourAccessKeyID accessKeySecret = yourAccessKeySecret mode = RamRoleArn roleArn = acs:ram::137918634953****:role/Alice roleSessionName = session_name_example region=cn-hangzhou
通过如下命令查询examplebucket中的对象。
ossutil ls oss://examplebucket -c ~/.ossutilconfig
