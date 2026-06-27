于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。
功能ID（FunctionID/FuncId）：235。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| variable_type | String | 是 | 变量类型，取值： header：用户请求中携带的 header（request header）。 arg：用户请求 URL 中携带的参数（query string parameter）。 uri：用户请求 URL 中携带的路径（path）。 cookie：用户请求中携带的 cookie（request cookie）。 | uri |
| variable | String | 是 | 变量名称。 说明 variable_type=uri 的情况下，variable 只能固定=uri。 | uri |
| conditions | String | 是 | 条件，取值： ==：表示“等于”。 !=：表示“不等于”。 | == |
| value | String | 是 | 变量的取值。 | /image |
| origin | String | 是 | 回源查询 DNS 使用的域名（即用户请求中对应的变量值，匹配后需要回源到指定的源站地址）。 | origin.example.com |
