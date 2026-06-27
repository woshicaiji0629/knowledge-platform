## 分页方式概述
日志服务支持在使用[GetLogs API](developer-reference/api-sls-2020-12-30-getlogs.md)查询分析日志时对查询分析结果内容进行分页，查询结果和分析结果使用不同的分页方法。若要提前获取总的日志行数，请参见[GetHistograms](developer-reference/api-sls-2020-12-30-gethistograms.md)。
查询语句：使用关键字查询，获取原始日志内容。通过GetLogs API中的offset和line参数实现分页。更多信息，请参见[查询概述](log-search-overview.md)。
分析语句：使用SQL对查询结果进行分析，获取统计结果。通过SQL中的LIMIT语法实现分页。更多信息，请参见[查询与分析概述](log-analysis-overview.md)和[LIMIT](limit-clause.md)[子句](limit-clause.md)。
