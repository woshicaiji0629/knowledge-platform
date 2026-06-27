# 使用ALB应对大流量和高并发场景的解决方案-负载均衡-阿里云

Source: https://help.aliyun.com/zh/slb/anipop-uses-alb

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/slb/documents/product-overview.md)

- [安全合规](products/slb/documents/security-and-compliance.md)

- [服务支持](products/slb/documents/support.md)

- [客户案例](products/slb/documents/customer-use-cases.md)

[首页](https://help.aliyun.com/zh)

# 【客户案例】开心消消乐使用ALB从容应对大流量和高并发场景

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/slb)

[我的收藏](https://help.aliyun.com/my_favorites.html)

开心消消乐作为一款深受国民喜爱的单机游戏，经常面临大流量和高并发场景。为了更好地调度流量并实现负载分担，开心消消乐通过应用型负载均衡 ALB（Application Load Balancer）转发流量，实现按需弹性的方式应对大流量和高并发场景。本文以开心消消乐为例说明ALB解决方案的客户需求、方案架构、以及方案优势等内容。

## 客户需求

开心消消乐经常会在某些节庆日、特定运营活动节点迎来流量高峰。开心消消乐大数据中心会通过分析游戏运行指标，按需调度流量升级终端用户的服务体验。但由于活动前无法预估业务高峰会达到多大的流量水平，因此常常需要根据地域、时间段、终端等数据分析临时手工增减机器。

IT网络运维管理人员经常面临以下问题：

- 

运维管理工作量大：有⾼并发流量、⾼QPS需求时，运维人员需要管理多组服务端进⾏业务负载分担，运维管理工作量大。

- 

重要业务需要人工干预多：在业务高峰期，为保障重要请求不受影响，需要部署两组服务器端，且需要根据URL进行手工调度。

- 

七层业务调度最佳路由能力差：部分业务需要基于Header调度时，由于七层路由能力有限导致业务一直在服务端运行。

## 方案架构

因为ALB单实例七层处理能力高达100万QPS，能够自动根据用户访问量调度流量，从容应对大流量和高并发场景。所以推出ALB解决方案来确保开心消消乐在大流量和高并发场景下更好地调度流量。方案架构如下图所示。

## 方案优势

- 

超强性能，按需弹性：单个ALB实例可提供⾼达100万QPS能⼒，运维人员无需预估业务高峰值，ALB即可根据实际业务情况，自动弹性地应对业务高峰。

- 

简化运维，节约人力：DDoS直接回源ALB，将以往多个实例合并为⼀个ALB实例，降低日常运维管理难度。

- 

更低时延，更优体验：部署一套服务端，通过URL转发规则实现不同优先级业务的差异化调度，满足个性化路由转发需要。

- 

面向未来，可扩展：ALB可以作为容器的Ingress入口，容器化技术演进可平滑升级。

## 更多信息

- 

[什么是应用型负载均衡](products/slb/documents/application-load-balancer/product-overview/what-is-alb.md)[ALB](products/slb/documents/application-load-balancer/product-overview/what-is-alb.md)

- 

[云解析](https://help.aliyun.com/zh/dns/alibaba-cloud-dns#topic-2035878)[DNS](https://help.aliyun.com/zh/dns/alibaba-cloud-dns#topic-2035878)

- 

[什么是](https://help.aliyun.com/zh/anti-ddos/anti-ddos-origin/product-overview/what-is-anti-ddos-origin#concept-63643-zh)[DDoS](https://help.aliyun.com/zh/anti-ddos/anti-ddos-origin/product-overview/what-is-anti-ddos-origin#concept-63643-zh)[原生防护](https://help.aliyun.com/zh/anti-ddos/anti-ddos-origin/product-overview/what-is-anti-ddos-origin#concept-63643-zh)

[上一篇：【客户案例】NLB助力EMQ构建高性能企业级MQTT物联网接入平台](products/slb/documents/nlb-helps-emq-build-a-high-performance-enterprise-class-mqtt-iot-access-platform.md)[下一篇：应用型负载均衡ALB](products/slb/documents/application-load-balancer.md)

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
