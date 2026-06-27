o"。 |
| indent(value, n=4) | 对每一行字符串进行缩进，默认缩进 4 个空格。 通过 n 参数，可指定缩进的空格数。 | 支持 | {{ "foobar\n" }}{{ indent("foo\nbar") }} 的结果如下： foobar foo bar {{ "foobar\n" }}{{ indent("foo\nbar", 2) }} 的结果如下： foobar foo bar |
| startswith(value, prefix) | 判断字符串是否以特定子串开始。 | 支持 | {{ startswith("football", "foo") }} 的结果为 true。 |
| endswith(value, suffix) | 判断字符串是否以特定子串结束。 | 支持 | {{ endswith("football", "all") }} 的结果为 true。 |
| removeprefix(value, prefix) | 移除字符串的前缀。 | 支持 | {{ removeprefix("football", "foot") }} 的结果为 ball。 |
| removesuffix(value, suffix) | 移除字符串的后缀。 | 支持 | {{ removesuffix("football", "ball") }} 的结果为 foot。 |
| split(value, sep=None, maxsplit=-1) | 切割字符串。 通过 sep 参数指定分隔符。 通过 maxsplit 参数限制切割次数。 如果未指定 maxsplit 或设置为-1，表示对切割数量没有限制。 | 支持 | {{ split('a b c ') }} 的结果为['a', 'b', 'c']。 {{ split('a-b-c', sep='-') }} 的结果为['a', 'b', 'c']。 {{ split('a-b-c', sep='-', maxsplit=1) }} 的结果为['a', 'b-c']。 {{ split('a<>b<>c', sep='<>') }} 的结果为['a', 'b', 'c']。 |
