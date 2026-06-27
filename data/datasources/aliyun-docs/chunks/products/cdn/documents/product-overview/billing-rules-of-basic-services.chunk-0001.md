## 注意事项
CDN服务计费的流量比日志中记录的流量多。因为CDN日志中记录的流量数据是应用层日志统计出的流量，但是实际网络请求中存在TCP/IP包头的消耗和TCP重传，因此实际产生的网络流量比应用层统计到的流量要高。详细信息，请参见[为什么监控查询流量、用量查询流量与日志统计流量有差异？](traffic-amount-in-the-monitoring-and-usage-analytics-or-in-the-usage-statistics-feature-different-from-the-logged-traffic-amount.md)。
如果您的CDN服务月消费金额大于10万元，阿里云CDN可以为您提供更灵活优惠的按月计费方式。请联系您的阿里云客户经理或通过阿里云[其它渠道](https://help.aliyun.com/zh/document_detail/464625.html#task-2155749)咨询洽谈。
如果您的CDN服务月消费金额不足10万元，或者流量波形不符合按月计费模式的使用要求（例如：月95计费模式不能用于存在异常突发带宽的场景下使用），阿里云CDN保留将月计费模式切换为按流量计费的权利。
阿里云CDN出账时间通常在当前计费周期结束后3~4小时左右，具体以系统实际出账时间为准。
