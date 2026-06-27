某个时间点的值，每个数据点由时间戳和值组成。其中时间戳精度为纳秒，值的类型为double。
数据结构
时序数据的写入协议和日志写入协议一致，使用Protobuf的[数据编码方式](developer-reference/data-encoding.md)。时序标识和数据点都在content字段中，具体表示方式如下所示。

| 字段 | 说明 | 示例 |
| --- | --- | --- |
| __name__ | Metric 名称。 | nginx_ingress_controller_response_size |
| __labels__ | Label 信息，格式为 {key}#$#{value}|{key}#$#{value}|{key}#$#{value} 。 说明 Label 的 Key 需按照字母顺序进行排序。 建议不要写入 Value 为空字符串的 Label。例如 Label 信息为 app#$#|controller_class#$#nginx ，则不建议将 Key 为 app 的 Label 写入时序库，可能造成 PromQL 聚合计算报错。 | app#$#ingress-nginx|controller_class#$#nginx|controller_namespace#$#kube-system|controller_pod#$#nginx-ingress-controller-589877c6b7-hw9cj |
| __time_nano__ | 时间戳。支持以秒（s）、毫秒（ms）、微秒（us）、纳秒（ns）等多种精度的时间戳写入。SQL 查询时，所有时间戳统一化为微秒（us）精度输出，确保时间计算的一致性。 | 1585727297293000 |
| __value__ | 值。 | 36.0 |

说明
除上表提到的字段之外，其他自定义字段（例如 Topic、Source、LogTags 等）在通过 SDK 写入时将不被存储到时序库中，详情可参考[通过](use-an-sdk-to-collect-metrics.md)[SDK](use-an-sdk-to-collect-metrics.md)[写入时序数据](use-an-sdk-to-collect-metrics.md)的说明部分。
示例
查询process_resident_memory_bytes指标在指定时间区间内的所有原始时序数据。
* | select * from "sls-mall-k8s-metrics.prom" where __name__ = 'process_resident_memory_bytes' limit all
