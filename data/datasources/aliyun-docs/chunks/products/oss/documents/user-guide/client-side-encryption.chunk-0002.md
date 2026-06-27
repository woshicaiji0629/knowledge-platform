## 背景信息
使用客户端加密时，会为每个Object生成一个随机数据加密密钥，用该随机数据加密密钥明文对Object的数据进行对称加密。主密钥用于生成随机的数据加密密钥，加密后的内容会作为Object的meta信息保存在服务端。解密时先用主密钥将加密后的随机密钥解密出来，再用解密出来的随机数据加密密钥明文解密Object的数据。主密钥只参与客户端本地计算，不会在网络上进行传输或保存在服务端，以保证主密钥的数据安全。
重要
客户端加密支持分片上传超过5 GB的文件。上传时需指定文件总大小和分片大小，除最后一个分片外，其他分片大小需一致，且必须是16的整数倍。
使用客户端加密上传文件后，加密元数据受保护，无法通过[CopyObject](../developer-reference/copyobject.md)修改Object meta信息。
对于主密钥的使用，目前支持如下两种方式：
[使用](client-side-encryption.md)[KMS](client-side-encryption.md)[托管用户主密钥](client-side-encryption.md)
[使用用户自主管理密钥](client-side-encryption.md)
完整的示例代码请参见[GitHub](https://github.com/aliyun/aliyun-oss-python-sdk/blob/master/examples/object_crypto.py)。
