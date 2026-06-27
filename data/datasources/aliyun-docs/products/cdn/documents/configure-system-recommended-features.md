# 推荐配置（可选）-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/configure-system-recommended-features

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

# 推荐配置（可选）

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

成功添加加速域名后，建议您进行缓存过期时间、带宽封顶、页面优化等功能的配置，可有效提升CDN的缓存命中率、安全性和访问性能。

## 提高缓存命中率与访问速度

访问速度慢通常与缓存命中率低有强关联性，推荐您配置缓存过期时间、过滤参数功能提升缓存命中率。

- 

- 

| 场景 | 说明 | 配置 |
| --- | --- | --- |
| 缓存命中率低、访问速度慢 | 设置的缓存时间过短或未设置缓存规则，导致频繁回源站获取资源。合理配置缓存过期时间，可有效提升资源的缓存命中率，提升访问性能。 缓存时间设置建议如下： 不常更新的静态文件：例如图片、应用下载类型等，缓存时间建议设置 1 个月以上。 频繁更新的静态文件：例如 JS、CSS 等，根据实际业务情况设置。 | [配置缓存过期时间](products/cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md) |
| 默认客户端回源获取资源时需精确匹配 URL 中 ? 之后的参数。开启忽略参数功能后，客户端回源获取资源时会去除 URL 请求中 ? 之后的参数，有效提高文件缓存命中率，减少回源次数。 | [忽略参数](products/cdn/documents/user-guide/ignore-parameters.md) |  |


如果您想了解缓存命中率低的原因，请参见[CDN](products/cdn/documents/alibaba-cloud-content-delivery-network-cache-hit-rate-is-low.md)[缓存命中率低](products/cdn/documents/alibaba-cloud-content-delivery-network-cache-hit-rate-is-low.md)。

## 提高CDN的访问安全性

为防止域名因受到攻击等原因产生突发高带宽，您可以设置监控报警，实时监控带宽的变化情况，或者通过带宽封顶功能，设置带宽上限，防止产生过高的带宽。

| 场景 | 说明 | 配置 |
| --- | --- | --- |
| 限制带宽过高 | 通过带宽封顶功能，设置带宽上限，当检测到某个统计周期的带宽超出您设置的带宽上限时，CDN 将停止为该域名提供加速服务，且该域名会被解析到无效地址 offline.***.com ，无法被继续访问。 | [配置带宽封顶](products/cdn/documents/user-guide/configure-bandwidth-caps.md) |
| 通过在云监控产品中创建报警规则，实现对网络带宽的报警监控，帮助您及时了解带宽异常并快速进行处理。 | [设置报警](products/cdn/documents/user-guide/set-an-alert-rule.md) |  |


## 提高CDN的访问性能

结合您的实际业务需求，通过配置页面优化、Range回源、智能压缩功能，可缩小访问文件的体积，提升资源加速效率和页面可读性。

| 场景 | 说明 | 配置 |
| --- | --- | --- |
| 提高访问性能 | CDN 会自动删除页面的冗余内容，例如 HTML 页面、内嵌 JavaScript 和 CSS 中的注释以及重复的空白符，可有效去除页面的冗余信息，缩小文件体积，提高加速分发效率。 | [页面优化](products/cdn/documents/user-guide/enable-html-optimization.md) |
| 客户端通知源站服务器只返回指定范围的部分内容，适用于音视频等较大文件的内容分发加速，可减少回源流量消耗，并提升资源的响应时间。 | [配置](products/cdn/documents/user-guide/object-chunking.md) [Range](products/cdn/documents/user-guide/object-chunking.md) [回源](products/cdn/documents/user-guide/object-chunking.md) |  |
| CDN 节点向您返回请求的资源时，会对文本文件进行 Gzip 压缩，可有效缩小传输文件的大小，提升文件传输效率，减少带宽消耗。 | [Gzip](products/cdn/documents/user-guide/use-the-gzip-compression-feature.md) [压缩](products/cdn/documents/user-guide/use-the-gzip-compression-feature.md) |  |


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
