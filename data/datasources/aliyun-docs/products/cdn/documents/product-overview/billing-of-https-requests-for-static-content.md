# 静态HTTPS请求数的计费标准及示例-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/product-overview/billing-of-https-requests-for-static-content

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

# 静态HTTPS请求数

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在CDN中开启HTTPS功能后，将根据产生的静态HTTPS请求数单独计费，支持按量后付费和[资源包预付费](https://common-buy.aliyun.com/?spm=5176.7933777.J_3537169050.7.2429496eQ1aMgi&commodityCode=dcdnpaybag#/buy)模式。

说明

- 

CDN下行流量包不可抵扣HTTPS请求费用。

- 

CDN仅支持静态加速，只产生静态请求相关的计费数据；全站加速同时支持静态加速和动态加速，当域名使用全站加速提供加速服务，且存在动态请求时，才会产生动态请求相关的计费数据（即动态HTTPS请求数和动态HTTP请求数）。

- 

CDN与全站加速可以共享购买的静态HTTPS请求数资源包。

## 计费详情

按量后付费方式：

| 计费项 | 计费周期 | 价格（ 元/万次 ） |
| --- | --- | --- |
| 静态 HTTPS 请求数 | 按小时计费，实时扣费。 | 2024 年 2 月 1 日起，静态 HTTPS 请求数每月前 500 万次免费，超过 500 万次后，按每万次 0.05 元计费。 说明 实际价格以 [静态](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.10.1b444ee22Dxy8y#/cdn/detail) [HTTPS](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.10.1b444ee22Dxy8y#/cdn/detail) [请求价格](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.10.1b444ee22Dxy8y#/cdn/detail) 为准。 |


资源包预付费方式：请参见[资源包计费](https://common-buy.aliyun.com/?spm=5176.8064714.J_884289.1.720c2d40U29Yvz&commodityCode=dcdnpaybag&request=%7B%22dcdntype%22:%22dcdnhttps%22,%22cdn_https%22:%2210000000%22,%22pack%22:%22FPT_dcdnpaybag_deadlineAcc_1541151058%22,%22ord_time%22:%221:Year%22%7D)。

说明

- 

购买了请求数资源包的情况下，超过500万次的免费额度后，超额的请求数优先使用资源包抵扣。

- 

资源包的额度全部消耗后，若仍有超出部分则自动转为后付费方式，按量扣费。

## 计费示例

说明

示例仅供参考，请以实际价格为准。

用户A、用户B、用户C开通了HTTPS功能并产生静态HTTPS请求后，产生的费用如下表所示：

| 用户 | 产生的 HTTPS 静态请求数 | 购买预付费资源包费用（元） | 按量后付费费用（元） | 总费用（元） |
| --- | --- | --- | --- | --- |
| 用户 A | 1400 万次 | 0（未购买） | [(14000000-5000000)/10000]x0.05=45 | 45 |
| 用户 B | 1400 万次 | 40（预付费资源包-1000 万次） | 0（未产生按量后付费费用） | 40 |
| 用户 C | 2300 万次 | 40（预付费资源包-1000 万次） | [(23000000-5000000-10000000)/10000]x0.05=40 | 80 |


## 用量查询

### 按量后付费

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，选择用量查询。

- 

在用量查询页面，选择HTTPS请求数，单击查询查看。

### 预付费资源包

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，选择资源包管理。

- 

在资源包管理查看已购资源包使用情况。

[上一篇：增值服务计费](products/cdn/documents/product-overview/billing-of-value-added-services.md)[下一篇：静态QUIC请求数](products/cdn/documents/product-overview/billing-of-quic-requests-for-static-content.md)

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
