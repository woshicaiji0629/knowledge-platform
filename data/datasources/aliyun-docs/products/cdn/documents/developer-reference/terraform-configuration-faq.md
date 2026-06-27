# 使用Terraform配置CDN证书的常见问题-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/developer-reference/terraform-configuration-faq

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/cdn/documents/product-overview.md)

- [快速入门](products/cdn/documents/getting-started.md)

- [操作指南](products/cdn/documents/user-guide.md)

- [实践教程](products/cdn/documents/use-cases.md)

- [安全合规](products/cdn/documents/security-and-compliance.md)

- [开发参考](products/cdn/documents/developer-reference.md)

- [服务支持](products/cdn/documents/support.md)

- [视频专区](products/cdn/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# Terraform配置常见问题

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

使用Terraform配置CDN时，如果遇到疑问请参考以下常见问题及处理建议。

## 如何在创建CDN加速域名时配置证书？

在使用[alicloud_cdn_domain_new](https://help.aliyun.com/zh/terraform/alicloud-cdn-domain-new)资源创建CDN加速域名时，可以通过设置certificate_config参数来配置证书。示例如下：

使用数字证书管理服务的证书resource "alicloud_cdn_domain_new" "domain" { scope = "overseas" domain_name = "mycdndomain-${random_integer.default.result}.alicloud-provider.cn" cdn_type = "download" sources { type = "ipaddr" content = "1.1.x.x" priority = 20 port = 80 weight = 15 } certificate_config { server_certificate_status = "on" cert_type = "cas" cert_id = "1111111" cert_region = "cn-hangzhou" } }

手动上传证书resource "alicloud_cdn_domain_new" "domain" { scope = "overseas" domain_name = "mycdndomain-${random_integer.default.result}.alicloud-provider.cn" cdn_type = "download" sources { type = "ipaddr" content = "1.1.x.x" priority = 20 port = 80 weight = 15 } certificate_config { server_certificate_status = "on" cert_type = "upload" cert_name = "cert-xxxxxxxxx" server_certificate = "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----" private_key = "-----BEGIN RSA PRIVATE KEY-----\n...\n-----END RSA PRIVATE KEY-----" } }

## 配置证书后，证书状态是否需要手动开启？

不需要。只要填写了certificate_config参数块，默认会自动开启证书状态（server_certificate_status = "on"）。无需额外配置。

## cert_type支持的证书类型有哪些？分别代表什么？

证书类型通过cert_type参数指定，支持两种类型：

- 

upload：手动上传证书（需提供公钥和私钥，分别填写server_certificate和private_key）。

- 

cas：使用阿里云数字证书管理服务的SSL证书（需填写cert_id证书ID和cert_region证书地域）。

说明

free类型的免费证书已不再支持。

## 选择upload类型时需要哪些必填参数？

当cert_type = "upload"时，必须提供以下参数：

- 

server_certificate：证书公钥（PEM格式）。

- 

private_key：证书私钥（PEM格式）。

certificate_config { cert_type = "upload" cert_name = "cert-xxxxxxxxx" server_certificate = "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----" private_key = "-----BEGIN RSA PRIVATE KEY-----\n...\n-----END RSA PRIVATE KEY-----" }

## 选择cas类型时需要哪些必填参数？

当cert_type = "cas"时，必须提供以下参数：

- 

cert_id：阿里云证书中心的证书ID（可在证书详情页获取）。

- 

cert_region：阿里云数字证书管理服务所在地域，根据账号类型选择（默认为cn-hangzhou）：

- 

中国站账号：cn-hangzhou

- 

国际站账号：ap-southeast-1

certificate_config { server_certificate_status = "on" cert_type = "cas" cert_id = "1111111" cert_region = "cn-hangzhou" }

## cert_region参数有什么用？如何设置cert_region参数？

cert_region参数用于设置阿里云数字证书管理服务所在地域，在cert_type = "cas"（使用阿里云云盾证书）时，该参数为必填。填写规则如下：

- 

云盾证书所在的阿里云账号为中国站账号时，配置为cn-hangzhou。

- 

云盾证书所在的阿里云账号为国际站账号时，配置为ap-southeast-1。

[上一篇：使用Terraform添加CDN域名出现HTTPS配置报错](products/cdn/documents/developer-reference/using-terraform-to-add-cdn-domain-name-results-in-https-configuration-error.md)[下一篇：CLI集成示例](products/cdn/documents/developer-reference/cli-integration-example.md)

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
