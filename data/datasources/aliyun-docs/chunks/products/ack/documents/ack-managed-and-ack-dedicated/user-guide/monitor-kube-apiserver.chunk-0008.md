### 大盘使用指导
大盘基于组件指标和相关PromQL绘制，包括关键指标、概览、资源分析、QPS和时延、准入控制器和Webhook、客户端分析部分。
大盘构成模块如下，常见的使用顺序为：
[关键指标](monitor-kube-apiserver.md)：快速查看集群关键指标。
[概览](monitor-kube-apiserver.md)：分析API Server的响应时延、当前处理请求数和是否有限流发生。
[资源分析](monitor-kube-apiserver.md)：查看托管侧组件的资源水位。
[QPS](monitor-kube-apiserver.md)[和时延](monitor-kube-apiserver.md)：通过多维度深入分析QPS、RT。
[APF](monitor-kube-apiserver.md)[限流](monitor-kube-apiserver.md)：根据[APF](https://kubernetes.io/docs/concepts/cluster-administration/flow-control/)指标确认API Server的请求流量分布、限流状态以及系统性能瓶颈。
[注入控制器和](monitor-kube-apiserver.md)[Webhook](monitor-kube-apiserver.md)：分析准入控制器和Webhook的QPS、RT。
[客户端分析](monitor-kube-apiserver.md)：通过客户端多维度分析QPS。
