# 资源包-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/resource-plan

# 资源包概述
OSS默认按量付费。您可以购买OSS资源包，资源包相比按量付费更划算。OSS资源包可以抵扣存储、流量等费用。如果资源包到期或额度全部抵扣完后，如果仍有超出部分，自动转为按量付费。
说明
OSS提供部分功能的试用资源包可供您免费试用，具体信息可参见[查看](https://free.aliyun.com/?searchKey=oss&spm=a311a.7996332.0.0.3e9930807zHxhz&scm=20140722.M_9553144.P_154.MO_1802-ID_9553144-MID_9553144-CID_20080-ST_7663-V_1)[OSS](https://free.aliyun.com/?searchKey=oss&spm=a311a.7996332.0.0.3e9930807zHxhz&scm=20140722.M_9553144.P_154.MO_1802-ID_9553144-MID_9553144-CID_20080-ST_7663-V_1)[试用资源包](https://free.aliyun.com/?searchKey=oss&spm=a311a.7996332.0.0.3e9930807zHxhz&scm=20140722.M_9553144.P_154.MO_1802-ID_9553144-MID_9553144-CID_20080-ST_7663-V_1)。
## 资源包类型
| 资源包 | 说明 |
| --- | --- |
| 存储包 | 抵扣 OSS 文件 或 ECS 快照 的存储费用 |
| 标准-同城冗余存储包 | 抵扣标准-同城冗余存储类型的 OSS 文件的存储费用 |
| 标准-本地冗余存储包 | 抵扣标准-本地冗余存储类型的 OSS 文件 或 ECS 快照 的存储费用 重要 如果您已购买某个地域的预留空间，则不再支持购买中国内地通用或同地域的标准-本地冗余存储包。 |
| 低频-同城冗余存储包 | 抵扣低频-同城冗余存储类型的 OSS 文件的存储费用 |
| 低频-本地冗余存储包 | 抵扣低频-本地冗余存储类型的 OSS 文件的存储费用 |
| 归档-同城冗余存储包 | 抵扣归档-同城冗余存储类型的 OSS 文件的存储费用 |
| 归档-本地冗余存储包 | 抵扣归档-本地冗余存储类型的 OSS 文件的存储费用 |
| 冷归档-本地冗余存储包 | 抵扣冷归档-本地冗余存储类型的 OSS 文件的存储费用 |
| 流量包 | 抵扣 OSS 使用过程中产生的 流量 费用 |
| 下行流量包 | 抵扣数据通过互联网从 OSS 传输到客户端所产生的流量费用 |
| 回源流量包 | 抵扣数据从 OSS 传输到 CDN 边缘节点所产生的回源流量费用 |
| 传输加速包 | 抵扣用户通过传输加速域名访问 OSS 时所产生的加速流量费用 |
| 请求包 | 抵扣 Put 类和 Get 类请求费用 |
| 请求包-标准存储类型 | 抵扣标准类型的 Put 类和 Get 类请求 |
| 请求包-非标准存储类型 | 抵扣低频、归档、冷归档类型的 Put 类和 Get 类请求 |
| 高防基础包 | 抵扣 预留高防实例资源 所产生的费用 |
| OSS 加速器包 | 抵扣 OSS 加速器实例 所产生的配置容量费用 |
## 选购建议
### 建议1：根据使用场景选择资源包类型
常用的OSS资源包购买组合为存储包+下行流量包。存储包用于抵扣OSS存储和ECS快照的存储费用。下行流量包用于抵扣外网访问OSS文件的流量费用。
| 使用场景 | 用于抵扣的资源包 |
| --- | --- |
| 使用 OSS 存储文本、图片、音视频等文件，且存储类型为标准-本地冗余存储 | 标准-本地冗余存储包 |
| 创建并保留 ECS 快照 | 标准-本地冗余存储包 |
| 通过外网浏览或下载 OSS 里的文件 | 下行流量包 |
关于所有资源包类型的使用场景，请参见[资源包类型](resource-plan.md)。
### 建议2：根据账单的计费项选择资源包类型
如果您已有OSS账单，建议您根据[明细账单](https://usercenter2.aliyun.com/finance/expense-report/expense-detail-by-instance)里的计费项选择您要购买的资源包类型。
例如，计费项为标准存储（本地冗余）容量，那么您可以购买标准-本地冗余存储包抵扣该费用。
在账单详情页面，将统计项设置为计费项，统计周期设置为明细，并按产品筛选对象存储，即可查看各计费项的单价明细。
### 建议3：根据账单的用量选择资源包规格
如果您已有OSS账单，建议根据[明细账单](https://usercenter2.aliyun.com/finance/expense-report/expense-detail-by-instance)里的用量选择您要购买的资源包规格。
例如，标准存储（本地冗余）容量每小时的用量为40 GB，那么您可以购买40 GB的标准-本地冗余存储包抵扣该费用。
### 建议4：购买后仍然按小时扣费的排查方法
在[明细账单](https://usercenter2.aliyun.com/finance/expense-report/expense-detail-by-instance)页面，查看计费项的类型、用量、消费时间。
在[资源包列表](https://usercenter2.aliyun.com/ri/summary?commodityCode=)页面，查看生效的资源包的类型、总量、生效时间。
对比计费项和资源包。
| 问题示例 | 解决方案 |
| --- | --- |
| 账单有外网流出流量（NetworkOut）计费项，但资源包列表没有下行流量包。 | 购买下行流量包 |
| 账单有标准存储（本地冗余）容量计费项，但资源包列表没有 标准-本地冗余存储包 。 | 购买 标准-本地冗余存储包 |
| 账单的标准存储（本地冗余容量）计费项每小时有 100 GB 用量，但资源包列表的 标准-本地冗余存储包 总量为 40 GB。 | 将 标准-本地冗余存储包 规格升级至 100GB |
| 账单产生于购买资源包之前。 | 无 |
## 抵扣限制
OSS资源包仅支持抵扣当前阿里云账号下产生的费用，不支持跨账号抵扣。
OSS资源包为OSS服务专用资源包，不支持跨产品抵扣。
OSS资源包仅支持抵扣资源包购买后产生的费用，不支持抵扣资源包购买前产生的费用。
一种类型的资源包只能抵扣使用该资源包对应计费项产生的费用，不能抵扣所有费用。更多信息，请参见[资源包类型](resource-plan.md)。
OSS指定地域的资源包仅支持抵扣对应地域该资源包对应计费项产生的费用，中国内地通用资源包支持跨地域抵扣多个中国内地各地域该资源包对应计费项产生的费用。更多信息，请参见[抵扣地域](resource-plan.md)。
## 抵扣方式
| 抵扣方式 | 资源包 | 说明 |
| --- | --- | --- |
| 总量恒定型 | 存储包 高防基础包 OSS 加速器包 | 每小时都有固定额度 ，剩余额度不可转移到下个小时。 存储包 例如 ，10 TB 规格存储包每小时均可抵扣最多 10 TB 容量。 如果第一个小时存储量为 9 TB，则存储费用完全由存储包抵扣。 如果第二个小时存储量为 10 TB，则存储费用完全由存储包抵扣。 如果第三个小时存储量为 11 TB，则存储包抵扣 10 TB，超出的 1 TB 将按量付费。 高防基础包 例如 ，购买 2 个时长半年的单实例规格的高防基础包，则每小时均可抵扣最多 2 个高防实例产生的高防资源预留费用以及高防资源提前释放费用。 如果第一个小时内仅有 1 个高防实例，则完全由高防基础包抵扣。 如果第二个小时内共有 2 个高防实例，则完全由高防基础包抵扣。 如果第三个小时内共有 3 个高防实例，则高防基础包抵扣 2 个高防实例费用，超出的 1 个高防实例按量付费。 OSS 加速器包 例如 ，购买 100 GB 的 OSS 加速器包，则每小时均可抵扣所购买 OSS 加速器实例的配置容量总共 100 GB。 如果第一个小时内创建了 50 GB 的 OSS 加速器，则容量费用完全由 OSS 加速器包抵扣。 如果第二个小时内将该 OSS 加速器的容量修改为 100 GB，则容量费用完全由 OSS 加速器包抵扣。 如果第三个小时内将该 OSS 加速器的容量修改为 110 GB，则 OSS 加速器包抵扣 100 GB 容量费用，超出的 10 GB 按量付费。 |
| 包月周期型 | 下行流量包 | 每月都有固定额度 ，次月 1 号额度重置，当月剩余不可转移到下月。 例如 ，本月 18 日购买时长为 1 个月、规格为 100GB 的下行流量包，18 日至月底可抵扣 100GB 外网流出流量，超出部分按量计费。次月 1 日额度重置，次月 1 日至 18 日可再次抵扣 100GB，超出部分按量计费。 |
| 总量递减型 | 传输加速包 回源流量包 请求包-标准存储 请求包-非标准存储 | 按实际消费进行抵扣，直到余额清零或者过期。 传输加速包 例如 ，购买 5 TB 规格 3 个月，则 3 个月内总共有 5 TB 的传输加速流量抵扣额度，超出部分按量付费。 回源流量包 例如 ，购买 5 TB 规格半年，则半年内总共有 5 TB 的回源流量抵扣额度，超出部分按量计费。 请求包-标准存储 例如 ，购买 5000 万次规格 1 年，则 1 年内总共有 5000 万次针对标准类型的 Put 类和 Get 类请求次数抵扣额度，超出部分按量付费。 请求包-非标准存储 例如 ，购买 5000 万次规格 1 年，则 1 年内总共有 5000 万次针对低频、归档、冷归档类型的 Put 类和 Get 类请求次数抵扣额度，超出部分按量付费。 |
## 抵扣地域
除无需指定地域的高防护基础资源包外，您在购买OSS资源包时，都需要指定对应的地域。指定地域的资源包只能抵扣指定地域的费用。
说明
高防基础包支持抵扣可开通高防实例的各个地域的计量，但同一小时内只能抵扣单个地域单个实例的计量。如果同一小时内有多个地域产生高防计量，需要通过叠加购买高防基础包的方式进行抵扣。
| 地域类型 | 说明 |
| --- | --- |
| 指定地域专用 ① | 抵扣某个指定地域内对应资源的使用费用，不可跨地域共享。 ② |
| 中国内地通用 ① | 抵扣多个中国内地各地域对应资源的使用费用，可跨地域共享。 ③ |
| 传输加速地域 | 抵扣通过传输加速域名，从不同地域访问不同地域的 OSS 时，产生的上传、下载的传输加速流量费用。 |
| 传输加速 M2M | 抵扣通过传输加速域名，从中国内地访问中国内地的 OSS 时，产生的上传、下载的传输加速流量费用（AccM2MIn、AccM2MOut）。 |
| 传输加速 M2O_O2M | 抵扣通过传输加速域名，从非中国内地访问中国内地的 OSS，或者从中国内地访问非中国内地的 OSS 时，产生的上传、下载的传输加速流量费用（AccM2OIn、AccM2OOut、AccO2MIn、AccO2MOut）。 |
| 传输加速 O2O | 抵扣通过传输加速域名，从非中国内地访问非中国内地的 OSS 时，产生的上传、下载的传输加速流量费用（AccO2OIn、AccO2OOut）。 |
①中国内地通用资源包与中国内地指定地域专用资源包可以同时购买。抵扣费用时，优先抵扣中国内地指定地域专用资源包，超出额度后再抵扣中国内地通用资源包。如果仍有超出，则超出部分按量付费。
②例如，华北1（青岛）的资源包仅能抵扣华北1（青岛）对应资源的使用费用，无法抵扣其他地域内对应资源的使用费用。
③关于中国内地通用资源包支持抵扣的中国内地地域，请参见[中国内地通用资源包支持的地域](resource-plan.md)。
### 中国内地通用资源包支持的地域
| 资源包 | 地域 |
| --- | --- |
| 标准-本地冗余存储包 | 华东 1（杭州）、华东 2（上海）、华北 1（青岛）、华北 2（北京）、华北 3（张家口）、华北 5（呼和浩特）、华北 6（乌兰察布）、华南 1（深圳）、华南 2（河源）、华南 3（广州）、西南 1（成都）、华东 5（南京-本地地域-关停中）、华东 6（福州-本地地域-关停中）、华中 1（武汉-本地地域） |
| 低频-本地冗余存储包 |  |
| 归档-本地冗余存储包 |  |
| 冷归档-本地冗余存储包 |  |
| 标准-同城冗余存储包 |  |
| 低频-同城冗余存储包 |  |
| 归档-同城冗余存储包 |  |
| 下行流量包 |  |
| 回源流量包 |  |
| 请求包-标准存储 |  |
| 请求包-非标准存储 |  |
| OSS 加速器包 | 华东 1（杭州）、华东 2（上海）、华北 2（北京）、华北 6（乌兰察布）、华南 1（深圳） |
重要
华北3（张家口）地域当前不支持新建Bucket，但资源包仍可抵扣该地域已有Bucket的对应费用。
## 支持的操作
说明
“✓”表示资源包支持对应操作，“×”表示资源包不支持对应操作。
| 资源包 | [购买](purchase-resource-plans.md) | [换购](resource-pack-exchange-guide.md) ① | [升级](upgrade-resource-plans.md) | [续费](renew-resource-plans.md) | [叠加](purchase-resource-plans.md) ② | [明细](view-the-usage-details-of-a-resource-plan.md) | [预警](configure-alerts-for-resource-plans.md) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 标准-同城冗余存储包 | ✓ | × | ✓ | ✓ | ✓ | ✓ | × |
| 低频-同城冗余存储包 | ✓ | × | ✓ | ✓ | ✓ | ✓ | × |
| 归档-同城冗余存储包 | ✓ | × | ✓ | ✓ | ✓ | ✓ | × |
| 标准-本地冗余存储包 | ✓ | ✓ | ✓ | ✓ | × | ✓ | × |
| 低频-本地冗余存储包 | ✓ | × | ✓ | ✓ | × | ✓ | × |
| 归档-本地冗余存储包 | ✓ | × | ✓ | ✓ | × | ✓ | × |
| 冷归档-本地冗余存储包 | ✓ | × | ✓ | ✓ | ✓ | ✓ | × |
| 下行流量包 | ✓ | × | × | ✓ | ✓ | ✓ | ✓ |
| 回源流量包 | ✓ | × | × | × | ✓ | ✓ | ✓ |
| 传输加速包 | ✓ | × | × | × | ✓ | ✓ | ✓ |
| 请求包-标准存储类型 | ✓ | × | × | × | ✓ | ✓ | ✓ |
| 请求包-非标准存储类型 | ✓ | × | × | × | ✓ | ✓ | ✓ |
| 高防基础包 | ✓ | × | × | ✓ | ✓ | ✓ | × |
| OSS 加速器包 | ✓ | × | ✓ | ✓ | ✓ | ✓ | × |
①将已购买的资源包换购至OSS预留空间。
②购买多个相同类型的资源包。当您叠加购买多个相同类型的资源包时，优先抵扣先到期的资源包。例如，您2022年02月01日购买了规格为1 TB、时长为1年的中国内地通用下行流量包。另外，您在2022年03月01日购买了规格为1 TB、时长为3个月的中国内地通用下行流量包。此时，将优先抵扣2022年03月01日购买的下行流量包。
## 后续参考
[资源包购买指南](purchase-resource-plans.md)
[资源包换购指南](resource-pack-exchange-guide.md)
[资源包升级指南](upgrade-resource-plans.md)
[资源包续费指南](renew-resource-plans.md)
[资源包使用明细](view-the-usage-details-of-a-resource-plan.md)
[资源包预警设置](configure-alerts-for-resource-plans.md)
[资源包退款指南](refund-resource-plans.md)
[资源包](package-faq.md)
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
