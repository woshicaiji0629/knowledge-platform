## 一、创建RDS MySQL实例
访问[RDS](https://rdsbuy.console.aliyun.com/newCreate/rds/mysql)[实例标准创建页面](https://rdsbuy.console.aliyun.com/newCreate/rds/mysql)。
配置核心参数
您可以通过配置以下核心参数快速完成实例选型，其他参数保持默认值即可。
选择计费方式（示例值：按量付费）
短期使用建议选择按量付费，按小时付费，能随时释放实例。
长期使用建议选择包年包月，预付费模式，费用比按量付费更低。
业务波动大时建议选择Serverless，实例无固定规格，性能随业务负载自动调整。
选择地域（示例值：华东1（杭州））
如需通过ECS连接：选择ECS实例所在地域，可实现内网互通。
如需通过其他设备连接：选择离该设备较近的地域，可以降低网络时延，后续通过外网访问。
实例购买后地域不可更改，请谨慎选择。
选择引擎（示例值：MySQL 8.0）
支持MySQL 5.6、5.7、8.0，建议与业务侧数据库大版本保持一致。
如无版本需求，建议选择MySQL 8.0，可体验更丰富的功能。
选择产品系列与存储类型
不同[产品系列](https://help.aliyun.com/zh/document_detail/2787304.html)和[存储类型](https://help.aliyun.com/zh/document_detail/2545944.html)的实例会限制[部分产品功能](features.md)的使用。
如需体验RDS MySQL产品或短期试用，推荐选择高可用系列，存储类型为本地SSD盘或高性能云盘，以较低成本体验更多产品功能。
选择VPC
如需与同地域下的ECS实例内网互连，则需选择与ECS相同的VPC。其他情况下，保持默认值即可。
选择实例规格（示例值：通用规格 2核4 GB）
RDS MySQL提供了多种实例规格，您可以根据实际业务需要进行选择。如果购买后发现此规格无法满足需求，可以[变更规格配置](change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。
确认配置与下单支付
您可以在页面右侧查看与确认待购买实例的配置，将鼠标悬浮在查看明细上时，可以在弹窗中查看实例的费用明细。[RDS](billable-items-billing-methods-and-pricing.md)[实例费用](billable-items-billing-methods-and-pricing.md)与其付费方式、系列、规格、存储类型和存储空间大小等参数相关。
确认配置无误后，单击去支付按钮并支付。
说明
创建按量付费的RDS实例时，您的阿里云账户余额（即现
