| 参数 | 说明 | 是否必选 |
| --- | --- | --- |
| action | 操作类型，支持 ListK8sResource 和 GetK8sResource 。 | 是 |
| group | 目标资源的 API Group。 | 是 |
| version | 目标资源的 API Version。 | 否 |
| resource | 目标资源的复数名称（例如 persistentvolumeclaims ）。 | 是 |
| namespaced | 目标资源是否位于命名空间内。 true 或 false 。 集群范围内资源请使用 false 。 | 是 |
| namespace | 当 namespaced 为 true 时，指定查询的命名空间。 | 否 |
| name | 当 action 为 GetK8sResource 时，指定要获取的资源名称。 | 否 |
| labelSelector | 基于标签筛选资源，遵循 Kubernetes [Label Selector 规范](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors) 。 | 否 |
| limit | ListK8sResource 返回的资源数量上限。 | 否 |
| requestID | 请求的唯一 ID，建议使用 review.uid 。 | 否 |
| userInfo | 发起请求的用户信息，建议使用 review.userInfo 。 | 否 |
| requestFrom | 请求来源标识，通常为策略模板名称，用于日志追溯。 | 是 |
