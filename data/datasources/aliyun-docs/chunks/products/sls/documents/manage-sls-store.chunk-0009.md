### 时序数据（Metric）
时序数据由时序标识和数据点组成，相同时序标识的数据组成时间线。日志服务的时序数据类型遵循Prometheus的[定义规范](https://prometheus.io/docs/concepts/data_model/)，在时序库中所有的数据都按照时序类型存储。
时序标识
每条时间线都有一个唯一的时序标识，由Metric name和Labels组成。
Metric name是一个字符串类型的标识符，用于标识指标类型。Metric name需遵循正则表达式[a-zA-Z_:][a-zA-Z0-9_:]*。例如http_request_total表示接收到的HTTP请求的总数。
Labels由一组组键值对组成，各组键值对之间使用竖线（|）分割，用于标识指标的相关属性。Key需遵循正则表达式[a-zA-Z_][a-zA-Z0-9_]*，Value则不能包含竖线（ | ）。例如method为POST，URL为/api/v1/get。
数据点
数据点代表时间线在具体某个时间点的值，每个数据点由时间戳和值组成。其中时间戳精度为纳秒，值的类型为double。
数据结构
时序数据的写入协议和日志写入协议一致，使用Protobuf的[数据编码方式](developer-reference/data-encoding.md)。时序标识和数据点都在content字段中，具体表示方式如下所示。
