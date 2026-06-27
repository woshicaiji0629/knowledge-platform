在同一阿里云账号下。
申请SSL免费证书时不会自动添加www前缀，需手动输入完整的域名进行申请。
若因域名格式（如根域名与子域名）导致无法自动匹配，建议在数字证书管理服务控制台创建部署任务将证书部署至CDN，或下载证书文件后通过"自定义上传"方式配置。
Q：CDN配置HTTPS后访问返回ERR_SSL_PROTOCOL_ERROR或SSL_ERROR_NO_CIPHER_OVERLAP错误，如何解决？
该错误通常表示CDN节点未正确配置SSL证书或证书无效。请按以下步骤排查：
检查CDN控制台HTTPS配置，确保证书已上传并启用，且证书状态正常（未过期）。
若使用自定义证书，请确保证书格式正确（PEM格式）且私钥无密码保护。
确保证书与私钥匹配，且证书绑定的域名与加速域名一致。
若之前未配置过HTTPS证书，请先在CDN控制台完成证书配置。在配置完成前，可临时使用HTTP协议访问（去掉URL中的"s"）。
Q：如何通过API或CLI为CDN域名配置SSL证书？
可调用[SetCdnDomainSSLCertificate](../developer-reference/api-cdn-2018-05-10-setcdndomainsslcertificate.md)接口配置。
若使用阿里云CLI，命令示例如下：
aliyun cdn set-cdn-domain-ssl-certificate \ --domain-name <您的加速域名> \ --cert-name <证书名称> \ --cert-id <证书ID> \ --cert-type cas \ --ssl-protocol on \ --region cn-hangzhou
若上传自定义证书，需传入ssl-pub（公钥）和ssl-pri（私钥）参数，且cert-type设为upload。命令示例如下：
aliyun cdn set-cdn-domain-ssl-certificate \ --domain-name example.com \ --cert-name yourCertName \ --cert-type upload \ --ssl-protocol on \ --ssl-pub "<证书公钥PEM内容>" \ --ssl-pri "<私钥PEM内容>" \ --region cn-hangzhou
重要
不要将CSR文件内容传入接口。CSR文件仅用于申请证书，不能作为证书或私钥使用。
