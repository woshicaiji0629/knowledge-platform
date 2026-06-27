## API
可直接发起REST API请求，需在请求头中加入x-oss-request-payer: requester，并确保此请求头包含在签名计算中，签名的计算方法见[在](../developer-reference/recommend-to-use-signature-version-4.md)[Header](../developer-reference/recommend-to-use-signature-version-4.md)[中包含签名](../developer-reference/recommend-to-use-signature-version-4.md)。
GET /oss.jpg HTTP/1.1 Host: oss-example.oss-cn-hangzhou.aliyuncs.com Date: Fri, 24 Feb 2012 06:38:30 GMT Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
