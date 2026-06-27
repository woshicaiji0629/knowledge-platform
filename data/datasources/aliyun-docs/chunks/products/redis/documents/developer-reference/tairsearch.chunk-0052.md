## TFT.Search查询示例
创建水果商品索引。
TFT.CREATEINDEX idx:product '{"mappings":{"_source":{"enabled":true},"properties":{"product_id":{"type":"keyword","ignore_above":128},"product_name":{"type":"text"},"product_title":{"type":"text","analyzer":"jieba"},"product_group":{"type":"text","analyzer":"jieba"},"price":{"type":"double"},"stock":{"type":"integer"}}}}'
预期输出：
OK
添加文档数据。
TFT.MADDDOC idx:product '{"product_id":"fruits_001","product_name":"apple","product_title":"新鲜农家有机红苹果。","product_group":"中国山东","price":19.5,"stock":1000}' fruits_1 '{"product_id":"fruits_002","product_name":"banana","product_title":"新鲜野生超甜香蕉。","product_group":"菲律宾","price":24.0,"stock":2000}' fruits_2 '{"product_id":"fruits_003","product_name":"orange","product_title":"网红橘子、新鲜柑橘。","product_group":"中国重庆","price":30.2,"stock":3000}' fruits_3
预期输出：
OK
进行查询。
查询示例如下：
