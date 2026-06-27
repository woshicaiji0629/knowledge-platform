### 用法
通常情况下，在aggs子句中，您需要自定义聚合名称，并指定聚合类型与聚合字段（field），仅支持聚合数值类型与keyword类型的字段，例如：
TFT.SEARCH shares '{"query":{"term":{"investor":"Jay"}},"aggs":{"Jay_Sum":{"sum":{"field":"purchase_price"}}}}' # 自定义聚合名称为Jay_Sum、聚合类型为sum（求和）、聚合字段为purchase_price。
返回结果包含query的查询结果和aggs的聚合结果：
{"hits":{"hits":[{"_id":"16581351808123930","_index":"today_shares0718","_score":1.0,"_source":{"shares_name":"XAX","logictime":14300210,"purchase_type":1,"purchase_price":101.1,"purchase_count":100,"investor":"Jay"}},{"_id":"16581351809626430","_index":"today_shares0718","_score":1.0,"_source":{"shares_name":"XAX","logictime":14300310,"purchase_type":1,"purchase_price":111.1,"purchase_count":100,"investor":"Jay"}}],"max_score":1.0,"total":{"relation":"eq","value":2}},"aggregations":{"Jay_Sum":{"value":212.2}}}
说明
您可以在查询语句中加上"size":0，将仅返回aggs的结果。
