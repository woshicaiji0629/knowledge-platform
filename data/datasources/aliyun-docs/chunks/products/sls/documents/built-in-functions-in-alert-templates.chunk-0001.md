| 函数 | 说明 | 过滤器 | 示例 |
| --- | --- | --- | --- |
| string(value) | 将对象转为字符串类型。 | 支持 | {{ string(1.23) }} 的结果为 1.23。 此处的 1.23 为字符串类型。 |
| capitalize(value) | 将字符串的首字母转换为大写形式，其它字符转换为小写形式。 | 支持 | {{ capitalize("heLLO World") }} 的结果为 Hello world。 |
| lower(value) | 将字符串转换为小写形式。 | 支持 | {{ lower("FOO") }} 的结果为 foo。 |
| upper(value) | 将字符串转换为大写形式。 | 支持 | {{ upper("foo") }} 的结果为 FOO。 |
| title(value) | 返回标题化的字符串，即每个单词的首字母为大写形式，其余字母为小写形式。 | 支持 | {{ title("hello world") }} 的结果为 Hello World。 |
| trim(value) | 删除字符串头尾的空字符。 | 支持 | {{ trim(" foo\n") }} 的结果为 foo。 |
| replace(value, old, new) | 替换目标字符串。 | 不支持 | {{ replace("foo", "oo", "ly") }} 的结果为 fly。 |
| wordcount(value) | 统计单词个数。 | 支持 | {{ wordcount("hello world") }} 的结果为 2。 |
| truncate(value, n, end='') | 截断字符串。 通过 truncate(value, n)，指定截断的字符数。 通过 truncate(value, n, end='...')，指定要添加的后缀。 | 不支持 | {{ truncate("foo bar", 5) }} 的结果为 foo b。 {{ truncate("foo bar", 5, end="...") }} 的结果为 foo b...。 |
| quote(value) | 使用半角双引号（""）包裹字符串。 | 支持 | {{ quote(123) }} 的结果为"123" {{ quote("foo") }} 的结果为 "foo"。 |
| indent(value, n=4) | 对每一行字符串进行缩进，默认缩进 4 个空格。 通过 n 参数，可指定缩进的空格数。 | 支持 | {{ "foobar\n" }}{{ indent("foo\nbar") }} 的结果如下： foobar foo bar {{ "foobar\n" }}{{
