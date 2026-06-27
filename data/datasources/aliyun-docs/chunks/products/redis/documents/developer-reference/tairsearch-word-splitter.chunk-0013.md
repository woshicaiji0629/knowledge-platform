### Language
支持多国语言分词器，包括：chinese、arabic、cjk、brazilian、czech、german、greek、persian、french、dutch和russian。
可选参数：
stopwords：停用词，分词器会过滤这些词。配置时，停用词词典必须是一个数组，每个停用词必须是字符串，配置停用词后会覆盖默认停用词。各语言的默认停用词请参见[附录](tairsearch-word-splitter.md)[4：内置分词器](tairsearch-word-splitter.md)[Language](tairsearch-word-splitter.md)[各语言的默认停用词（Stopwords）](tairsearch-word-splitter.md)。
说明
暂不支持修改chinese分词器的停用词。
stem_exclusion：指定不需要进行词干化处理的词（Term），例如"apples"进行词干化处理后为"apple"。本参数默认为空，配置时，stem_exclusion必须是一个数组，每个词必须是字符串。
说明
仅brazilian、german、french和dutch分词器支持本参数。
配置示例：
