# 如何开启自动扩容-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/user-guide/enable-automatic-scale-up

# 开启自动扩容
云数据库 Tair（兼容 Redis）实例集成了数据库自治服务DAS（Database Autonomy Service）的自动扩容功能，当内存平均使用率达到阈值后会自动升级实例的规格，帮助您快速弹性适配业务高峰，避免内存溢出的风险，有效保障线上业务稳定性。
## 前提条件
实例满足下述条件：
Redis开源版或Tair（企业版）内存型。
部署模式为云原生版。
[标准架构](../product-overview/standard-master-replica-instances.md)。
## 费用说明
仅会产生因升级规格产生的费用，详情请参见[变配说明](../product-overview/configuration-changes.md)。
## 自动扩容流程
图 1.自动扩容流程
开启自动扩容功能后，当观测窗口内实例的内存平均使用率达到设定的阈值后，[DAS](https://help.aliyun.com/zh/das/product-overview/what-is-das#concept-2419191)将自动执行扩容操作（即升级实例规格到下一级更大的规格，例如从1 GB升级至2 GB）。完成扩容后，DAS会继续监测内存使用率，如果再次满足自动扩容的条件则会继续扩容，直到扩容至您设置的规格上限。
但DAS不会直接对实例执行回缩。如果您开启了订阅服务，当观测窗口实例的内存平均使用率降至30%以下时，DAS将通过您设定的方式（例如邮件）发送回缩建议给您，您可以在合适的时间执行手动降配操作以提高资源利用率。关于订阅服务的具体操作，请参见本文的操作步骤。
说明
为保障DAS可正常访问云数据库的相关资源，开启该功能后，系统会将名为[AliyunServiceRoleForDAS](https://help.aliyun.com/zh/das/user-guide/aliyunservicerolefordas-role#task-1930737)的关联角色授权给DAS使用。
如果自动扩容后，执行了手动变配操作，DAS判断您已人工手动降配，不会发送回缩建议给您。当您的实例再次触发了自动扩容，并达到回缩建议的阈值，DAS才会发送回缩建议给您。
## 自动扩容影响
自动扩容时的连接影响因实例类型而异：
云盘版实例：当主机资源充足时，扩容过程中不会出现连接闪断；当主机资源不足需要迁移时，会出现1~2次30秒内的连接闪断。
经典版实例：扩容时需要进行迁移，会出现1~2次30秒内的连接闪断。
为保障变配后的新实例能快速追平原实例的增量数据，在变配过程中，实例会出现1分钟内的只读状态。
为保障提供更出色的性能和稳定性，如果实例的小版本过低，在变更配置时，系统会将实例的小版本升级至最新。
## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在配置信息区域，开启自动扩容的开关。
在跳转到的DAS控制台对话框中，完成自动扩容和事件订阅设置。
在自治功能设置>优化和限流页签，勾选自动扩容，设置自动扩容参数。
| 配置 | 说明 |
| --- | --- |
| 内存平均利用率不小于 | 选择达到自动扩容的内存平均使用率阈值，单位为百分比，取值范围为 50%~90%，调整的颗粒度为 10%。 |
| 规格上限 | 选择可扩容到的最大规格。如果达到了自动扩容的阈值，DAS 会逐级扩容规格（例如从 1 GB 升级至 2 GB）并继续监测内存使用率，如在观测窗口内再次达到自动扩容的阈值，会继续扩容，直到扩容至您设置的规格上限。 |
| 观测窗口 | 选择观测窗口的时间，单位为分钟，最大取值为 30 分钟。 说明 本案例中的设置即表示，在 30 分钟的观测窗口内，如果内存平均使用率大于等于 70%，系统将对实例执行升级配置操作（最多升配至 64G 规格）。 |
单击确定。
此时返回至Tair控制台页面，查看该实例的自动扩容将显示为已开启。
若该实例未配置告警模板，您可以继续配置告警订阅，以便及时了解数据库实例的自动扩容情况。
选择告警模板，并单击模板选择完成，下一步。
系统会推荐告警模板并添加对应自治事件的告警规则，您可以依照系统提示进行配置。
说明
如果您已经为实例配置了告警模板，请依照系统提示，在告警模板添加对应自治事件的告警规则。
如果您需要自行设置告警模板和告警规则，请参见[配置告警模板](https://help.aliyun.com/zh/das/user-guide/configure-alert-templates)和[配置告警规则](https://help.aliyun.com/zh/das/user-guide/configure-alert-rules)。
选择告警联系组，并单击联系组选择完成，下一步。
新增联系组或联系人的操作请参见[管理告警联系人](https://help.aliyun.com/zh/das/user-guide/manage-alert-contacts)。
单击提交配置，并在弹出的对话框中确认告警配置。
此时，您已完成告警订阅配置。
## 常见问题
Q：实例开启自动扩容后，内存占用率非常高（如82%），为何还不自动升级？
A：请检查自动扩容的内存平均使用率阈值。例如设置为90%，则表示当实例在观测窗口期间的内存平均使用率达到90%及以上时会进行自动扩容。
Q：为什么开启读写分离后，自动扩容功能关闭了？
A：由于目前只有标准架构支持自动扩容功能，因此在启用读写分离后，将会关闭自动扩容功能。
## 相关文档
Redis开源版云原生集群架构实例还支持自动增加分片，更多信息请参见[自动增加分片](https://help.aliyun.com/zh/das/user-guide/automatic-shard-addition)。
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
