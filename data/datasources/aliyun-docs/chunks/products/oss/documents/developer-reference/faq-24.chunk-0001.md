## 签名错误排查方法
如果您的请求出现签名报错，您可以按照以下步骤进行排查。
确认签名所用的AccessKey ID与AccessKey Secret是否填写正确。
您可以使用AccessKey ID与AccessKey Secret登录ossbrowser来验证正确性。具体步骤，请参见[安装并登录](install-ossbrowser-1-0.md)[ossbrowser](install-ossbrowser-1-0.md)。
检查签名算法是否正确。
OSS提供两种携带签名的请求方式，分别为[在](include-signatures-in-the-authorization-header.md)[Header](include-signatures-in-the-authorization-header.md)[中包含签名](include-signatures-in-the-authorization-header.md)和[在](ddd-signatures-to-urls.md)[URL](ddd-signatures-to-urls.md)[中包含签名](ddd-signatures-to-urls.md)。关于这两种签名方式的算法说明如下：
在Header中包含签名
StringToSign = VERB + "\n" + Content-MD5 + "\n" + Content-Type + "\n" + Date + "\n" + CanonicalizedOSSHeaders + CanonicalizedResource Signature = base64(hmac-sha1(AccessKeySecret, StringToSign)
在URL中包含签名
StringToSign = VERB + "\n" + CONTENT-MD5 + "\n" + CONTENT-TYPE + "\n" + EXPIRES + "\n" + CanonicalizedOSSHeaders + CanonicalizedResource Signature = urlencode(base64(hmac-sha1(AccessKeySecret, StringToSign)))
如果业务场景允许，推荐您使用SDK访问OSS，免去手动计算签名的过程。具体步骤，请参见[使用阿里云](overview-63.md)[SDK](overview-63.md)[发起请求](overview-63.md)。
比对响应体中的StringToSign字段与您发起请求的内容是否存在差异。
StringToSign字段表示待签字符串，即签名算法中需要使用AccessKey Secret进行加密的内容。
请求示例如下：
PUT /bucket/abc?acl D
