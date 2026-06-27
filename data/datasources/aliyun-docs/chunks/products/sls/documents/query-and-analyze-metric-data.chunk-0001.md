## 校验PromQL语法
开启自动树状解析功能后，输入PromQL语句，系统将提示PromQL函数、聚合函数、指标名、标签名、标签值、时间范围等信息。更多信息，请参见[Prometheus](https://prometheus.io/docs/prometheus/latest/querying/functions/)[官方文档](https://prometheus.io/docs/prometheus/latest/querying/functions/)。
输入PromQL语句时，日志服务还支持实时进行语法校验。
正确语法
如果提示语法正确，表示校验通过且生成语法解析树。
错误语法
如果出现错误信息，表示校验不通过，仅生成部分语法解析树且提示错误位置与原因。
以下为存在语法错误的 PromQL 示例，其中[5]缺少时间单位（如m、s、h），导致解析错误4:1 parse error: unexpected <aggr:sum>：
label_replace( sum by(pod_name)( rate(container_cpu_usage_seconds_total{namespace= "redash"}[5]) ), "pod", "$1", "pod_name", "(.+)" )
在校验过程中，您还可以执行如下操作。
单击图标，刷新语法解析树。
单击图标，简化展示语法解析树中的节点信息。
单击图标、图标，展开或收起节点。
单击图标、图标，开启或关闭自动树状解析功能。
