选择 HTTPS 。 |
| 监听端口 | 输入用来接收请求并向后端服务器进行请求转发的监听端口，端口范围为 1~65535。通常 HTTP 协议使用 80 端口，HTTPS 协议使用 443 端口。 本文输入 443 。 |
| 监听名称 | 输入自定义监听名称。 |
| 高级配置 | 单击 修改 展开高级配置。 |

在配置SSL证书配置向导，选择一个服务器证书。
如果没有可选的服务器证书，您可以在下拉框中单击创建SSL证书进入证书中心，在证书中心[购买](https://help.aliyun.com/zh/ssl-certificate/purchase-an-ssl-certificate#task-q3j-zfp-ydb)或[上传](https://help.aliyun.com/zh/ssl-certificate/upload-an-ssl-certificate)服务器证书。
可选：打开启用双向认证，选择CA证书来源。
选择CA证书来源为阿里云签发，在选择默认CA证书下拉框中选择一个CA证书。
如果没有可选的CA证书，您可以在下拉框中单击购买CA证书，以[创建新](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468)[CA](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468)[证书](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468)。
选择CA证书来源为非阿里云签发，在选择默认CA证书下拉框中选择一个CA证书。
如果没有可选的自签名CA证书，您可以在下拉框中单击上传自签CA证书，在证书应用仓库页面，创建数据来源为上传CA证书的仓库，然后通过证书应用仓库[上传](https://help.aliyun.com/zh/ssl-certificate/create-and-manage-a-certificate-application-repository)自签名根CA或自签名子根CA证书。
说明
仅标准版和WAF增强版的ALB实例支持双向认证，基础版ALB实例不支持双向认证。
开启双向认证后，如果您后续需要关闭双向认证，请参考以下步骤。
在实例页面，单击目标实例ID。
在监听页签，单击目标HTTPS协议监听ID。
在监听详情页签，在SSL 证书区域关闭双向认证开关。
选择TLS安全策略，然后单击下一步。
如果没有可选的TLS安全策略，您可以在下拉框中单击创建 TLS 安全策略。
[TLS](tls-security-policies.md)[安全策略](tls-security-policies.md)包含HTTPS可选的TLS协议版本和配套的加密算法套件。
在选择服务器组配置向导，选择服务器组，查看后端服务器信息，然后单击下一步。
在配置审核配置向导，确认配置信息，然后单击提交。
