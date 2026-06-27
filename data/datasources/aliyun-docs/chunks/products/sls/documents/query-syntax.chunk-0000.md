## 基础语法
说明
[SLS Query Skill 智能查询分析日志](sls-query-skill-intelligent-log-query-and-analysis.md)：日志服务提供了Agent Skill，支持在本地 AI Agent 中通过自然语言查询和分析 SLS 日志数据。
[通过](copilot-automatic-generation-of-ai-assisted-sql-statements.md)[AI](copilot-automatic-generation-of-ai-assisted-sql-statements.md)[智能生成查询与分析语句（Copilot）](copilot-automatic-generation-of-ai-assisted-sql-statements.md)：日志服务也提供了AI智能辅助SQL语句的使用，支持自然语言生成SQL、解释复杂SQL、优化SQL语句。
查询语句与分析语句以|分割，格式为查询语句|分析语句，示例如下：
* | SELECT status, count(*) AS PV GROUP BY status

| 语句类型 | 说明 |
| --- | --- |
| 查询语句 | 查询条件，可以为关键词、数值、数值范围、空格、星号（*）等。 如果为空格或星号（*），表示无过滤条件。 重要 查询语句中建议不超过 30 个条件。 |
| 分析语句 | 重要 必须与查询语句一起使用，分析语句中无需填写 FROM 子句和 WHERE 子句，默认分析当前 LogStore 中的数据。分析语句不支持 offset，不区分大小写，末尾无需加分号。 对查询结果或全量数据进行计算和统计。日志服务支持的分析函数和语法： [SQL](sql-function.md) [函数](sql-function.md) [SQL](sql-syntax.md) [子句](sql-syntax.md) [机器学习函数](machine-learning-functions.md) |
