# 实例计费方式与计费规则-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/billing-methods

# 计费方式
云数据库 Tair（兼容 Redis）的实例规格费用支持按量付费、包年包月的计费方式。按量付费实例推荐搭配资源包，降低成本。
| 计费方式 | 优势 | 说明 |
| --- | --- | --- |
| 按量付费 | 灵活 | 支持随时创建与释放实例，释放实例后不再收费。 计费周期为 1 个小时。不足 1 小时，也按 1 小时收费。 账单出账时间通常在当前计费周期结束后 1 小时内，最长不超过 3 个小时，例如 9:00 am~10:00 am 的账单一般会在 11:00 am 以前生成。具体以系统出账时间为准。账单生成后会自动从您的账户中扣除费用以结算账单。 如果您在一个计费周期内更改了实例规格，计费将以该周期内的最高实例规格为准。 以 1:00 am~2:00 am 的计费周期为例，如果您在 1:10 am 时容量为 1 GB，1:20 am 时改为 8 GB，1:50 am 时改为 2 GB，则 1:00 am~2:00 am 这个计费周期按照 8 GB 容量规格的定价来收取费用。 适合临时性、突发性或业务经常有变化的场景。 |
| 按量付费+资源包 | 灵活、低价 | 计费周期、计费规则均与按量付费相同，但费用由预购的资源包自动抵扣。 按量付费的 经典 版 Tair（企业版） 实例或 经典 版 Redis 开源版 实例的实例规格费用，优先从资源包抵扣。若资源包剩余额度不足，超出部分的费用仍以按量付费的形式从账户中扣除，更多信息，请参见 [资源包](resource-plan-overview.md) 。 |
| 包年包月 | 低价 | 预付费方式，在创建实例时就需要支付费用。 包年包月的资源计费周期为订单的购买周期（以 UTC+8 时间为准），一个计费周期的起点为开通或续费资源的时间 （精确到秒），终点为到期日次日的零点（00:00:00）。 说明 包年包月以年、月为单位的计费周期，包年为 365 天，包月为 30 天。 适合长期使用场景，价格比按量付费更优惠。 |
创建实例后，支持转换计费方式。
Tair按照开通的实例容量规格收费，而不是按照实际使用的缓存容量收费。
例如您开通了一个2 GB的Tair实例，里面存储了256 MB的数据，则按照2 GB容量规格的定价来收取费用。
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
