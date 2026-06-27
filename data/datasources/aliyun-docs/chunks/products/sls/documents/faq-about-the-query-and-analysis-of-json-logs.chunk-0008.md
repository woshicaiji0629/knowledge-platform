## 如何设置json_path？
使用json_extract等函数从JSON日志中提取字段时，您需指定json_path，用于标明需要提取JSON对象中的哪一部分。json_path格式为$.a.b，美元符号（$）代表当前JSON对象的根节点，然后通过半角句号（.）引用到待提取的节点。
如果JSON对象的字段中存在特殊字符（例如http.path字段、http path字段、http-path字段等），则需要使用中括号[]代替半角句号（.），然后使用双引号（""）包裹字段名，例如* |SELECT json_extract_scalar(request, '$["http.path"]')。
说明
如果是通过SDK进行查询和分析，则需要对双引号（""）进行转义，例如* | select json_extract_scalar(request, '$[\"http.path\"]')。
提取JSON数组中的某个元素时，可以用中括号[]。在中括号中，通过数字来表示下标，下标从0开始。例如：
查看用户第一个订单的金额。
* | SELECT json_extract_scalar(request, '$.param.orders[0].payment')
查询和分析结果如下所示。
查看用户第一个订单中购买的第二件商品。
* | SELECT json_extract_scalar(request, '$.param.orders[0].commodity[1]')
查询和分析结果如下所示。
