# CDN日志查询下载转存推送-离线日志-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/user-guide/overview

# 概述
您可以通过分析CDN日志及时发现问题，并有针对性的解决问题，提升CDN服务质量。通过本文您可以了解CDN提供的日志相关的功能和产品。
## 相关功能
通过日志管理功能，您可以对CDN日志执行以下操作：
| 功能 | 说明 |
| --- | --- |
| [下载离线日志](offline-logs-quick-start.md) | 您可以查询指定时间、域名下日志，并下载保存。 |
| [通过函数计算转存离线日志](use-function-compute-to-deliver-logs.md) | 如果您需要将日志保存更长时间，则可以将日志转存至 OSS，方便您根据实际情况对日志进行保存和分析。 |
| [配置实时日志推送](configure-real-time-log-delivery.md) | 您可以通过实时日志推送功能，将 CDN 日志实时推送至日志服务，并进行日志分析，便于快速发现和定位问题。 |
## 相关产品
CDN日志管理相关产品如下：
函数计算
函数计算已经支持了多种CDN场景，包括：日志转存、刷新预热、资源封禁、域名添加和删除、域名启用和停用。具体触发方式请参见[CDN](https://help.aliyun.com/zh/functioncompute/fc-2-0/user-guide/overview-27)[事件触发器](https://help.aliyun.com/zh/functioncompute/fc-2-0/user-guide/overview-27)。
如果您想深入了解函数计算服务，请参见[什么是函数计算](https://help.aliyun.com/zh/functioncompute/fc-2-0/product-overview/what-is-function-compute)。
对象存储OSS
对象存储OSS是一款海量、安全、低成本、高可靠的云存储服务，用于存储和管理各种类型的文件。更多信息，请参见[什么是对象存储](../../../oss/documents/user-guide/what-is-oss.md)[OSS](../../../oss/documents/user-guide/what-is-oss.md)。
日志服务
日志服务提供实时的数据收集、存储和查询功能。更多信息，请参见[什么是日志服务](../../../sls/documents/what-is-log-service.md)。
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
