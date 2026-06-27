## TFT.ANALYZER

| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.ANALYZER analyzer_name text [INDEX index_name] [SHOW_TIME] |
| 命令描述 | 查询分词器分词效果。 |
| 选项 | analyzer_name ：分词器名称，支持内置分词器和自定义分词器。 若指定自定义分词器或修改了内置分词器的配置（停用词或词典），您还需要指定创建该分词器的索引名称（INDEX）。 text ：待分词的文档，utf-8 格式。 INDEX （可选）：分词器的索引名称。若指定自定义分词器或修改了内置分词器的配置（停用词或词典），该参数必选。 SHOW_TIME （可选）：指定是否返回分词执行的时间，单位为微秒（us）。 该时间包含词库加载的时间，当第一次加载 JiebaAnalyzer、IKAnalyzer 等具有较大内置词库的分词器时，耗时可能会达到秒级。 |
| 返回值 | 执行成功：返回 Token 信息，JSON 格式。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.ANALYZER standard "Tair is a nosql database" 返回示例： '{ "tokens":[ { "token":"Tair", "start_offset":0, "end_offset":4, "position":0 }, { "token":"nosql", "start_offset":10, "end_offset":15, "position":3 }, { "token":"database", "start_offset":16, "end_offset":24, "position":4 } ] }' |
