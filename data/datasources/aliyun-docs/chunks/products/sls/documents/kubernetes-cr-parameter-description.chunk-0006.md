### spec.config
采集配置主体，定义具体的输入、处理、输出插件。

| 子字段 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| sample | string | 否 | 日志样例，支持多条日志，总长度不超过 1500 字节。 |
| global | object | 否 | [全局配置](developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md) 。 |
| inputs | object 列表 | 是 | [输入插件](developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md) 列表，目前只允许配置 1 个输入插件。 |
| processors | object 列表 | 否 | 处理插件列表： [原生插件](developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md) [扩展插件](developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md) |
| flushers | object 列表 | 是 | [输出插件](developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md) 列表，目前只允许存在 1 个 flusher_sls 插件。 |
