## 日志样例
本文中介绍的各个案例是基于如下JSON格式的订单处理系统日志。
request字段为订单请求信息，JSON格式。一个请求中包含一个用户的多个订单，订单中包含购买的商品和支付总价。
response字段为订单处理结果。
请求成功时，response字段值为SUCCESS。
请求失败时，response字段值为JSON格式，包含errcode和msg信息。
您可以通过Logtail将该日志采集到日志服务中，进行查询与分析。具体操作，请参见[使用](collect-logs-in-json-mode.md)[JSON](collect-logs-in-json-mode.md)[模式采集日志](collect-logs-in-json-mode.md)。
