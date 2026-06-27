### 审计策略
审计策略定义了审计功能的配置和请求的采集规则。不同审计级别（Audit Level）的事件日志采集规则不同。Audit Level包括以下几种。

| Audit Level | 日志采集规则 |
| --- | --- |
| None | 符合规则的事件不予采集。 |
| Metadata | 采集请求的 Metadata，例如用户信息、时间戳等，但不采集请求体或返回体。 |
| Request | 采集请求的 Metadata 和请求体，但不采集返回体。不适用于非资源请求（Non-Resource Request）。 |
| RequestResponse | 采集请求的 Metadata、请求体和返回体。不适用于非资源请求（Non-Resource Request）。 |
