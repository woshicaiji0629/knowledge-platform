# This is a comment # Another comment # Yet another comment
执行以下命令：
:%s/^\s*#\s\?//
说明：
^：匹配行首。
\s*：匹配任意数量的空白字符（用于处理缩进）。
#：注释符号。
\s\?：匹配注释符后的一个可选空格。
//：表示将匹配到的内容替换为空，即删除。
命令会遍历整个文件，去除后文件如下所示：
This is a comment Another comment Yet another comment
