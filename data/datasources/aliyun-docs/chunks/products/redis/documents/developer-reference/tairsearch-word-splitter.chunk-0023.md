### IK
中文分词器，取值为ik_max_word或ik_smart。ik_max_word会拆分出文档中所有可能存在的Token；ik_smart会在ik_max_word的基础上，对Token进行二次识别，选择出最有可能的Token。
可选参数：
stopwords：停用词，分词器会过滤这些词。数组类型，单个停用词必须是字符串。配置后，会覆盖默认停用词。默认停用词如下：
["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", "with"]
userwords：自定义词典，数组类型，单个词必须是字符串，配置后会追加至默认词典中。默认词典请参见[IK](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20221207/lmbq/main.dic.txt)[默认词典](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20221207/lmbq/main.dic.txt)。
quantifiers：自定义量词词典，数组类型，单个词必须是字符串，配置后会追加至默认量词词典中。默认量词词典请参见[IK](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20221207/rmwb/quantifier.dic.txt)[默认量词词典](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20221207/rmwb/quantifier.dic.txt)。
enable_lowercase：是否将大写字母转换为小写，取值为true（默认，表示开启）或false（不开启）。
重要
由于本参数所控制的操作（将大写字母转换为小写）会发生在分词之前，若自定义词典中存在大写字母，请将本参数设置为false。
配置示例：
