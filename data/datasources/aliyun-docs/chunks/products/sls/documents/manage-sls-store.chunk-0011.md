### 事件数据（Event）
事件（Event）是指值得关注的、有价值的数据。例如监控告警数据、定期巡检作业的结果等。日志服务的事件数据遵循[CloudEvents](https://cloudevents.io/)协议规范，具体说明如下表所示。

| 字段类型 | 字段名 | 是否必选 | 数据格式 | 说明 |
| --- | --- | --- | --- | --- |
| 协议字段 | specversion | 是 | String | 根据 CloudEvents 协议规范，默认使用 1.0 。 |
| id | 是 | String | 事件 ID，您可以根据 source+id 来区分事件的唯一性。 |  |
| source | 是 | String | 通常用来标识事件发生的上下文信息，例如事件来源、发布事件的实例等。 |  |
| type | 是 | String | 事件类型，例如 sls.alert 。 |  |
| subject | 否 | String | 事件主题，是对 source 字段的补充，例如用于描述实际触发事件的对象。 |  |
| datacontenttype | 否 | String | 事件类型，默认取值为 application/cloudevents+json 。 |  |
| dataschema | 否 | URI | data 字段需要遵循的 Schema，默认为空。 |  |
| data | 否 | JSON | 具体的事件内容。不同来源和类型的事件格式会有差异。 |  |
| time | 是 | Timestamp | 事件时间，具体格式，请参见 [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) 。例如 2022-10-17T11:20:45.984+0800 。 |  |
| 扩展字段 | title | 是 | String | 事件标题。 |
| message | 是 | String | 事件描述。 |  |
| status | 是 | String | 事件状态。取值： ok info warning error |  |
