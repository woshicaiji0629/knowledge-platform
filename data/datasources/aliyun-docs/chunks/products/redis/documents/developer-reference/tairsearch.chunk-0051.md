### Aggregations查询示例
创建索引。
TFT.CREATEINDEX today_shares '{"mappings":{"properties":{"shares_name":{"type":"keyword"},"logictime":{"type":"long"},"purchase_type":{"type":"integer"},"purchase_price":{"type":"double"},"purchase_count":{"type":"long"},"investor":{"type":"keyword"}}}}' # 创建今日股票交易量索引 # shares_name：股票名称 # logictime：成交时间点 # purchase_type：购买类型 # purchase_price：成交价格 # purchase_count：成交数 # investor：投资者ID
预计输出：
OK
添加文档数据。
依次执行如下命令。
TFT.ADDDOC today_shares '{"shares_name":"XAX","logictime":14300210, "purchase_type":1,"purchase_price":101.1, "purchase_count":100,"investor":"Jay"}' TFT.ADDDOC today_shares '{"shares_name":"XAX","logictime":14300310, "purchase_type":1,"purchase_price":111.1, "purchase_count":100,"investor":"Jay"}' TFT.ADDDOC today_shares '{"shares_name":"YBY","logictime":14300410, "purchase_type":1,"purchase_price":11.1, "purchase_count":100,"investor":"Mila"}'
预计输出：
OK
进行查询。
查询示例如下：
