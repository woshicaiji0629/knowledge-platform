## 原理
对于事件日志，Windows提供了[Windows Event Log](https://docs.microsoft.com/en-us/windows/desktop/wes/windows-event-log)和[Event Logging](https://docs.microsoft.com/en-us/windows/desktop/EventLog/event-logging)两套API，前者是后者的升级，仅在Windows Vista及以上的版本中提供。Logtail插件会根据所运行的系统，自动选择API（优先选择Windows Event Log）来获取Windows事件日志。
Windows事件日志采用发布订阅的模式，应用程序或者内核将事件日志发布到指定的通道（例如Application、Security、System），Logtail通过对应的Logtail插件调用Windows API，实现对这些通道的订阅，从而不断地获取相关的事件日志并发送到日志服务。
Logtail支持同时采集多个通道事件，例如同时采集应用程序和系统日志。
