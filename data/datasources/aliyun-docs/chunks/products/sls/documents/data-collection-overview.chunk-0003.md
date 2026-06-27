### 主机/服务器中数据采集方案
当企业应用部署在阿里云ECS，自建服务器或其他云服务器等主机环境下，使用阿里云日志服务进行采集时请参考如下内容：
[持续采集主机文本日志](host-text-log-collection-auto-install.md)：对于应用日志支持多种解析格式，如Nginx,JSON,Apache,IIS,分隔符等，需要重点注意不同服务器与日志服务Project的关系，会影响日志服务采集器的安装方式。
[采集主机监控数据(Metric)](collect-metric-data-from-hosts.md)：支持采集主机CPU、内存、负载、磁盘、网络等监控数据。
[采集](collect-windows-event-logs.md)[Windows](collect-windows-event-logs.md)[事件日志](collect-windows-event-logs.md)：Windows事件日志采用发布订阅的模式，应用程序或者内核将事件日志发布到指定的通道，日志服务调用Windows API订阅这些通道，从而持续获取相关事件日志。
