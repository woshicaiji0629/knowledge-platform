### 基本语法
查询语句和分析语句以竖线|分割。查询语句可单独使用，分析语句必须与查询语句一起使用。即分析功能是基于查询结果或全量数据进行的。
查询语句|分析语句

| 类型 | 说明 |
| --- | --- |
| 查询语句 | 查询语句用于指定日志查询时的过滤规则，返回符合条件的日志。格式为： 查询语句 ，例如 status: 200 。 查询条件可使用关键词、数值、数值范围、空格、 * 等。 如果为空格或 * ，表示无过滤条件。更多信息，请参见 [查询语法与功能](query-syntax.md) 。 重要 查询语句中建议不超过 30 个条件。 |
| 分析语句 | 如需使用分析功能，则必须将日志采集到 Standard LogStore 中，且在配置索引时打开对应字段的 开启统计 开关。 分析语句对查询结果或全量数据进行计算和统计。日志服务支持的分析函数和语法，请参见： [SQL](sql-function.md) [函数](sql-function.md) ：SQL 函数通常用于对数据进行计算、转换和格式化。例如，计算总和、平均值、字符串操作、日期处理等。 [SQL](sql-syntax.md) [子句](sql-syntax.md) ：SQL 子句用于构建完整的 SQL 查询或数据操作语句，决定数据的来源、条件、分组、排序等。 [嵌套子查询](nested-subquery.md) ：嵌套子查询是指将一个 SELECT 语句嵌套在另一个 SELECT 语句中，用于复杂的分析场景。 [Logstore](join-queries-on-a-logstore-and-a-mysql-database.md) [和](join-queries-on-a-logstore-and-a-mysql-database.md) [MySQL](join-queries-on-a-logstore-and-a-mysql-database.md) [联合查询分析](join-queries-on-a-logstore-and-a-mysql-database.md) ：支持通过 Join 语法将 LogStore 与 MySQL 联合查询，结果可保存至 MySQL。 [使用](use-spl-to-query-and-analyze-logs.md) [SPL](use-spl-to-query-and-analyze-logs.md) [查询和分析日志](use-spl-to-query-and-analyze-logs.md) ：当您需要对日志数据进行结构化信息提取、字段操作和数据过滤时，可以使用 SPL。 重要 分析语句默认分析当前 LogStore 中的数据，不需要填写 FROM 子句和 WHERE 子句。 分析语句不支持使用 offset，不区分大小写，末尾不需要加分号。 |
