# 实例升降配的计费方法与退款规则-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/configuration-changes

# 变配说明
云数据库 Tair（兼容 Redis）支持按需升降配，包括变更实例架构、变更分片规格、变更分片数量等，帮助您提高资源利用率，优化成本结构。本文介绍实例升配的费用以及实例降配的退款说明。
## 按量付费变配
按量付费实例变更配置，按生成订单时的实例配置计费。
按量付费实例为先使用后付费，因此不涉及降配退款。
## 包年包月变配
包年包月实例在到期前和到期后均可变更配置。如果变配的目标规格比现有规格的价格高，则需要升级配置，反之为降级配置。例如，读写分离8 GB版（5只读节点）的价格比16 GB集群版的价格高，从后者变配到前者为升级配置。
| 变配方式 | 计费说明 |
| --- | --- |
| 升级 | 升配费用=（新配置剩余时长的官网目录价-老配置剩余时长的官网目录价）x 剩余时长可享受的优惠折扣 新配置剩余时长的官网目录价=新配置的官网目录单价*剩余时长 老配置剩余时长的官网目录价=老配置的官网目录单价*剩余时长 关于 新配置的配置单价 、 老配置的配置单价、剩余时长 的计费说明，请参见 [升配事项介绍](https://help.aliyun.com/zh/user-center/description-of-ascenting-rules) 。 |
| 降级 | 降配退款金额=在线退款金额×新老配置差价比例（多个订单会分别计算后求和） 关于 在线退款金额 、 新老配置差价比例 的详细说明，请参见 [退订规则说明](https://help.aliyun.com/zh/user-center/cancel-subscription/#p-y71-3cg-wq4) 。 |
## 版本间变配
Redis开源版经典版实例可变配到Tair（企业版）。
Tair（企业版）实例不可变配至Redis开源版。
## 常见问题
### 退订后资金流向
退订后退款的资金一般遵循原路退款的规则，退款回原付款的渠道。
通过支付宝支付的订单，自2019年3月29日之后，付款后18个月（548天）内发生退订，退订款项退至支付使用的支付宝账号，如遇退款失败，则退回至您阿里云的账户余额。
通过网银支付的订单，在支付后的90天内退订，退订款项一般原路退回原付款的银行卡，如遇银行退款失败，则退回至您阿里云的账户余额。
通过账户余额支付的订单，直接退至账户余额。
其他支付方式（如微信支付、银联云闪付等）支付的订单优先原路退回；若失败则退至阿里云的账户余额。
特殊情况说明
已开具发票的订单退款情况：
如退款金额小于账号当前可开票金额，则优先原路退回；若超出原路退款时限，则退回账户余额。
如退款金额大于账号当前可开票金额，则直接退回账户余额，用户如需取回，需要[处理欠票](https://help.aliyun.com/zh/user-center/manage-shortfalls)后，再申请提现。
退款金额限制：
优惠券抵扣的部分不支持退回，仅退还以现金或储蓄卡方式支付的订单款项。
### 退款到账时间
产品退订成功，退款大约会在2个工作日内退回（退款仅指用户以现金或储值卡方式支付的订单款项，用户通过代金券、优惠券抵扣的部分不支持退回）。
通过网银支付的订单发生退订且满足原路退回，受银行受理时间影响，预计2-3个工作日内到账。
## 相关文档
变更分片的内存规格，变更经典部署实例的架构、分片数和只读节点数，请参见[变更实例配置](../user-guide/change-the-configurations-of-an-instance.md)。
云原生集群架构的实例，增加或减少集群的分片数，请参见[调整集群分片数](../user-guide/adjust-the-number-of-cluster-shards.md)。
云原生实例开启读写分离功能，请参见[开启读写分离](../user-guide/enable-read-write-splitting.md)。
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
