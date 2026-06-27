# 如何为RDS PostgreSQL云盘实例缩容存储空间-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/reduce-the-storage-capacity-of-an-apsaradb-rds-for-postgresql-instance-that-uses-essds

# RDS PostgreSQL云盘实例缩容存储空间
如果您初始购买的存储空间过大，而实际使用量远小于存储空间时，为避免资源浪费，可使用此功能进行存储空间缩容。
说明
RDS PostgreSQL设置了存储空间自动扩容后，暂不支持自动缩容，您也可以在业务数据减少后，使用此功能减少存储空间。
## 前提条件
实例满足以下条件：
大版本：PostgreSQL 10或以上版本
存储类型：ESSD云盘或高性能云盘
说明
您可以前往实例基本信息页查看以上信息。
如果在2022年10月10日前（旧架构实例）创建的云盘实例，需要升级内核小版本到最新后，再缩容存储空间。更多信息，请参见[升级内核小版本](update-the-minor-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md)。
如果您的RDS实例为高性能本地盘实例，建议使用大版本升级功能，将实例升级到云盘高版本，在升级的同时支持存储空间缩容。更多信息，请参见[升级数据库大版本](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md)。
您的阿里云账号没有未支付的续费订单。
您可以前往[订单列表](https://usercenter2.aliyun.com/order/list)页查看是否存在未支付的订单，然后支付或作废订单。
实例状态为运行中。
只读实例存储空间缩容时，其所属主实例的状态必须为运行中。
## 使用限制
警告
存储空间缩容不支持使用了逻辑复制功能的实例。在缩容任务完成后，可能会导致启用逻辑复制功能的实例出现逻辑复制槽丢失或WAL日志被移除，从而引发逻辑复制中断。
手动云盘缩容一天内最多操作2次，避免频繁的缩容操作导致服务受损。
允许在同一系列、同一架构下缩容，缩容后的最小空间由公式min{使用量*1.3，使用量+400 GB}计算，不得低于当前规格允许的最小存储空间，存储空间调整步长5 GB。
各级别云盘允许的最小存储空间为：
ESSD PL0：10 GB
ESSD PL1：20 GB
ESSD PL2：500 GB
ESSD PL3：1500 GB
高性能云盘：10 GB
存储空间缩容示例
假设实例的存储类型为ESSD PL1云盘（最小存储空间为20 GB），存储空间为2000 GB：
使用量为10 GB，根据公式计算得13 GB，低于20 GB，最小可缩容至20 GB。
使用量为500 GB，根据公式计算得650 GB，最小可缩容至650 GB。
使用量为1500 GB，根据公式计算得1900 GB，最小可缩容至1900 GB。
只读实例的存储空间必须大于或等于其所属主实例的存储空间。建议先缩容主实例存储空间，再缩容只读实例的存储空间。
## 影响
云盘缩容会造成30秒的闪断，闪断过程中，与数据库、账号、网络等相关的大部分操作都无法执行，请尽量在业务低峰期执行缩容操作。请确保应用具备重连机制，重连机制需要在您的应用程序中设置。
## 费用
涉及费用变更，详情请参见[变配的计费规则](../product-overview/specification-changes.md)。
## 操作步骤
### 非Serverless实例
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在配置信息区域，单击变更配置。
（可选）如果您是包年包月实例，在弹出的对话框中，单击立即降配，单击下一步。
滑动滑块或单击减号图标，调整存储空间。
说明
缩容后的最小空间由公式min{使用量*1.3，使用量+400 GB}计算，不得低于当前规格允许的最小存储空间，存储空间调整步长5 GB。
选择切换时间。
云盘缩容涉及数据迁移，您可以根据业务情况，选择立即执行或可维护时间内进行切换。
立即执行：立即开始迁移，迁移过程对实例无影响，迁移完成后进行切换，切换会有闪断。
可维护时间内进行切换：立即开始迁移，迁移过程对实例无影响，但是迁移完成后不切换，等到可维护时间才切换，切换会有闪断。详情请参见[设置可维护时间段](set-the-maintenance-window-of-an-apsaradb-rds-for-postgresql-instance.md)。
单击确认下单，在弹出的变配前后实例对比信息窗口中，确认变更信息，单击继续支付完成支付。
### Serverless实例
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在实例资源区域，单击存储空间后的修改。
在修改页签中，滑动滑块或单击减号按钮，调整存储空间，然后单击确定。
说明
缩容后的最小空间由公式min{使用量*1.3，使用量+400 GB}计算，不得低于当前规格允许的最小存储空间，存储空间调整步长5 GB。
在弹出的调整弹性设置对话框中确认变配信息后单击确认。
当实例运行状态变为升降配中时，表示正在进行缩容。
## 常见问题
Q：云盘版RDS PostgreSQL实例存储空间缩容一般闪断多久？
A：缩容会造成30秒的闪断，闪断过程中，与数据库、账号、网络等相关的大部分操作都无法执行，请尽量在业务低峰期执行缩容操作。请确保应用具备重连机制，重连机制需要在您的应用程序中设置。
Q：SSD云盘的RDS PostgreSQL实例如何缩容？
A：SSD云盘已停止售卖，暂不支持缩容，您可以将SSD云盘升级到ESSD云盘后，再进行缩容。更多信息，请参见[【停售/下线】部分](../apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[RDS](../apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[实例不再提供](../apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[SSD](../apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[云盘售卖](../apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)。
## 相关文档
如果还需要修改实例的其他配置，请参见[变更配置](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)。
您可以通过API修改存储空间及其他实例配置。
| API | 描述 |
| --- | --- |
| [ModifyDBInstanceSpec](../developer-reference/api-rds-2014-08-15-modifydbinstancespec.md) | 缩容云盘存储空间时，您需要将 DBInstanceStorage 参数值修改为缩容的目标空间值，其他参数请按需配置。 |
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
