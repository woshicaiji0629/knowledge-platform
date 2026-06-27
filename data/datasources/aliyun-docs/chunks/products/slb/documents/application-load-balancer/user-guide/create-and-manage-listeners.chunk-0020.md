## 管理链路追踪
仅标准版和WAF增强版的ALB实例支持链路追踪。链路追踪的详细说明和开启指导，请参见[通过](../use-cases/untitled-document-1698045154408.md)[ALB](../use-cases/untitled-document-1698045154408.md)[链路追踪实现业务全链路分析](../use-cases/untitled-document-1698045154408.md)。
开启链路追踪后，会产生可观测链路 OpenTelemetry 版和日志服务相关费用。
前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，单击目标实例ID，在监听页签找到目标监听，单击监听ID。
在监听详情页签的链路追踪区域，根据需要进行如下操作。

| 操作 | 说明 |
| --- | --- |
| 开启链路追踪 | 开启 链路追踪 开关，在 开启链路追踪 对话框中配置参数后单击 保存 。 |
| 编辑链路追踪 | 单击 编辑链路追踪 ，在对话框中修改 采样率 后单击 保存 。 |
| 关闭链路追踪 | 关闭 链路追踪 开关，在 关闭链路追踪 对话框中单击 确定 。 |
| 查看链路追踪 | 在 调用链分析 右侧单击 查看 ，前往可观测链路 OpenTelemetry 版控制台查看请求数据。更多信息，请参见 [调用链分析](https://help.aliyun.com/zh/opentelemetry/user-guide/analyze-traces) 。 |
