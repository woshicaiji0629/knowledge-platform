m" }
origin_request_header
功能说明：配置回源HTTP请求头（新），该功能详细介绍请参见控制台配置说明[修改出站请求头](../user-guide/configure-custom-request-headers.md)。
功能ID（FunctionID/FuncId）：228。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| header_operation_type | String | 是 | 请求头操作，取值： add：添加。 delete：删除。 modify：变更。 rewrite：替换。 | add |
| header_name | String | 是 | 请求头名称。 | Accept-Encoding |
| header_value | String | 否 | 请求头值。一个请求头参数中可以配置多个值，多个值用英文逗号（,）分隔。 | gzip |
| duplicate | String | 否 | 是否允许重复添加名称相同的请求头。当 header_operation_type 使用 add 时（即执行增加操作），需要设置是否允许重复： on：允许。 off：不允许。 | off |
| header_source | String | 否 | 查找需要替换的参数值。当 header_operation_type 使用 rewrite 时（即执行替换操作），需要设置该参数，取值支持正则表达式。 | value1 |
| header_destination | String | 否 | 替换后的参数值。当 header_operation_type 使用 rewrite 时（即执行替换操作），需要设置该参数。 | value123 |
| match_all | String | 否 | 设置匹配模式。当 header_operation_type 使用 rewrite 时（即执行替换操作），需要设置匹配模式： on：匹配所有（所有匹配上的值都会被替换）。 off：仅匹配第一个（只有第一个匹配上的值会被替换）。 | off |
