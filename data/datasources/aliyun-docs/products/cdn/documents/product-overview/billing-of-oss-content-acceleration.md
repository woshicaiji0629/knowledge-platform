# 计费项构成与优惠资源包-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/product-overview/billing-of-oss-content-acceleration

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

# CDN加速OSS计费说明

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

阿里云OSS可提供低成本的存储，CDN可以实现静态资源加速分发。您可将静态资源（包括静态脚本、音视频、图片、附件等文件）托管在阿里云OSS中，并使用CDN加速，降低存储成本的同时，加速资源分发并减轻源站压力。

## 计费说明

当OSS作为CDN源站时，可能会产生以下费用：CDN服务费+OSS服务费。

重要

CDN服务费与OSS服务费各自独立计费（例如流量费），价格存在差异，具体价格请查看对应产品的计费规则。

计费项和流量费说明如下：

- 

可能产生的计费项

| 计费项 | 说明 |
| --- | --- |
| CDN 服务费 | 主要为“CDN 下行流量费”。 根据实际业务情况，可能还会存在“静态 HTTPS 请求费”等其他费用。详细计费项，请参见 [CDN](products/cdn/documents/product-overview/billing-overview.md) [计费概述](products/cdn/documents/product-overview/billing-overview.md) 。 |
| OSS 服务费 | 主要为“ OSS 流出到 CDN 流量费+ 数据存储费”。 根据实际业务情况，可能还会存在“OSS 请求费用”等其他费用。详细计费项，请参见 [OSS](products/oss/documents/billing-overview.md) [计量计费概述](products/oss/documents/billing-overview.md) 。 |


- 

流量费说明

当OSS作为CDN源站时，可能会产生CDN下行流量费（由CDN计费）和OSS流出到CDN流量费（由OSS计费）。

- 

CDN下行流量费：用户从CDN节点请求资源，节点将资源下发给客户端时产生的流量费用；流量从CDN流向客户端，消耗的流量由CDN计费。价格详见[CDN](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.5be031c9TyAAu1#/cdn/detail/cdn)[定价-按流量计费](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.5be031c9TyAAu1#/cdn/detail/cdn)。

- 

CDN节点回源到OSS产生的流量，不计费。

- 

OSS流出到CDN节点产生的流量费：流量从OSS流向CDN，由OSS计费。价格详见[OSS](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.26443048xzpfk5#/oss/detail/ossbag)[定价-流量费用-OSS](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.26443048xzpfk5#/oss/detail/ossbag)[流出到](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.26443048xzpfk5#/oss/detail/ossbag)[CDN](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.26443048xzpfk5#/oss/detail/ossbag)[流量](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.26443048xzpfk5#/oss/detail/ossbag)。

说明

阿里云CDN回源阿里云OSS的流量优惠说明：

- 

用户需要在控制台上把源站类型设置为“OSS域名”，这样阿里云OSS产品会将来自阿里云CDN产品的回源流量识别为“CDN回源流出流量”，从而享受到更优惠的价格。

- 

如果用户在控制台上把源站类型误设为“源站域名”，阿里云OSS产品会将来自阿里云CDN产品的回源流量识别为“外网流出流量”，这种情况下就享受不到优惠价格。

- 

当CDN回源节点和回源的OSS的存储空间均在非中国内地区域时，OSS流出到CDN的流量免费。

## 优惠资源包说明

如果您使用CDN加速OSS中的资源，OSS和CDN均提供了资源包，可有效降低您的回源成本。

| 资源包 | 使用说明 |
| --- | --- |
| [CDN](https://common-buy.aliyun.com/?spm=5176.197032.J_5834642020.4.141442c417YQT6&commodityCode=dcdnpaybag#/buy) [下行流量包](https://common-buy.aliyun.com/?spm=5176.197032.J_5834642020.4.141442c417YQT6&commodityCode=dcdnpaybag#/buy) | 用于抵扣 CDN 节点将资源下发给客户端时产生的流量费用，超出部分自动按量计费。 |
| [CDN](https://common-buy.aliyun.com/?spm=5176.197032.J_5834642020.4.141442c417YQT6&commodityCode=dcdnpaybag#/buy) [静态](https://common-buy.aliyun.com/?spm=5176.197032.J_5834642020.4.141442c417YQT6&commodityCode=dcdnpaybag#/buy) [HTTPS](https://common-buy.aliyun.com/?spm=5176.197032.J_5834642020.4.141442c417YQT6&commodityCode=dcdnpaybag#/buy) [请求数资源包](https://common-buy.aliyun.com/?spm=5176.197032.J_5834642020.4.141442c417YQT6&commodityCode=dcdnpaybag#/buy) | 用于抵扣 CDN 加速服务中产生的静态 HTTPS 请求费用，超出部分自动按量计费。 |
| [OSS](https://common-buy.aliyun.com/?spm=5176.8064714.J_323065.pricedetail1111.59762bc6BGAZfq&commodityCode=ossbag&request=%7B%22region%22%3A%22china-common%22%7D#/buy) [回源流量包](https://common-buy.aliyun.com/?spm=5176.8064714.J_323065.pricedetail1111.59762bc6BGAZfq&commodityCode=ossbag&request=%7B%22region%22%3A%22china-common%22%7D#/buy) | 用于抵扣 CDN 回源时产生的流量费用，超出部分自动按量计费。 |
| [OSS](https://common-buy.aliyun.com/?spm=5176.8064714.J_323065.pricedetail1111.59762bc6BGAZfq&commodityCode=ossbag&request=%7B%22region%22%3A%22china-common%22%7D#/buy) [标准存储包](https://common-buy.aliyun.com/?spm=5176.8064714.J_323065.pricedetail1111.59762bc6BGAZfq&commodityCode=ossbag&request=%7B%22region%22%3A%22china-common%22%7D#/buy) | 用于抵扣“标准存储-本地冗余” 和“ECS 快照” 的存储容量，超出部分自动按量计费。 |


## 相关文档

- 

[CDN](products/cdn/documents/use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)[加速](products/cdn/documents/use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)[OSS](products/cdn/documents/use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)[资源](products/cdn/documents/use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)

[上一篇：设置资源包预警](products/cdn/documents/product-overview/configure-low-capacity-alerts.md)[下一篇：变更计费方式](products/cdn/documents/product-overview/change-the-metering-method.md)

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
