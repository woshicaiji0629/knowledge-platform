# 启用CPU拓扑感知调度-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/topology-aware-cpu-scheduling

# CPU拓扑感知调度
当多个应用运行在同一节点时，CPU资源争抢和频繁的上下文切换可能导致性能敏感型应用产生抖动。通过启用CPU拓扑感知调度，可将应用进程独占绑定到指定CPU核心（即CPU绑核），减少因核心切换和跨NUMA访存带来的性能不确定性。
## 工作原理
Kubernetes默认依赖内核的CFS调度器（Completely Fair Scheduler）来实现CPU的负载均衡。该调度器通过公平分配CPU时间片将负载“打散”到各个核心，但可能因忽略了CPU的物理拓扑导致性能敏感型应用的性能抖动。
Kubernetes的[CPU Manager（](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/#static-policy)[static](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/#static-policy)[策略）](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/#static-policy)能够为Pod绑定并独占CPU核心，但仍存在以下局限：
调度器无感知：原生kube-scheduler仅在节点维度做决策，无法感知整个集群的CPU拓扑，不能为Pod在全局范围内寻找最优的物理核心布局。
拓扑不敏感：static策略在节点内分配核心时，不感知NUMA架构，可能导致跨NUMA节点的内存访问，引入额外延迟。
灵活性不足：该策略严格要求Pod的QoS为[Guaranteed](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#guaranteed)，不适用于[Burstable](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#burstable)和[BestEffort](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#burstable)类型的Pod。
为此，ACK基于新版Scheduling Framework提供了增强的CPU拓扑感知调度能力，由ACK kube-scheduler和ack-koordinator协同完成。
节点拓扑上报：ack-koordinator实时感知本地的CPU物理拓扑（如Socket、NUMA、缓存），并将其上报至调度中心。
全局拓扑感知调度：kube-scheduler基于全局拓扑信息，在集群范围内为Pod筛选出当前最优节点，并规划核心分配方案（如在选择最优节点时默认寻找已绑定应用数量最少的核）。该分配方案会作为调度结果写入Pod的Annotation中。
本地绑核执行：Pod调度至目标节点后，ack-koordinator会根据Pod的 Annotation 并修改其对应Cgroup的cpuset.cpus文件，以完成物理核心的绑定。
## 适用场景
性能敏感型应用：对CPU上下文切换延迟极度敏感，如高频交易、实时数据处理。
NUMA敏感型应用：部署在神龙裸金属（Intel、AMD）等多核、多Socket服务器上，且业务性能受内存访问延迟影响巨大，期望避免跨NUMA访存。
确定性算力需求：需要稳定、可预期的计算能力，如科学计算、大数据分析任务。
遗留应用适配：应用尚未完成对云原生场景的适配，例如在设置线程数量时未考虑容器规格（而是整机物理核数量），导致性能下降。
重要
不建议在以下场景中启用此功能：
CPU超卖环境：绑核的资源独占特性与超卖的资源共享模型存在不兼容，可能造成资源浪费并干扰超卖调度逻辑。
通用型或I/O密集型应用：大多数Web服务、中间件等应用对CPU核心切换不敏感，无需启用此功能。
## 准备工作
已创建ACK托管集群Pro版，且已配置节点池的CPU Policy（cpuManagerPolicy）为none。请参见[自定义节点池](customize-the-kubelet-configurations-of-a-node-pool.md)[kubelet](customize-the-kubelet-configurations-of-a-node-pool.md)[配置](customize-the-kubelet-configurations-of-a-node-pool.md)配置cpuManagerPolicy取值。
已安装[ack-koordinator](../../product-overview/ack-koordinator-fka-ack-slo-manager.md)，且组件版本为0.2.0及以上。
## 步骤一：部署示例应用
本文以一个Nginx应用为例，介绍如何启用CPU拓扑感知调度，实现CPU绑核。
创建nginx-app.yaml。
展开查看YAML
apiVersion: apps/v1 kind: Deployment metadata: name: nginx-deployment namespace: default labels: app: nginx spec: replicas: 1 selector: matchLabels: app: nginx template: metadata: labels: app: nginx spec: containers: - name: nginx image: alibaba-cloud-linux-3-registry.cn-hangzhou.cr.aliyuncs.com/alinux3/nginx_optimized:20240221-1.20.1-2.3.0 ports: - containerPort: 80 command: - "sleep" - "infinity" resources: requests: cpu: 4 memory: 8Gi limits: # 设置cpu值，需为整数。 cpu: 4 memory: 8Gi
部署应用。
kubectl apply -f nginx-app.yaml
[登录](overview-of-node-management.md)[Pod](overview-of-node-management.md)[所在节点](overview-of-node-management.md)，获取Pod的UID和Container ID。
获取Pod名称。
执行kubectl get pods -n <your-namespace>查看Pod名称，如nginx-deployment-6f5899*****。
获取Pod UID。
# 将 <your-pod-name> 替换为Pod实际名称 kubectl get pod <your-pod-name> -n default -o jsonpath='{.metadata.uid}{"\n"}'
预期输出：
uid: a78a02b5-c87f-4e74-9ddd-254c163*****
获取Container ID。
# 将 <your-pod-name> 替换为Pod实际名称 kubectl describe pod <your-pod-name> -n default
在输出的Containers字段下定位Container ID，并删去前缀（如containerd://）。
预期输出：
Containers: nginx: Container ID: containerd://b8b88a70096aabb0aea197dd2aba78d15bcbe9145198ef46a0474b31*****
确认节点的cgroup版本。
stat -fc %T /sys/fs/cgroup/
输出为cgroup_root：系统使用 cgroup v1。
输出为cgroup2fs：系统使用 cgroup v2。
根据cgroup版本执行对应的验证命令，查看CPU绑核情况。
在cgroup路径中，Pod UID中的-需替换为_。如原始Pod UID为a78a02b5-c87f-4e74-9ddd-254c163*****，则路径中使用的格式为a78a02b5_c87f_4e74_9ddd_254c163*****。
cgroup v1：
# 将 <POD_UID> 和 <CONTAINER_ID> 替换为实际值 cat /sys/fs/cgroup/cpuset/kubepods.slice/kubepods-pod<POD_UID>.slice/cri-containerd-<CONTAINER_ID>.scope/cpuset.cpus
cgroup v2：
# 将 <POD_UID> 和 <CONTAINER_ID> 替换为实际值 cat /sys/fs/cgroup/kubepods.slice/kubepods-pod<POD_UID>.slice/cri-containerd-<CONTAINER_ID>.scope/cpuset.cpus.effective
预期输出为一个范围，代表容器可以使用节点上的所有核心，未进行绑定。
0-31
## 步骤二：启用CPU拓扑感知调度功能
可通过为Pod添加Annotation来启用CPU拓扑感知调度。
[普通绑核策略](topology-aware-cpu-scheduling.md)：通用策略，遵循1:1的绑核原则，为Pod绑定resources.limits.cpu所指定的数量的核心。优先选择同一NUMA节点内的CPU核，以保证良好的内存访问性能。
[自动绑核策略](topology-aware-cpu-scheduling.md)：针对特定硬件优化的策略，优先通过绑定一个完整的物理核心簇（如AMD CPU的CCX/CCD）来最大化CPU局部性并提升并发度。推荐在特定的大规格（如32核及以上）AMD机型上使用。
重要
启用CPU拓扑感知调度时，请勿在Pod上直接指定nodeName，kube-scheduler不参与此类Pod的调度过程。可使用nodeSelector等字段配置亲和性策略来指定节点调度。
## 普通绑核策略
配置方法：
在YAML中添加Annotationcpuset-scheduler: "true"
Pod中：在metadata.annotations字段中添加
工作负载（例如Deployment）中：在spec.template.metadata.annotations字段中添加
在Containers字段中配置resources.limits.cpu的取值（需为整数），限定CPU绑核范围。
配置示例：
apiVersion: apps/v1 kind: Deployment metadata: name: nginx-deployment namespace: default labels: app: nginx spec: replicas: 1 selector: matchLabels: app: nginx template: metadata: annotations: # 设置为true，启用CPU拓扑感知调度 cpuset-scheduler: "true" labels: app: nginx spec: containers: - name: nginx image: alibaba-cloud-linux-3-registry.cn-hangzhou.cr.aliyuncs.com/alinux3/nginx_optimized:20240221-1.20.1-2.3.0 ports: - containerPort: 80 command: - "sleep" - "infinity" resources: requests: cpu: 4 memory: 8Gi limits: # 设置cpu值，需为整数 cpu: 4 memory: 8Gi
结果验证：
可通过以下两种方式查看。
## 查看节点Cgroup文件
等待Pod正常运行后，再次[登录其所在节点](overview-of-node-management.md)，查看CPU绑核情况。
Pod UID中的-需替换为_。
cgroup v1：
# 将 <POD_UID> 和 <CONTAINER_ID> 替换为实际值 cat /sys/fs/cgroup/cpuset/kubepods.slice/kubepods-pod<POD_UID>.slice/cri-containerd-<CONTAINER_ID>.scope/cpuset.cpus
cgroup v2：
# 将 <POD_UID> 和 <CONTAINER_ID> 替换为实际值 cat /sys/fs/cgroup/kubepods.slice/kubepods-pod<POD_UID>.slice/cri-containerd-<CONTAINER_ID>.scope/cpuset.cpus.effective
预期输出为一组核心ID，与limits.cpu: 4的设置相符，表明绑核成功。
0-3
## 检查Pod Annotation
Pod调度至目标节点后，ack-koordinator会根据Pod的 Annotation 并修改其对应Cgroup的cpuset.cpus文件，以完成物理核心的绑定。
查看Podcpuset信息。
# 将 <your-pod-name> 替换实际Pod名称 kubectl get pod <your-pod-name> -n default -o yaml | grep "cpuset:"
预期输出：
cpuset: '{"nginx":{"0":{"elems":{"0":{},"1":{},"2":{},"3":{}}}}}'
输出结果说明：
"nginx":{...}：针对名为nginx的容器的配置。
"0":{...}：最外层的键"0"代表NUMA节点ID。本示例表示所有绑定的核都位于同一NUMA Node 0上，避免了跨NUMA访存的性能损耗。
"elems":{"0":{},"1":{},"2":{},"3":{}}：键代表被绑定的物理CPU核心ID。此示例中，容器被成功绑定到了0、1、2、3这四个核心上，与limits.cpu: 4相符。
## 自动绑核策略
配置方法：
添加两个Annotation：cpuset-scheduler: "true"和cpu-policy: "static-burst"
Pod中：在metadata.annotations字段中添加
工作负载（例如Deployment）中：在spec.template.metadata.annotations字段中添加
在Containers字段中配置resources.limits.cpu的取值（需为整数），限定CPU绑核范围。
配置示例：
apiVersion: apps/v1 kind: Deployment metadata: name: nginx-deployment namespace: default labels: app: nginx spec: replicas: 1 selector: matchLabels: app: nginx template: metadata: annotations: # 设置为true，启用CPU拓扑感知调度 cpuset-scheduler: "true" # 设置为static-burst，启用自动绑核与NUMA亲和策略 cpu-policy: "static-burst" labels: app: nginx spec: containers: - name: nginx image: alibaba-cloud-linux-3-registry.cn-hangzhou.cr.aliyuncs.com/alinux3/nginx_optimized:20240221-1.20.1-2.3.0 ports: - containerPort: 80 command: - "sleep" - "infinity" resources: requests: cpu: 4 memory: 8Gi limits: # 设置cpu值，需为整数 cpu: 4 memory: 8Gi
结果验证：
自动绑核策略会实时分析节点的CPU拓扑和资源使用情况，绑核数量可能会大于Pod的显式请求。绑核情况可通过以下两种方式查看。
## 查看节点Cgroup文件
等待Pod正常运行后，再次[登录其所在节点](overview-of-node-management.md)，查看CPU绑核情况。
Pod UID中的-需替换为_。
cgroup v1：
# 将 <POD_UID> 和 <CONTAINER_ID> 替换为实际值 cat /sys/fs/cgroup/cpuset/kubepods.slice/kubepods-pod<POD_UID>.slice/cri-containerd-<CONTAINER_ID>.scope/cpuset.cpus
cgroup v2：
# 将 <POD_UID> 和 <CONTAINER_ID> 替换为实际值 cat /sys/fs/cgroup/kubepods.slice/kubepods-pod<POD_UID>.slice/cri-containerd-<CONTAINER_ID>.scope/cpuset.cpus.effective
预期输出为一组确切的核心ID，表明绑核成功。
0-7
## 检查Pod Annotation
Pod调度至目标节点后，ack-koordinator会根据Pod的 Annotation 并修改其对应Cgroup的cpuset.cpus文件，以完成物理核心的绑定。
查看Podcpuset信息。
# 将 <your-pod-name> 替换实际Pod名称 kubectl get pod <your-pod-name> -n default -o yaml | grep "cpuset:"
预期输出：
cpuset: '{"nginx":{"0":{"elems":{"0":{},"1":{},"2":{},"3":{},"4":{},"5":{},"6":{},"7":{}}}}}'
输出结果说明：
"nginx":{...}：针对名为nginx的容器的配置。
"0":{...}：最外层的键"0"代表NUMA节点ID。本示例表示所有绑定的核都位于同一NUMA Node 0上，避免了跨NUMA访存的性能损耗。
"elems":{"0":{},"1":{},"2":{},"3":{},"4":{},"5":{},"6":{},"7":{}}：键代表被绑定的物理CPU核心ID。此示例中，容器已绑定至0～7核心上。
## 相关操作
### 停用CPU拓扑感知调度（CPU核心解绑）
编辑应用YAML，从spec.template.metadata.annotations中移除Annotationcpuset-scheduler: "true"和cpu-policy: "static-burst"（如有）。
在业务低峰期应用修改后的YAML，等待Pod重启后变更生效。
重要
解绑后，Pod 进程不再被绑定到特定物理核心，可能会在节点所有可用 CPU 核心之间切换。潜在影响包括：
因跨核心的上下文切换，CPU 使用率可能微幅上升。
对于计算密集型应用，由于无法独占核心，可能会重新出现因 CPU 资源争抢导致的性能抖动。
当多个高负载 Pod 的进程被调度至同一核心时，可能导致该核心负载瞬时过高，进而触发容器的 CPU 限流（Throttling）。
## 生产环境使用建议
可观测性：在启用绑核前后，[接入阿里云](use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md)[Prometheus](use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md)[监控](use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md)，密切关注应用的关键性能指标（如RT、QPS）以及节点的CPU使用率、CPU Throttling等指标，关注绑核带来的性能变化。
分批变更：对于多副本应用，建议采用金丝雀发布或分批更新的方式，逐步启用或停用绑核策略，以控制变更风险。
## 费用说明
ack-koordinator组件本身的安装和使用免费，但在以下场景中可能产生额外费用。
ack-koordinator是非托管组件，安装后将占用Worker节点资源。您可以在安装组件时配置各模块的资源申请量。
ack-koordinator默认会将资源画像、精细化调度等功能的监控指标以Prometheus的格式对外透出。若您配置组件时开启了ACK-Koordinator开启Prometheus监控指标选项并使用了阿里云Prometheus服务，这些指标将被视为[自定义指标](../../../../arms/documents/prometheus-monitoring/basic-metrics.md)并产生相应费用。具体费用取决于您的集群规模和应用数量等因素。建议您在启用此功能前，仔细阅读阿里云Prometheus[Prometheus 实例计费](../../../../arms/documents/prometheus-monitoring/product-overview/billing-description.md)，了解自定义指标的免费额度和收费策略。您可以通过[用量查询](../../../../arms/documents/prometheus-monitoring/product-overview/billing-and-usage-query.md)，监控和管理您的资源使用情况。
## 相关文档
ACK支持[GPU](../../topology-aware-gpu-scheduling.md)[拓扑感知调度](../../topology-aware-gpu-scheduling.md)，可在节点的GPU组合中选择具有最优训练速度的组合。
可将集群中已分配但未使用的资源量化并提供给低优先级任务使用，以实现[动态资源超卖](dynamic-resource-overcommitment.md)。
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
