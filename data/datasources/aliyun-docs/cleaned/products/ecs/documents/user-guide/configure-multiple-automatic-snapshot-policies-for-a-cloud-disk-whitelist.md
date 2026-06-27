# 为云盘设置自动快照策略-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/configure-multiple-automatic-snapshot-policies-for-a-cloud-disk-whitelist

# 为云盘设置自动快照策略
当业务对于同一块云盘上的快照创建时间、创建快照的频率和保留时长有不同需求时，可以为单块云盘绑定多个自动快照策略，满足短期高频备份、长期保存等多种备份需求。
## 适用范围
请确保云盘满足以下任一条件：
云盘已挂载到ECS实例，且实例状态为运行中（Running）或已停止（Stopped）。
云盘状态为待挂载（Available），且曾挂载至ECS实例。
通过调用[DescribeDisks](../developer-reference/api-ecs-2014-05-26-describedisks.md)，查看AttachedTime字段可判断云盘是否存在挂载历史。
## 操作步骤
### 为单块云盘设置自动快照策略
访问[ECS](https://ecs.console.aliyun.com/disk/)[控制台-块存储-云盘](https://ecs.console.aliyun.com/disk/)。在页面左侧顶部，选择目标资源所在的资源组和地域。
在目标云盘的操作列中，单击设置快照策略。
在设置自动快照策略页面，可添加或删除策略。单块云盘最多支持存在10个自动快照策略。
添加策略：在设置自动快照策略下拉列表中选择已有策略，或单击新建策略依照界面提示完成策略创建后，单击确认设置。
删除策略：在设置自动快照策略中单击策略末尾叉号后，单击确认设置。
重要
删除自动快照策略后，将不再自动创建对应快照，请注意数据保护。
### 为自动快照策略绑定云盘
访问[ECS](https://ecs.console.aliyun.com/autoSnapshotPolicy/region)[控制台-自动快照策略](https://ecs.console.aliyun.com/autoSnapshotPolicy/region)。在页面左侧顶部，选择目标资源所在的资源组和地域。
在目标策略的操作列中，按需操作。
绑定云盘：单击绑定云盘。在可选云盘区域，选中目标云盘后，单击确定绑定。
已绑定当前策略或已绑定满10个策略的云盘将无法选中。
解绑云盘：单击解绑云盘。在可选云盘区域，选中目标云盘后，单击确定解绑。
重要
云盘解绑后，将不再按该策略自动创建快照，请注意数据保护。
## 费用说明
创建快照策略本身不收费，但策略成功执行后会根据任务类型收取相关费用。可通过设置自动快照随云盘释放、建议定期删除不再使用的自动快照以及归档快照的方式[降低快照存储成本](reduce-snapshot-fees.md)。
自动创建快照任务：所有通过策略创建的快照，会按其快照容量收取[标准快照存储费](../snapshots-1.md)。
跨地域复制任务：若策略启用了跨地域复制功能，除源地域的标准快照费外，还会产生[复制快照流量费](../snapshots-1.md)和目标地域的标准快照存储费。
## 配额与限制
每块云盘支持绑定的自动快照策略，上限为 10 个。
单块云盘支持同时存在的快照创建任务数（包括自动与手动创建）存在上限，如果策略触发时，超过最大任务数限制，任务将被跳过，并在下一个计划时间点重新判断。不同云盘类型的任务数上限如下：
| 云盘类型 | 任务数上限 |
| --- | --- |
| ESSD 系列云盘（ESSD、ESSD AutoPL、ESSD Entry 和 ESSD 同城冗余） | 10 |
| 上一代云盘（SSD 云盘/高效云盘/普通云盘） | 1 |
当策略启用快照跨地域复制时，需确保云盘未存在相同源和目的地域的跨地域复制任务，若存在，任务将被跳过，并在下一个计划时间点重新判断。
每块云盘最多支持自动快照个数请参见[快照的使用限制](limitations.md)。当自动快照数量达到上限时，系统会删除由策略生成的时间最早的自动快照。请根据业务需求合理规划快照的保留时间，避免重要快照被意外删除。
## 更多操作
### 设置自动快照随云盘释放
默认情况下，自动快照的生命周期遵循自动快照策略的保留时间，不会随云盘释放，可根据需求开启自动快照随云盘释放属性。
重要
开启自动快照随云盘释放属性后，当释放云盘（手动释放、随实例释放或更换操作系统）时，即使自动快照未到期，也会随云盘释放而提前删除。
访问[ECS](https://ecs.console.aliyun.com/disk/)[控制台-块存储-云盘](https://ecs.console.aliyun.com/disk/)。在页面左侧顶部，选择目标资源所在的资源组和地域。
在目标云盘的操作列中，单击编辑属性
在编辑云盘属性对话框中，选中自动快照随云盘释放选项。
后续可根据需要取消选中，关闭自动快照随云盘释放。
单击确定。
### 如何查看创建的自动快照？
策略执行后，会自动在[ECS](https://ecs.console.aliyun.com/snapshot)[控制台-快照](https://ecs.console.aliyun.com/snapshot)页面生成快照。
自动快照命名格式为auto2.0_yyyyMMdd_SnapshotPolicyId，快照来源为自动创建。其中：
auto2.0：表示自动快照。
手动快照和自动快照的区别请参见[手动快照和自动快照有什么区别？](../data-protection-and-recovery-faqs.md)
yyyyMMdd：创建快照的日期，y表示年、M表示月、d表示天。
SnapshotPolicyId：快照对应的自动快照策略ID。
例如，auto2.0_20241225_sp-2zeff8vy17u91rn5****表示2024年12月25日创建的一份自动快照，自动快照策略ID为sp-2zeff8vy17u91rn5****。
## 相关文档
可通过API接口完成以下操作：
为云盘设置自动快照策略：[ApplyAutoSnapshotPolicy](../api-applyautosnapshotpolicy.md)
取消云盘设置的自动快照策略：[CancelAutoSnapshotPolicy](../api-cancelautosnapshotpolicy.md)
设置自动快照随云盘释放：[ModifyDiskAttribute](../api-modifydiskattribute.md)
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
