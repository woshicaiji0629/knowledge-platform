# 如何在CDN上配置SSL证书实现安全的HTTPS访问-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-an-ssl-certificate

# 配置HTTPS证书
为CDN加速域名配置HTTPS证书，能够加密客户端与CDN节点间的通信链路，防止数据在公网传输中被窃取或篡改，提升业务安全。在阿里云数字证书管理服务（原SSL）中购买的证书支持批量部署至CDN平台，具体操作请参见：[批量配置](configure-an-ssl-certificate-for-multiple-domain-names.md)[HTTPS](configure-an-ssl-certificate-for-multiple-domain-names.md)[证书](configure-an-ssl-certificate-for-multiple-domain-names.md)。
## 适用范围
配置前，需了解以下功能边界和约束，以确保证书能成功部署：
购买证书：如果您没有证书，可以选择在[SSL](https://yundunnext.console.aliyun.com/?p=cas#/certExtend/buy)[证书管理控制台](https://yundunnext.console.aliyun.com/?p=cas#/certExtend/buy)申请个人测试证书（原免费证书）或购买正式证书。
私钥要求：如果您选择上传自定义证书，则上传的证书私钥必须是无密码保护的，请先[验证私钥文件是否已去除密码保护](faq-about-https.md)。
国密证书（SM2）：CDN控制台目前不支持直接配置SM2国密双证证书。如需使用国密证书，请通过API接口[设置国密证书](../developer-reference/api-cdn-2018-05-10-setcdndomainsmcertificate.md)进行配置。
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击HTTPS配置。
在HTTPS证书区域，单击修改配置。
在HTTPS设置界面，打开HTTPS安全加速开关，并配置证书相关参数。在弹窗中，开启HTTPS安全加速开关（开启后将产生 HTTPS 请求数计费）。
如果您已在[数字证书管理服务（原](https://yundunnext.console.aliyun.com/?p=cas#/certExtend/buy)[SSL）](https://yundunnext.console.aliyun.com/?p=cas#/certExtend/buy)中购买了证书，请选择云盾（SSL）证书中心，并在证书名称中选择已购买的证书。
说明
如果无法选择您购买的证书，请检查已购买证书绑定的域名和加速域名是否相同。
如果您使用的是第三方服务商签发的证书，请选择自定义上传（证书+私钥），您需要在设置证书名称后，上传证书（公钥）和私钥，该证书将在阿里云数字证书管理服务中保存，您可以在[我的证书](https://yundun.console.aliyun.com/?spm=5176.2020520110.all.12.16df56a1u1IhI6&p=cas#/cas/home)中查看。
自定义上传证书对证书（公钥）和私钥格式要求严格。如果您出现配置错误或看不懂配置示例，可以参考[上传自定义证书](configure-an-ssl-certificate.md)处理证书（公钥）和私钥，然后上传。
| 参数 | 说明 |
| --- | --- |
| 证书名称 | 为要上传的证书设置一个名称。 仅支持使用英文字母、英文句号、数字、下划线（ _ ）和短划线（ - ），且不能与已有证书名称重复。 |
| 证书（公钥） | 填写步骤一中证书文件内容的 PEM 编码。 |
| 私钥 | 填写步骤一中私钥内容的 PEM 编码。由于私钥信息敏感，上传后不支持在控制台查看或导出，需在本地妥善保管。 |
单击确定，完成配置。
## 验证HTTPS配置是否生效
浏览器验证：使用浏览器访问https://您的加速域名。如果地址栏出现安全锁标志，且点击后能看到正确的证书信息，则表示配置成功。
命令行验证：执行curl -I https://您的加速域名，如果能正常返回200，则表示HTTPS服务可用。
## HTTPS证书配置与回源端口的关系
CDN加速域名的HTTPS证书配置直接影响客户端可用的访问协议，进而影响回源协议和端口。
未配置HTTPS证书时，CDN仅支持HTTP协议访问，回源端口为80。
配置HTTPS证书并开启HTTPS安全加速后，CDN同时支持HTTP和HTTPS协议访问。
回源协议设置为跟随客户端模式时，CDN根据客户端访问协议自动选择回源端口：HTTP访问走80端口回源，HTTPS访问走443端口回源。
回源协议的详细配置方法，请参见[配置回源协议](configure-the-origin-protocol-policy.md)。
## 关闭HTTPS安全加速
如果您不再使用HTTPS安全加速功能，可随时在CDN控制台关闭HTTPS安全加速。关闭HTTPS安全加速实时生效，关闭后使用HTTPS方式无法访问资源，且不再保留证书或私钥信息。
再次开启HTTPS安全加速时，需要重新选择需要使用的证书。
## 上传自定义证书
如果您拥有的是第三方服务商签发或自签名的证书，需要先将证书和私钥处理成CDN支持的格式，然后上传。
证书（公钥）
CDN只支持上传PEM格式的证书。其他格式的证书需要参考[证书格式转换](certificate-formats.md)将其转换成PEM格式。针对不同证书颁发机构的证书，对证书内容的上传有不同的要求：
Root CA机构颁发的证书（一个证书文件）
使用文本编辑器即可打开PEM格式的证书文件，将以-----BEGIN CERTIFICATE-----开头和以-----END CERTIFICATE-----结尾的内容一并上传。
-----BEGIN CERTIFICATE----- [证书内容] -----END CERTIFICATE-----
中级机构颁发的证书（多个证书文件）
需将服务器证书、所有中间CA证书按顺序拼接成一个完整的证书链文件。文件内容应遵循以下格式：
-----BEGIN CERTIFICATE----- [服务器证书内容] -----END CERTIFICATE----- -----BEGIN CERTIFICATE----- [中间CA证书内容] -----END CERTIFICATE-----
私钥
私钥的扩展名一般为.key或.pem。使用文本编辑器即可打开私钥文件。不同内容的私钥上传要求区别如下：
RSA私钥直接上传
如果私钥内容以-----BEGIN RSA PRIVATE KEY-----开头，-----END RSA PRIVATE KEY-----结尾，则直接上传私钥内容。
-----BEGIN RSA PRIVATE KEY----- [私钥内容] -----END RSA PRIVATE KEY-----
其他格式私钥先转换格式再上传
如果您得到的是以-----BEGIN PRIVATE KEY-----开头，以-----END PRIVATE KEY-----结尾的私钥，您需要使用OpenSSL工具的转换命令先对私钥进行转换，然后将转换后的私钥内容按照直接上传的操作处理。其中old_server_key.pem为转换前的私钥，new_server_key.pem为转换后的私钥。
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
## 计费说明
启用HTTPS安全加速功能会产生额外费用。
计费项：静态HTTPS请求数。此费用独立于CDN流量费，按账户下所有加速域名产生的静态HTTPS请求总数计费。
付费模式：支持按量后付费和购买[静态](https://common-buy.aliyun.com/?spm=5176.7933777.J_3537169050.7.2429496eQ1aMgi&commodityCode=dcdnpaybag#/buy)[HTTPS](https://common-buy.aliyun.com/?spm=5176.7933777.J_3537169050.7.2429496eQ1aMgi&commodityCode=dcdnpaybag#/buy)[请求数资源包](https://common-buy.aliyun.com/?spm=5176.7933777.J_3537169050.7.2429496eQ1aMgi&commodityCode=dcdnpaybag#/buy)（预付费）两种模式。
成本提醒：
CDN下行流量包不可抵扣HTTPS请求产生的费用。
购买的静态HTTPS请求数资源包可被CDN和DCDN共享使用。
## 参考文档
| 文档 | 描述 |
| --- | --- |
| [配置协议重定向](configure-url-redirection.md) | 您可以通过配置强制跳转 HTTPS 功能，将客户端到 CDN 节点的请求强制重定向为更安全的 HTTPS 请求。 |
| [配置](configure-hsts.md) [HSTS](configure-hsts.md) | 开启 HSTS（HTTP Strict Transport Security）功能，您可以强制客户端（例如：浏览器）使用 HTTPS 与 CDN 节点创建连接，提高安全性。 |
| [配置](configure-ocsp-stapling.md) [OCSP Stapling](configure-ocsp-stapling.md) | CDN 节点预先缓存在线证书验证结果并下发给客户端，无需浏览器直接向 CA 站点查询证书状态，减少用户验证时间。 |
## 常见问题
[私钥文件如何去除密码保护？](faq-about-https.md)
[源站已经配置了](faq-about-https.md)[HTTPS，CDN](faq-about-https.md)[上还需要配置](faq-about-https.md)[HTTPS](faq-about-https.md)[吗？](faq-about-https.md)
[源站的](faq-about-https.md)[HTTPS](faq-about-https.md)[证书更新了，CDN](faq-about-https.md)[上需要同步更新吗？](faq-about-https.md)
[为什么大多数设备能够顺利访问通过](faq-about-https.md)[HTTPS](faq-about-https.md)[协议加速的域名，但是一些设备却无法访问？](faq-about-https.md)
Q：CDN域名更新或更换SSL证书后，HTTPS访问仍失败或显示旧证书，如何处理？
确保证书已正确部署：登录CDN控制台，在HTTPS配置中确认已选择新证书或上传了新证书内容。
检查域名匹配：确保证书绑定的域名与CDN加速域名完全一致（包括www前缀等）。
清除缓存：配置生效后（通常1~10分钟），需清除CDN节点缓存及本地浏览器缓存后再测试。可使用无痕浏览器窗口进行验证。
若源站证书更新，CDN侧不会自动同步，必须手动在CDN控制台更新证书。
Q：CDN配置HTTPS证书后，浏览器访问仍提示"不安全"或显示混合内容警告，如何排查？
检查网页源代码中是否引用了HTTP协议的资源（片、JS、CSS），需将其替换为HTTPS协议地址以解决混合内容问题。
清理本地浏览器缓存或使用无痕模式访问，排除缓存导致的旧证书显示。
确认客户端系统时间是否正确。系统时间不正确可能导致证书验证失败。
若使用iOS设备访问报错，可能是证书链不完整，建议使用在线工具（如[myssl.com](https://myssl.com/)）检测并补全中间证书后重新上传。
Q：为什么在CDN控制台选择"云盾（SSL）证书中心"证书时，找不到已购买的证书或提示域名不匹配？
检查证书绑定的域名是否与当前CDN加速域名完全一致。例如二级域名image.example.com不能直接使用主域名example.com的证书，需单独为该二级域名申请证书。
检查账号是否一致，确保证书和CDN域名在同一阿里云账号下。
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
## 相关API
| API | 描述 |
| --- | --- |
| [SetCdnDomainCSRCertificate](../developer-reference/api-cdn-2018-05-10-setcdndomaincsrcertificate.md) | 设置 CSR 文件。 |
| [DescribeDomainCertificateInfo](../developer-reference/api-cdn-2018-05-10-describedomaincertificateinfo.md) | 获取指定加速域名证书信息。 |
| [SetCdnDomainSSLCertificate](../developer-reference/api-cdn-2018-05-10-setcdndomainsslcertificate.md) | 设置某域名下证书功能是否启用及更新证书信息。 |
| [SetCdnDomainCSRCertificate](../developer-reference/api-cdn-2018-05-10-setcdndomaincsrcertificate.md) | 设置指定域名下的 HTTPS 证书。 |
| [DescribeCdnDomainByCertificate](../developer-reference/api-cdn-2018-05-10-describecdndomainbycertificate.md) | 根据证书信息获取加速域名。 |
| [DescribeCdnCertificateDetail](../developer-reference/api-cdn-2018-05-10-describecdncertificatedetail.md) | 查询 CDN 证书详细信息。 |
| [DescribeCdnCertificateList](../developer-reference/api-cdn-2018-05-10-describecdncertificatelist.md) | 获取证书列表信息。 |
| [DescribeCertificateInfoByID](../developer-reference/api-cdn-2018-05-10-describecertificateinfobyid.md) | 获取指定证书信息。 |
| [DescribeCdnHttpsDomainList](../developer-reference/api-cdn-2018-05-10-describecdnhttpsdomainlist.md) | 获取用户所有证书信息。 |
| [DescribeUserCertificateExpireCount](../developer-reference/api-cdn-2018-05-10-describeusercertificateexpirecount.md) | 获取用户证书过期的域名数。 |
| [SetCdnDomainSMCertificate](../developer-reference/api-cdn-2018-05-10-setcdndomainsmcertificate.md) | 设置国密证书。 |
| [DescribeCdnSMCertificateList](../developer-reference/api-cdn-2018-05-10-describecdnsmcertificatelist.md) | 查询国密证书列表。 |
| [DescribeCdnSMCertificateDetail](../developer-reference/api-cdn-2018-05-10-describecdnsmcertificatedetail.md) | 查询国密证书详情。 |
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
