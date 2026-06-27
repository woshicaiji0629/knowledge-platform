### 分析语句
用于对日志数据进行过滤、转换、统计、聚合等操作，例如统计一段时间内数据的平均值、获取数据的同比和环比结果。分析语句必须配合查询语句一起使用，格式为查询语句|分析语句，语法说明请参见[SQL](sql-syntax-and-functions.md)[分析语法与功能](sql-syntax-and-functions.md)。
示例：查询日志中所有记录，并分析各请求状态的数量，可使用以下语句。
* | SELECT status, count(*) AS PV GROUP BY status
更多查询分析示例，请参见[SQL](sql-function.md)[函数](sql-function.md)和[SQL](sql-syntax.md)[子句](sql-syntax.md)。
说明
默认情况下，在日志库列表单击LogStore时，系统会进入查询 / 分析页面并自动执行一次查询操作。您可单击页面右上角的图标，在查询设置页签下，关闭该功能或设置查询时间。
