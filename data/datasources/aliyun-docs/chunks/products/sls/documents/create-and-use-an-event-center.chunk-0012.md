## 日志样例
采集到的日志样例如下所示。
hostname: cn-hangzhou.i-***********" level: Normal pod_id: 2a360760-**** pod_name: logtail-ds-blkkr event_id: { "metadata":{ "name":"logtail-ds-blkkr.157b7cc90de7e192", "namespace":"kube-system", "selfLink":"/api/v1/namespaces/kube-system/events/logtail-ds-blkkr.157b7cc90de7e192", "uid":"2aaf75ab-****", "resourceVersion":"6129169", "creationTimestamp":"2019-01-20T07:08:19Z" }, "involvedObject":{ "kind":"Pod", "namespace":"kube-system", "name":"logtail-ds-blkkr", "uid":"2a360760-****", "apiVersion":"v1", "resourceVersion":"6129161", "fieldPath":"spec.containers{logtail}" }, "reason":"Started", "message":"Started container", "source":{ "component":"kubelet", "host":"cn-hangzhou.i-***********" }, "firstTimestamp":"2019-01-20T07:08:19Z", "lastTimestamp":"2019-01-20T07:08:19Z", "count":1, "type":"Normal", "eventTime":null, "reportingComponent":"", "reportingInstance":"" }

| 日志字段 | 数据类型 | 说明 |
| --- | --- | --- |
| hostname | String | 事件发生所在的主机名。 |
| level | String | 日志等级，包括 Normal、Warning。 |
| pod_id | String | Pod 的唯一标识，仅在该事件类型和 Pod 相关时才具有此字段。 |
| pod_name | String | Pod 名，仅在该事件类型和 Pod 相关时才具有此字段。 |
| event_id | JSON | 事件的详细内容。该字段为 JSON 类型的字符串。 |
