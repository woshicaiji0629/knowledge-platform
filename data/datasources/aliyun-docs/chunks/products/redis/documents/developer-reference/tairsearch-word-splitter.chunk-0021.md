### jieba
推荐的中文分词器，可以按照预先训练好的词典或者指定的词典拆分文档。
可选参数：
userwords：自定义词典，数组类型，单个词必须是字符串。配置后会追加至默认词典中，默认词典请参见[Jieba](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20221207/iomh/dict.txt.small.txt)[默认词典](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20221207/iomh/dict.txt.small.txt)。
重要
自定义词典的单词中不能出现空格与特殊字符：\t、\n、，和。。
use_hmm：对于字典中不存在的词，是否使用隐式马尔科夫链模型判断成词，取值为true（默认，表示开启）或false（不开启）。
配置示例：
