### 地图（Pro版本）
以地图作为背景，通过图形颜色、图像标记的方式展示地理数据信息。比如按国家分组统计每个国家的记录数（count）。
(*)| select ip_to_country(remote_addr) as address, count(1) as count group by address order by count desc limit 10
使用场景：[地图](maps.md)用于展示地理空间数据。适用于分析地理位置相关的数据，如人口分布、城市扩张、交通流量等。
选择更多图表，请参见[流图](flow-chart.md)、[计量图](bar-gauge.md)、[直方图](histogram.md)、[雷达图](radar-chart.md)、[交叉表](cross-table.md)、[散点图](scatter-chart.md)、[拓扑图](topology-chart.md)、[火焰图](flame-graph.md)、[Markdown](manage-a-markdown-chart.md)[图表](manage-a-markdown-chart.md)、[时间轴](display-query-results-on-a-timeline-chart.md)、[词云](display-query-results-on-a-word-cloud.md)、[桑基图](display-query-results-in-a-sankey-diagram.md)、[高德地图](gaud-map.md)、[轨迹图](display-query-results-on-a-trail-map.md)、[矩形树图](display-query-results-on-a-treemap-chart.md)、[时序状态图](timing-state-diagram.md)、[漏斗图](display-query-results-on-a-funnel-chart.md)。
