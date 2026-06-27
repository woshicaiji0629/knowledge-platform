## 采集异常问题排查指引
采集异常问题的成因复杂多样，且不同原因可能导致相同表象，甚至有时异常无法及时发现。因此需要如下指引，以实现异常的及时识别、排查与分类诊断。
登录[日志服务控制台](https://sls.console.aliyun.com/)，在日志应用区域单击SLS数据洞察。在接入管理的SLS采集规则列表页签中，按照对话框提示开启功能。
[CloudLens for SLS](cloudlens-for-sls.md)帮助监控与管理日志服务资源，提高问题定位的效率，及时感知与响应多维度指标的异常。
回到Project列表中，单击目标Project。
单击日志存储，在日志库中，将鼠标悬浮于目标LogStore上，随后单击右侧的图标，单击基础版诊断查看异常诊断信息。
高级版诊断提供异常诊断仪表盘，并支持更长时间的异常信息查询。详情可参考[运行情况诊断与监控](automatic-diagnosis-and-monitoring-of-loongcollector-operation.md)。
根据诊断显示的错误类型查阅[采集常见错误类型](loongcollector-collection-exception-troubleshooting.md)，排查错误原因。或在 /usr/local/ilogtail/目录下的ilogtail.LOG与logtail_plugin.LOG中查看客户端日志详情。
