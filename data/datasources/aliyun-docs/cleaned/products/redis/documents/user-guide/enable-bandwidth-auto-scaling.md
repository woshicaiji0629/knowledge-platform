# 开启实例的带宽弹性伸缩-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/user-guide/enable-bandwidth-auto-scaling

# 开启带宽弹性伸缩
当您的业务将面对突发或计划中的流量高峰时，您可以使用云数据库 Tair（兼容 Redis）的带宽弹性伸缩功能。该功能将实时检测带宽的平均使用率，当带宽使用率达到阈值后自动增加实例带宽，在流量高峰过去后，该功能也支持自动缩回实例带宽。该功能可帮助您轻松对应各类流量高峰，专注于业务提升。
## 前提条件
实例为Redis开源版或Tair（企业版）[内存型](../product-overview/dram-based-instances.md)、[持久内存型](../product-overview/persistent-memory-optimized-instances-1.md)。
## 功能概述
由于不同实例规格对应的带宽存在差异，如果流量超过了带宽上限，可能会导致阻塞，从而影响服务性能。您可以开启带宽弹性伸缩功能来避免此类情况。与变更实例规格相比，调整带宽可以帮助您迅速提升带宽，节约整体费用，并且不会引发连接的中断，实现即开即用。
### 带宽弹性伸缩流程
开启该功能后，系统会根据您设定的带宽弹性伸缩策略和观察时间自动执行下述操作（扩展或回缩的带宽大小由系统自动计算）：
触发带宽扩展阈值：为实例扩展带宽并持续监测，如果再次触发则继续扩展带宽，最多支持额外增加原实例默认带宽的6倍，但增加的上限为192 MB/s。
如需更大的带宽，推荐使用Tair（企业版），Tair实例各规格支持的最大带宽均为96 MB/s以上。您也可以升级至Tair（企业版）后再执行调整带宽操作。
触发带宽回缩阈值：为实例回缩带宽并持续监测，如果再次触发则继续回缩带宽，最低可回缩至实例规格的默认带宽。
说明
每次扩缩容的目标带宽为：实际使用带宽（MB/s）/（（扩展阈值 + 回缩阈值）/2）。每次扩缩容后，会尽量使实际带宽使用率处于扩展阈值与回缩阈值的中间。
例如：实例的默认带宽为96MB/s，设置扩展阈值为70%、缩容阈值为30%、观测窗口为15分钟，如果带宽平均使用率大于等于70%，则会触发扩展操作，扩展后的目标带宽为（（96*70%））/（（70% + 30%）/ 2）） = 135MB/s；如果带宽平均使用率小于等于升级后的30%，系统将对该实例执行带宽回缩操作（最小会缩容至当前实例规格的默认带宽）。
### 注意事项
为保障DAS可正常访问云数据库的相关资源，开启该功能后，系统会将名为[AliyunServiceRoleForDAS](https://help.aliyun.com/zh/das/user-guide/aliyunservicerolefordas-role#task-1930737)的关联角色授权给DAS使用。
若实例为云原生版读写分离架构时，实例将以实际使用带宽最高的节点为主，并统一扩缩容所有节点。
若实例为集群架构或经典版读写分离架构时，带宽观测和扩缩容的粒度为数据分片或只读节点，各节点独立进行扩缩容，不会彼此影响。
### 应用场景
当您遇到下述业务场景，您可以通过本功能调整实例的带宽。
展开查看详细应用场景
| 适用场景 | 说明 |
| --- | --- |
| 灵活地应对流量高峰 | 例如业务将迎来限时秒杀活动，届时将会带来流量高峰，高峰过后需要减少带宽以节省资源，需要灵活地变更带宽。 |
| 快速消除带宽对业务影响 | 例如业务中临时出现较多的大 Key 读写，需要快速消除带宽限制避免影响业务，同时为处理大 Key 问题预留时间。 |
| 低成本地应对访问倾斜 | 实例为 [集群架构](../product-overview/cluster-master-replica-instances.md) 或 [读写分离架构](../product-overview/read-or-write-splitting-instances-1.md) ，某些数据分片或只读节点的访问比较频繁，带宽频频到达上限，而其他数据分片或只读节点的带宽使用率较低。 开启该功能后，系统可精准识别带宽不足的数据分片或只读节点，自动为其升级带宽，无需升级整体实例的带宽或规格，极大降低使用成本，提升运维便利性。 |
### 费用说明
根据增加的带宽量和使用时长，按小时产生费用，不同地域的收费标准有所区别。更多信息，请参见[计费项](../product-overview/billable-items.md)。
说明
实例默认的带宽不会产生费用，只有在默认带宽的基础上增加带宽时收费。
## 功能限制
实例完成自动带宽扩展后，需要经过至少1小时的冷却时间才可触发自动带宽回缩。同时，两次自动带宽扩展操作之间有1分钟的冷却时间。
说明
若流量增长过快并超过扩容阈值，在冷却期内将触发流量告警，且此时发起的弹性扩容操作将会失败。
实例整体带宽最多支持额外增加原实例默认带宽的6倍，但增加的上限为192 MB/s。
说明
例如：
Tair内存型2 GB标准架构的默认带宽为96 MB/s，该实例可调整的带宽上限为96 MB/s + 192 MB/s = 288 MB/s。
Redis开源版256 MB标准架构的默认带宽为10 MB/s，该规格最多可增加60 MB/s，最终实例带宽上限为10 MB/s + 60 MB/s = 70 MB/s。
如需更大的带宽，您可以通过升级实例规格，或升级实例架构（例如从标准架构升级至集群架构），获取更高的带宽性能，更多信息请参见[实例规格](../product-overview/overview-4.md)。
不建议同时手动调整实例带宽和开启带宽弹性伸缩功能。
若同时使用：当手动设置带宽达到上限，将不再会触发自动带宽扩展。且随着流量的减少，自动带宽回缩会将手动设置的带宽回缩至实例规格的默认带宽。
说明
例如：
实例带宽默认为10 MB/s，手动设置70 MB/s后，当触发扩展阈值时，因超过伸缩6倍上限，则不会自动扩展；
若同规格实例手动设置40 MB/s，当触发扩展阈值时，最高会自动扩展至70 MB/s；当触发缩容阈值时，会进行缩容，直至缩容至默认规格带宽10 MB/s。
如果实例存在未到期的带宽包，则无法开通带宽弹性伸缩功能。请先退订实例的带宽包，详情请参见[退订管理](https://help.aliyun.com/zh/user-center/refund-management/)。
若执行下述操作将会导致的带宽弹性伸缩功能自动失效，您需要根据业务需求重新开启该功能：
| 执行的操作 | 例外情况 |
| --- | --- |
| [升级大版本](upgrade-the-major-version-1.md) | 无 |
| [变更实例配置](change-the-configurations-of-an-instance.md) | 当实例为标准架构时，仅升级规格不会导致带宽配置失效。 |
| [更换实例所属的可用区](migrate-an-instance-across-zones.md) | 实例为标准架构时，不会导致带宽配置失效。 |
自动带宽调整功能基于实时性能趋势数据进行决策。若性能趋势数据发生非预期中断或存在较大延迟，该功能将因缺乏有效输入而无法正常运行。
## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在配置信息区域，单击带宽 MB/s后的修改。
说明
若首次访问DAS控制台，请按照界面提示，完成账号授权。
开启自动弹性带宽的开关。
在跳转到的DAS控制台对话框中，完成带宽弹性伸缩策略和事件订阅设置。
设置带宽弹性伸缩策略。
| 类别 | 参数 | 说明 |
| --- | --- | --- |
| 自动带宽扩展 | 自动带宽扩展 | 单击打开该功能的开关。 |
| 带宽平均使用率不小于 | 扩展阈值，选择触发自动带宽扩展操作的带宽平均使用率阈值，单位为百分比，取值范围为 50%~95%。 说明 系统会取入流量和出流量平均使用率中较大的值作为带宽平均使用率。 该实例的带宽最多支持额外增加原实例默认带宽的 6 倍，但增加的上限为 192 MB/s，您也可以关注当前对话框的提示信息。 |  |
| 观测窗口 | 选择观测窗口的时间，单位为分钟。 说明 观测窗口内带宽的 平均使用率 大于等于阈值时， 则会触发自动带宽扩展 。 |  |
| 自动带宽回缩 | 自动带宽回缩 | 单击打开该功能的开关，开启该功能需要先打开 自动带宽扩展 开关。 |
| 带宽平均使用率不大于 | 缩容阈值，选择触发自动带宽回缩操作的带宽平均使用率阈值，单位为百分比，取值范围为 10%~70%，但至少需要比扩展阈值低 10%。 说明 系统会取入流量和出流量平均使用率中较大的值作为带宽平均使用率。 |  |
单击确定。
Tair控制台上，自动弹性带宽开关已打开表示功能已开启。
可选：设置告警配置，以便及时了解数据库实例的自动带宽扩展或回缩情况，您可以依照系统提示进行配置。
说明
如果您已经为实例配置了告警模板，则不会提示告警配置。
如果您需要自行设置告警模板和告警规则，请参见[配置告警模板](https://help.aliyun.com/zh/das/user-guide/configure-alert-templates)和[配置告警规则](https://help.aliyun.com/zh/das/user-guide/configure-alert-rules)。
展开查看详细步骤
选择系统推荐告警模板，系统会添加弹性伸缩事件的告警监控项。
选择需要告警通知的告警联系组。
单击提交配置，并在弹出的对话框中确认告警配置。
## 相关文档
如需定时升级Tair实例带宽，请参见[定时升级](../use-cases/scheduled-upgrade-of-the-temporary-bandwidth-of-the-redis-instance.md)[Tair](../use-cases/scheduled-upgrade-of-the-temporary-bandwidth-of-the-redis-instance.md)[临时带宽](../use-cases/scheduled-upgrade-of-the-temporary-bandwidth-of-the-redis-instance.md)。
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
