### 迭代
循环语句用于对数组和对象进行迭代操作。支持如下几种使用方式：

| 使用方式 | 示例 |
| --- | --- |
| 数组迭代 | {% for result in alert.results %} {{ result }} {% endfor %} |
| 数组迭代，包含下标 | 使用 enumerate 函数对数组进行下标迭代。关于 enumerate 函数的更多信息，请参见 [enumerate](built-in-functions-in-alert-templates.md) [函数](built-in-functions-in-alert-templates.md) 。 {% for index, result in enumerate(alert.results) %} {{ index }}: {{ result }} {% endfor %} 下标默认从 0 开始。您也可以通过 enumerate 函数中的 start 参数自定义起始下标。例如： {% for index, result in enumerate(alert.results, start=1) %} {{ index }}: {{ result }} {% endfor %} |
| 对象迭代 | 通过 items()方法将对象转为 Key:Value 形式的数组进行迭代。 {% for key, val in alert.labels.items() %} {{ key }}: {{ val }} {% endfor %} |
| 嵌套使用 | {% for result in alert.fire_results %} {% for key, val in result.items() %} {{ key }}: {{ val }} {% endfor %} {% endfor %} |
