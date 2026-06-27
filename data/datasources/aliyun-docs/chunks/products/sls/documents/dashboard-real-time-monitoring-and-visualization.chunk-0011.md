### 柱状图（Pro版本）
柱状图使用垂直的柱子显示类别之间的数值比较，用于描述分类数据，并统计每一个分类中的数量。例如展示UV最高的前5个host及其页面访问量（PV）。
(*)| select host, COUNT(*) as pv, approx_distinct(remote_addr) as uv GROUP BY host ORDER BY uv desc LIMIT 5
使用场景：[柱状图](column-chart.md)主要用于比较不同类别或不同时间点的数据大小。适用于展示分类数据，如不同产品的销售量、不同地区的人口数量等。
