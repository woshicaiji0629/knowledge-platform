# 通过Kubernetes CRD采集集群容器日志（标准输出/文件）
为了统一管理阿里云容器服务ACK集群或自建 Kubernetes 集群在多环境、多集群场景下的日志采集配置，避免因手动配置导致的不一致、效率低下及变更不可追溯等问题，可采用Kubernetes 的自定义资源（CRD）方式定义采集配置。通过该方式，无论是 ACK 集群还是自建 Kubernetes 集群，均可使用kubectl或 CI/CD 流水线实现配置的版本化管理、环境差异化部署和自动化发布。结合 LoongCollector 的热加载能力，配置变更后可立即生效，无需重启采集组件，提升运维效率与系统的可维护性。
旧版CRD-AliyunLogConfig的配置方式已停止维护，请使用新版AliyunPipelineConfig，新旧版的能力对比请参见[CRD](use-crd-to-manage-collection-configurations.md)[类型](use-crd-to-manage-collection-configurations.md)。
重要
对于通过自定义资源（CRD）创建的采集配置，只能通过更新对应的CRD进行修改。在日志服务控制台上所做的更改不会同步至CRD，也不会生效。
