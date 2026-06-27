# 添加边缘节点-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/add-an-edge-node

# 添加边缘节点
ACK Edge集群的边缘节点池支持添加多种类型的资源，例如不同地域的ECS节点，IDC节点，其他厂商云节点，以及分布在工厂、门店、车辆和船舶中的服务器节点。本文介绍如何在ACK Edge集群中的边缘节点池中添加边缘节点。
## 前提条件
已[创建](create-an-ack-edge-cluster-1.md)[ACK Edge](create-an-ack-edge-cluster-1.md)[集群](create-an-ack-edge-cluster-1.md)。
## 使用限制
请确保您的集群配额充足。如需添加更多节点，请[到配额平台提交申请](https://quotas.console.aliyun.com/products/csk/quotas)扩大配额。关于ACK Edge集群的配额限制，请参见[配额与限制](../../product-overview/limits.md)。
添加边缘节点时会访问部分域名地址，需要节点侧网络安全组放开限制允许访问。具体信息，请参见[公网接入的网络配置](network-configuration-for-public-network-access.md)。
在添加边缘节点时需要选择节点操作系统，目前支持接入以下节点操作系统。
| 系统架构 | 系统版本 | 系统内核版本 | 边缘 Kubernetes 集群版本 |
| --- | --- | --- | --- |
| AMD64/x86_64 | Anolis7.9、Anolis8.6 | 4.19.X | ≥1.16.9-aliyunedge.1 |
| AMD64/x86_64 | Alibaba Cloud Linux 2.1903 | 4.19.X | ≥1.20.11-aliyunedge.1 |
| AMD64/x86_64 | Alibaba Cloud Linux 3 | 5.10.X | ≥1.20.11-aliyunedge.1 |
| AMD64/x86_64 | CentOS 7.4、CentOS 7.5、CentOS 7.6、CentOS 7.7、CentOS 7.8、CentOS 7.9 | 3.10.X | 1.12.6-aliyunedge.1≤集群版本≤1.30.7-aliyun.1 |
| AMD64/x86_64 | CentOS 8.0、CentOS 8.2 | 4.18.X | 1.18.8-aliyunedge.1≤集群版本≤1.30.7-aliyun.1 |
| AMD64/x86_64 | Ubuntu 16.04 | 4.4.X | 1.18.8-aliyunedge.1≤集群版本≤1.30.7-aliyun.1 |
| AMD64/x86_64 | Ubuntu 18.04 | 4.15.X | 1.12.6-aliyunedge.1≤集群版本≤1.30.7-aliyun.1 |
| AMD64/x86_64 | Ubuntu 18.04 | 5.4.X | ≥1.16.9-aliyunedge.1 |
| AMD64/x86_64 | Ubuntu 18.04 | 5.11.X | ≥1.18.8-aliyunedge.1 |
| AMD64/x86_64 | Ubuntu 20.04 | 5.4.X | ≥1.18.8-aliyunedge.1 |
| AMD64/x86_64 | Ubuntu 20.04、Ubuntu 22.04 | 5.15.X | ≥1.26.3-aliyun.1 |
| AMD64/x86_64 | Ubuntu 24.04 | 6.8.X | ≥1.30.7-aliyun.1 |
| AMD64/x86_64 | Red Hat Enterprise Linux 8.8、Red Hat Enterprise Linux 8.10 | 4.18.X | 1.26.3-aliyun.1≤集群版本≤1.30.7-aliyun.1 |
| AMD64/x86_64 | Kylin V10 | 4.19.X | ≥1.26.3-aliyun.1 |
| AMD64/x86_64 | UnionTech OS Server 20 | 4.19.X | ≥1.26.3-aliyun.1 |
| AMD64/x86_64 | Red Hat Enterprise Linux 9.3 | 5.14.X | ≥1.30.7-aliyun.1 |
| Arm64 | CentOS 8.0 | 4.19.X | ≥1.14.8-aliyunedge.1 |
| Arm64 | Ubuntu 18.04 | 4.9.X | 1.14.8-aliyunedge.1≤集群版本≤1.30.7-aliyun.1 |
| Arm64 | Ubuntu 18.04 | 4.19.X | ≥1.14.8-aliyunedge.1 |
| Arm64 | Ubuntu 20.04 | 5.10.X | ≥1.22.15-aliyunedge.1 |
若您想在集群中添加GPU节点，添加方式请参见[添加](add-a-gpu-node.md)[GPU](add-a-gpu-node.md)[节点](add-a-gpu-node.md)。
## 添加节点
## 1.26及以上版本集群
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点池。
在节点池页面，选择目标节点池右侧操作列的> 添加已有节点。
进入添加现有边缘节点页面，配置云边缘通信参数和高级选项。
说明
如果以下界面参数无法满足需求，您可以参考下文[参数列表](add-an-edge-node.md)修改生成脚本中edgeadm的参数完成配置。
| 分类 | 配置项 | 说明 |
| --- | --- | --- |
| 云边缘通信配置 | Token 有效时间 | 表示脚本的有效时间。默认值为 1 小时。 如果您需要长时间使用同一个脚本做批量添加，可以适当增加脚本的生效时间。 |
|  |  |  |
| 启用静默模式 | 是否启用静默模式。 在边缘节点接入执行过程中，某些步骤可能需要您介入做出判断，例如是否需要将节点上已存在的运行时重新安装。 默认为是，表示所有的问题回答自动回复 yes ，自动推进流程。 |  |
| 高级选项 | 节点标签（Labels） | 为待接入的节点添加标签。 节点池支持给节点池内所有节点添加标签的功能。如果该 label 与节点池上的 label key 名称冲突，节点池上定义的 label 优先级更高。 |
| 污点（Taints） | 为待接入的节点添加污点。 |  |
| 注释 | 为待接入的节点添加注解。 如果该 annotations 与节点池上的 annotations 名称冲突，节点池上定义的 annotations 优先级更高。 |  |
| 自动完成时间同步 | 开启后，表示由 edgeadm 自动完成时间同步。 |  |
| 节点网络接口 | 指定用于获取节点 IP 和容器网络通信使用的主机网卡名称。如设置为空，将自动选择默认路由对应的网卡。 |  |
| 组件下载自 | 节点上系统组件镜像的下载来源。默认为公网。 通过私网下载时，节点需已接入专线节点池。 |  |
| 运行时工作目录 | 指定运行时的工作目录，该配置在 manageRuntime 为 true 时才会生效。 containerd 运行时的默认路径为 /var/lib/containerd 。 |  |
配置完成后单击确定，进入提交结果页面，单击复制，到您的边缘节点上粘贴并执行该脚本。
添加边缘节点成功后，终端输出如下日志，最后一行表示节点已成功加入集群。
I0410 10:54:25.801554 19419 join-node.go:241] [join-node] Config the kubelet service configuration successfully. I0410 10:54:25.801590 19419 join-node.go:246] [join-node] Adding edge hub static yaml I0410 10:54:25.801662 19419 join-node.go:279] [join-node] Add edge hub static yaml is ok I0410 10:54:25.801666 19419 join-node.go:384] [join-node] Start to joining node to cluster. I0410 10:54:27.338166 19419 join-node.go:393] [join-node] Join node to cluster successfully. I0410 10:54:27.338214 19419 install.go:151] [install-edgehub] Checking edgehub status I0410 10:54:37.357405 19419 install.go:156] [install-edgehub] Edgehub is ok I0410 10:54:37.357421 19419 install.go:86] [install-edgehub] Reconfiguring the kubelet configuration files. I0410 10:54:37.364387 19419 install.go:103] [install-edgehub] Reconfigure the kubelet configuration files successfully. I0410 10:54:37.364400 19419 install.go:104] [install-edgehub] Restarting the kubelet. I0410 10:54:52.626540 19419 install.go:127] [install-edgehub] Restart the kubelet successfully. I0410 10:54:52.626613 19419 postcheck.go:77] [post-check] Checking docker status I0410 10:54:52.629194 19419 postcheck.go:86] [post-check] docker is ok I0410 10:54:52.629208 19419 postcheck.go:92] [post-check] Checking kubelet status I0410 10:54:52.631661 19419 postcheck.go:100] [post-check] Kubelet is ok I0410 10:54:52.631671 19419 postcheck.go:106] [post-check] Checking edgehub status I0410 10:54:52.642345 19419 postcheck.go:113] [post-check] Edgehub is ok I0410 10:54:52.642356 19419 postcheck.go:129] [post-check] Checking addon kube-proxy status. I0410 10:54:52.683227 19419 postcheck.go:133] [post-check] kube-proxy is OK. I0410 10:54:52.683243 19419 postcheck.go:129] [post-check] Checking addon flannel status. I0410 10:54:52.724501 19419 postcheck.go:133] [post-check] flannel is OK. I0410 10:54:52.724518 19419 postcheck.go:129] [post-check] Checking addon coredns status. I0410 10:54:52.764745 19419 postcheck.go:133] [post-check] coredns is OK. I0410 10:54:52.764763 19419 postcheck.go:165] [post-check] Callback to the OpenAPI. I0410 10:54:53.014706 19419 postcheck.go:178] [post-check] Callback to the OpenAPI successfully. I0410 10:54:53.014760 19419 postcheck.go:66] This node joined into the cluster successfully.
## 1.26以下版本集群
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点池。
在节点池页面，选择目标节点池右侧操作列的>添加已有节点。
进入添加节点页面，默认通过手动添加方式添加现有实例。
说明
目前手动添加的方式支持添加云上ECS节点、云上ENS节点和非云节点。
单击下一步进入实例信息页面，您可以在此处填写节点接入配置，具体的配置参数，请参见[参数列表](add-an-edge-node.md)。
选择架构为AMD64/X86_64或ARM64，勾选轻量化接入后，在配置区域的 JSON 编辑器中设置接入参数，例如将enableIptables、quiet、manageRuntime设为true，在allowedClusterAddons中指定kube-proxy、flannel、coredns。
说明
脚本有效时间的默认值是1小时，如果您需要长时间使用同一个脚本做批量添加，可以适当增加脚本的生效时间。当脚本有效时间配置为0小时，表示脚本永远生效。
配置完成后单击下一步，进入添加完成页面，单击复制，到您的边缘节点上粘贴并执行该脚本。
## 参数列表
如果控制台上已有参数无法满足需求，您可以根据以下参数列表修改生成脚本中edgeadm的参数完成配置。
| 参数 | 与控制台对应的参数 | 参数说明 | 描述 |
| --- | --- | --- | --- |
| quiet | 启用静默模式 | 是否启用静默模式。在节点接入执行过程中，某些步骤可能需要您介入做出判断，例如是否需要将节点上已存在的运行时重新安装。 | true ：默认值，假设所有的问题回答自动回复 yes ，自动推进流程。 false ：节点接入过程中，可能需暂停以获取您的确认，节点接入过程可能中断。 |
| manageRuntime | 无 | 是否由 edgeadm 检测并安装运行时。 | true ：默认值，检测并安装运行时。 false ：不安装运行时，需要用户在节点上提前安装好运行时。 |
| nodeNameOverride | 无 | 设置节点名。 | "" ：默认值，表示使用主机名。 "XXX" ：表示指定节点名为 XXX。 "*" ：表示随机生成 6 位字符串。 "*.XXX" ：表示随机生成 6 位字符串+XXX 后缀。 |
| allowedClusterAddons | 无 | 需要安装的组件列表。普通节点需要配置为["kube-proxy","flannel","coredns"]。 | ["kube-proxy","flannel","coredns"] ：默认值。 |
| gpuVersion | 无 | 表示要接入的节点是否为 GPU 节点，默认为空。 当前支持的 GPU 版本，请参见 [GPU](add-a-gpu-node.md) [型号](add-a-gpu-node.md) 。 | "" ：默认值，表示不作为 GPU 节点接入。 ACK Edge 集群 从 1.26 版本开始，接入 Nvidia GPU 时，无需配置 gpuVersion 参数直接接入，由接入工具自动检查 GPU 型号并安装相关组件。 |
| labels | 节点标签（Labels） | 表示接入时节点要加的标签。节点池支持给节点池内所有节点添加标签的功能。如果该 label 与节点池上的 label key 名称冲突，节点池上定义的 label 优先级更高。 | {} ：表示不添加任何标签。 |
| annotations | 注释 | 表示接入时给节点加的注解。如果该 annotations 与节点池上的 annotations 名称冲突，节点池上定义的 annotations 优先级更高。 | {} ：表示不添加任何注解。 |
| taints | 污点（Taints） | 表示接入时给节点加上的污点。 | [] |
| nodeIface | 无 | 指定主机网卡，该参数有两个作用： kubelet 从指定的网卡获取节点 IP 信息。 设置容器网络插件 flannel 使用的网卡。 | "" ：如果设为空，kubelet 将按如下顺序获取节点 IP。 在 /etc/hosts 中寻找与主机名同名的记录。 默认路由所在的网络接口的 IP 地址。 flannel 将使用节点默认路由所在的网卡。 |
| runtimeRootDir | 运行时工作目录 | 指定运行时的工作目录，该配置在 manageRuntime 为 true 时才会生效。 | "" ：默认值。 当运行时为 Docker 时，默认路径为 /var/lib/docker 。 当运行时为 Containerd 时，默认路径为 /var/lib/containerd 。 |
| imageRepoType | 组件下载自 | 指定节点上系统组件镜像的下载来源。 | "" ：默认值，表示专线节点池的节点从内网下载镜像，普通节点池的节点从公网下载镜像。 public ：表示从公网下载镜像。 private ：表示从内网下载镜像（节点已接入专线节点池）。 |
| selfHostNtpServer | 自动完成时间同步 | 是否手动完成时间同步。 | false ：默认值，表示由 edgeadm 自动完成时间同步。 true ：表示不需要自动时间同步，已经手动完成时间同步。 |
| flannelIface | 节点网络接口 | flannel 使用的网卡名（不推荐使用，可以使用 nodeIface 参数代替）。 | "" ：默认值，flannel 使用节点默认路由所使用的网卡。 |
| enableIptables | 无 | edgehub 是否开启 iptables 优化（不推荐使用，1.22 后已废弃）。 | false ：表示不启用 iptables。 |
## 相关文档
如果您在添加边缘节点时遇到问题，请参见[诊断边缘节点问题](diagnose-edge-node-problems.md)。
如果您需要移除不使用的边缘节点，请参见[移除边缘节点](remove-edge-nodes.md)。
如果您需要实现边缘节点的自主管理，请参见[设置边缘节点自治](configure-node-autonomy.md)。配置后，当云边网络断开时，边缘节点上的业务仍然可以持续稳定地运行。
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
