# 什么是弹性保障（EA）-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/overview-of-elasticity-assurance

# 弹性保障概述
当业务面临资源需求高峰需要创建按量付费实例时，可能因库存不足而创建失败。弹性保障（Elasticity Assurance, EA）通过预留专属私有池资源，为按量付费实例提供容量保障。
## 应用场景
| 需求场景 | 周期性资源需求 | 偶发性资源需求 | 高峰期资源需求 |
| --- | --- | --- | --- |
| 示意图 |  |  |  |
| 补充说明 | 适用于可预测的、周期性资源高峰。保障任务按时启动，平谷期不浪费资源。 | 为应对突发事件或流量洪峰预留资源，确保业务的快速响应和高可用性。 | 在双十一、春节等全网资源紧张期间，为核心业务提前预留资源，避免因资源争抢导致业务受损。 |
| 场景示例 | 月末财务对账、周末批量渲染、每日定时数据分析。 | 突发热点事件响应、应用扩容、在线业务容灾切换。 | 视频直播、电商大促、在线游戏开服、票务秒杀。 |
## 核心概念
购买弹性保障后，系统会在指定的可用区，预留匹配实例规格与数量的资源，形成一个[私有池](private-pools.md)。
公共池指所有用户共享的资源池。创建实例时，如果没有指定私有池，系统会默认从公共池中分配资源。
| 特性 | 专有私有池 | 开放私有池 |
| --- | --- | --- |
| 访问策略 | 严格绑定（强保障） ：仅使用专有私有池，若容量不足则创建失败。 | 优先 + 回退 ：优先使用开放私有池，若容量不足则自动尝试使用公共资源池。 |
| 资源隔离 | 为特定业务或场景预留，隔离性强。 | 可作为通用容量池，供多个业务场景共享使用。 |
| 使用方式 | 创建实例时使用 指定模式， 指定一个专有私有池。 | 创建实例时使用 指定模式， 指定一个开放私有池 。 创建实例时使用 开放模式 。 |
弹性保障-分时保障：在指定周期内（如30天）按预设时段（如每天18:00~24:00）预留资源。
弹性保障：在整个指定周期内（如3个月）持续、不间断地预留资源。
## 操作步骤
### 流程概述
购买弹性保障：购买弹性保障，获得一个私有池。
创建 ECS 实例：创建实例时，指定已购弹性保障的私有池。
验证与管理：查看私有池使用情况及关联实例。
### 弹性保障-分时保障
步骤一：购买弹性保障
访问[ECS](https://ecs.console.aliyun.com/elasticity-assurance/region/cn-hangzhou)[控制台-弹性保障](https://ecs.console.aliyun.com/elasticity-assurance/region/cn-hangzhou)。
单击创建弹性保障。
开始时间和结束时间间隔至少7天，最多365天。
重复规则：支持配置多条，最多10条。
支持按日/周/月重复周期设定保障时段，时间段最低4小时，累计保障时长不得低于整个周期总时长的10%。
鼠标悬浮保障时段(UTC)预览可查看保障时段详情。
资源池类型：
开放模式：开放私有池。
专有模式：为特定场景或业务预留的专有私有池。
勾选我已知悉，单击立即购买。
返回[ECS](https://ecs.console.aliyun.com/elasticity-assurance/region/cn-hangzhou)[控制台-弹性保障](https://ecs.console.aliyun.com/elasticity-assurance/region/cn-hangzhou)，当状态为资源已锁定或预定生效中时，表示购买成功。
步骤二：使用弹性保障创建实例
访问[ECS](https://ecs.console.aliyun.com/elasticity-assurance/region/cn-hangzhou)[控制台-弹性保障](https://ecs.console.aliyun.com/elasticity-assurance/region/cn-hangzhou)。
在资源预定页面，单击目标弹性保障操作列的购买实例。
付费类型选择按量付费，其他配置参考[自定义购买实例](create-an-instance-by-using-the-wizard.md)完成。
展开页面底部的高级选项，选择私有池类型。
开放：系统优先匹配开放私有池，若容量不足，则尝试使用公共池。
不使用：不使用私有池，仅使用公共池。
指定：指定一个匹配的开放或专有私有池。
单击确认下单。
步骤三：查看弹性保障信息
访问[ECS](https://ecs.console.aliyun.com/elasticity-assurance/region/cn-hangzhou)[控制台-弹性保障](https://ecs.console.aliyun.com/elasticity-assurance/region/cn-hangzhou)。
在弹性保障页面，单击弹性保障的ID，进入资源详情页查看私有池容量使用情况等信息。
在关联实例区域可查看使用该弹性保障创建的实例。
### 弹性保障
步骤一：购买弹性保障
访问[ECS](https://ecs.console.aliyun.com/resourceAssuranceV2/region)[控制台-资源管家](https://ecs.console.aliyun.com/resourceAssuranceV2/region)，选择购中确定性保障>资源预定。
在资源预定页签，单击创建资源预定，进入配置页面。
所需资源信息：选择需要预留资源的地域/可用区、资源规格和预留数量。
预定资源方式：
预定方式：选择弹性保障-立即生效/指定时间生效。
购买时长：支持按月或按年购买，时长从1个月到5年不等。
私有资源池信息：
开放：开放私有池。
专有：为特定场景或业务预留的专有私有池。
资源方案推荐：
系统会基于库存优先、多可用区容灾、性能优先等维度提供更多推荐方案，最终以选定方案预留资源。
对比表格列出原方案、库存优先/性能优先和多可用区冗灾三行方案，各列包括规格名称、地域/可用区、台数、参考价格、vCPU、内存、内网带宽等指标，单击目标方案前的单选按钮即可选定。
单击下一步：确认信息，核对配置。
阅读预定须知，勾选我已确认，单击创建预定单。
返回列表页，当状态显示为预定生效中时，表示已购买成功。
步骤二：使用弹性保障创建实例
访问[ECS](https://ecs.console.aliyun.com/resourceAssuranceV2/region)[控制台-资源管家](https://ecs.console.aliyun.com/resourceAssuranceV2/region)，选择购中确定性保障>资源预定。
在资源预定页面，单击目标资源预定操作列的购买实例。
付费类型选择按量付费，其余配置参考[自定义购买实例](create-an-instance-by-using-the-wizard.md)完成。
在高级选项（选填）区域，选择私有池类型。
开放：系统优先匹配开放私有池，若容量不足，则尝试使用公共池。
不使用：不使用任何私有池，仅使用公共池。
指定：指定一个开放私有池或者专有私有池。
步骤三：查看弹性保障信息
访问[ECS](https://ecs.console.aliyun.com/resourceAssuranceV2/region)[控制台-资源管家](https://ecs.console.aliyun.com/resourceAssuranceV2/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
在资源管家左侧导航栏，选择购中确定性保障>资源预定。
在资源预定页签下，筛选预定方式为弹性保障。
在筛选出的弹性保障列表中，单击弹性保障的ID，进入资源详情页查看私有池容量使用情况等信息。
在关联实例区域可查看使用该弹性保障创建的实例。
### API
步骤一：创建和购买弹性保障
调用[CreateElasticityAssurance](../developer-reference/api-ecs-2014-05-26-createelasticityassurance.md)接口创建弹性保障或者弹性保障-分时保障。
调用[PurchaseElasticityAssurance](../developer-reference/api-ecs-2014-05-26-purchaseelasticityassurance.md)接口购买一个准备完毕且处于未激活状态的弹性保障服务。
步骤二：使用弹性保障创建实例
调用[RunInstances](../developer-reference/api-ecs-2014-05-26-runinstances.md)接口创建实例。
通过PrivatePoolOptions.MatchCriteria指定私有池类型。若私有池类型选择指定模式（Target），必须通过PrivatePoolOptions.Id设置目标私有池ID。
步骤三：查看和修改弹性保障
查询
调用[DescribeElasticityAssurances](../developer-reference/api-ecs-2014-05-26-describeelasticityassurances.md)接口查询弹性保障服务的详细信息。
调用[DescribeElasticityAssuranceInstances](../developer-reference/api-ecs-2014-05-26-describeelasticityassuranceinstances.md)接口查询弹性保障服务已匹配实例列表。
修改
调用[ModifyElasticityAssurance](../developer-reference/api-ecs-2014-05-26-modifyelasticityassurance.md)接口修改一个弹性保障服务的部分信息，包含名称、描述、容量。
调用[ModifyInstanceAttachmentAttributes](../developer-reference/api-ecs-2014-05-26-modifyinstanceattachmentattributes.md)接口修改实例的私有池匹配模式。
## 使用场景与策略推荐
场景一：核心业务 - 保障资源确定性
适用业务：电商大促、游戏开服、金融结算等核心应用。
推荐策略：购买专有私有池，并在创建实例时使用指定模式。
使用效果：只要私有池容量未用尽，实例即可创建成功，避免因公共资源不足导致的失败风险。
场景二：高优先级业务 - 兼顾保障与弹性
适用业务：数据分析、批量计算、在线业务的常规扩容等，希望能优先保障，但也接受公共资源作为补充的场景。
推荐策略：购买开放私有池，并在创建实例时使用开放模式。
使用效果：优先使用预留的保障容量。若保障容量耗尽，系统自动尝试使用公共资源池。
场景三：非核心或开发测试 - 成本优先
适用业务：开发、测试环境，或能容忍偶发性创建失败的非核心业务。
推荐策略：在创建实例时选择不使用私有池。
使用效果：使用公共资源池，但需接受因公共资源池库存波动可能导致的创建失败。
## 计费说明
弹性保障的费用由两部分构成：
保障费用（预付费）：购买弹性保障时需一次性支付的保障服务费。
实例费用（按量计费）：从私有池中成功创建的按量付费实例，按标准价格计费。
| 保障方式 | 弹性保障（分时） | 弹性保障 |
| --- | --- | --- |
| 示意图 |  |  |
| 保障费用计算方式 | 预留容量 × 30 天 × 24 小时 实例规格包月价格 ​ × 10% × 保障时长（小时） 保障时长为非连续时间段的累加时长。 | 预留容量 × 实例规格包月价格 × 40% × 保障时长（月） |
| 总费用 | 保障费用 + 实例费用 |  |
实例费用抵扣顺序： 对于由弹性保障创建的按量付费实例，其小时账单按以下顺序匹配优惠进行抵扣：
[节省计划](../savings-plans.md)
[地域级预留实例券](../reserved-instances.md)
不支持可用区级预留实例券。
若无适用优惠，则按标准按量付费价格出账。
## 使用限制
支持范围：仅部分地域、可用区和实例规格支持弹性保障，实际以控制台购买页面为准。
不可变更与释放：弹性保障购买后不支持修改容量、取消订单或提前释放。到期后自动失效。
资源属性匹配：创建实例时，所选的地域、可用区、实例规格必须与弹性保障的属性严格匹配。
保障范围：仅保障 ECS 实例规格容量可用性，不保障云盘、公网 IP、弹性网卡等关联资源的库存。
实例操作影响：对已创建的实例执行升降配操作，会使其脱离弹性保障的私有池，不再享受资源确定性保障。
## 应用于生产环境的建议
与弹性伸缩集成：建议将弹性保障与弹性伸缩（ESS）结合使用，实现自动化资源调度。
在[创建](https://help.aliyun.com/zh/auto-scaling/user-guide/create-an-ecs-scaling-group)或[修改伸缩组](https://help.aliyun.com/zh/auto-scaling/modify-a-scaling-group#concept-qkz-nkx-rfb)时，设置的资源池策略以优先使用弹性保障的私有池容量。
资源池策略选项：
私有池优先：优先使用指定的私有池，如果私有池容量不足，则自动匹配开放类型的私有池或公共池。
仅限私有池：必须使用私有池容量，否则实例启动失败。
配置步骤：
登录[弹性伸缩控制台](https://essnew.console.aliyun.com/)。
创建或修改伸缩组。
在[伸缩配置](https://help.aliyun.com/zh/auto-scaling/user-guide/manage-scaling-configurations#9f06c1bc759oq)的高级设置中选择资源池策略，并指定一个弹性保障的私有池。
监控与告警：建议通过云监控（CloudMonitor）[创建报警规则](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/create-an-alert-rule)对关键指标设置告警，及时掌握容量使用情况。例如当可用容量低于总容量的 20% 时触发告警：
产品选择ECS私有资源池。
指标选择实例个数使用率，报警级别选择警告（Warn），阈值设置20%。
## 相关文档
[弹性保障和容量预定比对](overview-29.md)
## 常见问题
Q：实例释放后，弹性保障的容量为什么没有立即更新？
A：实例释放需要耗时，建议避免频繁创建和释放操作，以防容量未及时更新导致后续创建失败。
Q：单个弹性保障可以跨可用区使用吗？
A：不能。如有跨可用区保障需求，可在不同可用区创建多个弹性保障。
Q：弹性保障是否支持变更实例规格？
A：不支持。弹性保障绑定的实例规格在购买后不可更改。
Q：如何查看私有池剩余容量？
A：在弹性保障列表页，单击弹性保障ID，在资源详情可查看容量使用情况。
Q：弹性保障的标签有什么作用？
A：创建实例时，开放私有池支持通过实例标签匹配。
绑定标签：为实例绑定相同的标签，可自动匹配对应开放私有池。
弹性保障生效后，始终以购买时绑定的标签匹配私有池。
未绑定标签：系统自动匹配一个开放私有池。
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
