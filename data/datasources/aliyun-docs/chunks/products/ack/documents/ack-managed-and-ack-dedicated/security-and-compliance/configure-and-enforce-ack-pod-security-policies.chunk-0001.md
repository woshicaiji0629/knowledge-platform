## 策略治理介绍
自Kubernetes 1.21起，PodSecurityPolicy（PSP）被标记为弃用（Deprecated）状态。为此，ACK升级了原先基于PSP的策略管理功能。基于使用[OPA](https://www.openpolicyagent.org/)策略的Gatekeeper Admission Controller，ACK扩展了相应的策略治理状态统计、日志上报检索等能力，同时内置了种类丰富的策略治理规则库，提供符合更多Kubernetes应用场景的策略规则。在规则配置上，您可以在控制台上白屏化配置，降低使用策略治理相关能力的门槛。
