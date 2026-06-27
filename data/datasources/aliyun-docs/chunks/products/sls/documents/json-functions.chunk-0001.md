| 函数名称 | 语法 | 说明 | 支持 SQL | 支持 SPL |
| --- | --- | --- | --- | --- |
| [json_array_contains](json-functions.md) [函数](json-functions.md) | json_array_contains( x , value ) | 判断 JSON 数组中是否包含某个值。 | √ | √ |
| [json_array_get](json-functions.md) [函数](json-functions.md) | json_array_get( x , index ) | 获取 JSON 数组中某个下标对应的元素。 | √ | × |
| [json_array_length](json-functions.md) [函数](json-functions.md) | json_array_length( x ) | 计算 JSON 数组中元素的数量。 | √ | √ |
| [json_extract](json-functions.md) [函数](json-functions.md) | json_extract( x , json_path) | 从 JSON 对象或 JSON 数组中提取一组 JSON 值（数组或对象）。 | √ | √ |
| [json_extract_scalar](json-functions.md) [函数](json-functions.md) | json_extract_scalar( x , json_path ) | 从 JSON 对象或 JSON 数组中提取一组标量值（字符串、整数或布尔值）。类似于 json_extract 函数。 | √ | √ |
| [json_extract_bool](json-functions.md) [函数](json-functions.md) | json_extract_bool(x, json_path) | 从 JSON 对象或 JSON 数组中提取 boolean 值。 | √ | × |
| [json_extract_long](json-functions.md) [函数](json-functions.md) | json_extract_long(x, json_path) | 从 JSON 对象或 JSON 数组中提取 bigint 值。 | √ | × |
| [json_extract_double](json-functions.md) [函数](json-functions.md) | json_extract_double(x, json_path) | 从 JSON 对象或 JSON 数组中提取 double 值。 | √ | ×
