## 标准JSON解析
将Object类型的JSON日志结构化，解析为键值对形式。

| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，固定值为 processor_parse_json_native 。 | # ...在 spec.config 下... processors: # JSON 解析插件配置 - Type: processor_parse_json_native # 原始日志字段来源 SourceKey: content |
| SourceKey String （必选） 源字段名。 |  |
| KeepingSourceWhenParseFail boolean （可选） 解析失败时，是否保留源字段，默认为 false 。 |  |
| KeepingSourceWhenParseSucceed boolean （可选） 解析成功时，是否保留源字段，默认为 false 。 |  |
| RenamedSourceKey String （可选） 保留源字段时，用于存储源字段的字段名，默认不改名。 |  |
