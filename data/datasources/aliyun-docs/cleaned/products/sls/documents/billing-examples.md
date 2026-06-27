# 不同计费方式的费用计算案例-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/billing-examples

# 计费案例
本文介绍日志服务计费案例。
## 按量付费方式
### 按使用功能计费模式案例
案例1
（免费使用日志服务）假设您有1台服务器，每天产生10 MB日志，您希望通过日志服务（Shard数量为1个，保存时间为1天）分析每天的日志，并通过Java程序实时订阅。假设本案例中的上传压缩率为20%。具体明细如下表所示。
| 计费项 | 说明 | 月计量 | 月计费 |
| --- | --- | --- | --- |
| 活跃 Shard 租用 | 只创建 1 个 LogStore 且只使用 1 个 Shard，则当月活跃 Shard 租用量为 31 个*天。 | 31 个*天 | 免费 |
| 读写流量 | 上传日志时的网络流量：10 MB/天×20%×31 天=62 MB 通过 Java 订阅日志时的网络流量：10 MB/天×20%×31 天=62 MB | 124 MB | 免费 |
| 存储空间-日志存储 | 日志存储量：10 MB/天×20%×31 天=62 MB 被构建索引的日志存储量：10 MB/天×31 天=310 MB | 372 MB | 免费 |
| 索引流量-日志索引 | 开启全文索引，每天产生 10 MB 索引流量，则当月索引流量为 310 MB。 | 310 MB | 免费 |
| 读写次数 | 批量上传日志到日志服务的次数。 | 少于 100 万次 | 免费 |
案例2
A网站的访问日志平均为200 Byte/条，1天共1亿条日志，即每天日志量约为18.6 GB。目前A网站通过日志服务（Shard数量为2个，保存时间为3天）分析网站运营情况。假设本案例中的上传压缩率为20%且不计免费额度。
1天的费用为8.68794元，具体明细如下表所示。
| 计费项 | 说明 | 日计量 | 单价 | 日计费 |
| --- | --- | --- | --- | --- |
| 读写流量 | 上传日志到日志服务的网络流量为 18.6 GB×20%=3.72 GB。 | 3.72 GB | 0.180 元/GB/天 | 0.6696 元 |
| 索引流量-日志索引 | 开启全文索引，产生 20 GB 索引流量，其中 1.4 GB 为保留字段的索引流量。 | 20 GB | 0.350 元/GB/天 | 7 元 |
| 存储空间-日志存储 | 日志存储量：每天上传 18.6 GB，保存 3 天后的日存储量为 18.6 GB/天×20%×3 天=11.16 GB。 被构建索引的日志存储量：每天为 20 GB，保存 3 天后的总存储量为 20 GB/天×3 天=60 GB。 | 71.16 GB | 0.0115 元/GB/天 | 0.81834 元 |
| 读写次数 | 批量上传日志到日志服务，约 100 万次请求。 | 100 万次 | 0.12 元/百万次/天 | 0.12 元 |
| 活跃 Shard 租用 | 业务峰值流量为 6 MB/s，需配置 2 个 Shard。 | 2 个 | 0.04 元/个/天 | 0.08 元 |
案例3
B应用1天内产生10 GB时序数据，并通过20万次请求上传至日志服务（Shard数量为2个，保存时间为3天）。假设本案例中的上传压缩率为20%且不计免费额度。
1天的费用为2.59元，具体明细如下表所示。
| 计费项 | 说明 | 日计量 | 单价 | 日计费 |
| --- | --- | --- | --- | --- |
| 读写流量 | 上传时序数据到日志服务的网络流量为 10 GB×20%=2 GB。 | 2 GB | 0.180 元/GB/天 | 0.36 元 |
| 索引流量-时序流量 | 日志服务自动配置所有字段的索引。 | 10 GB | 0.200 元/GB/天 | 2 元 |
| 存储空间-时序存储 | 时序数据存储量：每天上传 10 GB，保存 3 天后的平均存储量为 10 GB/天×20%×3 天=6 GB。 被构建索引的时序数据存储量：每天为 10 GB，保存 3 天后的平均存储量为 10 GB/天×3 天=30 GB。 | 36 GB | 0.0035 元/GB/天 | 0.126 元 |
| 活跃 Shard 租用 | 业务峰值流量为 6 MB/s，需配置 2 个 Shard。 | 2 个 | 0.04 元/个/天 | 0.08 元 |
| 读写次数 | 批量上传时序数据到日志服务，约 20 万次请求。 | 20 万次 | 0.12 元/百万次/天 | 0.024 元 |
案例4
A公司在日志服务上存储了400亿条日志，并在执行查询和分析操作时，开启了SQL独享版功能。单次查询和分析费用说明如下：
说明
本案例仅针对SQL独享版计费项，不对其他计费项进行说明。
| 计费项 | 说明 | 单次计量 | 单价 | 单次计费 |
| --- | --- | --- | --- | --- |
| SQL 独享版 | 单次查询和分析操作消耗的 CPU 时间为 3.6 秒。如何获取 CPU 时间，请参见 [获取](dedicated-sql.md) [CPU](dedicated-sql.md) [时间](dedicated-sql.md) 。 | 3.6 秒/3600=0.001 小时 | 0.35 元/核*小时 | 0.00035 元 |
### 按写入数据量计费案例
案例1
A客户写入数据量1天10 TB，数据保存30天，同时使用到了数据加工、查询分析、定时SQL、智能告警、数据投递等功能，具体明细如下表所示：
| 计费项 | 说明 | 日计量 | 单价 | 日计费 |
| --- | --- | --- | --- | --- |
| 原始写入数据量 | 上传日志至日志服务，写入数据量为 10 TB。 | 10 TB | 0.4 元/GB | 4000 元 |
| 日志存储 | 数据存储时长为 30 天。 | 按写入数据量计费方式在数据写入后 30 天内享受免费存储权益，无费用产生。 | 热存储： 0.0115 元/GB/天 低频存储： 0.005 元/GB/天 | 0 元 |
案例2
B客户写入数据量1天10 TB，产生5 TB存储，数据保存31天，超过30天数据存储在低频存储数据层，同时使用到了数据加工、查询分析、定时SQL、智能告警、数据投递等功能。具体明细如下表所示：
| 计费项 | 说明 | 日计量 | 单价 | 日计费 |
| --- | --- | --- | --- | --- |
| 原始写入数据量 | 上传日志至日志服务，写入数据量为 10 TB。 | 10 TB | 0.4 元/GB | 4000 元 |
| 日志存储 | 数据存储时长为 31 天，存储量为 5 TB。 | 按写入数据量计费方式在数据写入后 30 天内享受免费存储权益，无费用产生。 第 31 天产生数据低频存储费用，存储量为 5 TB。 | 低频存储： 0.005 元/GB/天 | 25.6 元 |
## 资源包方式
如下计费以公共云版本的资源包为例。
某客户每天的日志服务的使用量为2个Shard、100 GB读写流量、400 GB索引流量、存储数据稳定在10000 GB。具体费用如下：
| 计费项 | 说明 |
| --- | --- |
| 读写流量 | 100 GB×0.18 元/GB=18 元 |
| 索引流量-日志索引 | 400 GB×0.35 元/GB=140 元 |
| 存储空间-日志存储 | 10000 GB×0.0115 元/GB/天=115 元/天 |
| 活跃 Shard 租用 | 2 个*0.04 元=0.08 元 说明 当您在创建 LogStore 时配置 Shard 数目 为 2 时，表示您每天租用 2 个 Shard，每月（按 30 天计算）使用量为 60 Shard*天。 |
说明
资源包价格以控制台实际优惠价格为准。
| 计费周期 | 按量付费 | 一年期包月计划 | 节省费用 |
| --- | --- | --- | --- |
| 每月费用 | （18+140+115+0.08）元*30 天=8192.4 元 | 购买 8 个 1000 CU/月和 2 个 100 CU/月的一年期资源包，详细费用说明如下： 8*8520 元/12 个月+2*900 元/12 个月=5830 元 | 如果您购买一年期的资源包，则相比按量付费，每月可节省的费用：8192.4 元-5830 元=2362.4 元 |
| 一年总费用 | （18+140+115+0.08）元*30 天*12 个月=98308.8 元 | 购买 8 个 1,000 CU/月和 2 个 100 CU/月的一年期资源包，详细费用说明如下： 8*8520 元+2*900 元=69960 元 | 如果您购买一年期的资源包，则相比按量付费，每年可节省的费用：98308.8 元-69960 元=28348.8 元 |
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
