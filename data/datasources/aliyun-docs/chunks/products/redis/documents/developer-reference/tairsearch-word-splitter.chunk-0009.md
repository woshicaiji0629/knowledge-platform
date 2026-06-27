### Pattern
根据指定的正则表达式拆分文档，正则表达式匹配的词将作为分隔符。例如指定的正则表达式是"aaa"，对"bbbaaaccc"文档进行分词，会得到"bbb"和"ccc"，同时根据lowercase参数决定是否将英文Token转为小写，并过滤停用词。
组成部分：
Tokenizer：[Pattern Tokenizer](tairsearch-word-splitter.md)。
Token Filter：[LowerCase Token Filter](tairsearch-word-splitter.md)和[Stop Token Filter](tairsearch-word-splitter.md)。
可选参数：
pattern：正则表达式，正则表达式匹配的词将作为分隔符，默认为\W+，更多语法信息请参见[Re2](https://github.com/google/re2/wiki/Syntax)。
stopwords：停用词，分词器会过滤这些词。配置时，停用词词典必须是一个数组，每个停用词必须是字符串，配置停用词后会覆盖默认停用词。默认停用词如下：
["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", "with"]
lowercase：是否将Token转换为小写，取值为true（默认，表示开启）或false（不开启）。
flags：正则表达式是否大小写敏感，默认为空（表示大小写敏感），取值为CASE_INSENSITIVE（表示大小写不敏感）。
配置示例：
