## 分词器的工作流程
TairSearch分词器由Character Filter、Tokenizer和Token Filter三部分组成，其工作流程依次为Character Filter、Tokenizer和Token Filter，其中Character Filter和Token Filter可以为空。其具体作用如下：
Character Filter：负责将文档进行预处理，每个分词器可以配置零个或者多个Character Filter，多个Character Filter会按照指定顺序执行。例如将"(:"字符替换成"happy"字符。
Tokenizer：负责将输入的文档拆分成多个Token（词元），每个分词器仅能配置一个Tokenizer。例如通过Whitespace Tokenizer将"I am very happy"拆分成["I", "am", "very", "happy"]。
Token Filter：负责对Tokenizer产生的Token进行处理，每个分词器可以配置零个或者多个Token Filter，多个Token Filter会按照指定顺序执行。例如通过Stop Token Filter过滤停用词（Stopwords）。
