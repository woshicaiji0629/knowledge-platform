### Jieba
推荐的中文分词器，可以按照预先训练好的词典或者指定的词典拆分文档，采用Jieba搜索引擎模式，同时将英文Token转为小写，并过滤停用词。
组成部分：
Tokenizer：[Jieba Tokenizer](tairsearch-word-splitter.md)。
Token Filter：[LowerCase Token Filter](tairsearch-word-splitter.md)和[Stop Token Filter](tairsearch-word-splitter.md)。
可选参数：
userwords：自定义词典，数组类型，单个词必须是字符串。配置后会追加至默认词典中，默认词典请参见[Jieba](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20221207/iomh/dict.txt.small.txt)[默认词典](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20221207/iomh/dict.txt.small.txt)。
重要
为了更好的分词效果，Jieba内置了一个较大的词典，约占用20 MB内存，该词典在内存中仅会保留一份。在首次使用Jieba时才会加载词典，这可能会导致首次使用Jieba分词器时延时出现微小的抖动。
自定义词典的单词中不能出现空格与特殊字符：\t、\n、，和。。
use_hmm：对于字典中不存在的词，是否使用隐式马尔科夫链模型判断成词，取值为true（默认，表示开启）或false（不开启）。
stopwords：停用词，分词器会过滤这些词。数组类型，单个停用词必须是字符串。配置后，会覆盖默认停用词。默认停用词请参见[Jieba](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20221207/zqiu/Jieba_stop_words.utf8.txt)[默认停用词](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20221207/zqiu/Jieba_stop_words.utf8.txt)。
配置示例：
