## 背景信息
K8s事件中心已内置告警规则模板、SLS ACK内置行动策略、SLS ACK内置用户组、SLS ACK Pod内置内容模板、SLS ACK内置内容模板、SLS ACK Node内置内容模板和SLS ACK Object内置内容模板。日志服务提供的内置资源可满足大部分告警场景，它们之间的关联如下：
通过告警规则模板指定SLS ACK内置行动策略。
通过SLS ACK内置行动策略指定SLS ACK内置用户组和内容模板（SLS ACK Pod内置内容模板、SLS ACK内置内容模板、SLS ACK Node内置内容模板和SLS ACK Object内置内容模板）。
触发告警后，日志服务会根据行动策略给指定用户发送告警通知。
