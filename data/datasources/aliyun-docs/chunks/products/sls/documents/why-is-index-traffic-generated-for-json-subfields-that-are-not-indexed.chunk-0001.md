## 示例
下述日志中的result字段为JSON类型，且只对result.anomaly_type字段设置了索引。在计算索引流量时，会将result字段名和result字段值中的所有内容都计入到索引流量中，即dim_name等字段名和字段值，都将按照text类型计入到索引流量中。
- 日志样例{ "result": { "anomaly_type": "None", "dim_name": "body_bytes_sent", "is_anomaly": false, "score": 0, "value": "4850.000000" } }
- 索引配置字段result的类型设置为json，分隔符为,':"=0[]{}?@&<>/\n\t\r；其子字段anomaly_type的类型设置为text，并开启索引。
该文章对您有帮助吗？
反馈
