# 抢占式实例如何计费-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/spot-instance

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 抢占式实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

抢占式实例采用先使用后付费，市场价格根据供需关系实时变化，相对于按量付费最高能节约90%的成本。

## 计费项

抢占式实例的计费项仅包含实例规格，不包含镜像、云盘、公网带宽（按固定带宽）、快照等。

## 计费规则

### 计费公式

- 

计费时长：从成功创建到释放抢占式实例的时长。

- 

市场价格：指的是实例规格的价格，不包括云盘、公网带宽等资源的价格。

- 

出价：是您愿意为所选购的抢占式实例支付的最高价格。

说明

出价并非实例的实际计费价格，实际计费是以市场价格来计算。

- 

- 

- 

- 

| 实例使用时长设置 | 设定实例使用 1 小时 | 无确定使用时长 |
| --- | --- | --- |
| 计费示意图 |  |  |
| 说明 | 阿里云会保障实例在创建后 1 小时内不会被自动释放；超过 1 小时后，系统实时比较出价与市场价格、检查资源库存，来决定实例的持有和回收。 | 实例在创建后的运行时长没有保障，系统会立即实时比较出价与市场价格、检查资源库存，来决定实例的持有和回收。 |
| 实例计费价格 | 计费时长≤1 小时：成交时的市场价格 计费时长>1 小时：各时段的市场价格 | 各时段的市场价格 |
| 计费公式 | 计费时长≤1 小时：成交时的市场价格*计费时长 计费时长>1 小时：成交时的市场价格*1 小时+∑（各时段市场价格*各时段市场价格的计费时长） | ∑（各时段市场价格*各时段市场价格的计费时长） |


说明

相同实例规格的情况下，无确定使用时长在市场价格上会比设定实例使用1小时的抢占式实例优惠一些，与是否超过设定使用时长无关。

### 计费周期

按秒计算费用，按整点小时区间产生一条消费明细。

## 计费示例

说明

市场价格随供需变动，变动的时间周期不定，以下仅为示例。

- 

- 

- 

- 

- 

|  | 场景 1：设定实例使用 1 小时 假设您在 9:40 出价（设置单台上限价）6 元/小时，以 5 元/小时的市场价格成功竞得了一台抢占式实例， 设定实例使用 1 小时 ，实例在 11:00 时由于出价小于市场价格被通知中断回收并在 5 分钟后释放。 费用计算 说明 抢占式实例根据实际使用时长 按秒级 来累计计算费用，小时价格除以 3600 即可得到每秒的价格。 实际使用时长为 5100 秒（9:40~11:05），超过 1 小时，1 小时内的计费价格为成交时市场价格，即 5 元/小时；1 小时后，中断回收前计费价格为各时段市场价格。实际产生费用如下： 使用 1 小时 费用 = 成交时的市场价格 * 计费时长 9:40~10:40（成交时市场价格 5 元/小时、使用 3600 秒）：（5/3600）*3600=5 元。 使用 1 小时后 费用 = ∑（各时段市场价格*各时段市场价格的计费时长） 10:40~11:00（市场价格 6 元/小时、使用 1200 秒）：（6/3600）*1200=2 元。 11:00~11:05（市场价格 8 元/小时、使用 300 秒）：（8/3600）*300=0.67 元。 总费用 = 5 + 2 + 0.67 = 7.67 元。 |
| --- | --- |
|  | 场景 2：设定无确定使用时长 假设您在 9:40 出价跟随市场价格（使用自动出价），以 4 元/小时的市场价格成功竞得了一台抢占式实例， 设定无确定使用时长 ，实例在 11:00 时由于库存不足被通知中断回收并在 5 分钟后释放。 费用计算 说明 抢占式实例根据实际使用时长 按秒级 来累计计算费用，小时价格除以 3600 即可得到每秒的价格。 实际使用时长为 5100 秒（9:40~11:05），计费价格为各时段市场价格。实际产生费用如下： 计费时长内费用 = ∑（各时段市场价格*各时段市场价格的计费时长） 9:40~10:00（市场价格 4 元/小时、使用 1200 秒）：（4/3600）*1200=1.33 元。 10:00~11:00（市场价格 5 元/小时、使用 3600 秒）：（5/3600）*3600=5 元。 11:00~11:05（市场价格 6 元/小时、使用 300 秒）：（6/3600）*300=0.5 元。 总费用 = 1.33 + 5 + 0.5 = 6.83 元。 |


## 账单查询

请参见[查看抢占式实例账单](products/ecs/documents/view-billing-details.md)。

## 欠费说明

如果账号内存在欠费账单，您无法正常使用抢占式实例资源。欠费会导致ECS实例停机，甚至释放资源。请尽快充值结清欠费账单，避免因资源的停机或释放而影响业务。

## 相关文档

- 

[什么是抢占式实例](products/ecs/documents/user-guide/what-is-a-spot-instance.md)

- 

[创建抢占式实例](products/ecs/documents/user-guide/create-a-spot-instance.md)

- 

[抢占式实例最佳实践](products/ecs/documents/use-cases/best-practices-for-preemptible-instances.md)

[上一篇：按量付费](products/ecs/documents/pay-as-you-go-1.md)[下一篇：节省计划](products/ecs/documents/savings-plans-1.md)

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
