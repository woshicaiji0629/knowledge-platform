# 基础服务计费方式定价规则-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/product-overview/billing-rules-of-basic-services

# 基础服务计费
阿里云CDN的基础服务支持按流量计费、按带宽峰值计费和月结95带宽峰值计费，您可以根据实际业务场景选择合适的计费方式。通过本文您可以详细了解CDN基础服务的计费方式和注意事项。
说明
无特别说明的情况下，CDN的按流量计费、按带宽峰值计费和月结95带宽峰值计费，都是指在CDN的L1节点上产生的下行流量带宽。
## 注意事项
CDN服务计费的流量比日志中记录的流量多。因为CDN日志中记录的流量数据是应用层日志统计出的流量，但是实际网络请求中存在TCP/IP包头的消耗和TCP重传，因此实际产生的网络流量比应用层统计到的流量要高。详细信息，请参见[为什么监控查询流量、用量查询流量与日志统计流量有差异？](traffic-amount-in-the-monitoring-and-usage-analytics-or-in-the-usage-statistics-feature-different-from-the-logged-traffic-amount.md)。
如果您的CDN服务月消费金额大于10万元，阿里云CDN可以为您提供更灵活优惠的按月计费方式。请联系您的阿里云客户经理或通过阿里云[其它渠道](https://help.aliyun.com/zh/document_detail/464625.html#task-2155749)咨询洽谈。
如果您的CDN服务月消费金额不足10万元，或者流量波形不符合按月计费模式的使用要求（例如：月95计费模式不能用于存在异常突发带宽的场景下使用），阿里云CDN保留将月计费模式切换为按流量计费的权利。
阿里云CDN出账时间通常在当前计费周期结束后3~4小时左右，具体以系统实际出账时间为准。
## 按流量计费（默认）
| 适用场景 | 计费规则 |
| --- | --- |
| 适用于流量曲线波动较大，有带宽尖峰，全天带宽利用率小于 30%的用户。 | 计费说明 ：按照每月从阿里云 CDN 节点流出的实际流量阶梯计费。 计费项 ：流量。 付费方式 ：按量后付费或 [资源包预付费](https://common-buy.aliyun.com/?spm=5176.7933777.J_3537169050.2.2429496ezmVFeY&commodityCode=dcdnpaybag#/buy) 。 出账周期 ：按小时结算，账单出账时间通常在当前计费周期结束后 3~4 小时左右，具体以系统实际出账时间为准。 |
计费示例
按流量计费的官网报价：
说明
以下仅为示例，实际价格以[官网报价](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.7.1e5b3a30Sj5ONL#/cdn/detail)为准。
| 流量阶梯（计费单位：元/GB） | 中国内地-CN | 北美-NA | 欧洲-EU | 亚太 1 区-AP1 | 亚太 2 区-AP2 | 亚太 3 区-AP3 | 中东、非洲-MEAA | 南美-SA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0GB-10TB（含） | 0.24 | 0.46 | 0.46 | 0.58 | 0.78 | 0.69 | 1.31 | 1.31 |
| 10TB-50TB（含） | 0.23 | 0.46 | 0.46 | 0.58 | 0.78 | 0.69 | 1.31 | 1.31 |
| 50TB-100TB（含） | 0.21 | 0.39 | 0.39 | 0.45 | 0.67 | 0.60 | 1.18 | 1.18 |
| 100TB-1PB（含） | 0.18 | 0.20 | 0.20 | 0.38 | 0.57 | 0.51 | 0.98 | 0.92 |
| 大于 1PB | 0.15 | 0.16 | 0.16 | 0.35 | 0.52 | 0.46 | 0.92 | 0.85 |
示例场景（以中国内地的流量费用为例）：
03月01日00:00:00至03月09日23:59:59累计消耗的流量为10200 GB，03月10日00:00:00至01:00:00消耗的流量为90 GB，月累计消耗流量为10290 GB。10日00:00:00至01:00:00使用的90 GB中，有40 GB落在0 GB~10 TB阶梯内，单价为0.24元/GB，剩下的50 GB在10 TB~50 TB阶梯内，单价为0.23元/GB。
账单计算：
说明
10 TB=10240 GB。
03月01日00:00:00-03月09日23:59:59的账单金额为：10200 GB×0.24元/GB=2448元。
03月10日00:00:00-01:00:00的账单金额为：40 GB×0.24元/GB+50 GB×0.23元/GB=21.1元。
03月01日00:00:00-03月10日01:00:00的账单总金额为：（10200 GB+40 GB）×0.24元/GB+50 GB×0.23元/GB=2469.1元。
## 按带宽峰值计费
重要
按带宽峰值计费方式请联系您的阿里云客户经理或通过阿里云[其它渠道](https://help.aliyun.com/zh/document_detail/464625.html#task-2155749)咨询，且需满足近30天内的带宽峰值超过5 Gbps。
| 适用场景 | 计费规则 |
| --- | --- |
| 适用于流量曲线比较平稳，全天带宽利用率大于 30%的用户。 | 计费说明 ：按照每日的带宽峰值计费。每 5 分钟统计一个带宽数据，每日得到 288 个值，取其中的最大值。 计费项 ：峰值带宽。 付费方式 ：按量后付费。 出账周期 ：按日计费，每日零点后出前一日账单并扣费，具体出账时间以系统为准。 |
计费示例
按峰值带宽计费的报价：
说明
仅为示例，实际价格以[官网报价](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.7.1e5b3a30Sj5ONL#/cdn/detail)为准。
| 流量阶梯（计费单位：元/Mbps/天） | 中国内地-CN | 北美-NA | 欧洲-EU | 亚太 1 区-AP1 | 亚太 2 区-AP2 | 亚太 3 区-AP3 | 中东、非洲-MEAA | 南美-SA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0-500Mbps（含） | 0.6 | 1.64 | 1.64 | 2.86 | 3.81 | 3.94 | 5.91 | 5.32 |
| 500Mbps-5Gbps（含） | 0.58 | 1.51 | 1.51 | 2.52 | 3.43 | 3.76 | 5.77 | 5.18 |
| 5Gbps-20Gbps（含） | 0.56 | 1.38 | 1.38 | 2.21 | 3.05 | 3.47 | 5.64 | 5.05 |
| 大于 20Gbps | 0.54 | 1.31 | 1.31 | 1.91 | 2.67 | 3.17 | 5.58 | 4.99 |
场景示例及账单计算（以中国内地的峰值带宽费用为例）：
2020年03月09日，用户A在中国内地的峰值带宽为400 Mbps，带宽费用=400 Mbps×0.6元/Mbps/天=240元。
2020年03月10日，用户A在中国内地的峰值带宽为1 Gbps，带宽费用=1000 Mbps×0.58元/Mbps/天=580元。
## 月结95带宽峰值计费
说明
月结95带宽峰值计费方式请联系您的阿里云客户经理或通过阿里云[其它渠道](https://help.aliyun.com/zh/document_detail/464625.html#task-2155749)咨询申请。
| 适用场景 | 计费规则 |
| --- | --- |
| 适用于流量较大，且无法预期流量峰值或月消费金额大于 10 万元的用户。 | 计费说明 ：以每 5 分钟的下行带宽作为计量点，每天统计 288 个（（60/5）*24）计量点，每月计量点个数 N=288*（当月计费天数）。对所有计量点按照带宽大小进行降序排序，并且按照带宽由大到小扣除 M（M=N*0.05，如果有出现小数点的情况，则去掉小数点后的数值以后取整）个点，则第 M+1 个点的带宽值即为当月的 95 计费带宽。 举例 1：3 月份有 31 天，总计费点数为 288*31=8928，将 8928 个点按带宽降序排列后，扣除的点数为 8928*0.05=446.4，去掉小数点取整=446，则第 447 个点为当月 95 带宽。 举例 2：4 月份有 30 天，总计费点数为 288*30=8640，将 8640 个点按带宽降序排列后，扣除的点数为 8640*0.05=432，则第 433 个点为当月 95 带宽。 举例 3：2 月份是 29 天的情况下，总计费点数为 288*29=8352，将 8352 个点按带宽降序排列后，扣除的点数为 8352*0.05=417.6，去掉小数点取整=417，则第 418 个点为当月 95 带宽。 举例 4：2 月份是 28 天的情况下，总计费点数为 288*28=8064，将 8064 个点按带宽降序排列后，扣除的点数为 8064*0.05=403.2，去掉小数点取整=403，则第 404 个点为当月 95 带宽。 计费项 ：月结 95 带宽峰值。 付费方式 ：按量后付费。 计算方式 ： 最终费用为各个分区的月结 95 带宽费用之和。 某个分区的月结 95 带宽费=所在分区的月结 95 带宽值×所在分区的月结 95 带宽单价×有效因子。 说明 有效因子 ：有效因子=当月有效天数/当月总天数。例如，2021 年 04 月，月总天数为 30 天，账期有效天数为 26 天，则有效因子为 26÷30=0.86666667。 有效天数 ：95 计费生效日开始到当月月末的间隔天数。例如，2021-04-05 为 95 计费生效时间，则 2021 年 04 月的有效天数为 26。 出账周期 ：当前计费周期结束的下个自然月 1 日的凌晨。 例如：2021 年 03 月 01 日会生成 2 月份完整月（2021-02-01 00:00:00 至 2021-02-28 23:59:59）的计费账单。 说明 账单生成后会自动从您的账户余额中扣除相应费用以结算账单，请您确保结算时账户余额充足，避免因欠费导致 CDN 停服。欠费规则，请参见 [欠费说明](overdue-payments.md) 。 您查看 95 带宽峰值用量，预估本月 95 带宽消费金额。详细信息，请参见 [用量概述](../user-guide/resource-usage-overview.md) 。 |
计费示例
示例场景：
以1个月30天为例，假设当月的有效天数为26天，用户当月的中国内地月结95带宽值为900 Mbps，带宽单价为15 元/Mbps/月（不是实际价格，实际单价请以阿里云商务提供的价格为准），其他国家及地区峰值为0 Mbps。
说明
月结95带宽峰值的具体带宽单价，请联系您的阿里云客户经理或通过阿里云[其它渠道](https://help.aliyun.com/zh/document_detail/464625.html#task-2155749)咨询。
账单计算：
中国内地的月结95带宽费用：所在分区的月结95带宽值（900 Mbps ）×所在分区的月结95带宽单价（15 元/Mbps/月）×有效因子（26÷30）=11700元。
其他国家及地区的月结95带宽费用：0元。
总的月结95带宽费用：11700元（中国内地区域月结95带宽费用）+0元（其他国家及地区月结95带宽费用）=11700元。
## 突发带宽说明
因为业务增长、资源被盗刷或被攻击等原因，加速域名可能会产生突发带宽，符合以下情况之一的都属于突发带宽。
带宽计费，单账户符合以下情况之一的都属于突发带宽：
本自然月CDN总带宽比上个自然月的总带宽超出500 Gbps。
上个自然月带宽峰值为0，本自然月CDN总带宽增量超过200 Gbps。
本自然月CDN总带宽峰值增量超出上月计费带宽的30%。
流量计费：单个加速域名，本自然月的带宽峰值超过10Gbps。
如果另有约定，以实际约定为准。
如果您对CDN服务有突发带宽使用需求，您需提前至少3个工作日（重大节日的突发，包括但不限于春晚、双十一等，需要提前至少1个月申请）联系阿里云申请突发带宽用量。申请成功后且在双方约定的突发量级内，阿里云可确保您的服务不受影响；如果申请失败或未申请，对于突发带宽阿里云有权采取限流等措施来保障全网用户的稳定性，由此导致的可用性问题，阿里云不承担责任。
如果您需申请突发带宽用量，请联系您的阿里云客户经理或通过阿里云[其它渠道](https://help.aliyun.com/zh/document_detail/464625.html#task-2155749)咨询洽谈。申请成功后阿里云将按照与您重新商定的价格标准进行计费；如果申请失败或未申请，阿里云将按照您当前的价格标准进行计费，详细费用最终以CDN账单为准。
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
