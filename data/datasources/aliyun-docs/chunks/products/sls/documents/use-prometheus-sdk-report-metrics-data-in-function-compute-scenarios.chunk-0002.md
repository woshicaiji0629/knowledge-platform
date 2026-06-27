## 集成Prometheus
Prometheus能够自动生成多种维度的监控指标并内置维护了各种标签信息，结合Prometheus内置维护的指标信息，上报时序数据到时序库，根据不同场景，有两种模式。

| 方式 | 说明 |
| --- | --- |
| Pull 模式 | Pull 模式采集并上报指标数据，包含以下四个阶段： 在原项目中引入 Prometheus SDK，使用 SDK 创建并维护各种指标项。 对外暴露一个 /metrics 的 HTTP 接口，采集进程（Prometheus、VMAgent、iLogtail 等）定时访问该接口以获取编码后的指标数据。 采集进程解析从 HTTP 接口获取到的指标数据并转换成符合 Prometheus RemoteWrite PB 协议的编码数据。 采集进程请求 SLS 时序库的 RemoteWrite HTTP 接口写入时序数据。 |
| Push 模式 | Push 模式表示主动推送指标数据到时序库中。日志服务时序库支持两种主动上报时序数据的方式： 通过 [SLS SDK](use-an-sdk-to-collect-metrics.md) 以日志格式将时序数据写入到时序库中。 使用 Prometheus SDK 以开源标准格式将时序数据写入到时序库中，详细见 [代码示例](use-prometheus-sdk-report-metrics-data-in-function-compute-scenarios.md) 。 |
