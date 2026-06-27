edential-helper | 安全组件 | 可以在 ACK 集群中免密拉取 ACR 默认版或企业版私有镜像的组件。 | addons { name = "aliyun-acr-credential-helper" } |
| gatekeeper | 安全组件 | 帮助管理和应用集群内的 Open Policy Agent（OPA）策略，实现命名空间标签管理等功能。 | addons { name = "gatekeeper" } |
| kritis-validation-hook | 安全组件 | 部署可信容器环节中进行容器镜像签名验证的关键组件。 | addons { name = "kritis-validation-hook" } ​ |
| security-inspector | 安全组件 | 实现安全巡检功能的关键组件。 | addons { name = "security-inspector" } |
| ack-kubernetes-webhook-injector | 安全组件 | 一款可以从多种阿里云产品白名单中动态加入或移出 Pod IP 的 K8s 组件，免去手动配置 Pod IP 到云产品白名单的操作。 | addons { name = "ack-kubernetes-webhook-injector" } |
| ack-arena | 其他 | 对开源 Arena 的安装做进一步简化，能够实现在控制台一键安装 Arena 的目标。 | addons { name = "ack-arena" } |
| ack-cost-exporter | 其他 | 容器服务 ACK 成本分析功能进行数据处理的插件。 | addons { name = "ack-cost-exporter" } |
| ack-kubernetes-cronhpa-controller | 其他 | 使用 ack-kubernetes-cronhpa-controller 实现应用负载定时伸缩。 | addons { name = "ack-kubernetes-cronhpa-controller" } |
| ack-virtual-node | 其他 | 基于社区开源项目 Virtual Kubelet，扩展了对 Aliyun Provider 的支持，并做了大量优化，实现 Kubernetes 与弹性容器实例 ECI 的无缝连接。 | addons { name = "ack-virtual-node" } |
| aesm | 其他 | Intel® SGX Architectural Enclave Service Manager (Intel® SGX AESM) 是 Intel® SGX 的系统组件，主要提供了 SGX Encla
