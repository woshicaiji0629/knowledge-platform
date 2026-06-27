## 日志服务控制台查询分析后报错
如果是查询分析语句相关的问题可以借助Copilot智能辅助工具帮助排查，也可以使用SQL优化进行分析，具体请参考[通过](copilot-automatic-generation-of-ai-assisted-sql-statements.md)[AI](copilot-automatic-generation-of-ai-assisted-sql-statements.md)[智能生成查询与分析语句（Copilot）](copilot-automatic-generation-of-ai-assisted-sql-statements.md)。
在日志服务控制台的查询分析界面中，执行按天统计 Top10 客户端 IP 访问量的 SQL 查询后，查询结果显示日志条数: 0，时间轴图表无数据点；随后 Copilot 智能辅助工具自动介入，弹出诊断建议并修正查询语句，最终返回正确的分析结果。该动画演示了 Copilot 辅助排错的完整流程。
同时日志服务也支持使用本地Agent Skill的方式进行智能查询，具体请参考[SLS Query Skill 智能查询分析日志](sls-query-skill-intelligent-log-query-and-analysis.md)。
