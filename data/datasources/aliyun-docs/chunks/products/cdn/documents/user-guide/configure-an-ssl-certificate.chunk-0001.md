## 适用范围
配置前，需了解以下功能边界和约束，以确保证书能成功部署：
购买证书：如果您没有证书，可以选择在[SSL](https://yundunnext.console.aliyun.com/?p=cas#/certExtend/buy)[证书管理控制台](https://yundunnext.console.aliyun.com/?p=cas#/certExtend/buy)申请个人测试证书（原免费证书）或购买正式证书。
私钥要求：如果您选择上传自定义证书，则上传的证书私钥必须是无密码保护的，请先[验证私钥文件是否已去除密码保护](faq-about-https.md)。
国密证书（SM2）：CDN控制台目前不支持直接配置SM2国密双证证书。如需使用国密证书，请通过API接口[设置国密证书](../developer-reference/api-cdn-2018-05-10-setcdndomainsmcertificate.md)进行配置。
