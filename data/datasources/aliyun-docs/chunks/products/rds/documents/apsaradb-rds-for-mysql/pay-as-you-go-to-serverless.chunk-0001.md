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
