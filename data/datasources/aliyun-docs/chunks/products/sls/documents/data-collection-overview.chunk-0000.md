## 数据采集方式
数据采集作为使用日志服务功能的第一步，目的是将目标数据传输并保存到日志服务中，以便后续使用日志服务的其他功能。例如对数据进行[查询与分析](quick-guide-to-query-and-analysis.md)，对数据格式与内容进行[数据加工处理](data-processing-new-version-quick-start.md)，将数据[消费](data-consumption-and-subscription.md)或[投递](data-shipping-overview.md)到第三方系统等。
重要
日志服务提供的采集方式仅支持采集增量数据，若需要历史数据请使用[数据导入](data-collection-overview.md)。
概念介绍：
[LoongCollector（原](loongcollector-collection.md)[Logtail）](loongcollector-collection.md)：Logtail是日志服务提供的日志采集Agent，用于采集阿里云ECS、自建IDC或其他云厂商等服务器上的日志。Logtail基于日志文件采集，无需修改应用程序代码，且采集日志不会影响应用程序运行。LoongCollector是日志服务推出的新一代采集Agent，是Logtail的升级版，兼容Logtail的同时性能更佳。
[SDK](use-sdks-to-collect-logs.md)[采集](use-sdks-to-collect-logs.md)：日志服务支持直接使用SDK/API等方式在代码中进行定制化开发，相比其他方式灵活性更高。
