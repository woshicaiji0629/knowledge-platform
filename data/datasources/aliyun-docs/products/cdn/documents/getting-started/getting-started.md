# 新手指引-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/getting-started/getting-started

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

# 新手指引

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍从开通CDN服务到使用CDN实现加速的全流程，便于您快速上手CDN实现资源加速。

## 核心概念

以下是CDN中涉及的基本概念，便于您更准确地理解和使用CDN。更多涉及CDN的概念，请参考[CDN](products/cdn/documents/product-overview/terms.md)[基本概念](products/cdn/documents/product-overview/terms.md)。

| 概念 | 解释 |
| --- | --- |
| 源站 | 网站的服务器，存放着网站的原始文件（如图片、CSS、JS 文件等）。CDN 从此获取内容并分发给用户。 |
| 加速域名 | 希望通过 CDN 加速的域名，即用户在浏览器中访问的域名，例如 www.example.com 。 |
| CNAME 记录 | 一种 DNS 解析记录。需将加速域名的解析记录类型从 A 记录或 AAAA 记录更改为 CNAME，并指向 CDN 服务提供的一个专属域名地址，访问请求才会被引导至 CDN 网络。 |
| 边缘节点 | CDN 部署在全球各地、靠近用户的服务器。用户的访问请求会被智能调度到最近的边缘节点，由该节点直接响应，实现加速。 |
| 回源 | 当边缘节点没有缓存用户请求的文件或缓存已过期时，边缘节点向 源站 请求获取最新文件的过程。 |
| 缓存命中率 | 成功由 CDN 边缘节点缓存直接响应的请求次数占总请求次数的比例。缓存命中率越高，加速效果越好，回源请求越少，源站压力也越小。 |


## 计费指南

- 

阿里云CDN的计费分为基础服务计费（CDN加速产生的费用）+增值服务计费（HTTPS请求次数计费、实时日志投递条数计费等）。更多计费信息请参见[阿里云](products/cdn/documents/product-overview/billing-overview.md)[CDN](products/cdn/documents/product-overview/billing-overview.md)[计费概述](products/cdn/documents/product-overview/billing-overview.md)。

- 

基础服务计费只要您使用阿里云 CDN 就会自动收费；增值服务计费的各个计费项默认关闭，需要您手动开通才会计费。

- 

基础服务计费和增值服务计费默认都采用按量付费，用多少，付多少。

- 

对于基础服务计费和增值服务计费，阿里云CDN也提供了优惠的资源包，帮助您降低成本，详情可参见[资源包选购](products/cdn/documents/product-overview/guidelines-for-choosing-resource-plans.md)。

## 使用流程

### 阶段一：准备工作

开始配置前，请确保已准备好以下资源：

- 

一个域名：拥有该域名的管理权限，可以修改其DNS解析记录。

- 

一个公网可访问的源站：可以是一个IP地址、另一个域名或阿里云OSS存储空间（Bucket）的访问地址。

说明

