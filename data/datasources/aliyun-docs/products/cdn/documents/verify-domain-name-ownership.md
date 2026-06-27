# 添加CDN域名时完成域名归属权验证-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/verify-domain-name-ownership

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

# 验证域名归属权

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您首次将一个域名添加到CDN系统中时，需要完成域名归属权验证。验证通过后您再次添加该域名或子域名时，无需再次验证。

## 方法一：DNS解析验证（推荐）

本文以加速域名image.example.com为例，为您介绍如何通过DNS解析验证来验证域名归属权。

- 

在验证页面，单击方法1：DNS解析验证，获取主机记录、记录值。

重要

在验证完成前请不要关闭验证页面。DNS解析验证偶尔会出现验证失败的情况，您还可以尝试使用方法二：文件验证。

- 

在您的域名解析服务商，添加TXT记录。

下文以阿里云的云解析为例介绍如何添加TXT记录，在其他域名解析服务商（例如：腾讯云、新网等）的配置方法类似。

- 

登录[云解析](https://dns.console.aliyun.com)[DNS](https://dns.console.aliyun.com)[控制台](https://dns.console.aliyun.com)。

- 

在公网权威解析页面，找到加速域名的根域名example.com，并单击右侧的解析设置。

- 

单击添加记录，记录类型选择为TXT，填写步骤1中阿里云CDN提供的主机记录、记录值，其余参数保持默认即可。

- 

单击确定，完成添加。

- 

等待TXT解析生效，返回CDN控制台，单击点击验证，完成验证。

如果系统提示“验证失败”，请检查TXT记录是否正确填写，并等待DNS记录生效后重新验证。

以加速域名image.example.com为例，检查TXT记录是否正确方法：

说明

- 

域名首次配置TXT解析记录后将会实时生效，修改TXT解析记录通常会在10分钟后生效（具体生效时间长短取决于域名DNS解析配置的TTL时长，默认为10分钟）。

- 

如果Linux系统没有安装nslookup命令程序，centos系：yum install bind-utilsUbuntu系：apt-get install dnsutils执行命令自动安装。

## Windows系统

在系统内打开cmd命令界面，输入nslookup -type=TXT verification.example.com，根据当前的TXT结果，可以查看解析记录是否生效或正确。

## Linux系统

在命令界面内，输入nslookup -type=TXT verification.example.com，根据当前的TXT结果，可以查看解析记录是否生效或正确。

## 方法二：文件验证

- 

在验证页面，单击方法2: 文件验证。

重要

在验证完成前请不要关闭验证页面。

- 

单击verification.html，下载验证文件。

- 

手动将验证文件上传到您主域名服务器（例如您的ECS、OSS、CVM、COS、EC2等）的根目录。例如：当前加速域名为image.example.com，您需要将该文件上传至example.com的根目录下。

- 

确保可通过http://example.com/verification.html访问到该文件后，即可点击验证进行验证。

阿里云CDN后台将访问您服务器中http://example.com/verification.html文件链接进行验证。

- 

如果文件内的记录值与验证文件记录值一致，则通过验证。

- 

如果验证失败，请确保上述文件链接可访问，并且您上传的文件正确。

## 常见问题

在添加新的加速域名时，您可能会遇到如下问题：

- 

Q：为什么要做域名归属权验证？

A：为了确保域名只被真正的拥有者添加，避免出现用户A的域名被用户B添加导致域名冲突及安全隐患问题。

- 

Q：我有多个阿里云账号，每个账号首次添加新域名时都要做归属权验证吗？

A：是的。多个账号视为多个不同的独立用户，每个账号都需要对新域名进行一次归属权验证。

- 

Q：我已完成DNS验证或文件验证，是否可以删除用作验证的DNS记录或文件？

A：可以。要求您添加的DNS解析或文件，只用作添加域名时的归属权验证，验证通过后您可以删除记录或文件。

- 

Q：已经添加到阿里云CDN控制台的存量域名，需要做域名归属权验证吗？

A：不需要。例如您已经添加了example.aliyundoc.com，且配置了CDN分配的CNAME在正常使用中，则视为您拥有aliyundoc.com的解析权。您后续再添加**.aliyundoc.com、***.aliyundoc.com等任意aliyundoc.com的子域名，都无需再验证。

- 

Q：通过API接口AddCdnDomain添加域名是否需要域名归属权验证？

A：需要。和控制台添加一样，您可以选择DNS解析验证或文件验证，先配置好DNS或在源站根目录放置好验证文件，然后调用AddCdnDomain接口添加加速域名。

- 

Q：我无法完成DNS验证或文件验证，怎么办？

A：您可以[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)说明无法完成域名归属权验证的原因，并提交可以证明您持有该域名的资料，我们将进行人工审核。

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
