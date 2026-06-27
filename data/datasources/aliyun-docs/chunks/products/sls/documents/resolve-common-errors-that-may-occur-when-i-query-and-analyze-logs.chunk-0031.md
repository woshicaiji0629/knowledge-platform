## Invalid JSON path: ...[​](https://sls.aliyun.com/doc/sqlerror/invalid_json_path.html#invalid-json-path)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
非法JSON访问路径。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
您在SQL中使用JSON函数（如json_extract、json_extract_scalar、json_size等）访问指定的JSON路径时，未指定有效路径。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
正常指定json_path，格式为$.a.b。其中$代表当前JSON对象的根节点，半角句号.引用到待提取的节点（可级联），但是当JSON对象的字段中存在特殊字符（如.、空格、-等），例如 http.path、http path、http-path等，则需要使用中括号[]代替半角句号.，然后使用双引号""包裹字段名，例如：
* | SELECT json_extract_scalar(request, '$["X-Power-Open-App-Id"]')
您可以参考[JSON](json-functions.md)[函数](json-functions.md)使用说明，了解JSON函数和json_path的具体用法。您还可以参考[查询和分析](faq-about-the-query-and-analysis-of-json-logs.md)[JSON](faq-about-the-query-and-analysis-of-json-logs.md)[日志的常见问题](faq-about-the-query-and-analysis-of-json-logs.md)了解json_path的具体使用方式。
