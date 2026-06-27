## 分隔符解析
通过分隔符将日志内容结构化，解析为多个键值对形式。支持单字符分隔符和多字符分隔符。

| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，固定值 processor_parse_delimiter_native 。 | # ...在 spec.config 下... processors: # 分隔符解析插件配置 - Type: processor_parse_delimiter_native # 原始字段来源，通常为 content SourceKey: content Separator: ',' Quote: '"' # 按顺序定义提取后的字段名 Keys: - time - ip - request - status - size - user_agent |
| SourceKey String （必选） 源字段名。 |  |
| Separator String （必选） 字段分隔符，例如 CSV 使用逗号 (,)。 |  |
| Keys [String] （必选） 提取的字段列表。 |  |
| Quote String （可选） 引用符，用于包裹包含特殊字符（如逗号）的字段内容。 |  |
| AllowingShortenedFields boolean （可选） 是否允许提取的字段数量小于 Keys 的数量，默认为 true 。若不允许，则此情景会被视为解析失败。 |  |
| OverflowedFieldsTreatment String （可选） 当提取的字段数量大于 Keys 的数量时的行为，默认为 extend 。可选值包括： extend ：保留多余的字段，且每个多余的字段都作为单独的一个字段加入日志，多余字段的字段名为 _column$i_ ，其中 $i 代表额外字段序号，从 0 开始计数。 keep ：保留多余的字段，但将多余内容作为一个整体字段加入日志，字段名为 _column0_ 。 discard ：丢弃多余的字段。 |  |
| KeepingSourceWhenParseFail boolean （可选） 解析失败时，是否保留源字段，默认为 false 。 |  |
| KeepingSourceWhenParseSucceed boolean （可选） 解析成功时，是否保留源字段，默认为 false 。 |  |
| RenamedSourceKey String （可选） 保留源字段时，用于存储源字段的字段名，默认不改名。 |  |
