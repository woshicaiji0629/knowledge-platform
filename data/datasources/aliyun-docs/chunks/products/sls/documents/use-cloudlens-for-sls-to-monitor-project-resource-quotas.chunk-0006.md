### 额度监控
额度监控项分类说明如下：

| 分类 | 监控项 | 说明 |
| --- | --- | --- |
| 实时水位监控 | [基础资源配额水位监控](use-cloudlens-for-sls-to-monitor-project-resource-quotas.md) | 监控 Project 内 LogStore 数量、机器组数量、Logtail 采集配置水位是否超阈值预期百分比。 依赖时序库：internal-monitor-metric |
| [数据读写配额水位监控](use-cloudlens-for-sls-to-monitor-project-resource-quotas.md) | 监控 Project 写入流量、Project 写入次数超配额次数。 依赖时序库：internal-monitor-metric |  |
| 额度超限监控 | [资源配额超限次数监控](use-cloudlens-for-sls-to-monitor-project-resource-quotas.md) | 监控基础配额、数据读写超配额次数。 依赖日志库：internal-error_log |

基础资源配额水位监控
单击新建告警，配置告警规则。
选择创建告警需要挂载的Project为存储全局错误日志和监控指标所在Project。
根据业务场景配置告警触发条件、以及告警策略。
根据下表完成配置，其余参数保持默认即可，具体信息，可参见[创建日志告警监控规则](alarm-settings-quick-start.md)。
