### 格式化函数

| 函数 | 说明 | 过滤器 | 示例 |
| --- | --- | --- | --- |
| escape_markdown(value) | 转义特殊的 Markdown 字符。 | 支持 | {{ escape_markdown("__a__ **b** #c") }} 的结果为 &#95;&#95;a&#95;&#95; &#42;&#42;b&#42;&#42; &#35;c 。 |
| escape_html(value) | 转义特殊的 HTML 字符。 | 支持 | {{ escape_html("<div>") }} 的结果为 &lt;div&gt; 。 |
| to_json(value) | 将对象转为 JSON 格式。 | 支持 | {{ to_json("foo") }} 的结果为"foo"。 {{ to_json(1.23) }} 的结果为 1.23。 {{ to_json(True) }} 的结果为 true。 {{ to_json(alert.labels) }} 的结果为{"host": "host-1", "app": "nginx"}。 |
| parse_json(value) | 将字符串解析为 JSON 数据结构。 | 支持 | {{ parse_json('{"foo": "bar"}').foo }} 的结果为 bar。 {{ parse_json('[1, 2, 3]')[1] }} 的结果为 2。 |
