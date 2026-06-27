## 删除MetricStore
重要
删除MetricStore前必须删除其对应的Logtail配置。具体操作，请参见[删除](manage-logtail-configurations-for-log-collection.md)[Logtail](manage-logtail-configurations-for-log-collection.md)[采集配置](manage-logtail-configurations-for-log-collection.md)。
如果该MetricStore上还启用了数据投递，建议删除前停止向该MetricStore写入新数据，并确认MetricStore中已有的数据已经全部投递成功。
删除全部MetricStore的当天仍会产生存储等费用，次日不再产生任何费用。即您在删除全部MetricStore的第三天不会再收到日志服务的账单。
删除MetricStore后，以当前MetricStore为数据源的导出任务、数据加工任务、定时SQL任务和以当前MetricStore为目标的导入任务都将被删除。
删除MetricStore前，建议在任务管理>全部任务查看当前Project的全部任务，并删除与当前MetricStore关联的任务。
在时序存储>日志库页签中，将鼠标悬浮在目标MetricStore上，选择删除。
警告
MetricStore一旦删除，其存储的时序数据将会被永久删除，不可恢复，请谨慎操作。
在确认对话框中，单击确认。
