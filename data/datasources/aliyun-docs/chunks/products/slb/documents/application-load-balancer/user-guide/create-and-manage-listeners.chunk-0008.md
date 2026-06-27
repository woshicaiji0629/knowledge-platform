ate/create-and-manage-a-certificate-application-repository)[CA](https://help.aliyun.com/zh/ssl-certificate/create-and-manage-a-certificate-application-repository)[证书](https://help.aliyun.com/zh/ssl-certificate/create-and-manage-a-certificate-application-repository)。
仅标准版和WAF增强版实例支持双向认证，基础版不支持。
步骤三：选择服务器组
在选择服务器组配置向导，选择服务器组，并查看后端服务器信息，然后单击下一步。
步骤四：配置审核
在配置审核页面，确认配置信息，单击提交。
快速创建监听
前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，单击目标实例ID，在监听页签下单击快速创建监听。
在快速创建监听对话框中，完成以下参数的配置，然后单击确定。
选择监听协议：HTTP、HTTPS或QUIC。
监听端口：端口范围为1~65535。通常HTTP使用80端口，HTTPS使用443端口。
选择服务器证书（仅HTTPS和QUIC监听）：选择服务器证书。如果没有可选的服务器证书，可单击创建SSL证书进入证书中心，在证书中心[购买](https://help.aliyun.com/zh/ssl-certificate/purchase-an-ssl-certificate#task-q3j-zfp-ydb)或[上传](https://help.aliyun.com/zh/ssl-certificate/upload-an-ssl-certificate)服务器证书。
TLS安全策略（仅HTTPS监听）：选择TLS安全策略。如需自定义TLS协议版本和加密算法套件，可单击创建 TLS 安全策略并创建自定义策略。更多信息，请参见[TLS](tls-security-policies.md)[安全策略](tls-security-policies.md)。
转发的后端服务器组：选择后端服务器组类型和后端服务器。
