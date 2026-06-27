# 云数据库Tair（兼容 Redis）的计费项和计费规则-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/product-overview/billable-items

# 计费项
创建云数据库 Tair（兼容 Redis）实例时，您需要根据实例的规格支付相应的费用。在实例运行过程中，如果备份文件超过免费额度、开通了审计日志功能或升级了实例的带宽，也会产生相应的费用。
云数据库 Tair（兼容 Redis）的计费组成如下。
| 计费项 | 说明 |
| --- | --- |
| [实例规格费用](billable-items.md) | [创建实例](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md) 时，根据实例规格和购买时长产生费用，支持包年包月、按量付费的计费方式。 按量付费实例推荐搭配资源包，降低成本。 更多关于计费方式的信息，请参见 [计费方式](billing-methods.md) 。 说明 该项费用中包含磁盘费用，磁盘费用不可调整，磁盘用于系统运行，例如存储日志、备份临时文件、AOF 文件等。 |
| [其他费用](billable-items.md) （非必须） | 备份费用：当备份文件用量超过免费额度后，超出部分将按量收费。 审计日志：开通后，将根据审计日志占用的存储空间和保存时间，按小时出账。 带宽升级：系统将根据升级带宽的大小和使用时间，按小时出账。 |
## 实例规格费用
不同规格和地域的实例费用各不相同，具体价格信息请参见[售卖页](https://common-buy.aliyun.com/?commodityCode=kvstore_prepaid_public_cn&regionId=cn-hangzhou)。
## 其他费用
### 备份费用
云数据库 Tair（兼容 Redis）为每个实例提供了免费的备份存储额度，当备份文件超过免费额度后，超出的部分将按量计费。
免费额度 = 实例规格默认内存大小（Tair[磁盘型](essd-based-instances-1.md)以磁盘存储空间为准）
当备份文件超出免费额度后，将以约0.0075元/GB/天进行按量计费，不同地域略有浮动，具体单价以实际账单为准。
### 审计日志存储空间与带宽升级费用
审计日志所使用的存储空间按小时出账，并按出账时占用的存储空间计费。例如华东1（杭州）的实例使用了100 GB的存储空间，则一小时产生的费用为0.8元。
实例升级的带宽按小时出账。例如：华东1（杭州）地域中的某个实例，手动增加带宽10 MB/s，则1小时产生的费用为0.014（元）* 10（MB）= 0.14元。
重要
实际价格以产品购买页面为准。
| 地区 | 地域 | Region ID（API 使用） | 审计日志存储单价（ 元 /GB/小时） | 带宽单价（ 元 /MB/小时） |
| --- | --- | --- | --- | --- |
| 亚太 | 华东 1（杭州） | cn-hangzhou | 0.008 | 0.014 |
| 华东 2（上海） | cn-shanghai | 0.008 | 0.014 |  |
| 华东 5（南京-本地地域） | cn-nanjing | 0.008 | 0.014 |  |
| 华东 6（福州-本地地域） | cn-fuzhou | 0.008 | 0.014 |  |
| 华北 1（青岛） | cn-qingdao | 0.008 | 0.014 |  |
| 华北 2（北京） | cn-beijing | 0.008 | 0.014 |  |
| 华北 3（张家口） | cn-zhangjiakou | 0.008 | 0.014 |  |
| 华北 5（呼和浩特） | cn-huhehaote | 0.008 | 0.014 |  |
| 华北 6（乌兰察布） | cn-wulanchabu | 0.008 | 0.014 |  |
| 华南 1（深圳） | cn-shenzhen | 0.008 | 0.014 |  |
| 华南 2（河源） | cn-heyuan | 0.008 | 0.014 |  |
| 华南 3（广州） | cn-guangzhou | 0.008 | 0.014 |  |
| 华中 1（武汉-本地地域） | cn-wuhan-lr | 0.008 | 0.014 |  |
| 西南 1（成都） | cn-chengdu | 0.008 | 0.014 |  |
| 中国（香港） | cn-hongkong | 0.018 | 0.017 |  |
| 新加坡 | ap-southeast-1 | 0.018 | 0.017 |  |
| 马来西亚（吉隆坡） | ap-southeast-3 | 0.0122 | 0.017 |  |
| 印度尼西亚（雅加达） | ap-southeast-5 | 0.0122 | 0.017 |  |
| 菲律宾（马尼拉） | ap-southeast-6 | 0.0122 | 0.017 |  |
| 泰国（曼谷） | ap-southeast-7 | 0.0122 | 0.017 |  |
| 日本（东京） | ap-northeast-1 | 0.0122 | 0.017 |  |
| 韩国（首尔） | ap-northeast-2 | 0.0122 | 0.017 |  |
| 欧洲与美洲 | 德国（法兰克福） | eu-central-1 | 0.018 | 0.017 |
| 英国（伦敦） | eu-west-1 | 0.018 | 0.017 |  |
| 美国（硅谷） | us-west-1 | 0.018 | 0.017 |  |
| 美国（弗吉尼亚） | us-east-1 | 0.018 | 0.017 |  |
| 中东 | 阿联酋（迪拜） | me-east-1 | 0.018 | 0.017 |
| 沙特（利雅得） | me-central-1 | 0.0122 | 0.017 |  |
## 常见问题
Q：实例是否会产生流量费用？
A：在实例默认带宽内不会收费。当使用专有网络（VPC）时，流量是免费，即在云服务器ECS或其他服务与Tair之间进行的数据传输是免费的。若申请公网地址，后续产生的公网流量同样不收费。但如果实例的带宽成为瓶颈并且需要更多流量，您可以额外购买带宽包以进行带宽升级。
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
