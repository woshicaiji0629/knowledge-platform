## 选择upload类型时需要哪些必填参数？
当cert_type = "upload"时，必须提供以下参数：
server_certificate：证书公钥（PEM格式）。
private_key：证书私钥（PEM格式）。
certificate_config { cert_type = "upload" cert_name = "cert-xxxxxxxxx" server_certificate = "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----" private_key = "-----BEGIN RSA PRIVATE KEY-----\n...\n-----END RSA PRIVATE KEY-----" }
