# 实例版本升级配置与操作指南-云数据库Tair-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/update-the-minor-version

# 升级小版本与代理版本
云数据库 Tair（兼容 Redis）会不断地对数据库（DB）内核与Proxy（代理节点）组件进行深度优化，用于丰富云产品功能或修复已知缺陷，提升服务稳定性。您可以在控制台上将数据库内核与Proxy组件一键升级至最新版本，也可以按需配置自动升级策略。
## 注意事项
升级数据库版本时，实例将先升级备（Replica）实例或准备新实例，到达指定的执行时间后，执行主备切换或实例切换，完成升级操作。在实例切换阶段，实例最多将存在60秒以内的只读状态（等待数据完全同步），同时会发生秒级的连接闪断，请确保应用程序具备重连机制。
升级Proxy版本：
若实例为云原生版，实例中的Proxy节点将依次进行重启，所有连接会断开，请确保业务具备重连机制。
若实例为经典版，实例将采用热升级技术，新版本代理节点会根据旧版本代理节点的客户端连接信息来恢复连接，可实现连接不中断（可能出现毫秒级的延迟抖动）。但BLOCK、Transactions、Pub/Sub等类型的命令将会中断，请确保业务中的这些命令具备重连机制。若客户端使用直连地址连接实例，则所有命令都不受影响。
较新的小版本可能只在部分地域灰度发布。系统会自动检测实例的小版本，若控制台上小版本升级、代理版本升级按钮处于无法单击的状态，表示当前实例的小版本已经是最新。
除非特别说明，实例内核的小版本均会确保兼容性，因此您无需担心升级可能带来的兼容型问题，更多信息请参见[Tair](../support/apsaradb-for-redis-enhanced-edition-1.md)[小版本发布日志](../support/apsaradb-for-redis-enhanced-edition-1.md)、[Redis](../support/apsaradb-for-redis-community-edition.md)[开源版小版本发布日志](../support/apsaradb-for-redis-community-edition.md)与[Proxy](../support/apsaradb-for-redis-proxy-nodes.md)[小版本发布日志](../support/apsaradb-for-redis-proxy-nodes.md)。
警告
升级小版本不会改变实例的连接地址、数据、白名单配置以及已创建的账号密码等配置信息，但仍然建议您：
在业务低峰期进行升级。
确保应用程序具备重连机制。
## 更新级别说明
LOW（低）：一般级别，包含日常新功能升级（例如新增某个功能）。
MEDIUM（中）：推荐级别， 包含功能模块优化类的升级（例如优化了某个功能）。除此以外，还包含了LOW级别所包含的更新内容。
HIGH（高）：重要级别，包含影响稳定性或安全性的重要升级（例如修复某个漏洞或缺陷）。除此以外，还包含LOW和MEDIUM级别所包含的更新内容。
## 配置自动升级
您可以在版本管理中心了解每个实例的版本状况、当前是否为最新版本等信息。同时，您可以在该功能中配置自动升级策略，或升级的实例版本，帮助您从全局视角对实例版本进行统一管理。
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域。
在左侧导航栏，单击版本管理中心。
在页面左上角，选择目标地域。
在版本管理中心页面，您可以看到当前地域下所有实例的当前小版本、是否为最新小版本等信息。
单击实例右侧的配置，并打开自动升级开关，配置自动升级操作。
开启后，系统会周期性检查版本发布状态，如发现新版本则将在60天内的可升级时段内进行自动升级。如遇特殊情况需延后升级，例如近期同一账号下运维事件过多则需要顺延等待。
可升级时段与实例的可维护时段相同，不论修改哪一个，都将同步修改另外一个。
说明
支持勾选多个实例，批量完成升级或配置操作。
支持在事件中心>计划内事件中查询实例版本的升级记录。
## 手动升级
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在配置信息区域框，将鼠标悬浮至版本或代理版本右侧的提示图标，查看版本的发布日志。
查阅版本发布日志后，可选择升级>小版本升级或代理版本升级。
说明
若无法单击小版本升级或代理版本升级按钮，表示当前实例的版本已经是最新，无需升级。
在右侧弹出的面板中，选择升级的执行时间。
单击确定。
## 常见问题
Q：如何确认Tair实例的小版本是不是最新版？
A：若小版本升级或代理版本升级按钮为浅灰色且无法单击，表示当前版本已为最新，无需升级。
若单击后会弹出面板，则表示小版本不是最新版，您可以按照上述说明完成升级。
Q：能否升级到指定小版本？
A：不支持，无法指定小版本，默认会升级到最新小版本。小版本都会向前兼容，您无需担心兼容性问题。
Q：为什么选择了执行时间为可维护时间内执行，实例的状态还是变成了小版本升级中？
A：系统在执行相应的升级前置工作，例如申请资源、同步数据等，不会执行实例切换或主备切换，不会影响实例提供服务。只有在执行实例切换或主备切换时，才会产生60秒以内的只读状态和秒级的连接闪断。
Q：将实例的升级策略改为自动升级后，为什么一直没有升级？
A：不会立即升级。系统会周期性检查版本发布状态，如发现新版本则将在60天内的可升级时间段内进行自动升级。如遇特殊情况需延后升级，例如近期同一账号下运维事件过多则需要顺延等待。您可以在[事件中心](query-and-manage-pending-events.md)查询升级计划，也可以立即执行手动升级。
Q：为什么选择手动升级，还是会收到小版本升级的事件通知？
A：手动升级只会关闭小版本自动升级服务，但在版本存在高危风险、版本过老停止维护等情况下，实例仍会产生小版本升级事件。若收到小版本升级事件，您可以在[事件中心](https://kvstore.console.aliyun.com/Redis/eventToDo/cn-hangzhou)按需调整升级时间（推荐）或取消。
Q：为什么集群实例不同数据分片节点的小版本不一样？
A：经典版集群架构的数据分片节点在重建、主备切换时会默认部署最新的小版本，这会造成不同数据分片节点的小版本不一致，但这不会引发兼容性问题。而控制台或API显示的是该集群的最低版本。当对实例执行小版本升级、变配操作时，各数据分片节点的小版本会统一对齐。
说明
云原生版集群实例的小版本总是一致的。
## 相关API
| API | 说明 |
| --- | --- |
| [DescribeEngineVersion](../developer-reference/api-r-kvstore-2015-01-01-describeengineversion-redis.md) | 查询实例的大版本和小版本信息，同时可查询到小版本的发布日志信息。 |
| [ModifyInstanceMinorVersion](../developer-reference/api-r-kvstore-2015-01-01-modifyinstanceminorversion-redis.md) | 升级实例的小版本。 |
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
