## 步骤一：创建索引
创建索引后，才能对日志进行查询分析，索引分为全文索引和字段索引，索引的概念、类型、配置示例、计费说明等信息，请参见[创建索引](create-indexes.md)。本文为网站日志创建字段索引。
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标Logstore。
在LogStore的查询和分析页面的右上角，选择查询分析属性>属性。如果您还未开启索引，请单击开启索引。
配置字段索引，然后单击确定。可以手动逐条添加字段索引，也可以单击自动生成索引，日志服务会根据预览数据中的第一条日志自动配置索引。
重要
配置索引后，只对新写入的数据生效。如果您要查询历史数据，请使用[重建索引](reindex-logs-for-a-logstore.md)。
如果您要使用分析语句（SELECT），必须在配置索引时打开对应字段的统计功能。
日志服务默认已为部分保留字段开启索引。更多信息，请参见[保留字段](reserved-fields.md)。
在查询分析对话框中，单击自动生成索引按钮自动生成字段索引。生成的字段包括 body_bytes_sent（long）、client_ip（text）、host（text）、http_host（text）、http_user_agent（text）、request_length（long）、request_method（text）等。text 类型字段的分词符默认为,"';=()[]{}?@&<>/:\n\t\r，大小写敏感和包含中文开关均关闭，开启统计开关均打开。确认后单击确定。
