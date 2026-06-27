# 多租户安全-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/multi-tenancy-security

# 多租户安全
本文主要介绍如何同时保证租户之间公平地分配共享集群资源，以最大程度的避免恶意租户对其他租户的攻击。
## 背景信息
隔离的安全程度分为软隔离(Soft Multi-tenancy)和硬隔离（Hard Multi-tenancy）。
软隔离更多面向企业内部的多租需求，该形态下默认不存在恶意租户，隔离是为了内部团队间的业务保护和对可能的安全攻击进行防护。
硬隔离更多面向对外提供服务的服务供应商，由于该业务形态下无法保证不同租户中业务使用者的安全背景，默认租户之间以及租户与K8s系统之间是存在互相攻击的可能，因此也需要更严格的隔离作为安全保障。
## 软多租
您可以使用原生Kubernetes特性来实现软多租，例如namespace、roles、role bindings以及network polices，在租户之间实现逻辑分离。例如，RBAC可以防止租户访问或操纵彼此的资源。qoutas和limit ranges控制每个租户可以消耗的集群资源量，而network polices可以防止部署到不同命名空间的应用程序相互通信。
这些控制措施不能阻止来自不同租户的Pod共享一个节点。您可以使用nodeselector、anti-affinity规则、taints和tolerations来强制将不同租户的Pod调度到不同的节点上，这通常称为独立租户节点。在租户数量很多的场景下，这样做会变得相当复杂且成本过高。
使用Namespaces实现的软多租不允许您向租户提供命名空间的过滤列表，因为命名空间是全局范围的资源对象。如果租户能够查看指定命名空间，则可以查看集群内的所有命名空间。
使用软多租，租户保留默认情况下为集群内运行的所有服务查询CoreDNS的能力。攻击者可以在集群中的任何Pod中运行dig SRV..svc.cluster.local来利用此特性。如果您需要限制对集群内运行的服务的DNS记录的访问，请使用CoreDNS的防火墙或策略插件。具体操作，请参见[kubernetes-metadata-multi-tenancy-policy](https://github.com/coredns/policy#kubernetes-metadata-multi-tenancy-policy)。
企业内部环境
第一种是在企业环境中，该场景下集群的所有用户均来自企业内部，这也是当前很多K8s集群客户的使用模式，因为服务使用者身份的可控性，相对来说这种业务形态的安全风险是相对可控的。每个租户通常会与一个行政部门（例如部门或团队）保持一致。
在类似这种场景中，集群管理员通常负责创建命名空间和管理策略。还可以实现托管管理模型，在该模型中，某些个人被赋予对命名空间的监管权，允许他们对非策略相关的对象（如deployments、services、pod、jobs等）执行CRUD操作。
Docker提供的隔离机制在此场景中是可以接受的，或者需要增加额外的控制，例如Pod安全策略 (PSP)。如果需要更严格的隔离，还需要限制不同命名空间中服务之间的通信。
Kubernetes即服务（KaaS）
软多租户可用于您希望提供Kubernetes即服务 (KaaS) 的场景之中。使用KaaS，您的应用程序与提供一组PaaS服务的控制器和CRD集合一起托管在共享集群中。租户直接与Kubernetes API服务器交互，并被允许对非策略对象执行CRUD操作。还有自助功能，例如允许租户创建和管理他们自己的命名空间。在类似此种环境中，租户被假定正在运行不可信代码。
要在此类环境中隔离租户，您可能需要实施严格的Network Policies以及Pod Sandboxing。具体操作，请参见[安全容器](https://www.aliyun.com/solution/cloudnative/securecontainer?spm=5176.21213303.1391245.1.4f323edayDJh1a)。
软件即服务 (SaaS)
在此环境中，每个租户都与在集群中运行的应用程序的特定实例相关联。每个实例通常都有自己的数据，并使用通常独立于Kubernetes RBAC的单独的访问控制。
与其他场景不同，SaaS环境中的租户不直接与Kubernetes API交互。而是SaaS应用程序负责与Kubernetes API交互以创建每个租户所需要的对象。
## Kubernetes原生配置
Kubernetes在架构上是面向单租户的容器编排管理平台，即控制平面的单个实例在集群内的所有租户之间共享。您可以使用各种Kubernetes对象来实现多租户隔离的目的。例如，可以使用命名空间和基于角色的访问控制 (RBAC)，以在逻辑上将租户彼此隔离。同样，Quotas和Limit Ranges可用于控制每个租户可以消耗的集群资源量。然而，集群是唯一提供强大安全边界的结构。这是因为设法获得对集群内主机的访问权的攻击者可以检索所有安装在该主机上的Secrets、ConfigMaps和Volumes。还可以模拟Kubelet，这将允许操纵节点的属性或在集群内横向移动。下面的Kubernetes原生配置可以帮助您降低使用像Kubernetes这样的单租户平台的风险，在一定程度上实现上述场景中租户之间的隔离。
命名空间
Namespaces是实现软多租的基础。Namespaces允许您将集群分为不同的逻辑层。Quotas、Network Policies、Service Accounts和其他资源对象都需要在Namespaces范围内实现多租。
AuthN&AuthZ&Admission
ACK集群的授权分为RAM授权和RBAC授权两个步骤，其中RAM授权作用于集群管理接口的访问控制，包括对集群的CRUD权限（如集群可见性、扩缩容、添加节点等操作），而RBAC授权用于集群内部Kubernetes资源模型的访问控制，可以做到指定资源在命名空间粒度的细化授权。ACK授权管理为租户内用户提供了不同级别的预置角色模板，同时支持绑定多个用户自定义的集群角色，此外支持对批量用户的授权。具体操作，请参见[授权](../../ack-managed-and-ack-dedicated/user-guide/authorization-overview.md)。
网络策略
默认情况下，Kubernetes集群中的所有Pod都允许相互通信。使用Network Policies更改此默认设置。
Network Policies使用标签或IP地址范围限制Pod之间的通信。在需要租户之间严格网络隔离的多租户环境中，需要添加两条规则：
拒绝Pod之间通信的默认规则。
允许所有Pod查询DNS服务器以进行名称解析。
资源配额&限制范围
Quotas用于定义集群中托管的工作负载的限制。使用Quotas，您可以指定Pod可以消耗的最大CPU和内存量，也可以限制可以在集群或命名空间中分配的资源数量。Limit ranges允许您声明每个限制的最小值、最大值和默认值。
在共享集群中过度使用资源通常是有益的，因为可以让您最大限度地利用资源。但是，对集群的无限制访问会导致资源匮乏，从而导致性能下降和应用程序可用性损失。如果一个Pod的请求设置得太低，实际资源利用率超过了节点的容量，节点就会开始遇到CPU或内存压力。发生这种情况时，Pod可能会重启或从节点中驱逐。
为了防止这种情况发生，您应该在多租户环境中对命名空间实施Quotas，以强制租户在集群上调度Pod时指定请求和限制。这样做还可以限制Pod可以消耗的资源量来缓解潜在的拒绝服务风险。
在KaaS场景中，您可以使用Quotas来分配集群资源以与租户需要的保持一致。
Pod优先级和抢占
当您想为不同的客户提供不同的服务质量 (QoS) 时，Pod优先级和抢占会很有用。例如，使用Pod优先级，您可以将客户A的Pod配置为以高于客户B的优先级运行。当可用容量不足时，Kubelet会从客户B驱逐低优先级的Pod以容纳客户A的高优先级Pod。在SaaS环境中，通过这种方式为愿意获得更高质量服务从而支付更高价格的客户提供服务方便。
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
## 硬多租
硬多租可以通过为每个租户配置单独的集群来实现。虽然这在租户之间提供了非常强的隔离，但有如下几个缺点：
当您拥有很多租户时，成本会很高。您不仅需要为每个集群支付控制平面成本，而且无法在集群之间共享计算资源。这样会导致碎片化，其中一部分集群未被充分利用，其他集群则被过度利用。
您可能需要购买或构建特殊工具来管理这些集群。随着时间的推移，管理成百上千个集群可能会变得过于繁重。
和创建命名空间相比，为每个租户创建集群会很慢。在高度监管的行业或需要强隔离的SaaS环境中，需要采用硬多租方法。
## 未来方向
Kubernetes社区已经认识到软多租目前的缺点以及硬多租的挑战。多租户特别兴趣小组 (SIG) 正尝试通过几个孵化项目来解决这些问题：
Virtual Cluster提案描述了一种机制，用于为集群中的每个租户（也称为“Kubernetes on Kubernetes”）创建控制平面服务的单独实例，包括API Server、Controller Manage和Scheduler。更多信息，请参见[Virtual Cluster](https://github.com/kubernetes-sigs/cluster-api-provider-nested/tree/main/virtualcluster)。
HNC提案 (KEP) 描述了一种通过策略对象继承以及租户管理员创建子命名空间的能力在命名空间之间创建父子关系的方法。更多信息，请参见[HNC](https://github.com/kubernetes-sigs/hierarchical-namespaces)。
Multi-Tenancy Benchmarks提案提供了使用命名空间进行隔离和分段共享集群的指南，以及命令行工具Kubectl-mtb用于验证是否符合的指南。更多信息，请参见[Multi-Tenancy Benchmarks](https://github.com/kubernetes-sigs/multi-tenancy/tree/master/benchmarks)。
## 相关文档
[k-rail](https://github.com/cruise-automation/k-rail)
[kiosk](https://github.com/loft-sh/kiosk)
[DevSpace](https://github.com/loft-sh/devspace)
[多租户特别兴趣小组](https://github.com/kubernetes-sigs/multi-tenancy)
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
