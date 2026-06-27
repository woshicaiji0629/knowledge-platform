### 列表和对象函数

| 函数 | 说明 | 过滤器 | 示例 |
| --- | --- | --- | --- |
| enumerate(value) | 将一个可迭代的对象组合为一个索引序列，并列出原始元素和元素的下标。 | 不支持 | {{ enumerate(["foo", "bar"]) }} 的结果为[(0, 'foo'), (1, 'bar')]。 |
| list(value) | 将一个可迭代的对象转换为列表类型。 | 支持 | {{ list(("foo", "bar")) }} 的结果为 ['foo', 'bar']。 {{ list("foo") }} 的结果为 ['f', 'o', 'o']。 |
| dict(value) | 创建一个字典，类似于直接使用 {} 创建字典。 | 不支持 | {{ dict(foo=1, bar="hello") }} 的结果为{'foo': 1, 'bar': 'hello'}。 |
| first(value) | 返回列表中的第一项。 | 支持 | {{ first([1, 2, 3]) }} 的结果为 1。 |
| last(value) | 返回列表中的最后一项。 | 支持 | {{ last([1, 2, 3]) }} 的结果为 3。 |
| sort(value, reverse=true) | 对列表中的元素进行排序。 通过 reverse=true ，可实现逆序排序。 | 支持 | {{ sort([3, 1, 2]) }} 的结果为[1, 2, 3]。 {{ sort([3, 1, 2], reverse=true) }} 的结果为[3, 2, 1]。 |
| dictsort(value) | 将对象中的键值对（Key:Value）按照 Key 进行排序，返回数组。 | 支持 | alert.labels 字段示例 { "host": "host-1", "app": "nginx" } 内容模板配置 {%- for key, val in dictsort(alert.labels) %} {{ key }}: {{ val }} {%- endfor %} 结果 app: nginx host: host-1 |
| join(value, d='') | 使用连接符连接列表中的元素。 通过 d 参数，可指定连接符。 | 支持 | {{ join([1, 2, 3]) }} 的结果为 123。 {{ join([1, 2, 3], ',') }} 的结果为 1,2,3。 |
