## 上传自定义证书
如果您拥有的是第三方服务商签发或自签名的证书，需要先将证书和私钥处理成CDN支持的格式，然后上传。
证书（公钥）
CDN只支持上传PEM格式的证书。其他格式的证书需要参考[证书格式转换](certificate-formats.md)将其转换成PEM格式。针对不同证书颁发机构的证书，对证书内容的上传有不同的要求：
Root CA机构颁发的证书（一个证书文件）
使用文本编辑器即可打开PEM格式的证书文件，将以-----BEGIN CERTIFICATE-----开头和以-----END CERTIFICATE-----结尾的内容一并上传。
-----BEGIN CERTIFICATE----- [证书内容] -----END CERTIFICATE-----
中级机构颁发的证书（多个证书文件）
需将服务器证书、所有中间CA证书按顺序拼接成一个完整的证书链文件。文件内容应遵循以下格式：
-----BEGIN CERTIFICATE----- [服务器证书内容] -----END CERTIFICATE----- -----BEGIN CERTIFICATE----- [中间CA证书内容] -----END CERTIFICATE-----
私钥
私钥的扩展名一般为.key或.pem。使用文本编辑器即可打开私钥文件。不同内容的私钥上传要求区别如下：
RSA私钥直接上传
如果私钥内容以-----BEGIN RSA PRIVATE KEY-----开头，-----END RSA PRIVATE KEY-----结尾，则直接上传私钥内容。
-----BEGIN RSA PRIVATE KEY----- [私钥内容] -----END RSA PRIVATE KEY-----
其他格式私钥先转换格式再上传
如果您得到的是以-----BEGIN PRIVATE KEY-----开头，以-----END PRIVATE KEY-----结尾的私钥，您需要使用OpenSSL工具的转换命令先对私钥进行转换，然后将转换后的私钥内容按照直接上传的操作处理。其中old_server_key.pem为转换前的私钥，new_server_key.pem为转换后的私钥。
