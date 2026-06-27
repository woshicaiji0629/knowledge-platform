### DAS：SQL洞察和审计
DAS企业版V3、V2、V1的计费项账单产品为数据库自治服务。不能用RDS的节省计划或资源包抵扣。
计费详情
企业版 V3
重要
企业版 V3按使用的功能细分了计费项，使计费更加灵活，使用成本大大降低。
开通企业版 V3后，默认收取日志流量费用，其他计费将根据对应功能的使用情况进行收取。
支持企业版 V1和V2免费迁移至企业版 V3，迁移完成前按照当前版本计费，迁移完成后按照迁移目标版本计费。详情请参见[DAS](https://help.aliyun.com/zh/das/user-guide/faq#a3a950500f3s3)[企业版间数据如何迁移？](https://help.aliyun.com/zh/das/user-guide/faq#a3a950500f3s3)
企业版 V3计费方式简介
计费案例
根据服务使用场景、选用功能可分为以下2个案例：
运维场景
支持全量SQL日志记录和聚类分析，可用于快速查询定位分析问题SQL，对受影响业务应急处理和后续深度优化，功能详见[SQL](https://help.aliyun.com/zh/das/user-guide/sql-explorer-and-audit-5/)[洞察和审计](https://help.aliyun.com/zh/das/user-guide/sql-explorer-and-audit-5/)。本场景可选开启功能如下：
假设您的实例每天都有10GB写入流量，设置SQL日志存储为30天，日志索引热存储为7天。
说明
SQL日志存储时长即为您的SQL日志存储总时间，默认为冷存储。例如，在以上场景，开通日志索引后，新产生的日志会先以7天热存储形式存储，超过7天之后，剩余23天则转入冷存储。
