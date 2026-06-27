### spec.LogStores
可选配置，用于声明需要创建的LogStore，其作用如下：
仅在创建时生效：所有参数（除name外）都只在 LogStore 首次创建时有效。如果 LogStore 已存在，这些配置将被忽略，不会影响已有 LogStore 的属性。
不决定数据发送目标：此列表不控制日志发送到哪个 LogStore。真正的发送目标由config.flushers中的输出插件（如flusher_sls）决定。
可选配置：如果目标 LogStore 已经存在，可以不用在此处定义。
仅支持增删，不支持修改：可以向列表中添加新的 LogStore 或删除某项，但无法通过更新此配置来修改已创建的 LogStore 属性（如 TTL、Shard 数量等）。如需修改，请通过控制台或 API 操作。
