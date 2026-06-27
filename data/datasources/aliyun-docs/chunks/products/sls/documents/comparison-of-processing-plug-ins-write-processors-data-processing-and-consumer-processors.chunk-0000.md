## 背景信息
[处理插件配置](customize-logtail-plug-ins-to-process-data.md)：日志服务采集器提供了丰富的处理配置，不仅支持处理插件，还支持以[SPL](use-logtail-spl-to-parse-logs.md)[语句](use-logtail-spl-to-parse-logs.md)在客户端对数据进行处理。
[写入处理器](sls-write-processor.md)：写入处理器可以与LogStore进行关联，写入LogStore的数据会默认由写入处理器在服务端进行处理。
[数据加工](data-processing-new-edition-overview.md)：数据先写入一个源LogStore，然后再根据加工规则进行处理，处理后的数据写入到目标LogStore。
[消费处理器](data-consumption-processor.md)：通过配置消费处理器，支持在消费LogStore时通过SPL实时进行数据处理，消费处理器支持SDK、Flink、DataWorks等三方服务集成。
