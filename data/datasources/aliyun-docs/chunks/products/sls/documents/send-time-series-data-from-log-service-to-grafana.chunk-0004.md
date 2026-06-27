## Prometheus查询API
日志服务提供了兼容Prometheus的查询API，可直接配置日志服务作为Grafana的Prometheus数据源，同时也支持用各类Prometheus API直接访问。支持的API如下：

| API 名称 | 示例 |
| --- | --- |
| [Instant queries](https://prometheus.io/docs/prometheus/latest/querying/api/#instant-queries) | GET /api/v1/query POST /api/v1/query |
| [Range queries](https://prometheus.io/docs/prometheus/latest/querying/api/#range-queries) | GET /api/v1/query_range POST /api/v1/query_range |
| [Getting label names](https://prometheus.io/docs/prometheus/latest/querying/api/#getting-label-names) | GET /api/v1/labels POST /api/v1/labels |
| [Querying label values](https://prometheus.io/docs/prometheus/latest/querying/api/#querying-label-values) | GET /api/v1/label/<label_name>/values |
| [Finding series by label matchers](https://prometheus.io/docs/prometheus/latest/querying/api/#finding-series-by-label-matchers) | GET /api/v1/series POST /api/v1/series |

该文章对您有帮助吗？
反馈
