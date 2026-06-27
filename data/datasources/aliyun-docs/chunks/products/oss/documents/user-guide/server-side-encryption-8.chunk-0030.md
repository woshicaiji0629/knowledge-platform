## 使用OSS完全托管密钥进行加解密
OSS负责生成和管理数据加密密钥，并采用高强度、多因素的安全措施进行保护。数据加密的算法采用行业标准的AES256（即256位高级加密标准）和国密SM4算法。
配置方式如下：
配置Bucket加密方式
配置Bucket加密方式为OSS完全托管，并指定加密算法为AES256或SM4。此后，所有上传至此Bucket的Object都会默认被加密。
为目标Object配置加密方式
上传Object或修改Object的meta信息时，在请求中携带x-oss-server-side-encryption参数，并设置参数值为AES256或SM4。此时，OSS将使用OSS完全托管的密钥加密Object。更多信息，请参见[PutObject](../developer-reference/putobject.md)。
