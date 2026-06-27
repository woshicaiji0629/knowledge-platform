### 数据脱敏
对日志中的敏感数据进行脱敏处理。
效果示例：

| 未经任何处理的原始日志 | 脱敏结果 |
| --- | --- |
| [{'account':'1812213231432969','password':'04a23f38'}, {'account':'1812213685634','password':'123a'}] | [{'account':'1812213231432969','password':'********'}, {'account':'1812213685634','password':'********'}] |

配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>脱敏处理：
原始字段：解析日志前，用于存放日志内容的原始字段。
脱敏方式：
const：将敏感内容替换成所修改的字符串。
md5：将敏感内容替换为其对应的MD5值。
替换字符串：选择脱敏方式为const时，需要输入字符串，用于替换敏感内容。
被替换内容前的内容表达式：用于查找敏感内容，使用[RE2](https://github.com/google/re2/blob/master/doc/syntax.txt)[语法](https://github.com/google/re2/blob/master/doc/syntax.txt)配置。
被替换的内容表达式：敏感内容的表达式，使用[RE2](https://github.com/google/re2/blob/master/doc/syntax.txt)[语法](https://github.com/google/re2/blob/master/doc/syntax.txt)配置。
