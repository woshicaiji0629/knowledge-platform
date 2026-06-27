域名。通过内网和外网访问同一个Region所需要的Endpoint也是不同的。例如杭州Region的外网Endpoint是oss-cn-hangzhou.aliyuncs.com，内网Endpoint是oss-cn-hangzhou-internal.aliyuncs.com。具体的内容请参见[各个](regions-and-endpoints.md)[Region](regions-and-endpoints.md)[对应的](regions-and-endpoints.md)[Endpoint](regions-and-endpoints.md)。
访问密钥
AccessKey简称AK，指的是访问身份验证中用到的AccessKey ID和AccessKey Secret。OSS通过使用AccessKey ID和AccessKey Secret对称加密的方法来验证某个请求的发送者身份。AccessKey ID用于标识用户；AccessKey Secret是用户用于加密签名字符串和OSS用来验证签名字符串的密钥，必须保密。对于OSS来说，AccessKey的来源有：
Bucket的拥有者申请的AccessKey。
被Bucket的拥有者通过RAM授权给第三方请求者的AccessKey。
被Bucket的拥有者通过STS授权给第三方请求者的AccessKey。
更多AccessKey介绍请参见[创建](https://help.aliyun.com/zh/document_detail/53045.html#task968)[AccessKey](https://help.aliyun.com/zh/document_detail/53045.html#task968)。
原子性和强一致性
Object操作在OSS上具有原子性，操作要么成功要么失败，不存在中间状态的Object。当Object上传完成时，OSS即可保证读到的Object是完整的，OSS不会返回给用户一个部分上传成功的Object。
Object操作在OSS同样具有强一致性，当用户收到了上传（PUT）成功的响应时，该上传的Object进入立即可读状态，并且Object的冗余数据已经写入成功。不存在上传的中间状态，即执行read-after-write，却无法读取到数据。对于删除操作，用户删除指定的Object成功之后，该Object立即不存在。
关于OSS基本概念的完整介绍，请参见[基本概念](../terms-2.md)。
