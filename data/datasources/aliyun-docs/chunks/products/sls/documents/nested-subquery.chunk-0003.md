### 示例3
统计各个访问页面的访问次数及占比。
查询和分析语句
* | SELECT request_uri AS "访问页面", c AS "次数", round(c * 100.0 /(sum(c) over()), 2) AS "百分比%" FROM ( SELECT request_uri AS request_uri, count(*) AS c FROM log GROUP BY request_uri ORDER BY c DESC )
查询和分析结果
该文章对您有帮助吗？
反馈
