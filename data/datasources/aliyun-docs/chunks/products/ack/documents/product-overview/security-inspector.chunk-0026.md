### 2021年03月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.4.0.0-g541eb31-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.4.0.0-g541eb31-aliyun | 2021 年 03 月 15 日 | 支持 CIS Kubernetes 基线检查。 新增以下 Kubernetes 事件（当您触发扫描时，可以在事件中心看到相应事件）： SecurityInspectorConfigAuditStart：开始执行配置巡检。 SecurityInspectorConfigAuditFinished：配置巡检完成。 SecurityInspectorConfigAuditHighRiskFound：配置巡检完成后发现高风险配置。 SecurityInspectorBenchmarkStart：开始执行基线检查。 SecurityInspectorBenchmarkFinished：执行基线检查完成。 SecurityInspectorBenchmarkFailedCheckFound：执行基线检查完成后发现未通过的计分检查项。 | 此次升级不会对业务造成影响。 |
