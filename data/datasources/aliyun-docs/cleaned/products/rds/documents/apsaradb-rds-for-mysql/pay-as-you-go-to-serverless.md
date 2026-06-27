# 按量付费实例转Serverless-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/pay-as-you-go-to-serverless

# 按量付费转Serverless
本文介绍如何将RDS MySQL实例的付费类型由按量付费转换为Serverless。
## 应用场景
如果您的业务波动较大，或需要更大的存储空间，并且希望计算资源随业务负载自动弹性扩缩容，建议使用Serverless实例，可提高资源利用率和运维效率，帮助企业降本增效。
Serverless实例的适用场景，请参见[RDS MySQL Serverless](rds-mysql-serverless.md)[实例](rds-mysql-serverless.md)。
## 前提条件
实例满足以下条件：
引擎：MySQL
产品系列：基础系列或高可用系列
产品类型：标准版
存储类型：ESSD PL1云盘、高性能云盘
内核版本：大于等于以下版本且不属于[已下线版本](release-notes-for-alisql.md)：
MySQL 5.7 rds_20230228
MySQL 8.0 rds_20230324
付费类型：按量付费
说明
如果实例的付费类型是包年包月，[可以先转按量付费](change-the-billing-method-of-an-apsaradb-rds-for-mysql-instance-from-subscription-to-pay-as-you-go.md)，再转Serverless。
状态：运行中
实例为主实例且不带只读实例。
未启用X-Engine引擎。
未开通数据库代理服务。
未开通SSL加密功能。
未使用自定义密钥进行云盘加密。
说明
您可以在RDS控制台的实例详情页查看以上实例信息。
## 使用限制
按量付费与Serverless之间可以相互转换，但24小时内只允许转换一次。
如果实例所在可用区未售卖Serverless实例，或者资源不足，则无法进行转换。
## 影响
按量付费转Serverless会导致实例切换，请确保应用具有自动重连机制。自动重连机制需要在您的应用程序中设置。实例切换的影响请参见[实例切换的影响](untitled-document-1701914031929.md)。
按量付费转Serverless的实例，如果开启了PFS（performance schema），会导致内存占用率较高，进而影响RCU的弹降效率。
## 注意事项
Serverless实例会根据负载自动弹升弹降，并调整innodb_buffer_pool大小，因此转Serverless后对innodb_buffer_pool_size、innodb_buffer_pool_instances参数的自定义修改会被忽略。
建议设置RCU上限大于或等于当前规格核数，例如原实例为4核，则Serverless RCU扩缩上限设置为大于或等于4。
## 费用
按量付费转换为Serverless功能免费，Serverless的计费详情，请参见[Serverless](https://help.aliyun.com/zh/document_detail/447753.html)[费用](https://help.aliyun.com/zh/document_detail/447753.html)。
## 操作步骤
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，单击目标实例ID。
在基本信息页面的配置信息区域，单击转Serverless。
按需在RDS售卖页配置资源扩缩范围（RCU）、高级设置中的弹性策略和自动启停、切换时间参数。
说明
各配置项的含义和配置原则，请参见[配置](https://help.aliyun.com/zh/document_detail/421557.html)[Serverless](https://help.aliyun.com/zh/document_detail/421557.html)[实例](https://help.aliyun.com/zh/document_detail/421557.html)。
阅读转换须知和服务协议后，单击确认下单。
说明
在变更过程中，实例的运行状态将变为升降配中。变更完成后，实例的运行状态将变为运行中。
## 常见问题
Q：按量付费转换为Serverless后，为什么我在费用与成本>订购订单>我的订单中看到的订单为新购订单？
A：因为转换的实现原理为新购Serverless实例，再将原实例切换为新购实例，所以看到的订单为新购订单。
Q：使用自定义密钥加密的云盘实例，为什么不支持将付费类型从按量付费转换为Serverless？
A：由于Serverless实例为通用型规格的实例，[仅支持使用服务密钥（Default Service CMK）进行云盘加密](announcements-change-of-cloud-disk-encryption-instance-creation-from-january-15-2024.md)。
Q：按量付费转换为Serverless后，是否支持Sequence Engine?
A：支持，详情请参见[Sequence Engine](sequence-engine.md)。
## 相关API
| API | 描述 |
| --- | --- |
| [变更](../api-change-instance-configuration.md) [RDS](../api-change-instance-configuration.md) [实例](../api-change-instance-configuration.md) | 将付费类型由按量付费变更为 Serverless 时： 请确认实例原付费类型为按量付费，并且将 PayType 参数设置为 Serverless 。 请将 DBInstanceClass 参数设置为 mysql.n2.serverless.1c 。 其他参数（存储空间大小等）请传空值或与实例原参数值保持一致，不支持修改。 |
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
