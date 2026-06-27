## 工作原理
通过[Logtail](overview-19.md)[采集](overview-19.md)、[日志服务](developer-reference/overview-of-log-service-sdk.md)[SDK](developer-reference/overview-of-log-service-sdk.md)、[Web Tracking](use-the-web-tracking-feature-to-collect-logs.md)[功能](use-the-web-tracking-feature-to-collect-logs.md)等方式采集日志数据，数据会先经过写入处理器（IngestProcessor），然后写入LogStore。数据处理过程在日志服务中完成，不会占用客户端的资源。
写入处理器、[查询和分析日志](use-spl-to-query-and-analyze-logs.md)、[数据加工（新版）](data-processing-new-edition-overview.md)都支持[SPL](spl-overview.md)[语法](spl-overview.md)。
