### 使用场景
告警去重
标签属于触发告警的标识性属性，是告警指纹中的一部分，可用于告警去重。比如系统产生两条告警Alert1和Alert2，因为标签信息（labels）相同，只保留其中一条告警数据。告警指纹原理，请参见[基于告警指纹去重](deduplicate-alerts-based-on-fingerprints.md)。
// Alert1 { "aliuid": "12345", "project": "Project1", "alert_id": "alert-123", "labels": { "host": "host-1" }, "annotations": { "title": "CPU使用率过高", "desc": "CPU当前使用率为90%" } } // Alert2 { "aliuid": "12345", "project": "Project1", "alert_id": "alert-123", "labels": { "host": "host-1" }, "annotations": { "title": "CPU使用率过高", "desc": "CPU当前使用率为95%" } }
内容模板中引用标签
标签属于map类型，当您在告警规则中添加了标签，您可在告警内容模板中通过${labels}引用标签信息。
降噪控制
在告警策略中，标签信息可作为降噪控制的合并基准。比如您在合并基准时使用按告警规则+所有标签进行合并配置，如下图。更多信息，请参见[合并基准](deduplicate-alerts.md)。
通知分派
告警管理系统和通知管理系统根据标签属性进行告警管理和通知分派。比如您在配置行动策略时，根据标签配置不同的行动组，如下图。
