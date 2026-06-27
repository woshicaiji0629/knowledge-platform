## AccessKey（访问密钥）
AccessKey简称AK，指的是访问身份验证中用到的AccessKey ID和AccessKey Secret。OSS通过使用AccessKey ID和AccessKey Secret对称加密的方法来验证某个请求的发送者身份。AccessKey ID用于标识用户；AccessKey Secret是用户用于加密签名字符串和OSS用来验证签名字符串的密钥，必须保密。对于OSS来说，AccessKey的来源有：
Bucket的拥有者申请的AccessKey。
被Bucket的拥有者通过RAM授权给第三方请求者的AccessKey。
被Bucket的拥有者通过STS授权给第三方请求者的AccessKey。
更多AccessKey介绍请参见[创建](https://help.aliyun.com/zh/document_detail/53045.html#task968)[AccessKey](https://help.aliyun.com/zh/document_detail/53045.html#task968)。
