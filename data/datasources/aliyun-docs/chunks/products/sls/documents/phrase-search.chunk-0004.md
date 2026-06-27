## 示例
例如您要查询包含redo_index/1的日志。
使用非短语查询语句"redo_index/1"，日志服务将根据全文索引匹配部分关键词。在搜索栏中直接输入redo_index/1进行非短语查询时，日志服务会按分词符/拆分查询词，匹配到包含redo_index和1等词元的日志条目（如路径/redo_index/318/.../1/...、/redo_index/14912/.../1/...），返回大量非精确匹配结果。
使用短语查询语句#"redo_index/1"，日志服务将匹配完整的短语redo_index/1。使用短语查询语句#"redo_index/1"，日志服务精确匹配包含完整字符串redo_index/1的日志记录，查询结果中日志条目的文件路径字段包含/redo_index/1/完整片段，表明短语查询未对该字符串进行分词拆分。
例如您要查询包含02/Mar的日志（[调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log%3FslsRegion%3Dcn-shanghai%26isShare%3Dtrue%26queryString%3Drequest_time%20in%20%5B50%20100%5D)）。
使用非短语查询语句time_local: 02/Mar，日志服务将根据全文索引匹配部分关键词。
查询结果中包含time_local值为01/Mar/2025:15:02:56的日志条目。该条目的日期实际为01/Mar而非02/Mar，但因为时间部分15:02:56中包含关键词02，且日期部分包含关键词Mar，两个关键词被分别匹配命中，因此该条目也被返回。
使用短语查询语句time_local: #"02/Mar"，日志服务将匹配完整的短语02/Mar。
查询结果显示匹配到的日志中time_local字段值为02/Mar/2025:23:59:56，其中包含完整短语02/Mar，符合匹配预期。
该文章对您有帮助吗？
反馈
