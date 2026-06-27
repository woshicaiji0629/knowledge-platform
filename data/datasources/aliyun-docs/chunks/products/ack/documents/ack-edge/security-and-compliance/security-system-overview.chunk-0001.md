## 运行时安全
安全巡检
集群的应用开发人员应该遵循权限的最小化原则配置应用部署模板，攻击者往往是利用应用Pod中开启的不必要的特权能力发起逃逸攻击，因此阿里云容器服务Kubernetes版ACK（Alibaba Cloud Container Service for Kubernetes）提供了应用运行时刻的安全配置巡检能力，帮助您实时了解当前状态下运行应用的配置是否存在安全隐患。
巡检结果支持以报表化的方式展示，同时展示巡检对应扫描项的说明和修复建议。您还可以配置定期巡检，对应的扫描结果会写入到SLS指定的日志库中存储。具体操作，请参见[使用配置巡检检查集群](../../ack-managed-and-ack-dedicated/security-and-compliance/use-the-inspection-feature-to-detect-security-risks-in-the-workloads-of-an-ack-cluster.md)[Workload](../../ack-managed-and-ack-dedicated/security-and-compliance/use-the-inspection-feature-to-detect-security-risks-in-the-workloads-of-an-ack-cluster.md)[安全隐患](../../ack-managed-and-ack-dedicated/security-and-compliance/use-the-inspection-feature-to-detect-security-risks-in-the-workloads-of-an-ack-cluster.md)。
策略管理
ACK基于使用OPA策略的Gatekeeper准入控制器，扩展了策略治理状态统计和日志上报检索等能力，同时内置了种类丰富的策略治理规则库，提供更多符合K8s应用场景的策略规则。您可以在容器服务管理控制台上进行策略治理规则可视化配置，降低使用策略治理相关能力的门槛。更多信息，请参见[配置容器安全策略（新版）](../../ack-managed-and-ack-dedicated/security-and-compliance/configure-and-enforce-ack-pod-security-policies.md)。
通过使用ACK策略管理能力，可以帮助企业安全运维人员在应用部署阶段自动化阻断不符合策略要求的风险应用，提升集群内应用运行时安全水位，降低企业应用开发和运维团队的沟通和学习成本。
运行时监控和告警
当容器应用通过API Server的认证鉴权和准入控制校验成功部署后，在云原生应用零信任的安全原则下，还需要在容器应用的运行时刻提供相应的安全监
