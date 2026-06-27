# 通过配置TLS版本和加密套件实现HTTPS安全加密-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-tls-version-control

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

# 配置TLS版本与加密套件

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当客户端对节点发起请求时，节点响应并启动TLS握手，使用设置的TLS版本以确保通信安全。若客户端不支持该版本，连接将无法建立。您可按需调整TLS版本可平衡老旧浏览器兼容性与安全性：较低TLS版本扩大支持范围，但安全强度减弱；较高TLS版本则增强安全，但可能限制旧版浏览器访问。

## 背景信息

TLS（Transport Layer Security）即安全传输层协议，在两个通信应用程序之间提供保密性和数据完整性，最典型的应用就是HTTPS。HTTPS即HTTP over TLS，就是更安全的HTTP，运行在HTTP层之下，TCP层之上，为HTTP层提供数据加解密服务。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 协议 | 说明 | 支持的主流浏览器 |
| --- | --- | --- |
| TLSv1.0 | RFC2246，1999 年发布，基于 SSLv3.0，该版本易受各种攻击（如 BEAST 和 POODLE），除此之外，支持较弱加密，对当今网络连接的安全已失去应有的保护效力。不符合 PCI DSS 合规判定标准。 | IE6+ Chrome 1+ Firefox 2+ |
| TLSv1.1 | RFC4346，2006 年发布，修复 TLSv1.0 若干漏洞。 | IE 11+ Chrome 22+ Firefox 24+ Safri 7+ |
| TLSv1.2 | RFC5246，2008 年发布，是目前广泛使用的版本。 | IE 11+ Chrome 30+ Firefox 27+ Safri 7+ |
| TLSv1.3 | RFC8446，2018 年发布，最新的 TLS 版本，支持 0-RTT 模式（更快），只支持完全前向安全性密钥交换算法（更安全）。 | Chrome 70+ Firefox 63+ |


## 操作步骤

执行操作前，请您确保已成功配置HTTPS证书，操作方法请参见[配置](products/cdn/documents/user-guide/configure-an-ssl-certificate.md)[HTTPS](products/cdn/documents/user-guide/configure-an-ssl-certificate.md)[证书](products/cdn/documents/user-guide/configure-an-ssl-certificate.md)。

说明

默认开启TLSv1.0、TLSv1.1、TLSv1.2和TLSv1.3版本。

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击域名管理。

- 

在域名管理页面，找到目标域名，单击操作列的管理。

- 

在指定域名的左侧导航栏，单击HTTPS配置。

- 

在TLS加密套件与协议版本配置区域，根据需要选择加密套件和开启对应的TLS版本。

可配置的TLS协议版本包括TLSv1.0、TLSv1.1、TLSv1.2和TLSv1.3，根据需要开启或关闭对应版本。

支持如下加密套件，请根据需求选择：

- 

全部加密算法套件 (默认)：安全性较低，兼容性较高，支持的加密算法请见[CDN](products/cdn/documents/user-guide/default-tls-encryption-algorithms.md)[默认支持的](products/cdn/documents/user-guide/default-tls-encryption-algorithms.md)[TLS](products/cdn/documents/user-guide/default-tls-encryption-algorithms.md)[加密算法](products/cdn/documents/user-guide/default-tls-encryption-algorithms.md)。

- 

强加密算法套件：安全性较高，兼容性较低，支持的加密算法：

- 

TLS_AES_256_GCM_SHA384

- 

TLS_AES_128_GCM_SHA256

- 

TLS_CHACHA20_POLY1305_SHA256

- 

ECDHE-ECDSA-CHACHA20-POLY1305

- 

ECDHE-RSA-CHACHA20-POLY1305

- 

ECDHE-ECDSA-AES128-GCM-SHA256

- 

ECDHE-RSA-AES128-GCM-SHA256

- 

ECDHE-ECDSA-AES128-CCM8

- 

ECDHE-ECDSA-AES128-CCM

- 

ECDHE-ECDSA-AES256-GCM-SHA384

- 

ECDHE-RSA-AES256-GCM-SHA384

- 

ECDHE-ECDSA-AES256-CCM8

- 

ECDHE-ECDSA-AES256-CCM

- 

ECDHE-ECDSA-ARIA256-GCM-SHA384

- 

ECDHE-ARIA256-GCM-SHA384

- 

ECDHE-ECDSA-ARIA128-GCM-SHA256

- 

ECDHE-ARIA128-GCM-SHA256

- 

自定义加密算法套件：请根据需要选择加密套件。

TLS协议版本说明请参见[背景信息](products/cdn/documents/user-guide/configure-tls-version-control.md)。

[上一篇：配置协议重定向](products/cdn/documents/user-guide/configure-url-redirection.md)[下一篇：配置HSTS](products/cdn/documents/user-guide/configure-hsts.md)

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
