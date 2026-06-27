# 采集Kubernetes Pod文本日志（Sidecar模式）
在 Kubernetes 环境中，当您需要对特定应用的日志进行精细化管理、实现多租户隔离或确保日志采集与应用生命周期严格绑定时，Sidecar 模式是理想的日志采集方案。该模式通过在业务 Pod 中注入一个独立的 LoongCollector（Logtail） 容器，实现对该 Pod 内日志的专属采集，提供了强大的灵活性和隔离性。
