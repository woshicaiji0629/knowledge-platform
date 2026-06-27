## 停止计费说明
创建LogStore时，日志服务默认预留两个Shard。因此只要LogStore存在，无论是否使用都会产生活跃Shard租用费用。日志服务根据您的活跃Shard租用量收取费用。关于Shard租用费用详细说明，请参见[为什么会产生活跃](why-am-i-charged-for-active-shards.md)[Shard](why-am-i-charged-for-active-shards.md)[租用费用](why-am-i-charged-for-active-shards.md)。
即使没有写入任何日志，只要 LogStore 存在且未关闭索引，仍会因索引流量产生基础费用。
如果您不再需要使用LogStore存储日志，请及时删除，避免产生额外费用。具体操作，请参见[停止计费/删除](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
目前日志服务仅支持[修改数据保存时间](how-do-i-delete-logs.md)来删除日志，无法手动删除指定内容的日志，当日志保存时间达到您所设置的保存时间后，日志将被删除。如需降低存储费用，您可设置较短的存储周期。如果不再需要已有日志，您可直接[删除](stop-billing.md)[Project](stop-billing.md)[或](stop-billing.md)[LogStore](stop-billing.md)。
删除 Project 的当天仍会产生存储等费用，从次日开始不再产生新的费用。
日志服务按天出账。删除资源后，当天的费用会在次日生成账单。因此您在删除后的第三天查看账单时，即可确认无新增费用。
如果您的账号处于欠费状态，存储资源不会立即释放，系统将继续计费直至资源被回收（通常为停服 7 天后）。关于欠费后的具体处理规则，请参见[欠费说明](overdue-payments.md)。建议及时删除不需要的资源或为账号充值，以避免持续产生意外费用。
如果您的 Project 已开启回收站功能，删除 Project 后数据会进入回收站保留。在回收站保留期间，仍会产生存储费用。若需立即彻底停止计费，需要在回收站中将该 Project 彻底删除。关于回收站操作的详细说明，请参见[管理 Project 回收站](stop-billing.md)。
