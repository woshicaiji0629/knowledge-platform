## Column 'XXX' not in GROUP BY clause;please add the column in the index attribute
报错原因
在SQL语句中，如果您使用了GROUP BY子句，则在执行SELECT语句时，只能选择GROUP BY的列或者对任意列进行聚合计算，不允许选择非GROUP BY的列。例如* | SELECT status, request_time, COUNT(*) AS PV GROUP BY status为非法分析语句，因为request_time不是GROUP BY的列。
解决方法
修改查询和分析语句，然后重新执行。例如上述示例的正确语句为* | SELECT status, arbitrary(request_time), count(*) AS PV GROUP BY status。更多信息，请参见[GROUP BY](group-by-clause.md)[子句](group-by-clause.md)。
