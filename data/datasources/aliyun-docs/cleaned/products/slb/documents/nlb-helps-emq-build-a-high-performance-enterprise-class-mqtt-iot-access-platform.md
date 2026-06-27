# 使用NLB构建支持亿级并发的MQTT物联网接入平台-负载均衡-阿里云

Source: https://help.aliyun.com/zh/slb/nlb-helps-emq-build-a-high-performance-enterprise-class-mqtt-iot-access-platform

# 【客户案例】NLB助力EMQ构建高性能企业级MQTT物联网接入平台
EMQ使用NLB实现亿级设备的并发管理，构建高性能、高可靠、低成本的企业级MQTT物联网接入平台。
## 客户简介
EMQ是一家全球领先的物联网（IoT）消息中间件提供商和技术解决方案提供商。公司总部位于中国上海，专注于为企业和开发者提供高性能、可靠和安全的物联网消息传递平台。
## 业务挑战
作为一家创新驱动的公司，EMQ致力于解决物联网领域面临的挑战，包括大规模设备连接、消息传递效率和数据安全等方面。EMQ的核心产品是EMQ X，它是一款企业级开源物联网消息中间件，具有高度可伸缩性和灵活性。EMQ X支持多种通信协议和设备接入方式，包括MQTT、CoAP、WebSocket等，能够轻松连接和管理数百万台物联网设备。
客户此前主要采用私有协议和TCP连接，计划通过TLS加密，提升整体安全性。但因私有协议无法用HTTPS满足，而传统的负载均衡无法支持TCP SSL卸载，因此只能在后端应用服务器部署证书卸载，运维管理复杂。同时如何弹性应对海量并发连接与流量峰谷也是一个很大的挑战。
## 方案架构
通过NLB替换原有负载均衡+Nginx集群，实现SSL集中卸载，证书统一管理。EMQ基于NLB网络型负载均衡打造了大规模分布式物联网MQTT消息服务器EMQX，实现峰值并发达到一个亿，这意味着只需要购买一个NLB实例，EMQX可以一直扩展到满足亿级设备的并发管理，实现业务的平滑扩张。
## 客户价值
高性能：超高性能、自动弹性，满足数千万并发。
高可靠：通过洪峰上联限速能力，在海量新建上连时有效保护业务可靠性。
低成本：按LCU计费，无需高额保有成本，用多少付多少，无需担心闲置资源浪费。
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
