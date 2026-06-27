# 资源包抵扣时间、抵扣顺序和其他抵扣规则-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/product-overview/rules-for-applying-resource-plans

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

# 资源包抵扣规则

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

通过本文，您可以了解资源包抵扣时间、抵扣顺序和其他抵扣规则。

## 抵扣时间

- 

资源包购买后立即生效。

- 

资源包生效以后的实际抵扣时间会有3~4小时的延迟。

假如您在2021年08月12日10:30:30购买了有效期为1个月的1 TB中国内地下行流量资源包，则实际抵扣时间需要等到14:00:00左右，系统生成10:00:00~11:00:00这个时间段的流量计费账单时，才开始抵扣10:00:00~11:00:00的流量消耗。

## 抵扣顺序

资源包支持叠加购买，若您有多个相同类型的资源包，则抵扣顺序为：

- 

按照资源包到期时间，优先抵扣先到期的资源包。

- 

若多个资源包到期时间相同，则按购买顺序（先购买的优先）抵扣。

- 

同种类型的资源包的额度全部抵扣完后，若仍有超出部分则自动转为后付费方式，按量扣费。

如果您购买了2个中国内地区域的下行流量资源包，到期时间分别为2021年7月1日，和2021年8月1日，则优先抵扣到期时间为2021年7月1日的资源包。

## 抵扣范围与生效对象

资源包按账号生效，而非按域名生效。只要您的阿里云账号下有任意域名接入了 CDN 服务并产生了符合类型的用量，系统会自动从该账号内对应的有效资源包中抵扣，无需手动绑定或指定分配给特定域名。

- 

同一账号下的多个加速域名共用同一个资源包，系统根据各域名的实际用量自动抵扣。

- 

购买资源包后无需修改任何域名配置、无需手动部署或重新绑定 SSL 证书。只要域名已完成 CNAME 解析并正式接入 CDN，产生的流量即自动抵扣。

- 

无论是首次购买还是到期后重新购买新的资源包，均无需额外配置或修改域名设置。系统会自动优先抵扣符合条件（有效期内、匹配地域和类型）的资源包。旧资源包失效后，新资源包自动接续抵扣。

## 其他抵扣规则

- 

一种类型的资源包只能抵扣使用CDN过程中产生的对应费用，不能抵扣所有费用。

如果您购买了下行流量资源包，只能抵扣下行流量，不能用来抵扣HTTPS请求数等其他计费项。

- 

针对下行流量资源包，需要同时满足以下条件才能使用资源包抵扣：

- 

计费方式要求：CDN 服务的计费方式必须为按流量计费。如果您选择的是按峰值带宽计费，则无法使用流量资源包抵扣，相关费用按带宽计费规则结算。

- 

地域匹配要求：资源包有地域限制，不同加速区域的资源包不能相互抵扣。如果您购买了中国内地区域下行流量资源包，只能抵扣中国内地产生的下行流量，不能抵扣中国香港、中国澳门、中国台湾和其他国家和地区产生的下行流量费用。

- 

CDN 一口价资源包仅抵扣中国香港、中国澳门、中国台湾及海外地区的流量，不包含中国内地地区流量。若需抵扣中国内地下行流量，必须单独购买下行流量（中国内地）资源包。

如果您的业务覆盖全球，需同时购买中国内地下行流量资源包和海外/全球流量包，才能覆盖所有区域的费用。未购买对应区域资源包的流量将按后付费方式计费。

- 

如果资源包到期或耗尽，则会自动转为后付费方式，按量付费。请您及时查看资源包用量，根据实际情况选择是否叠加购买，否则可能会产生按量计费账单。

- 

如果您需要续购资源包，建议在旧资源包到期前一天购买新的同类型资源包。购买后新资源包立即生效，系统会按照到期时间优先抵扣旧资源包的剩余额度，旧资源包到期后自动切换至新资源包继续抵扣，实现无缝衔接，避免因资源包到期未续购而产生按量计费。

## 常见问题

CDN 资源包是否支持按月刷新或延期？

CDN 下行流量资源包的有效期通常为 1 年（具体以购买页为准），总容量固定（如 500 GB），并非每月刷新。资源包不支持延期，未用完的容量在到期后自动清零。按量抵扣的资源包无法直接续费，建议在到期之前一天重新购买新的资源包。如果您重新购买了同类型且在有效期内的资源包，剩余容量会自动叠加，系统优先抵扣先到期的资源包。

新购资源包能否抵扣历史账单或购买前的流量？

不能。新购买的资源包仅对购买后产生的新流量生效，无法回溯抵扣已出账的后付费账单或购买时间点之前产生的计费。虽然资源包购买后立即生效，但实际抵扣可能有 3~4 小时延迟（系统需等待对应时段的账单生成后再抵扣），这不影响资源包不追溯购买前用量的原则。

为什么购买了资源包仍收到到期提醒或产生小额扣费？

资源包通常仅抵扣下行流量费用。如果您的 CDN 服务产生了 HTTPS 请求数、HTTP 请求数等其他计费项费用，且这些费用未包含在资源包内，则会触发后付费账单。即使流量包未用完，因请求数等非流量费用产生的欠费或账单，系统仍可能发送到期或欠费提醒。建议登录阿里云控制台，在费用中心查看账单明细，确认扣费项目是否为请求数等非流量计费项。如需了解请求数的计费和抵扣规则，请参见相关计费文档。

资源包是否具备加速功能？

流量资源包仅用于抵扣流量产生的计费费用，不具备 CDN 回源加速或提升传输速度的功能。要实现加速效果，需要先在 CDN 控制台完成域名的接入配置（添加加速域名、配置 CNAME 解析等）。资源包仅在加速服务产生流量时抵扣费用。

资源包过期后能否开启自动续费？

资源包状态变为已过期后，自动续费功能不可用（开关显示为灰色），不支持对已过期的资源包开启自动续费。如果您希望继续使用资源包抵扣流量费用，需要重新购买一个新的资源包。

## 相关文档

[购买了资源包为什么仍会扣费或欠费？](products/cdn/documents/product-overview/why-am-i-still-charged-for-resources-after-i-purchase-resource-plans-of-alibaba-cloud-cdn.md)

[上一篇：资源包选购](products/cdn/documents/product-overview/guidelines-for-choosing-resource-plans.md)[下一篇：查询资源包明细](products/cdn/documents/product-overview/query-the-details-of-resource-plans-1.md)

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
