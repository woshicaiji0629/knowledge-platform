### 示例2
统计所有成功的请求中，每一种商品被购买的数量。您可以先提取order字段，将其转换为array(json)类型，再使用UNNEST语句将其展开，展开结果中的每一行代表一个订单。然后使用json_extract函数提取commodity字段，将其转换为array(json)类型，再使用UNNEST语句将其展开，展开结果中的每一行代表一个商品。最后再进行分组求和。具体思路请参见示例1。
* and response: SUCCESS | SELECT item, count(1) AS cnt FROM ( SELECT orderinfo FROM log, unnest( cast( json_extract(request, '$.param.orders') AS array(json) ) ) AS t(orderinfo) ), unnest( cast( json_extract(orderinfo, '$.commodity') AS array(json) ) ) AS t(item) GROUP BY item ORDER BY cnt DESC
查询和分析结果如下所示。
该文章对您有帮助吗？
反馈
