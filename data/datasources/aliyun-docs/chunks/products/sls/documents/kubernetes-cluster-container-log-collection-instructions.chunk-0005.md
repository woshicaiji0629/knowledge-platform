### 安装采集器
根据适用场景选择部署模式：
部署模式：日志服务支持Daemonset与Sidecar两种模式安装LoongCollector。
Daemonset 部署模式：一次配置，自动在集群的每个Node节点上部署一个 LoongCollector，大多数情况下使用该模式。
当使用Daemonset时，需要根据集群与日志服务的关系选择合适的部署方式。
当使用ACK集群时，ACK中已集成loongcollector-ds组件，只需在ACK控制台选择开启组件使用即完成安装，此方式默认与ACK集群所属阿里云账号绑定，即后续日志会存储在该阿里云账号的日志服务中。具体操作可参考[安装配置](loongcollector-installation-kubernetes-1.md)。
当使用ACK集群，但因为组织架构、权限隔离或统一监控等原因，需将该ACK的日志数据采集到另一个独立的阿里云账号的日志服务Project时，需要手动安装LoongCollector组件，并为其配置目标账号的主账号ID或访问凭证（AccessKey）来实.现关联。具体操作可参考[安装配置](loongcollector-installation-kubernetes-1.md)。
当使用自建集群时，需要手动安装LoongCollector组件，为其配置目标账号的主账号ID或访问凭证（AccessKey）来实现关联。具体操作可参考[安装配置](loongcollector-installation-kubernetes-1.md)。
安装LoongCollector是采集日志的前提，您也可以直接参考[通过](collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)[Kubernetes CRD](collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)[采集集群容器日志（标准输出/文件）](collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)进行完整的采集流程操作，其中包含了安装LoongCollector的步骤。
Sidecar部署模式：每个 Pod 中伴随业务容器注入一个 LoongCollector Sidecar容器，部署运维较复杂。当需要Serverless 容器日志采集、单节点 Pod 数据量远超Daemonset采集上限、K8s + 安全容器运行时的日志采集时，使用[采集](collect-k8s-cluster-logs-through-side
