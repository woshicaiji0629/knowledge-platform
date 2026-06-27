# 需要转换的私钥 -----BEGIN PRIVATE KEY----- [私钥内容] -----END PRIVATE KEY-----# 转换命令 openssl rsa -in old_server_key.pem -out new_server_key.pem
对于从第三方服务商下载或申请的证书，请注意区分公钥和私钥文件：
通常.pem或.crt文件包含公钥（证书内容），.key或.private文件包含私钥。
上传时，请将公钥文件（.pem或.crt）的内容填入"证书（公钥）"栏，将私钥文件（.key或.private）的内容填入"私钥"栏。
切勿上传CSR文件（Certificate Signing Request，证书签名请求）。CSR文件仅用于向证书颁发机构申请证书，不能作为证书或私钥上传使用。
若使用Nginx格式证书，请确保：
证书文件内容为PEM格式，以-----BEGIN CERTIFICATE-----开头；
私钥文件内容为PEM格式，以-----BEGIN RSA PRIVATE KEY-----或-----BEGIN PRIVATE KEY-----开头；
证书与私钥匹配；
去除文件中可能存在的额外空格、换行或非标准字符。
若证书链不完整，需将中间证书合并到主证书文件中一并上传。详细信息，请参见[证书格式说明](certificate-formats.md)。
