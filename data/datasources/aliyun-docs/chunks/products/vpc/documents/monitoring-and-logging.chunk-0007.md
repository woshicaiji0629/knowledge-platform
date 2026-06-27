## 云资源操作审计
VPC已接入阿里云操作审计，可提供统一的云资源操作日志管理，记录云账号下用户登录及资源访问操作，实现安全分析、入侵检测、资源变更追踪以及合规性审计。
操作审计可记录通过阿里云控制台、OpenAPI、开发者工具访问和使用云上产品和服务的[日志数据](https://help.aliyun.com/zh/actiontrail/product-overview/audit-events-of-vpc)。
默认追踪并记录最近90天的事件。如需保存更长时间的日志，则需要[创建跟踪](https://help.aliyun.com/zh/actiontrail/use-advanced-event-query-feature-to-query-events#section-uxh-m43-tqk)，将产生的时间记录到日志服务或对象存储OSS。
将事件投递到SLS或OSS后，可以[通过](https://help.aliyun.com/zh/actiontrail/user-guide/query-events-in-the-log-service-or-oss-console)[SLS](https://help.aliyun.com/zh/actiontrail/user-guide/query-events-in-the-log-service-or-oss-console)[或](https://help.aliyun.com/zh/actiontrail/user-guide/query-events-in-the-log-service-or-oss-console)[OSS](https://help.aliyun.com/zh/actiontrail/user-guide/query-events-in-the-log-service-or-oss-console)[控制台查询事件](https://help.aliyun.com/zh/actiontrail/user-guide/query-events-in-the-log-service-or-oss-console)。
[创建数据回补投递任务](https://help.aliyun.com/zh/actiontrail/user-guide/create-a-historical-event-delivery-task)可以跟踪历史事件，将跟踪历史投递到日志服务SLS。
