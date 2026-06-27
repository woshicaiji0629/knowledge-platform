### 通过生命周期规则进行的类型转换、过期删除操作，是否有日志记录？
所有成功通过生命周期规则进行的类型转换、过期删除操作都会有日志记录，日志记录字段如下：
Operation
CommitTransition：转换存储类型。
ExpireObject：删除过期Object。
Sync Request
lifecycle：触发的转换和删除操作。
关于OSS日志字段的更多信息，请参见[日志字段详情](../../../sls/documents/log-fields-13.md)。关于日志查询的费用说明，请参见[计费说明](real-time-log-query.md)。
