## 自定义分词器
TairSearch分词器的工作流程依次为Character Filter、Tokenizer和Token Filter，您可以按需配置Character Filter、Tokenizer和Token Filter参数。
配置方法：在properties中配置analyzer为自定义分词器，例如my_custom_analyzer，在settings中，指定自定义分词器（my_custom_analyzer）的相关配置。
参数说明：

| 参数 | 说明 |
| --- | --- |
| type （必选） | 固定为 custom ，表示自定义分词器。 |
| char_filter （可选） | 字符过滤器，在开始 Tokenizer 流程前，对文档进行预处理，默认为空，表示不进行预处理，当前仅支持 Mapping。 参数说明： type （必填）：固定为 mapping ，更多信息请参见 [附录](tairsearch-word-splitter.md) [1：支持的](tairsearch-word-splitter.md) [Character Filter](tairsearch-word-splitter.md) 。 |
| tokenizer （必选） | 分词器，必选且只能选择一个，取值为： whitespace 、 lowercase 、 standard 、 classic 、 letter 、 keyword 、 jieba 、 pattern 、 ik_max_word 和 ik_smart ，更多信息请参见 [附录](tairsearch-word-splitter.md) [2：支持的](tairsearch-word-splitter.md) [Tokenizer](tairsearch-word-splitter.md) 。 |
| filter （可选） | 词元过滤器，对 Token（Tokenizer 的结果）进行处理，例如删除停用词、将词元转换为小写等，支持多选，默认为空，表示不进行处理。 取值为： classic 、 elision 、 lowercase 、 snowball 、 stop 、 asciifolding 、 length 、 arabic_normalization 和 persian_normalization ，更多信息请参见 [附录](tairsearch-word-splitter.md) [3：支持的](tairsearch-word-splitter.md) [Token Filter](tairsearch-word-splitter.md) 。 |

配置示例：
