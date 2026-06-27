## 缓解措施
作为多租环境的安全管理员，您主要关心的是防止攻击者获得对底层主机的访问权限。应考虑采取以下控制措施来降低这种风险：
安全沙箱
相比于原有Docker运行时，安全沙箱为您提供的一种新的容器运行时选项，可以让您的应用运行在一个轻量虚拟机沙箱环境中，拥有独立的内核，具备更好的安全隔离能力。
安全沙箱特别适合于不可信应用隔离、故障隔离、性能隔离、多用户间负载隔离等场景。在提升安全性的同时，对性能影响非常小，并且具备与Docker容器一样的用户体验，例如日志、监控、弹性等。更多信息，请参见[安全沙箱](../../ack-managed-and-ack-dedicated/user-guide/overview-10.md)。
Open Policy Agent (OPA) & Gatekeeper
OPA（Open Policy Agent）是一种功能强大的策略引擎，支持解耦式的Policy Decisions服务并且在K8s集群中已经有了广泛应用。当现有RBAC在命名空间粒度的隔离不能够满足企业应用复杂的安全需求时，可以通过OPA提供object模型级别的细粒度访问策略控制。Gatekeeper是一个Kubernetes准入控制器，可以在应用部署时刻执行指定的已实施OPA策略。更多信息，请参考[Gatekeeper](https://github.com/open-policy-agent/gatekeeper)。
同时OPA支持七层的NetworkPolicy策略定义及基于Labels/Annotation的跨命名空间访问控制，可以作为K8s原生NetworkPolicy的有效增强。
Kyverno
Kyverno是一个面向Kubernetes而生的策略引擎，可以为Kubernetes资源产生验证、改变和生成配置的策略。Kyverno支持Kustomize Overlays风格的策略校验和Mutate修改，并且可以基于灵活的触发器跨命名空间克隆资源。更多信息，请参见[Kyverno](https://kyverno.io/)。
您可以使用Kyverno来隔离命名空间、实现Pod安全和其他最佳实践，并生成默认配置（例如网络策略）。具体操作，请参见[策略仓库](https://github.com/kyverno/policies/)。
