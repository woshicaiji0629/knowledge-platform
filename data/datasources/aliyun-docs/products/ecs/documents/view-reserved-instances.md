# 查看预留实例券使用明细、使用情况-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/view-reserved-instances

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

# 查看预留实例券

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

购买预留实例券后，您可以查看预留实例券支持抵扣的实例、计算力因子等信息，帮您判断预留实例券的匹配情况。通过查看预留实例券的账单明细以及使用率、覆盖率，您可以判断预留实例券的使用情况。

## 查看可抵扣的实例

购买预留实例券后，您可以通过抵扣预测功能帮您判断该预留实例券可以匹配哪些已购买的按量付费实例。

- 

访问[ECS](https://ecs.console.aliyun.com/reservedInstance/region)[控制台-预留实例券](https://ecs.console.aliyun.com/reservedInstance/region)。

- 

在预留实例券列表右上方，单击抵扣预测。

- 

选择预留实例券所属的地域/可用区。

- 

找到预留实例券，在预留实例券列表右侧单击查看可能抵扣的实例。

说明

- 

通过抵扣预测功能查看到的实例仅代表实例符合匹配要求，并不代表一定抵扣这些实例的账单，实际抵扣情况以账单为准。

- 

如果按量付费实例是通过E-MapReduce（EMR）、容器服务Kubernetes版（ACK）或弹性容器实例ECI创建的，则抵扣预测不能显示这些实例，但不影响实际的抵扣效果。

## 查看计算力因子

计算力因子代表了实例计算力的强弱，通常取决于vCPU数量。一张预留实例券的计算力 = 实例规格的计算力因子 * 预留实例券的实例数量。

查看预留实例券的计算力有以下作用：

- 

在拆分、合并预留实例券时，必须确保操作前后计算力相等，评估是否满足条件。

- 

在使用地域级预留实例券抵扣不同规格大小的按量付费实例时，评估预留实例券的使用情况。

- 

访问[ECS](https://ecs.console.aliyun.com/reservedInstance/region)[控制台-预留实例券](https://ecs.console.aliyun.com/reservedInstance/region)。

- 

在预留实例券列表右上方，单击查看计算力因子表。

- 

按规格族筛选，查看各实例规格的计算力因子。

您也可以单击下载将计算力因子表保存到本地，方便日后离线查看。

## 查看使用明细

您可以通过查看预留实例券的账单详情，了解预留实例券对按量付费实例的抵扣情况。

- 

访问[ECS](https://ecs.console.aliyun.com/reservedInstance/region)[控制台-预留实例券](https://ecs.console.aliyun.com/reservedInstance/region)。

- 

在预留实例券列表的操作列，单击查看账单。

说明

您也可以在预留实例券列表右上方，单击查看使用明细，查看当前地域下所有预留实例券的抵扣明细。

- 

在使用明细页签下查看当前预留实例券的抵扣明细，例如抵扣系数、抵扣账号以及被抵扣的实例等。

使用明细页面支持按消费开始时间、账号、实例名称、抵扣实例ID、抵扣商品账期筛选数据。明细表格还包含抵扣前剩余量、抵扣量、抵扣后剩余量、抵扣商品、抵扣计费项、实例原始用量、消费开始时间和消费结束时间等字段。

## 查看使用情况

您可以通过查看预留实例券的使用率判断预留实例券是否存在浪费，通过覆盖率判断预留实例券是否有效降低资源使用成本，并根据使用率和覆盖率优化预留实例券。

- 

使用率是指购买预留实例券后有多少比例参与了抵扣，使用率越大越说明预留实例券的使用效果越佳。

- 

覆盖率可以了解预留实例券在总体实例使用量中所覆盖的比例，覆盖率越大越说明预留实例券有效地帮助您降低了成本。

- 

访问[ECS](https://ecs.console.aliyun.com/reservedInstance/region)[控制台-预留实例券](https://ecs.console.aliyun.com/reservedInstance/region)。

- 

在预留实例券列表的操作列，单击查看账单。

- 

分别在使用率概况和覆盖率概况页签下，查看当前预留实例券的使用率和覆盖率。

使用率

在预留实例券的使用率概况页签中，时间粒度设为天，时间范围为2024-10-22至2024-10-23。页面上方展示总按量实例成本、总资源购买费用、总节省金额、潜在总节省金额四个汇总指标。中部使用率折线图显示2024-10-22日使用率约20%后降至0%。底部表格列出各预留实例券详情，包含开始/结束时间、当前状态、地域、可用区、规格、资源数量、操作系统、使用率、抵扣量、资源总量、资源购买费用、按量成本基线值、节省净值、潜在节省净值等列。其中一个已失效的ecs.g6.large规格实例使用率仅为21.66%，表明该预留实例券存在资源浪费。

覆盖率

在覆盖率概况页签下，页面顶部显示汇总指标：综合覆盖率5.05%、总使用量64.32 算力*小时、总抵扣量3.25 算力*小时。可通过时间粒度（天/周/月）和时间范围筛选数据，覆盖率折线图展示所选周期内覆盖率的变化趋势。底部表格列出各按量实例的覆盖率详情，包含账号、产品名称、产品明细、按量实例ID、统计周期、地域、规格、覆盖率、抵扣量、总用量、账单金额等列。例如一台规格为ecs.g6.large的云服务器 ECS 按量实例，其覆盖率为 21.31%，抵扣量为 3.25 算力*小时，总用量为 15.25 算力*小时。覆盖率报表数据以 T+3 日之后查询为准。

## 相关文档

您可以调用API[DescribeReservedInstances](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describereservedinstances.md)接口查询您已经购买的预留实例券详细信息。

[上一篇：拆分、合并或修改预留实例券](products/ecs/documents/split-merge-or-modify-reserved-instances.md)[下一篇：资源保障](products/ecs/documents/resource-assurance-1.md)

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
