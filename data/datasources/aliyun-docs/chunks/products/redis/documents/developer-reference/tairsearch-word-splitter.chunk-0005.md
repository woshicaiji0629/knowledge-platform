### Stop
根据非字母（non-letter）的符号拆分文档，并将Token转为小写，同时过滤停用词。
组成部分：
Tokenizer：[LowerCase Tokenizer](tairsearch-word-splitter.md)。
Token Filter：[Stop Token Filter](tairsearch-word-splitter.md)。
可选参数：
stopwords：停用词，分词器会过滤这些词。数组类型，单个停用词必须是字符串。配置后，会覆盖默认停用词。默认停用词如下：
["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", "with"]
配置示例：
