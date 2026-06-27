# 日志服务助力米连科技实现智能运维与数据分析-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/milian-technology

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [开始使用](products/sls/documents/start-using-sls.md)

- [资源管理](products/sls/documents/resource-management.md)

- [数据采集](products/sls/documents/data-collection-1.md)

- [数据处理](products/sls/documents/data-processing-sls.md)

- [数据存储](products/sls/documents/data-storage.md)

- [查询与分析](products/sls/documents/index-and-query.md)

- [数据监控](products/sls/documents/data-monitoring.md)

- [数据输出与集成](products/sls/documents/sls-log-output-and-integration.md)

- [技术解决方案](products/sls/documents/sls-technical-solutions.md)

- [开发参考](products/sls/documents/developer-reference.md)

- [安全合规](products/sls/documents/security-compliance.md)

- [常见问题](products/sls/documents/faq-15.md)

[首页](https://help.aliyun.com/zh)

# 米连科技

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

日志服务帮助米连科技解决了数据分散、问题排查效率低、数据分析手段少的问题，提升了IT运维、数据运营、风控等方面的能力。

## 公司简介

伊对是北京米连科技有限公司旗下品牌，公司成立于2015年，是国家高新技术企业和北京中关村高新技术企业。2019年公司营收近10亿人民币。2020年公司完成多家机构参与的近1亿美元的B轮投融资。伊对专注于移动端线上交友和相亲，将视频、直播和线上红娘创造性地融入该领域，开辟了视频恋爱社区的独立赛道，为单身人群提供了全新的社交体验，成为2019年互联网细分领域的亮点。更多信息，请参见[伊对](https://www.520yidui.com/schooling/index.html?tab=introduce)。

## 业务场景

伊对以恋爱为目的，提供实时视频互动和相亲场景，用户可以通过伊对认识喜欢的人，发送文字信息、语音、照片以及视频实时互动进行恋爱相亲。伊对会给新用户推荐最匹配的直播间，提供搜索功能，让男女双方都可以快速找到自己喜欢的人。在初期，伊对采用了ES和MySQL提供推荐和搜索业务。但是随着业务发展、架构的升级、数据量的增长，伊对需要寻找更强大的数据采集、处理和分析平台来满足运营团队日益增长的数据分析需求，保持伊对高速的用户增长率。

## 业务痛点

伊对面临的主要挑战如下：

- 

数据来源分散

客户使用不同的计算存储引擎，包括数据库类、大数据类、第三方服务等，需要统一规划和管理，避免产生数据孤岛；并且希望进一步提升开发和管理效率。

- 

业务量迅猛增长

随着业务和用户规模的提升，尤其是直播间相亲活动数量的成倍增长，系统复杂度和日志量也迅速地增长。但是由于自建的ES平台在高业务量下查询变得非常缓慢， 当出现系统问题时故障排查效率较低，用户体验无法得到充分和及时的保障。

- 

数据分析能力缺乏

伊对始终坚持以数据驱动产品运营，从最早的统计报表类需求，逐步扩展到基于算法的推荐、风控、运营交互式查询、用户行为分析等领域，但是与之对应的数据能力较为薄弱。

## 解决方案

针对数据来源分散、业务量迅猛增长、数据分析能力缺乏等挑战，阿里云提供了日志服务作为解决方案。

- 

统一日志采集

- 

Web前端日志：通过日志服务WebTracking方式采集上报到日志服务。

- 

APP前端日志：通过日志服务iOS和Android SDK采集上报到日志服务。

- 

服务端日志：通过日志服务Logtail采集方式上报到日志服务。

- 

统一智能运维平台

通过日志服务，客户构建了统一的智能运维平台。通过对各应用系统、服务器、数据库及网络安全产品等服务的访问日志做统一的采集，并利用日志服务的秒级查询、日志聚类、AI异常检测能力、多种告警方式，伊对构建了异常事件的快速分析与响应平台，确保了线上系统的稳定。以日志服务为基础的伊对智能运维平台，也应用在用户体验改善上，通过多维度的指标分析和图形化展现，为持续改善用户体验提供了数据基础。

- 

统一数据服务

通过以阿里云日志服务采集上来的数据为基础，结合离线计算、实时计算引擎和PAI机器学习平台，为客户提供统一的数据分析服务。

- 

API网关：作为统一数据服务出口。

- 

Quick BI：交互式报表制作，拖拽形式快速制作各种报表。

- 

DataV：固定格式的数据大屏。

[上一篇：哈啰出行](products/sls/documents/hellobike.md)[下一篇：资源管理](products/sls/documents/resource-management.md)

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
