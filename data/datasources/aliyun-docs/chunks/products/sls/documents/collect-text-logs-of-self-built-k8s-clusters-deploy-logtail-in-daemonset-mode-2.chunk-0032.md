### 配置多行日志采集
日志服务默认为单行模式，按行进行日志的切分与存储，导致含堆栈信息的多行日志被逐行切分，每一行作为独立日志存储和展示，不利于分析。
针对上述问题，可通过开启多行模式来改变日志服务的切分方式，并通过配置正则表达式匹配日志起始行，从而将原始日志按照起始行规则进行切分和存储。
核心配置：在[spec.config.inputs](kubernetes-cr-parameter-description.md)配置中添加Multiline参数。

| 关键字段详解 | 示例 |
| --- | --- |
| Multiline 开启多行日志采集功能。 Mode 模式选择，默认值为 custom 。 custom ：表示自定义正则表达式匹配行首。 JSON ：多行 JSON。 StartPattern 行首正则表达式，Mode 取值为 custom 时必填 。 | # ...在 spec.config 下... inputs: - Type: input_file # 开启多行日志采集功能 Multiline: # 模式选择：custom 表示自定义正则表达式匹配行首 Mode: custom # 正则表达式匹配每条日志的起始行（即新日志开始的标志） StartPattern: '\d+-\d+-\d+\s\d+:\d+:\d+' |
