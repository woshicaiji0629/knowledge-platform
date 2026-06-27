### 命令结构
ossutil常用命令格式如下：
ossutil command [argument] [flags] ossutil command subcommond [argument] [flags] ossutil topic
argument：参数，为字符串。
flags：选项，支持短名字风格-o[=value]/ -o [ value]和长名字风格--options[=value]/--options[ value]。如果多次指定某个排它参数，则仅最后一个值生效。
命令示例如下：
命令：ossutil cat oss://bucket/object
多级命令：ossutil api get-bucket-cors --bucket bucketexample
帮助主题：ossutil filter
