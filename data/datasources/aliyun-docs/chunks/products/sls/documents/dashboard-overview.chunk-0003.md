### 2. 添加统计图表
单击添加新图表。
配置和保存统计图表：
在页面左侧配置查询时间范围、LogStore、查询分析语句。
在页面右侧配置图表类型为折线图、x轴为t、y轴为pv、聚合列为request_method，单击页面上方的应用查看图表配置效果，然后单击确定保存图表。
查询分析语句如下：
SELECT DATE_FORMAT(DATE_TRUNC('minute', __time__), '%m-%d %H:%i') AS t, request_method, COUNT(*) AS pv GROUP BY t, request_method ORDER BY t ASC LIMIT 10000;
拖动统计图表调整大小，然后单击页面右上角的保存。
在弹出的保存仪表盘对话框中，填写仪表盘名称和备注，然后单击确认完成保存。