根据中国法律规定和工信部要求，对于解析至中国内地服务器的网站、App等服务，必须完成[域名备案](https://help.aliyun.com/zh/icp-filing/the-icp-registration-process/)以确认其合法性后方可对外提供服务。

### 阶段二：开通并配置CDN

- 

[开通](products/cdn/documents/activate-alibaba-cloud-cdn.md)[CDN](products/cdn/documents/activate-alibaba-cloud-cdn.md)[服务](products/cdn/documents/activate-alibaba-cloud-cdn.md)。

- 

[配置加速域名和源站](products/cdn/documents/getting-started/quick-access-to-alibaba-cloud-cdn.md)：

- 

根据网站用户来选择合适的域名加速区域。

| 用户所在位置 | 加速效果 | 加速区域选择 |
| --- | --- | --- |
| 中国内地 | 全球用户访问均会调度至中国内地加速节点进行服务（海外地区和中国香港、中国澳门、中国台湾地区的访问流量将会被调度至华东电信的 CDN 节点）。 | 仅中国内地 |
| 海外地区+中国香港、中国澳门、中国台湾地区 | 全球用户访问会调度至中国内地以外的地区的 CDN 加速节点进行服务（中国内地用户将会被调度至日本、新加坡和中国香港的 CDN 节点）。 | 全球（不包含中国内地） |
| 全球 | 全球用户访问将会择优调度至最近的加速节点进行服务。 | 全球 |


- 

若您的域名是首次添加到CDN控制台，则需要通过域名DNS解析来[验证域名归属权](products/cdn/documents/getting-started/quick-access-to-alibaba-cloud-cdn.md)，验证通过后您再次添加该域名或子域名时，无需再次验证。

- 

配置源站信息，以便在阿里云CDN未缓存数据时，能够访问您的服务器以获取资源。

- 

[配置](products/cdn/documents/getting-started/quick-access-to-alibaba-cloud-cdn.md)[HTTPS](products/cdn/documents/getting-started/quick-access-to-alibaba-cloud-cdn.md)[证书](products/cdn/documents/getting-started/quick-access-to-alibaba-cloud-cdn.md)：如果您的应用在配置阿里云CDN之前已经支持HTTPS访问或者您希望新域名可以支持HTTPS访问，请务必进行HTTPS证书的配置，否则您的域名将不会支持HTTPS访问。

如果您的域名之前就不支持HTTPS访问，并且暂时也不打算支持HTTPS访问，那么您可以直接跳过该配置。

- 

[CDN](products/cdn/documents/getting-started/quick-access-to-alibaba-cloud-cdn.md)[安全防护和性能优化配置](products/cdn/documents/getting-started/quick-access-to-alibaba-cloud-cdn.md)：

- 

恶意攻击或流量盗刷，都会导致突发的高带宽使用或大量数据传输，进而产生高额费用，因此，强烈建议您配置适当的安全防护措施以提前避免此类风险。

- 

进行缓存过期时间、页面优化等功能的配置，可有效提升CDN的缓存命中率和访问性能，降低回源流量。

### 阶段三：配置CNAME并切换流量

- 

[验证加速域名是否可用](products/cdn/documents/getting-started/quick-access-to-alibaba-cloud-cdn.md)：成功添加加速域名后，为保证DNS解析可以顺利切换而不影响现有业务，建议您先在本地测试加速域名，验证加速域名访问正常后，再将加速域名的DNS解析记录指向CNAME域名。

- 

[配置](products/cdn/documents/getting-started/quick-access-to-alibaba-cloud-cdn.md)[CNAME](products/cdn/documents/getting-started/quick-access-to-alibaba-cloud-cdn.md)：添加域名后，阿里云CDN会为您分配对应的CNAME域名，您需要在DNS服务商处将加速域名的DNS解析记录指向分配的CNAME域名，CDN服务才能生效。

## 常用功能

- 

[回源配置](products/cdn/documents/user-guide/back-to-origin-settings.md)：CDN提供了指定回源协议、指定回源地址、修改回源请求等丰富的配置，您可以根据自身业务完成定制化配置。

- 

[资源监控](products/cdn/documents/user-guide/resource-monitoring.md)：在CDN控制台的监控查询页面，可查看加速域名的访问流量/带宽、访问请求数、回源流量/带宽以及命中率等核心指标，全面了解加速效果。

- 

日志与报表：CDN提供了[离线日志](products/cdn/documents/user-guide/overview.md)、[实时日志](products/cdn/documents/user-guide/overview-1.md)和[运营报表](products/cdn/documents/user-guide/customize-an-operations-report-template-and-create-a-tracking-task.md)，可以帮助您及时发现问题，提升CDN服务质量。

- 

[刷新和预热资源](products/cdn/documents/user-guide/refresh-and-prefetch-resources.md)：适用于源站资源更新和发布、违规资源清理、域名配置变更，降低源站压力。

## 常见问题

是否可以直接使用根域名（如example.com）进行加速？

不建议。DNS规范要求根域名（@记录）的CNAME记录不能与其他记录（如MX邮件记录）共存。若根域名需要收发邮件，配置CNAME后将导致邮件服务中断。使用独立的二级域名（如www.example.com或static.example.com）是更安全、灵活的做法。

如何降低CDN使用成本？

- 

购买资源包：对于用量稳定的业务，购买流量或HTTPS请求数资源包通常比按量付费更划算。

- 

优化缓存规则：提高缓存命中率是降低成本最有效的方法。尽可能延长静态资源的缓存时间。

- 

开启带宽封顶：作为最后的成本保护措施，防止意外流量超出预算。

刷新和预热资源有什么区别？

- 

刷新：刷新操作的本质是向CDN边缘节点下发缓存失效指令，而非直接删除文件。边缘节点收到指令后，会将匹配的缓存资源标记为“失效”或“过期”。当用户再次请求该资源时，边缘节点发现缓存已失效，便会回源获取最新资源，并在返回给用户的同时重新缓存。

- 

预热：预热操作是由CDN边缘节点根据您提交的URL列表，主动向源站发起请求，将资源缓存到CDN边缘节点上，而非由源站主动推送。预热可提升新资源或活动页面的首次访问速度，同时减少活动上线时的回源压力，保护源站。

## 进阶与实践

更多功能和实践请参见[控制台操作指南](https://help.aliyun.com/zh/document_detail/436059.html)和[最佳实践](products/cdn/documents/use-cases/best-practices.md)。

## 启动CDN加速服务视频讲解

[上一篇：快速入门](products/cdn/documents/getting-started.md)[下一篇：快速接入阿里云CDN](products/cdn/documents/getting-started/quick-access-to-alibaba-cloud-cdn.md)

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
