# 通过配置CNAME域名实现网站加速-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/add-a-cname-record-for-a-domain-name

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

# 配置CNAME

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文档阐述了如何为已添加到阿里云CDN的加速域名配置CNAME记录。此项配置是激活CDN服务的最后一步，它将用户的访问请求指向CDN的边缘节点，从而实现全球内容分发与访问加速。

## 工作原理

[CNAME](products/cdn/documents/what-is-a-dns-cname-record.md)[记录](products/cdn/documents/what-is-a-dns-cname-record.md)，即Canonical Name Record，直译成中文就是"规范的名称记录"。其核心是利用DNS的别名机制。将一个域名映射到另一个域名。工作流程如下：

- 

用户访问www.example.com，用户的本地DNS解析器向公共DNS系统查询www.example.com的IP地址。

- 

云解析DNS查询www.example.com的DNS记录，发现其为CNAME记录，指向www.example.com.w.kunlunsl.com。

- 

云解析DNS继续查询www.example.com.w.kunlunsl.com的A记录（IP地址）。

- 

CDN的DNS调度系统接收到解析请求，根据用户的地理位置、网络状况和节点负载，动态地返回一个最优CDN边缘节点的IP地址。

- 

用户最终通过步骤4的IP地址与CDN边缘节点建立连接，并从节点获取缓存内容或由节点回源获取内容。

## 前提条件

- 

您已开通了CDN服务。如果未开通，请先[开通](products/cdn/documents/activate-alibaba-cloud-cdn.md)[CDN](products/cdn/documents/activate-alibaba-cloud-cdn.md)[服务](products/cdn/documents/activate-alibaba-cloud-cdn.md)。

- 

您已成功添加了加速域名。如果没有添加，请参见[添加加速域名](products/cdn/documents/add-a-domain-name.md)。

## 注意事项

- 

如果加速域名在配置CDN之前正在线上使用，为避免您的业务中断，您可以先通过[模拟访问测试](products/cdn/documents/test-whether-a-domain-name-is-accessible.md)来验证CNAME记录是否正常映射，验证通过后对原记录进行备份并在业务低峰期将原记录替换成CNAME记录。

- 

阿里云CDN、全站加速DCDN、直播以及点播产品的CNAME域名仅可以作为阿里云CDN的调度解析使用，对于恶意使用CNAME域名的行为，阿里云有权清退对应的域名和账号。

## 步骤一：获取加速域名的CNAME域名

