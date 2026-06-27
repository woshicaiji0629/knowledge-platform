# 抵扣多种云存储产品存储容量费用-存储容量单位包SCU-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/storage-capacity-units-1

# 存储容量单位包SCU
存储容量单位包SCU（Storage Capacity Unit）是一种预付费的存储容量资源包，可以抵扣云盘、快照和对象存储OSS等多种云存储产品的存储容量费用。本文主要介绍SCU的计费方式、抵扣规则及退款说明等。
## 计费方式
存储容量单位包SCU采用预付费的计费方式，按容量和有效期计费。付款类型为全预付，即需要一次性支付所有费用。费用计算如下：
预付费用 = 存储容量单位包价格 * 有效期
存储容量单位包价格：详细的单价请参见[产品定价](https://www.aliyun.com/price/product#/ecs/detail)。
有效期：支持选择1个月、2个月、3个月、半年、1年、3年或5年的购买时长。其中，按年付享有一定程度的价格优惠。
例如，您需要在华北2（北京）地域购买100 GB存储容量单位包SCU，有效期为2个月，华北2（北京）地域100 GB的存储容量单位包单价是100元/月，则购买SCU的费用为：预付费用=100元/月*2个月=200元。
## 购买并使用SCU
如何购买SCU：请参见[购买存储容量单位包](https://help.aliyun.com/zh/scu/purchase-an-scu)[SCU](https://help.aliyun.com/zh/scu/purchase-an-scu)。
如何使用SCU：购买SCU后，可以自动抵扣同地域内云盘和快照的按量付费账单。如果云盘和快照实际容量超出了SCU容量，超出部分将采用按量付费。
## 抵扣规则
### 抵扣系数
下表列出华北2（北京）地域SCU抵扣云盘和快照存储费用时的抵扣系数。其他地域和其他云产品的抵扣系数，请参见[产品定价](https://www.aliyun.com/price/product#/ecs/detail)。
| 类型 | 抵扣系数 | 说明 |
| --- | --- | --- |
| 高效云盘 | 0.35 | 每 0.35 GB 的 SCU 容量支持抵扣 1 GiB 高效云盘。 |
| SSD 云盘 | 1 | 每 1 GB 的 SCU 容量支持抵扣 1 GiB SSD 云盘。 |
| ESSD PL0 云盘 | 0.5 | 每 0.5 GB 的 SCU 容量支持抵扣 1 GiB ESSD PL0 云盘。 |
| ESSD PL1 云盘 | 1 | 每 1 GB 的 SCU 容量支持抵扣 1 GiB ESSD PL1 云盘。 |
| ESSD PL2 云盘 | 2 | 每 2 GB 的 SCU 容量支持抵扣 1 GiB ESSD PL2 云盘。 |
| ESSD PL3 云盘 | 4 | 每 4 GB 的 SCU 容量支持抵扣 1 GiB ESSD PL3 云盘。 |
| 标准快照 | 0.12 | 每 0.12 GB 的 SCU 容量支持抵扣 1 GB 标准快照。 |
### 抵扣顺序
云盘
云盘仅支持使用SCU抵扣按量存储费用，以节约使用成本。云盘存储费用的抵扣顺序为：SCU ＞ 按量付费。关于云盘更多的计费信息，请参见[块存储计费](block-storage-devices.md)。
快照
快照支持使用OSS标准-本地冗余存储包、SCU或预留空间抵扣按量存储费用，以节约使用成本。
如果您已购买某个地域的预留空间，则不再支持购买同地域的标准-本地冗余存储包。因此快照存储费用的抵扣顺序存在以下两种情况：
OSS标准-本地冗余存储包＞ SCU ＞ 按量付费
预留空间 > SCU > 按量付费
关于快照更多的计费信息，请参见[快照计费](snapshots-1.md)。
### 抵扣示例
使用SCU抵扣云盘存储费用
示例一：假设您使用的ESSD PL1云盘总容量为10 TiB，购买了10 TB存储容量单位包SCU。
则该云盘需要消耗的SCU容量为10 TB（10 TB * 1），即您购买的10 TB SCU可抵扣云盘的全部按量费用账单。
示例二：假设您使用的ESSD PL0云盘总容量为10 TiB、ESSD PL1云盘总容量为5 TiB，购买了10 TB存储容量单位包SCU。
则这些云盘需要消耗的SCU容量为10 TB（10 TB * 0.5 + 5 TB * 1） ，即您购买的10 TB SCU可抵扣这些云盘的全部按量费用账单。
示例三：假设您使用的ESSD PL3云盘总容量为1 TiB、ESSD PL2云盘总容量为2 TiB、ESSD PL1云盘总容量为2 TiB，购买了10 TB存储容量单位包SCU。
则这些云盘需要消耗的SCU容量为10TB（1 TB * 4 + 2 TB * 2 + 2 TB * 1），即您购买的10 TB SCU可抵扣这些云盘的全部按量费用账单。
示例四：假设您使用的SSD云盘总容量为12 TiB，购买了10 TB存储容量单位包SCU。
则该云盘需要消耗的SCU容量为12 TB（12 TB * 1），根据抵扣顺序（ SCU ＞ 按量计费），您购买的10 TB SCU可抵扣该云盘10 TiB按量费用账单，超出的2 TiB使用按量付费。
使用SCU抵扣快照存储费用
示例一：假设您2022年01月在华北2（北京）地域的快照容量为500 GB，在该地域分别购买多少OSS标准-本地冗余存储包和SCU才能完全抵扣快照存储费用？
OSS标准-本地冗余存储包：需购买500 GB可以完全抵扣。
SCU：需购买60 GB（500*0.12）可以完全抵扣。
示例二：假设您2022年01月在华北2（北京）地域的快照容量为500 GB，同时购买了200 GB的OSS标准-本地冗余存储包和40 GB的SCU ，SCU如何抵扣快照存储费用？
根据抵扣顺序（OSS标准-本地冗余存储包＞ SCU＞ 按量计费），则SCU抵扣情况如下：
先使用OSS标准-本地冗余存储包抵扣快照存储费用。
使用200 GB的OSS标准-本地冗余存储可以抵扣200 GB的快照存储费用。
再使用SCU抵扣快照存储费用。
快照剩余的300 GB需要消耗的SCU容量为（500 GB-200 GB）×0.12=36 GB，则需要使用36 GB SCU来抵扣剩余300 GB的快照存储费用。
## 过期
SCU超出有效期后，无法继续抵扣存储产品的按量付费账单。如果所在地域内没有其他SCU，原来被抵扣的存储产品均采用按量付费计费方式。
## 续费或升级
SCU不支持续费或升级，但您可以根据存储产品的使用情况多次购买SCU。
如果您购买的SCU不够使用，可以同时购买多个SCU叠加使用。
如果您购买的SCU即将到期，可以在到期前重新购买SCU并指定生效时间。
## 退款
购买SCU的五天内，可以申请无理由退款。
说明
每个阿里云账号每年只有一次五天无理由退款SCU的机会，即每个账号每年最多退款一次，可退还的上限是一个存储容量单位包。
退款时会扣除掉已经消费的金额，已使用的代金券等优惠折扣不退还。更多信息，请参见[退款规则及退款流程](https://help.aliyun.com/zh/document_detail/37096.html)。
## 相关文档
您可以调用API[PurchaseStorageCapacityUnit](developer-reference/api-ecs-2014-05-26-purchasestoragecapacityunit.md)接口购买一个或多个存储容量单位包。
您可以调用API[ModifyStorageCapacityUnitAttribute](developer-reference/api-ecs-2014-05-26-modifystoragecapacityunitattribute.md)接口修改存储容量单位包的名称或者描述信息。
您可以调用API[DescribeStorageCapacityUnits](developer-reference/api-ecs-2014-05-26-describestoragecapacityunits.md)接口查询存储容量单位包详细信息，包括SCU容量大小和状态等。
## 常见问题
关于存储容量单位包SCU的常见问题，请参见[计费](billing-faq.md)[FAQ](billing-faq.md)。
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
