# RDS MySQL极速变配-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/rapid-instance-type-change

# 极速变配
RDS MySQL本地盘实例支持极速变配功能，在宿主机资源充足时，实例可原地快速升配，无需数据迁移，变配过程不会发生连接闪断，适合对业务连续性要求较高的场景。
## 背景信息
在变更RDS MySQL实例规格时，系统需要将实例调整到目标规格。普通变配流程中，如果当前宿主机资源不足，系统会将实例迁移到其他宿主机，这一过程涉及底层数据迁移，并且在迁移完成切换时会产生约30秒的连接闪断。
极速变配通过检测当前宿主机的空闲资源，判断是否可以在原地完成规格升配。如果资源充足，实例将在原宿主机上直接弹升至目标规格，整个过程不涉及数据迁移，也不会产生连接闪断。
两种变配路径的对比如下：
命中极速变配：宿主机资源充足，实例在原地完成升配。无数据迁移，无连接闪断，变配耗时更短。
未命中极速变配：宿主机资源不足，实例需迁移到其他宿主机完成变配。涉及底层数据迁移，在任务完成切换时会产生约30秒的连接闪断。
## 前提条件
RDS MySQL实例的大版本为5.7及以上。如需查看或升级大版本，请参见[变更配置](change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。
实例的存储类型为本地盘。云盘实例暂不支持极速变配。
实例状态为运行中。
本次变配为以下操作之一：
升级实例规格（例如从4核16 GB升级到8核32 GB）。
扩容或缩容存储空间。
## 注意事项
降低规格不支持极速变配。极速变配仅适用于升级实例规格或变更存储空间的场景，降低实例规格时将走普通变配流程，可能涉及数据迁移并产生连接闪断。
默认不启用极速变配。在变配页面中，您需要主动点击评估是否极速变配按钮，系统才会评估当前宿主机资源是否支持极速变配。如果不点击评估，变配流程将按普通变配方式执行。
评估结果有时效性。评估命中极速变配后， 系统会保留5min左右的有效期（具体以控制台为准） ，您需要在控制台显示的时间内完成下单并支付，才能确保命中极速变配。超时后资源可能被其他任务占用，需要重新评估。
请确保应用具备重连机制。在未命中极速变配的情况下，变配过程涉及底层数据迁移，同时会产生约30秒的连接闪断，请确保您的应用程序具备自动重连能力，避免业务中断
## 操作步骤
登录[RDS](https://rdsnext.console.aliyun.com)[管理控制台](https://rdsnext.console.aliyun.com)，在左侧导航栏单击实例列表，在上方选择地域，然后单击目标实例ID。
在实例详情页面的基本信息区域，单击变更配置。
包年包月实例：在弹出的变更配置对话框中，选择立即升配，单击下一步，进入变配页面。
按量付费实例：直接进入变配页面。
在变配页面选择目标实例规格或存储空间。
在无损变配评估与配置区域，单击评估是否极速变配。
系统将自动评估当前宿主机资源是否充足，评估结果分为以下两种情况：
支持极速变配：页面显示蓝色提示框，提示"本地资源充足，在xxxx.xx.xx 11:14（UTC+8）前"下单并支付完成会进行极速变配，不涉及跨机数据迁移"。请在提示的截止时间（例如 2026.04.01 11:14（UTC+8））前完成后续步骤。
不支持极速变配：页面显示黄色提示框，提示本次变更会涉及底层数据搬迁，搬迁完成切换时会出现约30秒的连接闪断。您可以选择继续变配或稍后重试。
确认变配信息无误后，阅读并勾选服务条款，然后单击去支付。
重要
如果评估命中了极速变配，请务必在提示的截止时间前完成支付，否则系统不保证有足够资源进行极速变配，届时可能按照普通变配方式执行，涉及数据迁移和连接闪断。
## 常见问题
Q：评估未命中极速变配怎么办？
A：评估结果取决于当前宿主机的资源水位。如果本次未命中，说明当前宿主机的空闲资源不足以支持目标规格。您可以选择：
直接继续变配：系统将通过数据迁移方式完成变配，期间会产生约30秒的连接闪断，建议在业务低峰期执行。
稍后重新评估：等待一段时间后重新发起评估，宿主机资源水位可能会发生变化。
Q：评估命中后超时未支付会怎样？
A：如果在提示的截止时间内未完成支付，系统不保证有足够资源进行极速变配，届时可能按照普通变配方式执行，涉及数据迁移和连接闪断。建议评估命中后尽快完成支付。
Q：极速变配和普通变配在费用上有区别吗？
A：没有区别。极速变配和普通变配的费用相同，均按照目标规格和存储空间的定价计费。极速变配仅优化了变配过程的体验，不会产生额外费用。
## 相关文档
[变更配置](change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)
[实例变更项](configuration-items-for-an-apsaradb-rds-for-mysql-instance.md)
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
