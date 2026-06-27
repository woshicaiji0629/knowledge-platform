# 分析CDN拨测数据了解加速效果与命中率的关系-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/product-overview/alibaba-cloud-cdn-synthetic-monitoring-data

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

# CDN性能拨测数据参考

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

阿里云CDN不定期更新拨测数据，拨测的数据是针对同一个访问资源，通过CDN和直接访问源站的数据差别，您可以通过数据了解到，CDN加速的数据效果。

## 拨测数据

拨测说明：针对同一个资源，比对通过CDN加速，和直接访问源站数据，查看加速效果。

| 拨测时间 | 2022 年 11 月 14 日 |
| --- | --- |
| 拨测工具 | 博睿数据 |
| 拨测地域 | 包含全国 |
| 拨测运营商 | 覆盖中国联通、中国电信、中国移动 |
| 测试文件大小 | 1 MB |
| 拨测规则 | 同一个资源，通过定时任务分别在下午 14 点、15 点、16 点、17 点进行拨测（该文件未进行 CDN 预热） |
| 关注指标 | 下载速率，首包时间 |
| URL 地址 | CDN 加速 URL： http://*/network.csv |
| 源站访问 URL： http://*.oss-cn-beijing.aliyuncs.com/network.csv |  |


## 结果分析

| 时间 | 说明 | 建议 |
| --- | --- | --- |
| 14 点 | 该时间段 CDN 表现比直接访问源站差，刚通过 CDN 加速时，由于源站资源还未缓存至 CDN 节点，访问回源，导致性能较差。 | 提前进行预热对静态文件设置缓存时长，根据自身业务特点，缓存时长设置为 3 天、7 天、1 个月均可。 |
| 15 点 | 命中率回升后，CDN 质量变好，超过直接访问源站的性能。 | 对 CDN 的质量进行观察。 |
| 16 点 | 命中稳定后，CDN 质量数据大幅提升，包括总下载时间，首包等。 | 对 CDN 的质量进行观察，此时可以继续切量到 CDN。 |
| 17 点 | 命中稳定后，CDN 质量数据大幅提升，包括总下载时间，首包等。 | CDN 正常运行，可创建告警相关指标，对 CDN 进行日常监控。 |
| 总结 | CDN 加速质量从较差变好，受命中率的影响，命中稳定后，下载速率、和首包、建联时间提升明显。 |  |


[上一篇：CDN的性能指标](products/cdn/documents/product-overview/performance-indicators.md)[下一篇：动态与公告](products/cdn/documents/product-overview/announcements-and-updates.md)

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
