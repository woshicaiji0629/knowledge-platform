### 控制台
删除前清理。
删除LogStore前需先删除其对应的所有Logtail配置。
若该LogStore启用了日志投递，删除前请停止向该LogStore写入新数据，并确认LogStore中已有的数据已全部投递成功。
删除LogStore前，在任务管理中查看当前Project的全部任务，并删除与当前LogStore关联的任务。
删除步骤。
在日志存储>日志库页签中，将鼠标悬浮在目标LogStore上，选择删除。
在警告对话框中，单击确认删除。
删除后事项。
删除LogStore的当天仍会产生存储等费用，次日不再产生费用。即在删除LogStore的第三天不会再收到日志服务的账单。
删除LogStore后，以当前LogStore为数据源的导出任务、数据加工任务、定时SQL任务和以当前LogStore为目标的导入任务都将被删除。
