| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，固定值 processor_json 。 | # ...在 spec.config 下... processors: # 配置 JSON 字段展开插件 - Type: processor_json # 指定需要解析的原始字段名 SourceKey: content ExpandDepth: 0 ExpandConnector: '_' Prefix: expand IgnoreFirstConnector: false # 是否展开数组元素为独立字段 ExpandArray: false # 是否保留原始字段内容 KeepSource: true # 当原始字段缺失时是否报错 NoKeyError: true # 是否将原始字段名作为展开字段名的前缀 UseSourceKeyAsPrefix: false # 如果 JSON 解析失败，是否保留原始日志数据 KeepSourceIfParseError: true |
| SourceKey String （必选） 源字段名。 |  |
| ExpandDepth integer （可选） JSON 展开深度，默认值为 0。 0：表示展开到能解析成功的最深层级； 1：表示仅展开当前层级，以此类推。 |  |
| ExpandConnector String （可选） JSON 展开时字段名的连接符，默认为下划线（_）。 |  |
| Prefix String （可选） 指定 JSON 展开后字段名的前缀。 |  |
| IgnoreFirstConnector String （可选） 是否忽略第一个连接符，即是否在顶级字段前添加连接符，默认为 false 。 |  |
| ExpandArray boolean （可选） 是否展开数组类型，默认为 false 。 false（默认值）：不展开。 true：展开。例如 {"k":["1","2"]} 展开为 {"k[0]":"1","k[1]":"2"} 。 说明 Logtail 1.8.0 及以上版本支持该参数。 |  |
| KeepSource boolean （可选） 被解析后的日志中是否保留原始字段，默认为 true 。 true：保留 false：丢弃 |  |
| NoKeyError boolean （可选） 原始日志中没有指定的原始字段时，系统是否报错，默认为 true 。 true：报错 false：不报错 |  |
| UseSourceKeyAsPrefix boolean （可选） 是否将原始字段名作为所有 JSON 展开字段名的前缀。 |  |
| KeepSourceIfParseError boolean （可选） 解析日
