## JSON数组解析
使用json_extract函数，从JSON数组中提取JSON对象，更多json函数请参考[JSON](json-functions.md)[函数](json-functions.md)。

| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，SPL 插件类型为 processor_spl 。 | # ...在 spec.config 下... processors: # 使用 SPL 脚本处理日志字段 - Type: processor_spl # 脚本超时时间（单位：毫秒） TimeoutMilliSeconds: 1000 # SPL 脚本内容，用于从 content 字段中提取 JSON 数组中的元素 Script: >- * | extend json1 = json_extract(content, '$[0]'), json2 = json_extract(content, '$[1]') |
| Script String （必选） SPL 脚本内容，用于从 content 字段中提取 JSON 数组中的元素。 |  |
| TimeoutMilliSeconds integer （可选） 脚本超时时间，取值范围 0~10000，单位为毫秒，默认 1000。 |  |
