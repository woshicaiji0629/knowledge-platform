### 其他日志
如需保留Project仅删除LogStore，请参见[停止计费/删除](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
如需删除整个Project，请参见[管理](manage-a-project.md)[Project](manage-a-project.md)。
精细化停止计费：如果希望保留特定业务日志（如 OSS 访问日志）但停止其他无关 LogStore 的计费，可以单独删除不需要的 LogStore，而无需删除整个 Project。这样可以实现单独停止某类日志的计费。
说明
删除 LogStore 前，请先确认该 LogStore 不再被任何 Logtail 采集配置引用。控制台会在删除时自动检查，如存在 Logtail 采集配置将阻断删除操作并提示"该 LogStore 下存在 Logtail 采集配置，请先删除采集配置"。此外，建议在删除前也确认该 LogStore 没有被仪表盘、告警规则或数据加工任务引用，以免这些配置报错。
