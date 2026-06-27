### GET/LIST读请求时延和写请求时延
情况说明

| 正常情况 | 异常情况 | 说明 |
| --- | --- | --- |
| GET 读请求时延 、 LIST 读请求时延 、 写请求时延 与访问的集群资源数量和集群规模相关联，没有固定的正常与异常的时间分界，只要不影响业务即在接受范围内。例如，如果访问的某种资源量越大，那么 LIST 请求时间就会越长。一般情况下， GET 读请求时延 、 写请求时延 小于 1s， LIST 读请求时延 小于 5s，为正常现象。 | GET 读请求时延 、 写请求时延 大于 1s。 LIST 读请求时延 大于 5s。 | 请求的响应时延过长时，需要排除集群资源数量多、Webhook 调用慢等因素的影响。 |

推荐解决方案
查看面板，定位GET读请求时延、LIST读请求时延、写请求时延中导致非200返回值的请求类型和资源，并采取解决措施。
请求延时指标apiserver_request_duration_seconds_bucket的最大阈值是60s，超过60s的请求都会统计为60s。而登录Pod的请求POST pod/exec、读取日志的请求会建立长链接，该类请求时间通常会超过60s。问题定位时，您可忽略该类请求。
参见[准入](monitor-kube-apiserver.md)[Webhook](monitor-kube-apiserver.md)[时延](monitor-kube-apiserver.md)，分析是否由于Webhook执行较慢，导致API Server请求延时长。
