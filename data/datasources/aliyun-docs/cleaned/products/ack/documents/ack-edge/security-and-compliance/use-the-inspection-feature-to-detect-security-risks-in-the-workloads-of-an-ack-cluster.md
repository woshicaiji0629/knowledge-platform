# 使用配置巡检检查工作负载的安全配置风险-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/use-the-inspection-feature-to-detect-security-risks-in-the-workloads-of-an-ack-cluster

# 配置巡检检查集群工作负载
ACK提供巡检功能，帮助您扫描集群中工作负载配置的安全隐患。执行巡检任务后，系统会生成巡检报告，您可以根据报告结果查看并处理风险项，实时了解集群中工作负载的健康状态。
## 前提条件
集群版本为v1.14及以上版本。如需升级集群，请参见[手动升级集群](../../ack-managed-and-ack-dedicated/user-guide/update-the-kubernetes-version-of-an-ack-cluster.md)。
如果您当前使用的是RAM用户，请确保已参见下方内容完成RAM授权和RBAC授权。
RAM授权
请完成配置巡检页面的RAM授权操作，确保当前RAM用户拥有操作当前集群的配置巡检页面的权限，否则会出现权限不足无法操作配置巡检页面功能的问题。具体操作，请参见[使用](../../ack-managed-and-ack-dedicated/user-guide/create-a-custom-ram-policy.md)[RAM](../../ack-managed-and-ack-dedicated/user-guide/create-a-custom-ram-policy.md)[授予集群及云资源访问权限](../../ack-managed-and-ack-dedicated/user-guide/create-a-custom-ram-policy.md)。
展开查看配置巡检授权代码
{ "Statement": [ { "Action": [ "cs:DescribePolarisConfig", "cs:DescribePolarisJob", "cs:DescribePolarisCronJob", "cs:UpdatePolarisJob", "cs:UpdatePolarisCronJob" ], "Effect": "Allow", "Resource": [ "acs:cs:*:*:cluster/<yourclusterID>" ] } ], "Version": "1" }
如果您需要使用巡检报告功能，请完成日志服务指定logproject（当前集群logtail-ds组件所使用的logproject）的RAM授权，确保当前RAM用户拥有日志服务指定logproject的数据读取权限，否则会出现权限不足无法查看巡检报告的问题。具体操作，请参见[RAM](../../../../sls/documents/use-custom-policies-to-grant-permissions-to-a-ram-user.md)[自定义授权示例](../../../../sls/documents/use-custom-policies-to-grant-permissions-to-a-ram-user.md)。
展开查看日志服务日志读取授权代码
{ "Version": "1", "Statement": [ { "Action": [ "log:Get*", "log:List*" ], "Resource": "acs:log:*:*:project/<指定的Project名称>/*", "Effect": "Allow" } ] }
RBAC授权
请完成配置巡检页面涉及资源的RBAC授权，授予RAM用户指定集群的管理员权限，以确保RAM用户拥有操作配置巡检页面中涉及的Kubernetes资源的权限。具体操作，请参见[使用](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[RBAC](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[授予集群内资源操作权限](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)。
## 执行巡检
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择安全管理>配置巡检。
可选：按照页面提示安装并升级巡检组件。
巡检组件security-inspector本身不计费，但会占用您的Pod资源。组件介绍及变更记录，请参见[security-inspector](../../product-overview/security-inspector.md)。
执行巡检。
重要
请在业务低峰期执行巡检操作。
默认巡检所有支持的检查项，您可以在配置巡检页面右上方，单击巡检配置，然后配置巡检时执行的检查项。更多信息，请参见[检查项](use-the-inspection-feature-to-detect-security-risks-in-the-workloads-of-an-ack-cluster.md)。
立即执行：在配置巡检页面右上方，单击立即执行巡检。
定期执行：在配置巡检页面右上方，单击巡检配置，然后选中定期巡检，并配置巡检周期。
等待巡检完成后，在巡检详情页签，单击巡检结果对应操作列中的详情，查看检查结果。
## 巡检详情
巡检详情页面通过表格化的方式展示不同工作负载的详细巡检结果，主要包括以下功能：
支持按照是否有风险、命名空间、工作负载类别等条件对结果进行过滤展示工作负载的巡检通过项和风险项数量。
展示巡检结果的各个检查项的详细信息，包括Pod和Container维度的检查状态（已通过、未通过）、检查项详细说明以及加固建议。如有未通过的检查项无需处理，您可以将其加入白名单。
查看工作负载的YAML文件。
## 巡检报告
巡检报告页面主要展示最近执行的巡检扫描结果，主要包括以下几类信息：
扫描结果概览，包括总的检查条目数、检查各个资源项数目及百分比、整体的健康度。
各大类扫描结果统计，包括报告健康检查、镜像、网络、资源、安全等大类的结果。
各个Workload配置的详细扫描结果，包括资源类别、资源名称、命名空间、检查类型、检查项、检查结果等内容。
## 检查项
配置巡检功能会扫描并展示以下检查项的扫描结果。
| 检查项 ID | 检查项 | 检查的内容及安全风险 | 修复建议 |
| --- | --- | --- | --- |
| hostNetworkSet | 禁止容器共享主机的网络命名空间 | 通过检查 Workload 的 Pod spec 中是否配置了 hostNetwork: true ，检查是否配置了共享使用主机的网络 namespace。如果配置了，存在 Pod 中容器攻击主机网络、嗅探主机网络数据的风险。 | 修改 Pod spec，删除 hostNetwork 字段。 示例： |
| hostIPCSet | 禁止容器共享主机的 IPC 命名空间 | 通过检查 Workload 的 Pod spec 中是否配置了 hostIPC: true ，检查是否配置了共享使用主机的 IPC namespace。如果配置了，存在 Pod 中容器攻击主机上进程、嗅探主机上进程数据的风险。 | 修改 Pod spec，删除 hostIPC 字段。 示例： |
| hostPIDSet | 禁止容器共享主机的 PID 命名空间 | 通过检查 Workload 的 Pod spec 中是否配置了 hostPID: true ，检查是否配置了共享使用主机的 PID namespace。如果配置了，存在 Pod 中容器攻击主机上进程、采集主机上进程数据的风险。 | 修改 Pod spec，删除 hostPID 字段。 示例： |
| hostPortSet | 禁止容器内进程监听节点主机端口 | 通过检查 Workload 的 Pod spec 中是否配置了 hostPort ，检查是否配置了把容器中监听的端口映射到主机指定端口上。如果配置了，存在挤占主机可用端口以及被非预期的请求方请求容器端口的风险。 | 修改 Pod spec，删除 hostPort 字段。 示例： |
| runAsRootAllowed | 禁止以 root 用户启动容器 | 通过检查 Workload 的 Pod spec 中是否未配置 runAsNonRoot: true ，检查是否未配置使用非 root 用户运行容器。如果未配置，存在被容器中的恶意进程入侵用户应用、入侵主机甚至入侵整个集群的风险。 | 修改 Pod spec，增加 runAsNonRoot: true 。 示例： |
| runAsPrivileged | 禁止以特权模式启动容器 | 通过检查 Workload 的 Pod spec 中是否配置了 privileged: true ，检查是否配置了允许以特权模式运行容器。如果配置了，存在被容器中的恶意进程入侵用户应用、入侵主机甚至入侵集群的风险。 | 修改 Pod spec，删除 privileged 字段。 示例： |
| privilegeEscalationAllowed | 禁止容器内子进程拥有提升权限的能力 | 通过检查 Workload 的 Pod spec 中是否未配置 allowPrivilegeEscalation: false ，检查是否未配置禁止容器中的子进程拥有比父进程更高的权限。如果未配置，存在被容器中的恶意进程实现越权操作的风险。 | 修改 Pod spec，增加 allowPrivilegeEscalation：false 字段。 示例： |
| capabilitiesAdded | 禁用非必需的 Linux Capabilities | 通过检查 Workload 的 Pod spec 中的 capabilities 字段，检查是否配置了允许容器中的进程拥有 SYS_ADMIN、NET_ADMIN、ALL 等特权 Linux Capabilities。如果配置了，存在被容器中的恶意进程通过这些特权入侵用户应用、入侵或破坏组件和集群的风险。 | 修改 Pod spec，根据实际需求只添加必需的 Linux Capabilities，删除不需要的 Linux Capabilities。 不依赖额外 Linux Capabilities，删除所有不需要的 Linux Capabilities。示例： 只添加必需的 Linux Capabilities，删除所有不需要的 Linux Capabilities。示例： |
| notReadOnlyRootFileSystem | 开启容器内的文件系统只读功能 | 通过检查 Workload 的 Pod spec 中是否未配置 readOnlyRootFilesystem: true ，检查是否未配置容器中的文件系统是不可修改的。如果未配置，则存在被容器中的恶意进程恶意修改系统文件的风险。 | 修改 Pod spec，增加 readOnlyRootFilesystem: true ，如果有需要修改某个目录下文件的需求，可以通过 volumeMounts 实现。 示例： 如果需要修改某个目录下的文件，通过 volumeMounts 字段实现。 示例： |
| cpuRequestsMissing | 配置运行容器所需的最少 CPU 资源 | 通过检查 Workload 的 Pod spec 中是否未配置 resources.requests.cpu 字段，可以检查是否未配置运行容器所需的最少 CPU 资源。如果未配置，则 Pod 有被调度到资源紧张的节点上的风险，可能会出现容器内进程运行缓慢的情况。 | 修改 Pod spec，增加 resources.requests.cpu 字段。 示例： |
| cpuLimitsMissing | 限制运行容器可使用的最大 CPU 资源 | 通过检查 Workload 的 Pod spec 中是否未配置 resources.limits.cpu 字段，检查是否未配置运行容器所需的最大 CPU 资源。如果未配置，则存在被容器内的异常进程消耗大量节点资源，甚至把整个节点或集群的资源消耗殆尽的风险。 | 修改 Pod spec，增加 resources.limits.cpu 字段。 示例： |
| memoryRequestsMissing | 配置运行容器所需的最少内存资源 | 通过检查 Workload 的 Pod spec 中是否未配置 resources.requests.memory 字段，检查是否未配置运行容器所需的最少内存资源。如果未配置，Pod 有被调度到资源紧张的节点上的风险，可能会出现容器内进程 OOM 的风险。 | 修改 Pod spec，增加 resources.requests.memory 字段。 示例： |
| memoryLimitsMissing | 限制容器可使用的最大内存资源 | 通过检查 Workload 的 Pod spec 中是否未配置 resources.limits.memory 字段，检查是否未配置运行容器所需的最大内存资源。如果未配置，则存在被容器内的异常进程消耗大量节点资源，甚至把整个节点或集群的资源消耗殆尽的风险。 | 修改 Pod spec，增加 resources.limits.memory 字段。 示例： |
| readinessProbeMissing | 配置容器就绪探针 | 通过检查 Workload 的 Pod spec 中是否未配置 readinessProbe 字段，检查是否未配置检测容器内应用能否正常处理请求的探针。如果未配置，则存在容器内应用异常无法处理请求时仍旧有请求发送，继而导致业务异常的风险。 | 修改 Pod spec，增加 readinessProbe 字段。 示例： |
| livenessProbeMissing | 配置容器存活探针 | 通过检查 Workload 的 Pod spec 中是否未配置 livenessProbe ，检查是否未配置检测容器内应用是否出现异常需要重启容器的探针。如果未配置，存在容器内应用异常需要重启容器才能恢复时未及时重启导致业务异常的风险。 | 修改 Pod spec，增加 livenessProbe 字段。 示例： |
| tagNotSpecified | 容器使用明确的镜像版本 | 通过检查 Workload 的 Pod spec 中的 image 字段的值是否未包含镜像 Tag 或者使用了 latest 作为镜像 Tag，检查是否未配置运行容器时使用指定 Tag 的容器镜像。如果未配置，存在运行容器时运行了非预期的容器镜像版本导致业务异常的风险。 | 修改 Pod spec，修改 image 字段，使用指定的镜像 Tag，并且不要使用 latest 作为镜像 Tag。 示例： |
| anonymousUserRBACBinding | 禁止匿名用户访问集群 | 通过检查集群内的 RBAC（Role-based access control）绑定找出配置了匿名用户访问权限的配置项。如果配置了允许匿名用户访问集群资源的配置项，则存在被恶意匿名用户窃取集群敏感信息、攻击和入侵集群的风险。 | 修改扫描出来的 RBAC 绑定，根据实际情况删除允许匿名用户访问集群资源的权限配置项。 示例： |
## 事件
| 事件类型 | 事件名称 | 事件内容示例 | 事件说明 | 处理措施 |
| --- | --- | --- | --- | --- |
| Normal | SecurityInspectorConfigAuditStart | Start to running config audit | 开始执行巡检任务。 | 无需处理。 |
| Normal | SecurityInspectorConfigAuditFinished | Finished running once config audit | 巡检任务执行完成。 | 无需处理。 |
| Warning | SecurityInspectorConfigAuditHighRiskFound | 2 high risks have been found after running config audit | 巡检执行完之后，发现部分工作负载存在未修复的高风险检查项。 | 在集群的 配置巡检 页面的 巡检详情 页签，查看详细的巡检结果。 按需过滤选项中的 是否有风险 、 命名空间 和 工作负载类别 ，过滤查看有风险的工作负载。 单击 详情 ，查看该工作负载中每个检查项的检查结果。 对于确认无需修复的检查项，单击 加白名单 ，将该检查项加入白名单。 对于确认需要修复的检查项，单击 详情 ，参考加固建议进行修复。 |
## 相关文档
如需进一步提升Pod安全性，可启用安全策略管理功能。更多信息，请参见[启用安全策略管理](../../ack-managed-and-ack-dedicated/security-and-compliance/configure-and-enforce-ack-pod-security-policies.md)。
如需检查集群维度是否存在潜在风险，例如检查资源配额、资源水位等，可使用集群巡检功能。更多信息，请参见[使用集群巡检](../../ack-managed-and-ack-dedicated/user-guide/work-with-the-cluster-inspection-feature.md)。
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
