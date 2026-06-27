### 在处理读/写请求数量和请求限流速率
情况说明

| 正常情况 | 异常情况 | 说明 |
| --- | --- | --- |
| 通常情况下， 在处理读请求数量 和 在处理写请求数量 小于 100， 请求限流速率 为 0，为正常现象。 | 在处理读请求数量 、 在处理写请求数量 大于 100。 请求限流速率 大于 0。 | 当前在处理请求的队列积压时，需要排除短时请求量涌入导致处理延时、Webhook 调用慢等因素的影响。超过队列长度时， API Server 会限流，导致 请求限流速率 大于 0，影响集群稳定性。 |

推荐解决方案
查看[QPS](monitor-kube-apiserver.md)[和时延](monitor-kube-apiserver.md)和[客户端分析](monitor-kube-apiserver.md)，分析请求中占比位于头部的请求，评估是否符合预期。如果请求为实际业务发起，您可以判断是否需降低请求量。
参见[准入](monitor-kube-apiserver.md)[Webhook](monitor-kube-apiserver.md)[时延](monitor-kube-apiserver.md)，分析是否因为Webhook执行慢导致API Server请求处理慢。
