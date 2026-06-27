"such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", "with"]
userwords：自定义词典，数组类型，单个词必须是字符串，配置后会追加至默认词典中。默认词典请参见[IK](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20221207/lmbq/main.dic.txt)[默认词典](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20221207/lmbq/main.dic.txt)。
quantifiers：自定义量词词典，数组类型，单个词必须是字符串，配置后会追加至默认量词词典中。默认量词词典请参见[IK](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20221207/rmwb/quantifier.dic.txt)[默认量词词典](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20221207/rmwb/quantifier.dic.txt)。
enable_lowercase：是否将大写字母转换为小写，取值为true（默认，表示开启）或false（不开启）。
重要
由于本参数所控制的操作（将大写字母转换为小写）会发生在分词之前，若自定义词典中存在大写字母，请将本参数设置为false。
配置示例：