前往阿里云CDN控制台的[域名管理列表](https://cdn.console.aliyun.com/domain/list)，复制加速域名对应的CNAME记录值。

说明

如果刚添加域名后CNAME地址为空，请等待1-5分钟后刷新页面。系统生成CNAME地址需要少量时间。

## 步骤二：配置CNAME域名解析

重要

对于同一个主机记录，CNAME记录与其他多种记录类型互斥。在添加CNAME记录前，必须删除该主机记录下任何已存在的A、AAAA、MX或TXT等记录，否则会导致CNAME记录添加失败或DNS解析失败。更多关于冲突和解决方法，请参见[解析记录冲突规则](https://help.aliyun.com/zh/dns/pubz-dns-record-conflict-rules)。

- 

使用加速域名所在的阿里云账号，登录[云解析](https://dnsnext.console.aliyun.com/authoritative/domains)[DNS](https://dnsnext.console.aliyun.com/authoritative/domains)[控制台](https://dnsnext.console.aliyun.com/authoritative/domains)。

- 

在公网权威解析页面，找到您的域名，在域名右侧单击解析设置。

- 

单击添加记录。可以参考以下场景进行配置：

场景一：子域名（推荐）

这是最常见的场景。例如，配置一个www.example.com加速域名，使用该加速域名可以访问被加速的源站资源。

| 配置项 | 填写内容 | 说明 |
| --- | --- | --- |
| 记录类型 | CNAME | 固定选择 CNAME 类型 |
| 主机记录 | www | 填写域名的前缀部分。 |
| TTL 时间 | 10 分钟（推荐） | 解析记录的缓存时间，可以按需调整。 |
| 记录值 | 粘贴步骤一中获取的 CNAME 地址 | 确保地址完整，无任何修改。 |


场景二：根域名（例如example.com）

重要

根域名配置CNAME记录可能对根域名下MX记录（邮件服务器地址）产生影响，导致收不到邮件。如果您的根域名承载了邮件、认证、安全策略等关键服务，建议您使用场景一的子域名作为加速域名。

| 配置项 | 填写内容 | 说明 |
| --- | --- | --- |
| 记录类型 | CNAME | 固定选择 CNAME 类型 |
| 主机记录 | @ | 当使用根域名为加速域名时，主机记录为 @ 。 |
| TTL 时间 | 10 分钟（推荐） | 解析记录的缓存时间，可以按需调整。 |
| 记录值 | 粘贴步骤一中获取的 CNAME 地址 | 确保地址完整，无任何修改。 |


场景三：泛域名（例如*.example.com）

泛域名解析可以将所有未被精确定义的次级域名指向CDN。例如，当加速域名配置为*.example.com，次级域名cdn.example.com、test.example.com等域名都将被加速，并且都可以访问被加速的源站资源。更多信息可以参考[泛域名加速](products/cdn/documents/does-alibaba-cloud-cdn-support-wildcard-domain-names.md)。

| 配置项 | 填写内容 | 说明 |
| --- | --- | --- |
| 记录类型 | CNAME | 固定选择 CNAME 类型 |
| 主机记录 | * | 当使用根域名为加速域名时，主机记录为 * 。 |
| TTL 时间 | 10 分钟（推荐） | 解析记录的缓存时间，可以按需调整。 |
| 记录值 | 粘贴步骤一中获取的 CNAME 地址 | 确保地址完整，无任何修改。 |


- 

单击确认，完成添加。

## 步骤三：验证CNAME配置是否生效

重要

由于阿里云CDN校验域名的DNS解析记录的服务器部署在中国内地。如果您对域名做了分区域DNS解析配置，例如仅对域名的中国内地以外区域（中国香港、中国澳门、中国台湾、其他国家和地区）配置了阿里云CDN的CNAME地址，校验服务器将无法解析到该CNAME地址，且在CDN控制台该域名的CNAME状态会显示为待配置，这种情况不影响CDN的加速服务。

- 

方法一：检查CDN控制台状态

- 

前往阿里云CDN控制台的[域名管理列表](https://cdn.console.aliyun.com/domain/list)。

- 

选择目标域名，将鼠标指向加速域名的CNAME状态处，状态为已配置时，则表示CNAME配置已生效。

说明

云解析DNS上新增CNAME记录实时生效，修改CNAME记录在10分钟后生效（具体生效时间长短取决于域名DNS解析配置的TTL时长，10分钟为TTL的默认时长），在此期间控制台中状态可能仍显示待配置，请忽略。

- 

方法二：通过nslookup命令验证

- 

打开cmd程序（Windows）、终端（macOS/Linux）。

- 

输入nslookup -type=CNAME加速域名，如果返回的解析结果和CDN控制台上该加速域名的CNAME值一致，则表示CDN加速已经生效。例如：

nslookup -type=CNAME www.example.com

## 常见问题

- 

[CNAME](https://help.aliyun.com/zh/dns/pubz-dns-record-conflict-rules)[记录冲突规则和解决方法](https://help.aliyun.com/zh/dns/pubz-dns-record-conflict-rules)

- 

[解决](products/cdn/documents/cname-record-does-not-take-effect.md)[CNAME](products/cdn/documents/cname-record-does-not-take-effect.md)[解析未生效](products/cdn/documents/cname-record-does-not-take-effect.md)

- 

[CDN](products/cdn/documents/use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)[加速](products/cdn/documents/use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)[OSS](products/cdn/documents/use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)[资源实践](products/cdn/documents/use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)

- 

[CDN](products/cdn/documents/support/too-many-redirects-occur-after-my-domain-name-is-accelerated-by-alibaba-cloud-cdn.md)[加速后提示重定向的次数过多解决方案](products/cdn/documents/support/too-many-redirects-occur-after-my-domain-name-is-accelerated-by-alibaba-cloud-cdn.md)

- 

[解决](products/cdn/documents/user-guide/configure-an-ssl-certificate.md)[CDN](products/cdn/documents/user-guide/configure-an-ssl-certificate.md)[加速后提示使用了不受支持协议的问题](products/cdn/documents/user-guide/configure-an-ssl-certificate.md)

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
