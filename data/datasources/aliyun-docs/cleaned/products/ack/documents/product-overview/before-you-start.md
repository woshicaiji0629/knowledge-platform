# 使用容器服务ACK的注意事项及高危操作列表-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/product-overview/before-you-start

# 使用须知及高危风险操作说明
阿里云容器服务Kubernetes版（简称容器服务ACK）提供容器服务相关的技术架构以及核心组件的托管服务，对于非托管组件以及运行在ACK集群中的应用，不当操作可能会导致业务故障。为了更好地预估和避免相关的操作风险，在使用容器服务ACK前，请认真阅读本文中的建议与注意事项。
## 索引
| 信息项 | 相关文档 |
| --- | --- |
| [使用须知](before-you-start.md) | [数据面组件相关](before-you-start.md) [集群升级相关](before-you-start.md) [Kubernetes](before-you-start.md) [原生配置相关](before-you-start.md) [ACK Serverless](before-you-start.md) [集群相关](before-you-start.md) [注册集群相关](before-you-start.md) [应用目录相关](before-you-start.md) |
| [高危操作](before-you-start.md) | [集群相关高危操作](before-you-start.md) [节点池相关高危操作](before-you-start.md) [网络与负载均衡相关高危操作](before-you-start.md) [存储相关高危操作](before-you-start.md) [日志相关高危操作](before-you-start.md) |
## 使用须知
### 数据面组件相关
数据面组件指运行在客户ECS服务器上的系统组件，例如CoreDNS、Ingress、kube-proxy、terway、kubelet等。由于数据面组件运行在客户ECS服务器上，因此数据面组件运行的稳定性需要阿里云容器服务与客户共同维护。
阿里云容器服务ACK对数据面组件提供以下支持：
提供组件的参数化设置管理、定期功能优化、BugFix、CVE补丁等功能，并给出相应的指导文档。
提供组件的监控与报警等可观测能力的建设，部分核心组件会提供组件日志，并通过SLS透出给客户。
提供配置最佳实践和建议，容器服务将根据集群规模大小给出组件配置建议。
提供组件的定期巡检能力和一定的报警通知能力，检查项包括但不限于：组件版本、组件配置、组件负载、组件部署分布拓扑、组件实例数等。
您在使用数据面组件时，请遵循以下建议：
使用最新的组件版本。组件经常会发布新版本以修复Bug或提供新特性。您需要在新版本的组件发布后，在保证业务稳定的前提下选择合适的时机，遵循组件升级指导文档中的说明进行升级操作。更多信息，请参见[组件](../ack-managed-and-ack-dedicated/user-guide/component-overview.md)。
请在容器服务ACK的报警中心中设置联系人的邮箱地址、手机号码，并设置相应的报警信息接收方式，阿里云将通过这些渠道推送容器服务的报警信息、产品公告等。更多信息，请参见[容器服务报警管理](../ack-managed-and-ack-dedicated/user-guide/alert-management.md)和[如何设置消息接收？](https://help.aliyun.com/zh/account/message-received-management-settings#topic-2149123)。
在您收到组件稳定性风险报告后，请及时按照相关指引进行处理，消除安全隐患。
当您在使用数据面组件时，请通过[容器服务控制台](https://cs.console.aliyun.com)集群管理页面运维管理>组件管理的方式或者OpenAPI的方式配置组件的自定义参数。通过其他渠道修改组件配置可能会导致组件功能异常。更多信息，请参见[管理组件](../manage-system-components.md)。
请勿直接使用IaaS层产品的OpenAPI来变更组件的运行环境，包括但不限于使用ECS的OpenAPI更改ECS运行状态、修改Worker节点的安全组配置、更改Worker节点的网络配置以及通过负载均衡的OpenAPI修改SLB配置等，擅自改动IaaS层资源可能会导致数据面组件异常。
部分数据面组件受上游社区版组件影响，可能存在Bug或漏洞，请注意及时升级组件，以避免开源组件Bug或漏洞导致您的业务受损。
### 集群升级相关
请务必通过容器服务ACK的集群升级功能升级集群的K8s版本，自行升级K8s版本可能导致ACK集群的稳定性和兼容性问题。详细操作，请参见[升级集群和独立升级集群控制面和节点池](../ack-managed-and-ack-dedicated/user-guide/update-the-kubernetes-version-of-an-ack-cluster.md)。
阿里云容器服务ACK对集群升级提供以下支持：
提供集群K8s新版本的升级功能。
提供K8s新版本升级的前置检查功能，确保集群当前状态支持升级。
提供K8s新版本的版本说明文档，包括相较于前版本的变化。
提示升级到K8s新版本时因资源变化可能会发生的风险。
您在使用集群升级功能时，请遵循以下建议：
在集群升级前运行前置检查，并根据前置检查结果逐一修复集群升级的阻塞点。
详细阅读K8s新版本的版本说明文档，并根据ACK所提示的升级风险确认集群和业务的状态，自行判断升级风险。详细信息，请参见[Kubernetes](../overview-of-kubernetes-versions-supported-by-ack.md)[版本发布概览](../overview-of-kubernetes-versions-supported-by-ack.md)。
由于集群升级不提供回滚功能，请做好充分的升级计划和预后备份。
根据容器服务ACK的版本支持机制，在当前版本的支持周期内及时升级集群K8s版本。更多信息，请参见[版本说明](../ack-managed-and-ack-dedicated/user-guide/support-for-kubernetes-versions.md)。
### Kubernetes原生配置相关
请勿擅自修改Kubernetes的关键配置，例如以下文件的路径、链接和内容：
/var/lib/kubelet
/var/lib/docker
/etc/kubernetes
/etc/kubeadm
/var/lib/containerd
在YAML模板中请勿使用Kubernetes集群预留的Annotation，否则会造成资源不可用、申请失败、异常等问题。以kubernetes.io/和k8s.io/开头的Annotation为核心组件预留标签。违规示例：pv.kubernetes.io/bind-completed: "yes"。
### ACK Serverless集群相关
在以下场景中，ACK Serverless集群不提供赔付：
为简化集群运维，ACK Serverless集群提供部分系统组件托管能力，并在集群的组件开启托管后，负责其部署和维护。由于您误删托管组件依赖的K8s对象资源等其他情况导致业务受损时，ACK Serverless不提供赔付。
针对[阿里云容器服务](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud202010221416_90184.html)[Kubernetes](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud202010221416_90184.html)[版服务等级协议](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud202010221416_90184.html)下“除外情形”中列举的情况和原因，ACK Serverless不提供赔付。
### 注册集群相关
通过[容器服务管理控制台](https://cs.console.aliyun.com)的注册集群功能接入外部Kubernetes集群时，请确保外部集群与阿里云之间的网络稳定性。
容器服务ACK提供外部Kubernetes集群的注册接入，但无法管控外部集群自身的稳定性以及不当操作。因此当您通过注册集群配置外部集群节点的Label、Annotation、Tag等信息时，可能导致应用运行异常，请谨慎操作。
### 应用目录相关
为了丰富Kubernetes应用，容器服务ACK的应用市场提供了应用目录，它们是基于开源软件做了适配和二次开发的应用。ACK无法管控开源软件本身产生的缺陷，请知晓此风险。更多信息，请参见[应用市场](../ack-managed-and-ack-dedicated/user-guide/app-marketplace.md)。
## 高危操作
在使用容器服务ACK过程中相关功能模块存在高危操作，可能会对业务稳定性造成较大影响。在使用前请认真了解以下高危操作及其影响。
### 集群相关高危操作
| 分类 | 高危操作 | 影响 | 恢复方案 |
| --- | --- | --- | --- |
| API Server | 复用 API Server 所使用的 CLB 于其他场景，例如使用 LoadBalancer 类型 Service 复用该 CLB。 | 导致集群不可用，影响业务流量。 | 恢复原有配置，或请求售后服务支持。 |
| 修改 API Server 所使用的 CLB 的监听、服务器组、ACL 等控制 CLB 转发的配置、CLB 标签配置。 | 导致集群异常。 | 恢复原有配置。 |  |
| 删除 API Server 所使用的 CLB。 | 导致集群不可操作。 | 不可恢复，请重新创建集群。重建集群请参见 [创建](../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md) [ACK](../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md) [托管集群](../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md) 。 |  |
| Worker 节点 | 修改集群内节点安全组。 | 可能导致节点不可用。 | 将节点重新添加到集群自动创建的节点安全组中，请参见 [为实例（主网卡）关联安全组](../../../ecs/documents/user-guide/manage-ecs-instances-in-security-groups.md) 。 |
| 节点到期或被销毁。 | 该节点不可用。 | 不可恢复。 |  |
| 重装操作系统。 | 节点上组件被删除。 | 节点移出再加入集群。相关操作请参见 [移除节点](../ack-managed-and-ack-dedicated/user-guide/remove-a-node.md) 、 [添加已有节点](../ack-managed-and-ack-dedicated/user-guide/add-existing-ecs-instances-to-an-ack-cluster.md) 。 |  |
| 自行升级节点组件版本。 | 可能导致节点无法使用。 | 回退到原始版本。 |  |
| 更改节点 IP。 | 节点不可用。 | 改回原 IP。 |  |
| 自行修改核心组件（kubelet、docker、containerd 等）参数。 | 可能导致节点不可用。 | 按照官网推荐配置参数。 |  |
| 修改操作系统配置。 | 可能导致节点不可用。 | 尝试还原配置项或删除节点重新购买。 |  |
| 修改节点时间。 | 可能导致节点上组件工作异常。 | 还原节点时间。 |  |
| 通过不受 ACK 支持的方式向集群中添加节点算力资源。 | ACK 提供控制台、OpenAPI、CLI 等方式向集群中增加节点算力资源，请参见 [添加已有节点](../ack-managed-and-ack-dedicated/user-guide/add-existing-ecs-instances-to-an-ack-cluster.md) 。如果您通过其他方式向集群中添加了节点，ACK 无法识别此类节点的来源，无法提供节点生命周期管理、自动化运维和技术支持等产品能力。详细风险说明，请参见 [为什么控制台显示节点所属节点池的来源为“其他节点”？](../ack-managed-and-ack-dedicated/user-guide/faq-about-node-management.md) 。 | 建议通过节点池的方式纳管算力资源。如需继续使用，请自行确保节点与集群各组件（如 Kubernetes 组件、网络、存储、安全组件等）的兼容性。 |  |
| Master 节点（ACK 专有版集群） | 修改集群内节点安全组。 | 可能导致 Master 节点不可用。 | 将节点重新添加到集群自动创建的节点安全组中，请参见 [为实例（主网卡）关联安全组](../../../ecs/documents/user-guide/manage-ecs-instances-in-security-groups.md) 。 |
| 节点到期或被销毁。 | 该 Master 节点不可用。 | 不可恢复。 |  |
| 重装操作系统。 | Master 节点上组件被删除。 | 不可恢复。 |  |
| 自行升级 Master 或者 etcd 组件版本。 | 可能导致集群无法使用。 | 回退到原始版本。 |  |
| 删除或格式化节点 /etc/kubernetes 等核心目录数据。 | 该 Master 节点不可用。 | 不可恢复。 |  |
| 更改节点 IP。 | 该 Master 节点不可用。 | 改回原 IP。 |  |
| 自行修改核心组件（etcd、kube-apiserver、docker 等）参数。 | 可能导致 Master 节点不可用。 | 按照官网推荐配置参数。 |  |
| 自行更换 Master 或 etcd 证书 | 可能导致集群无法使用。 | 不可恢复。 |  |
| 自行增加或减少 Master 节点。 | 可能导致集群无法使用。 | 不可恢复。 |  |
| 修改节点时间。 | 可能导致节点上组件工作异常。 | 还原节点时间。 |  |
| 其他 | 通过 RAM 执行权限变更或修改操作。 | 集群部分资源如负载均衡可能无法创建成功。 | 恢复原先权限。 |
| 说明 仅适用于 1.26 以下版本的集群。 修改或删除集群内预置的 PodSecurityPolicy 相关资源（包括名称为 ack.privileged 的 PodSecurityPolicy 资源，名称以 ack:podsecuritypolicy: 开头的 ClusterRole、ClusterRoleBinding、Role 和 RoleBinding 资源）。 | 可能导致集群核心组件异常、可能导致无法在集群内创建和更新 Pod 资源。 | 恢复相关资源。具体操作，详见 [配置或恢复](../ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md) [ACK](../ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md) [默认的](../ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md) [Pod](../ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md) [安全策略](../ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md) 。 |  |
### 节点池相关高危操作
| 高危操作 | 影响 | 恢复方案 |
| --- | --- | --- |
| 删除伸缩组。 | 导致节点池异常。 | 不可恢复，只能重建节点池。重建节点池请参见 [创建节点池](../ack-managed-and-ack-dedicated/user-guide/create-a-node-pool.md) 。 |
| 通过 kubectl 移除节点。 | 节点池节点数显示和实际不符。 | 通过容器服务管理控制台或者节点池相关 API 移除指定节点（参见 [移除节点](../ack-managed-and-ack-dedicated/user-guide/remove-a-node.md) ）或者修改节点池的期望节点数进行缩容（参见 [创建和管理节点池](../ack-managed-and-ack-dedicated/user-guide/create-a-node-pool.md) ）。 |
| 直接释放 ECS 实例。 | 可能导致节点池详情页面显示异常。开启期望节点数的节点池为维持期望节点数，将会根据相应节点池配置自动扩容到期望节点数。 | 不可恢复。正确做法是通过容器服务管理控制台或者节点池相关 API 修改节点池的期望节点数进行缩容（参见 [创建和管理节点池](../ack-managed-and-ack-dedicated/user-guide/create-a-node-pool.md) ）或移除指定节点（参见 [移除节点](../ack-managed-and-ack-dedicated/user-guide/remove-a-node.md) ）。 |
| 对开启自动伸缩的节点池进行手动扩容或缩容。 | 自动伸缩组件会根据策略自动调整节点数，导致结果与期望不符。 | 不可恢复。自动伸缩节点池无需手动干预。 |
| 修改 ESS 伸缩组的最大或最小实例数。 | 可能导致扩缩容异常。 | 对于未开启自动伸缩组的节点池，ESS 伸缩组最大和最小实例数改为默认值 2000 和 0。 对于开启自动伸缩的节点池，将 ESS 伸缩组最大和最小实例数修改为与节点池最大和最小节点数一致。 |
| 添加已有节点前不进行数据备份。 | 添加前实例上的数据丢失。 | 不可恢复。 手动添加已有节点前必须对要保留的所有数据进行提前备份。 自动添加节点时会执行系统盘替换操作，需要您提前备份保存在系统盘中的有用数据。 |
| 在节点系统盘中保存重要数据。 | 节点池的自愈操作可能通过重置节点配置的方式修复节点，因此可能导致系统盘数据丢失。 | 不可恢复。正确做法是将重要数据存放于额外的数据盘或者云盘、NAS、OSS。 |
### 虚拟节点相关高危操作
| 高危操作 | 影响 | 恢复方案 |
| --- | --- | --- |
| 卸载虚拟节点组件。 | Serverless Pod 管理功能异常：已创建的 ECI Pod 和 ACS Pod 无法正常删除，也无法正常创建新的 ECI Pod 和 ACS Pod。 | 重新 [安装虚拟节点组件](../ack-managed-and-ack-dedicated/user-guide/virtual-node-overview.md) 。 |
### 网络与负载均衡相关高危操作
| 高危操作 | 影响 | 恢复方案 |
| --- | --- | --- |
| 修改内核参数 net.ipv4.ip_forward=0 。 | 网络不通。 | 修改内核参数为 net.ipv4.ip_forward=1 。 |
| 修改内核参数： net.ipv4.conf.all.rp_filter = 1|2 net.ipv4.conf.[ethX].rp_filter = 1|2 说明 ethX 代表所有以 eth 开头的网卡。 | 网络不通。 | 修改内核参数为： net.ipv4.conf.all.rp_filter = 0 net.ipv4.conf.[ethX].rp_filter = 0 |
| 修改内核参数 net.ipv4.tcp_tw_reuse = 1 。 | 导致 Pod 健康检查异常。 | 修改内核参数为 net.ipv4.tcp_tw_reuse = 0 。 |
| 修改内核参数 net.ipv4.tcp_tw_recycle = 1 。 | 导致 NAT 异常。 | 修改内核参数 net.ipv4.tcp_tw_recycle = 0 。 |
| 修改内核参数 net.ipv4.ip_local_port_range 。 | 导致网络偶发不通。 | 修改内核参数到默认值 net.ipv4.ip_local_port_range="32768 60999" 。 |
| 安装防火墙软件，例如 Firewalld 或者 ufw 等。 | 导致容器网络不通。 | 卸载防火墙软件并重启节点。 |
| 节点安全组配置未放通容器 CIDR 的 53 端口 UDP。 | 集群内 DNS 无法正常工作。 | 按照官网推荐配置放通安全组。 |
| 修改或者删除 ACK 添加的 SLB 的标签。 | 导致 SLB 异常。 | 恢复 SLB 的标签。 |
| 通过负载均衡控制台修改 ACK 管理的 SLB 的配置，包括 SLB、监听及虚拟服务器组。 | 导致 SLB 异常。 | 恢复 SLB 的配置。 |
| 移除 Service 中复用已有 SLB 的 Annotation，即 service.beta.kubernetes.io/alibaba-cloud-loadbalancer-id: ${YOUR_LB_ID} 。 | 导致 SLB 异常。 | 在 Service 中添加复用已有 SLB 的 Annotation。 说明 复用已有 SLB 的 Service 无法直接修改为使用自动创建 SLB 的 Service。您需要重新创建 Service。 |
| 通过负载均衡控制台删除 ACK 创建的 SLB。 | 可能导致集群网络异常。 | 通过删除 Service 的方式删除 SLB。删除 Service 请参见 [删除](../ack-managed-and-ack-dedicated/user-guide/service-management.md) [Service](../ack-managed-and-ack-dedicated/user-guide/service-management.md) 。 |
| 在安装 Nginx Ingress Controller 组件的情况下手动删除 kube-system 命名空间下的 nginx-ingress-lb Service。 | Ingress Controller 工作不正常，严重时产生崩溃。 | 使用以下 YAML 新建一个同名 Service。 apiVersion: v1 kind: Service metadata: annotations: labels: app: nginx-ingress-lb name: nginx-ingress-lb namespace: kube-system spec: externalTrafficPolicy: Local ports: - name: http port: 80 protocol: TCP targetPort: 80 - name: https port: 443 protocol: TCP targetPort: 443 selector: app: ingress-nginx type: LoadBalancer |
| 新增或修改 ECS 节点上 DNS 配置文件 /etc/resolv.conf 中 nameserver 选项。 | 若配置的 DNS 服务器配置不合理，可能导致 DNS 无法解析，影响集群正常运行。 | 您如果想要使用自建 DNS 服务器作为上游服务器，建议在 CoreDNS 侧进行配置。具体操作，请参见 [非托管](../ack-managed-and-ack-dedicated/user-guide/configure-coredns.md) [CoreDNS](../ack-managed-and-ack-dedicated/user-guide/configure-coredns.md) [配置说明](../ack-managed-and-ack-dedicated/user-guide/configure-coredns.md) 。 |
| 修改、删除 ACK 创建的弹性网卡、灵骏弹性网卡。 | Pod 网络中断。 | 不可恢复。 |
| 修改、删除网络相关 CRD。 podnetworkings.network.alibabacloud.com podenis.network.alibabacloud.com networkinterfaces.network.alibabacloud.com nodes.network.alibabacloud.com noderuntimes.network.alibabacloud.com *.cilium.io *.crd.projectcalico.org | Terway 组件将无法工作，严重时可能导致网络中断、Pod 异常。 | 不可恢复。 |
| 创建、修改、删除网络相关系统 CR。 podenis.network.alibabacloud.com networkinterfaces.network.alibabacloud.com nodes.network.alibabacloud.com noderuntimes.network.alibabacloud.com *.cilium.io *.crd.projectcalico.org | Terway 组件将无法工作，严重时可能导致网络中断、Pod 异常。 | 删除自定义 CR 定义，并重建关联的 Pod。 |
| 修改、删除 Terway 网络配置中非允许修改的字段。配置参数声明 [自定义](../ack-managed-and-ack-dedicated/user-guide/terway-configuration-parameters.md) [Terway](../ack-managed-and-ack-dedicated/user-guide/terway-configuration-parameters.md) [配置参数](../ack-managed-and-ack-dedicated/user-guide/terway-configuration-parameters.md) 。 | Terway 组件将无法工作，严重时可能导致网络中断、Pod 异常。 | 恢复原有配置，并重启节点。 |
### 存储相关高危操作
| 高危操作 | 影响 | 恢复方案 |
| --- | --- | --- |
| 控制台手动解挂云盘。 | Pod 写入报 IO Error。 | 重启 Pod，手动清理节点挂载残留。 |
| 节点上 umount 磁盘挂载路径 | Pod 写入本地磁盘。 | 重启 Pod。 |
| 节点上直接操作云盘。 | Pod 写入本地磁盘。 | 不可恢复。 |
| 多个 Pod 挂载相同云盘。 | Pod 写入本地磁盘或者报错 IO Error。 | 确保一个云盘给一个 Pod 使用。 重要 云盘为阿里云存储团队提供的非共享存储，只能同时被一个 Pod 挂载。 |
| 手动删除 NAS 挂载目录。 | Pod 写入报 IO Error。 | 重启 Pod。 |
| 删除正在使用的 NAS 盘或挂载点。 | Pod 出现 IO Hang。 | 重启 ECS 节点。重启具体操作，请参见 [重启](../../../ecs/documents/user-guide/restart-instances.md) [ECS](../../../ecs/documents/user-guide/restart-instances.md) [实例](../../../ecs/documents/user-guide/restart-instances.md) 。 |
### 日志相关高危操作
| 高危操作 | 影响 | 恢复方案 |
| --- | --- | --- |
| 删除宿主机 /tmp/ccs-log-collector/pos 目录。 | 日志重复采集。 | 不可恢复。该目录下的文件记录了日志的采集位置。 |
| 删除宿主机 /tmp/ccs-log-collector/buffer 目录。 | 日志丢失。 | 不可恢复。该目录是待消费的日志缓存文件。 |
| 删除 aliyunlogconfig CRD 资源。 | 日志采集失效。 | 重新创建删除的 CRD 以及对应的资源，但失效期间日志无法恢复。 删除 CRD 会关联删除对应所有的实例，即使恢复 CRD 后还需要手动创建被删除的实例。 |
| 删除日志组件。 | 日志采集失效。 | 重新安装日志组件并手动恢复 aliyunlogconfig CRD 实例，删除期间日志无法恢复。 删除日志组件相当于删除 aliyunlogconfig CRD 以及日志采集器 Logtail，期间日志采集能力全部丢失。 |
## 相关文档
[Nginx Ingress Controller](../ack-managed-and-ack-dedicated/user-guide/best-practices-for-the-nginx-ingress-controller.md)[使用建议](../ack-managed-and-ack-dedicated/user-guide/best-practices-for-the-nginx-ingress-controller.md)
[DNS](../ack-managed-and-ack-dedicated/user-guide/dns-best-practice.md)[最佳实践](../ack-managed-and-ack-dedicated/user-guide/dns-best-practice.md)
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
