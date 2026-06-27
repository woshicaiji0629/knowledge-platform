### Standard
基于[Unicode](https://unicode.org/reports/tr29/)[文本切割算法](https://unicode.org/reports/tr29/)拆分文档，并将Token（词元，Tokenizer的结果）转为小写、过滤停用词，适用于多数语言。
组成部分：
Tokenizer（分词器）：[Standard Tokenizer](tairsearch-word-splitter.md)。
Token Filter（词元过滤器）：[LowerCase Token Filter](tairsearch-word-splitter.md)和[Stop Token Filter](tairsearch-word-splitter.md)。
说明
未展示Character Filter（字符过滤器）表示无Character Filter。
可选参数：
stopwords：停用词，分词器会过滤这些词。数组类型，单个停用词必须是字符串。配置后，会覆盖默认停用词。默认停用词如下：
["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", "with"]
max_token_length：每个Token的长度上限，默认为255。若Token超过该长度，会根据指定的长度上限对Token进行拆分。
配置示例：
