新证书应用后通常一到三分钟生效。
QUIC监听仅需配置服务器证书，不支持双向认证。
如需多域名访问或挂载多个服务器证书，可为监听[添加扩展证书](../use-cases/configure-an-alb-instance-to-serve-multiple-domain-names-over-https.md)。
在配置SSL证书配置向导，选择服务器证书。
如果没有可选的服务器证书，可单击创建SSL证书进入证书中心，在证书中心[购买](https://help.aliyun.com/zh/ssl-certificate/purchase-an-ssl-certificate#task-q3j-zfp-ydb)或[上传](https://help.aliyun.com/zh/ssl-certificate/upload-an-ssl-certificate)服务器证书。
仅HTTPS监听：选择TLS安全策略。
系统提供多种预定义策略可直接选用。如需自定义TLS协议版本和加密算法套件，可单击创建 TLS 安全策略并创建自定义策略。更多信息，请参见[TLS](tls-security-policies.md)[安全策略](tls-security-policies.md)。
仅HTTPS监听（可选）：打开启用双向认证，选择CA证书来源并选择CA证书。
选择CA证书来源为阿里云签发，在选择默认CA证书下拉框中选择CA证书。如果没有可选的CA证书，可单击购买CA证书以[创建新](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468)[CA](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468)[证书](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468)。
选择CA证书来源为非阿里云签发，在选择默认CA证书下拉框中选择CA证书。如果没有可选的CA证书，可单击上传自签CA证书，通过证书应用仓库[上传自签名](https://help.aliyun.com/zh/ssl-certificate/create-and-manage-a-certificate-application-repository)[CA](https://help.aliyun.com/zh/ssl-certificate/create-and-manage-a-certificate-application-repositor
