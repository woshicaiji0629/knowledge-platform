### 饼图（Pro版本）
饼图通过将一个圆饼按照分类的占比划分成多个区块，整个圆饼代表数据的总量，每个区块（圆弧）表示该分类占总体的比例大小，所有区块（圆弧）的加和等于 100%。比如统计每个request_method（请求方法，如GET、POST等）的次数。
(*)| SELECT request_method, arbitrary(request_length) as len, COUNT(*) as c group by request_method
使用场景：[饼图](pie-chart.md)主要用于展示数据的占比关系。它适用于展示不同部分在整体中的比例，如不同产品的市场份额、各个部门的预算比例等。
