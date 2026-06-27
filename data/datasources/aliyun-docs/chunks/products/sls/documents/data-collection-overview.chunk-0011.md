## 数据脱敏/传输加密能力
[数据传输加密](data-encryption.md)：日志服务支持通过密钥管理服务KMS对数据进行加密存储，同时支持基于SSL/TLS的HTTPS加密传输。
[数据处理](data-processing-sls.md)：对日志数据进行格式化处理，根据数据传输流程阶段有以下三种数据处理方式。
[数据采集时处理（处理插件）](processing-plug-ins.md)：需要基于日志服务自研采集器LoongCollector（原Logtail），数据在从本地服务器往日志服务传输前脱敏，消耗本地服务器资源处理解析。
[数据写入时处理（写入处理器）](sls-write-processor.md)：在数据传输至日志服务但进行存储前处理，可进行脱敏规则的配置，消耗日志服务端资源，处理完成后进行数据存储。
[数据写入后处理（数据加工）](data-processing-new-version-quick-start.md)：对存储于日志服务的数据进行处理，可进行脱敏规则的配置，在往其他LogStore或第三方系统输出前脱敏。
