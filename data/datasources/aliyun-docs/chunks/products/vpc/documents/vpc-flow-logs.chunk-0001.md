## 使用限制
首次使用流日志功能时，需要：
在[流日志页面](https://vpc.console.aliyun.com/flowlog/)单击立即开通。如果曾在公测期间创建过流日志实例，也需单击立即开通后才能重新查看和管理这些实例。
在[流日志页面](https://vpc.console.aliyun.com/flowlog/)单击立即授权，然后单击确认授权。该操作会自动创建1个RAM角色AliyunVPCLogArchiveRole和1个RAM策略AliyunVPCLogArchiveRolePolicy，VPC默认通过此角色和策略来访问日志服务，来保证将流日志写入日志服务中。
已在[日志服务产品页](https://www.aliyun.com/product/sls/)开通了日志服务。
开启流日志后，新建弹性网卡的首次采集可能存在时间延迟（通常＜10分钟）。
流日志不支持采集[组播](../../cen/documents/user-guide/multicast-overview.md)流量。
