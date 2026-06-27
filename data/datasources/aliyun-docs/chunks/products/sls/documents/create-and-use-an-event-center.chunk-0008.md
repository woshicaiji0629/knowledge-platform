| 配置项 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| endpoint | string | 必选 | 日志服务的 Endpoint。更多信息，请参见 [服务入口](developer-reference/service-entrance.md) 。 |
| project | string | 必选 | 日志服务的 Project。 |
| LogStore | string | 必选 | 日志服务的 LogStore。 |
| internal | string | 自建 Kubernetes：必选。 | 自建 Kubernetes 必须设置为 false。 |
| regionId | string | 自建 Kubernetes：必选。 | 日志服务所在地域 ID。更多信息，请参见 [服务入口](developer-reference/service-entrance.md) 。 |
| accessKeyId | string | 自建 Kubernetes：必选。 | AccessKey ID，建议使用 RAM 用户的 AccessKey 信息。更多信息，请参见 [访问密钥](developer-reference/access-key.md) 。 |
| accessKeySecret | string | 自建 Kubernetes：必选。 | AccessKey Secret，建议使用 RAM 用户的 AccessKey 信息。更多信息，请参见 [访问密钥](developer-reference/access-key.md) 。 |

执行以下命令，将eventer.yaml中的配置应用到集群。
kubectl apply -f eventer.yaml
预期输出：
deployment.apps/kube-eventer created clusterrole.rbac.authorization.k8s.io/kube-eventer created clusterrolebinding.rbac.authorization.k8s.io/kube-eventer created serviceaccount/kube-eventer created
部署node-problem-detector。
具体操作，请参见[Github](https://github.com/kubernetes/node-problem-detector)。
