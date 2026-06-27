## Sidecar模式安装
当您需要对特定应用的日志进行精细化管理、实现多租户隔离或确保日志采集与应用生命周期严格绑定时，Sidecar 模式是理想的日志采集方案。该模式通过在业务 Pod 中注入一个独立的 LoongCollector（Logtail） 容器，实现对该 Pod 内日志的专属采集。若尚未部署业务应用，或仅用于测试，可直接使用[附录：YAML](loongcollector-installation-kubernetes-1.md)[示例](loongcollector-installation-kubernetes-1.md)快速验证流程。
