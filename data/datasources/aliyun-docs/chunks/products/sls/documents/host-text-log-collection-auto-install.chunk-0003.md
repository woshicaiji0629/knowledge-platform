## 采集配置创建流程
[准备工作](host-text-log-collection-auto-install.md)：创建Project和LogStore，Project是资源管理单元，用于隔离不同业务日志，而LogStore用于存储日志。
[配置机器组（安装](host-text-log-collection-auto-install.md)[LoongCollector）](host-text-log-collection-auto-install.md)：根据服务器类型，安装LoongCollector，并将其加入到机器组。使用机器组统一管理采集节点，对服务器进行配置分发与状态管理。
[创建并配置日志采集规则](host-text-log-collection-auto-install.md)：
[全局与输入配置](host-text-log-collection-auto-install.md)：定义采集配置的名称及日志采集的来源和范围。
[日志处理与结构化](host-text-log-collection-auto-install.md)：根据日志格式进行处理配置。
多行日志：适用于单条日志跨越多行（如 Java 异常堆栈、Python traceback），通过行首正则识别每条日志，并将同一日志的连续多行内容合并为一条完整日志。
结构化解析：通过配置解析插件（如正则、分隔符、NGINX 模式等）将原始字符串提取为结构化的键值对，每个字段都可以被独立查询与分析。
过滤处理：通过配置采集黑名单和内容过滤规则，筛选有效日志内容，减少冗余数据的传输与存储。
[日志分类](host-text-log-collection-auto-install.md)：通过配置日志主题（Topic）灵活区分不同业务、服务器、路径来源的日志。
查询分析配置：系统默认开启全文索引，支持关键词搜索。建议启用字段索引，以便对结构化字段进行精确查询和分析，提升检索效率。
[验证与故障排查](host-text-log-collection-auto-install.md)：完成配置后，验证日志是否成功采集，如遇采集无数据、心跳失败或解析错误等问题，参考[常见问题排查](host-text-log-collection-auto-install.md)。
