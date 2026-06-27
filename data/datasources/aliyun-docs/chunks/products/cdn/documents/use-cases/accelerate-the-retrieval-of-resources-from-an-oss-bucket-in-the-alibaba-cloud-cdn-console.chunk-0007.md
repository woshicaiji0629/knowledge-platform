### 步骤五：安全配置
启用 HTTPS 加密传输
如果应用在配置阿里云 CDN 之前已支持 HTTPS 访问，务必进行 HTTPS 证书的配置，否则域名将不再支持 HTTPS 访问。
说明
开启HTTPS将产生HTTPS请求数，静态HTTPS请求数每月前500万次免费，超过500万次后，开始计费。HTTPS请求数计费不能使用CDN流量包抵扣，请确保您的账户余额充足，或购买HTTPS请求包，避免欠费导致CDN停止服务。详情敬请参见[静态](../product-overview/billing-of-https-requests-for-static-content.md)[HTTPS](../product-overview/billing-of-https-requests-for-static-content.md)[请求数](../product-overview/billing-of-https-requests-for-static-content.md)。
HTTPS 请求数计费不能使用 CDN 流量包抵扣，请确保账户余额充足，或购买 HTTPS 请求包，避免欠费导致 CDN 停止服务。
前往阿里云 CDN 控制台的域名管理列表，找到之前添加的域名，点击，进入域名配置页面。
选择HTTPS配置页签中的HTTPS证书，点击修改配置。
在HTTPS设置界面，打开HTTPS安全加速开关，并选择证书：

| 证书类型 | 说明 |
| --- | --- |
| 云盾（SSL）证书中心 | 从阿里云 SSL 证书产品中选择已有证书。需在中搜索选择。 |
| 自定义上传（证书+私钥） | 手动上传 PEM 格式的证书内容和私钥。需设置证书名称、上传和。 |
|  | 阿里云 Digicert 免费 DV 证书，有效期一年，自动续签。不支持泛域名。需勾选授权同意复选框。 |
| CSR 证书 | 提交 CSR 证书签名请求后使用。 |
