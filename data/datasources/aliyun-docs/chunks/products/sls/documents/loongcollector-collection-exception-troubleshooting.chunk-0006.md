### 日志格式错误
采集格式不符合预期，检查采集配置信息,参考[持续采集主机文本日志](host-text-log-collection-auto-install.md)使用完整正则模式和插件模式提取字段。
json字段无法被解析提取：通过解析工具验证日志内容是否严格符合json object，插件不支持非json objet的解析，可以尝试修改原始字段格式来规避。
一整条日志是一个整体：可能是未设置分词符导致的，建议[了解索引内容按需配置](quick-guide-to-query-and-analysis.md)。
