# 使用Gang scheduling实现批量作业的All-or-Nothing调度-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/work-with-gang-scheduling

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-managed-and-ack-dedicated/product-overview.md)

- [快速入门](products/ack/documents/ack-managed-and-ack-dedicated/getting-started.md)

- [操作指南](products/ack/documents/ack-managed-and-ack-dedicated/user-guide.md)

- [实践教程](products/ack/documents/ack-managed-and-ack-dedicated/use-cases.md)

- [安全合规](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference.md)

- [服务支持](products/ack/documents/ack-managed-and-ack-dedicated/support.md)

[首页](https://help.aliyun.com/zh)

# 使用Gang scheduling

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

ACK基于新版的kube-scheduler框架实现Gang scheduling的能力。Gang scheduling主要用于确保一组关联的Pod能够同时调度到集群中的节点上，或者如果无法满足这种条件，则这些Pod都不会被调度，解决原生调度器无法支持All-or-Nothing作业调度的问题。这种策略在执行需要严格同步或共享资源的分布式应用时非常有用，例如Spark、Hadoop等大数据处理任务。本文介绍如何使用Gang scheduling。

## 重要提示

请预留足够资源：使用弹性节点池时请保证弹性节点池的最大资源量以及节点标签能够满足Pod需求，否则可能导致Pod无法使用弹性节点池弹出的节点，造成损失。

## 前提条件

已创建1.16及以上版本的[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[Pro](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[版](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。如需升级集群，请参见[手动升级集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/update-the-kubernetes-version-of-an-ack-cluster.md)。

## 功能介绍

Kubernetes目前已经广泛的应用于在线服务编排。为了提升集群的利用率和运行效率，ACK希望将Kubernetes作为一个统一的管理平台来管理在线服务和离线作业。由于调度器的限制，使得一些离线的工作负载无法迁移到Kubernetes。例如，某些有All-or-Nothing特点的作业要求所有的任务在同一时间被调度，如果只是部分任务启动的话，启动的任务将持续等待剩余的任务被调度。在最坏的情况下，所有作业都处于挂起状态，从而导致死锁。此情况下，调度器需要Gang scheduling策略。

Gang scheduling策略可在并发系统中将多个相关联的进程调度到不同处理器上同时运行。最主要的原则是保证所有相关联的进程能够同时启动，防止部分进程的异常，避免整个关联进程组的阻塞。例如，当您提交一个包含多个任务的批量Job时，可能会出现多个任务全部调度成功或者都调度失败的情况。这种All-or-Nothing调度场景，就被称作Gang scheduling。

ACK将一组需要同时调度的Pod称为PodGroup。您在提交All-or-Nothing作业时，可以设置labels字段，指定所属PodGroup的名称以及保证作业正常运行Task的最少运行个数。调度器会根据您指定的最少运行个数进行调度，只有当集群资源满足该Task最少运行个数时，才会统一调度，否则作业将一直处于Pending状态。

## 相关视频

下方视频介绍如何安装Arena并使用Arena提交Gang Scheduling任务。

## 使用方式

- 

使用Gang scheduling时，在创建的Pod处通过设置labels的形式配置min-available和name。使用这种方式时，调度器会自动创建对应的PodGroup，并将pod-group.scheduling.sigs.k8s.io/name的值作为PodGroup的Name，因此pod-group.scheduling.sigs.k8s.io/name的值必须满足DNS子域名的命名规则。详细要求，请参见[对象名称和](https://kubernetes.io/zh-cn/docs/concepts/overview/working-with-objects/names/#dns-label-names)[ID](https://kubernetes.io/zh-cn/docs/concepts/overview/working-with-objects/names/#dns-label-names)。

labels: pod-group.scheduling.sigs.k8s.io/name: tf-smoke-gpu pod-group.scheduling.sigs.k8s.io/min-available: "3"

- 

name：PodGroup的名称。

- 

min-available：该批Pod满足min-available的数量时，才能被统一创建及调度。

- 

您可以使用以下两种方式使用Gang scheduling策略。对于1.22及以上版本的集群，调度器版本需要高于1.xx.xx-aliyun-4.0。

- 

创建对应的PodGroup自定义资源，通过pod-group.scheduling.sigs.k8s.io或者pod-group.scheduling.sigs.k8s.io/name声明Pod对应的PodGroup，此时Pod与PodGroup处于同一命名空间下。

重要

自1.31版本起，ACK将不再支持scheduling.sigs.k8s.io/v1alpha1版本的PodGroup资源，仅支持scheduling.x-k8s.io/v1alpha1版本的PodGroup资源。

# PodGroup CRD spec apiVersion: scheduling.sigs.k8s.io/v1alpha1 kind: PodGroup metadata: name: nginx spec: scheduleTimeoutSeconds: 10 minMember: 3 --- # 为容器添加标签“pod-group.scheduling.sigs.k8s.io/name”。 labels: pod-group.scheduling.sigs.k8s.io/name: nginx

- 

在创建的Pod处通过设置annotations的形式设置min-available和name。不支持koordinator API中的total-number和mode参数。

annotations: gang.scheduling.koordinator.sh/name: "gang-example" gang.scheduling.koordinator.sh/min-available: "2"

说明

属于同一个PodGroup的Pod必须保持相同的优先级。

## 高级用法

### 使用限制

对于1.22及以上版本的集群，调度器版本需要高于1.xx.xx-aliyun-4.0。

### 声明GangGroup

使用Gang scheduling时，部分任务可能存在多种不同角色，例如PyTorch任务中的PS与Worker，这些角色对min-available的需求可能存在差异。使用单一的PodGroup时可能导致多个角色各自的min-available无法得到满足，使用多个PodGroup时又会导致整体失去Gang的保证。此情况下推荐您使用GangGroup功能，该功能允许您将多个Gang合并为一组。调度器在进行调度时只在多个Gang的min-available条件均满足时允许任务执行，保证任务的多个角色均满足min-available特性。

- 

当您使用Label方式时，可以在Pod上使用以下Label。

pod-group.scheduling.sigs.k8s.io/groups: "[\"default/gang-example1\", \"default/gang-example2\"]"

- 

当您使用PodGroup方式时，可以在PodGroup自定义资源上使用以下Label。

pod-group.scheduling.sigs.k8s.io/groups: "[\"default/gang-example1\", \"default/gang-example2\"]"

- 

当您使用Annotation方式时，可以在Pod上使用以下Annotation。

gang.scheduling.koordinator.sh/groups: "[\"default/gang-example1\", \"default/gang-example2\"]"

### 声明matchpolicy

使用Gang scheduling时，您可以通过声明match-policy以使PodGroup在对Pod进行计数时考虑不同类型的。

- 

当您使用Label方式时，可以在Pod上使用以下Label。

pod-group.scheduling.sigs.k8s.io/match-policy: "waiting-and-running"

- 

当您使用PodGroup方式时，可以在PodGroup自定义资源上使用以下Label。

pod-group.scheduling.sigs.k8s.io/match-policy: "waiting-and-running"

- 

如果您使用的是Annotation方式，目前仅支持once-satisfied匹配。

支持的各种匹配方式以及功能如下表所示。

| 匹配方式取值 | 说明 |
| --- | --- |
| only-waiting | 匹配时只关注完成资源预占的 Pod。 |
| waiting-and-running | 匹配时关注状态为 Running 的 Pod 以及完成资源预占的 Pod。 |
| waiting-running-succeed | 匹配时关注状态为 Succeed、Running 的 Pod 以及完成资源预占的 Pod。 |
| once-satisfied | 匹配时只关注完成资源预占的 Pod，匹配成功后该 PodGroup 不再生效。 |


## 示例

本文通过运行TensorFlow的分布式作业来展示Gang scheduling的效果。当前测试集群有4个GPU卡。

- 

安装Arena，在Kubernetes集群中部署Tensorflow作业运行环境。具体操作，请参见[安装](products/ack/documents/cloud-native-ai-suite/user-guide/install-arena.md)[Arena](products/ack/documents/cloud-native-ai-suite/user-guide/install-arena.md)。

说明

Arena是基于Kubernetes的机器学习系统开源社区Kubeflow中的子项目之一。Arena用命令行和SDK的形式支持了机器学习任务的主要生命周期管理（包括环境安装、数据准备，到模型开发、模型训练、模型预测等），有效提升了数据科学家工作效率。

- 

使用以下模板向集群中提交Tensorflow分布式作业，含有1个PS和4个Worker，每个Worker类型的Pod需要2个GPU。

展开查看完整示例

apiVersion: "kubeflow.org/v1" kind: "TFJob" metadata: name: "tf-smoke-gpu" spec: tfReplicaSpecs: PS: replicas: 1 template: metadata: creationTimestamp: null labels: pod-group.scheduling.sigs.k8s.io/name: tf-smoke-gpu pod-group.scheduling.sigs.k8s.io/min-available: "5" spec: containers: - args: - python - tf_cnn_benchmarks.py - --batch_size=32 - --model=resnet50 - --variable_update=parameter_server - --flush_stdout=true - --num_gpus=1 - --local_parameter_device=cpu - --device=cpu - --data_format=NHWC image: registry.cn-hangzhou.aliyuncs.com/kubeflow-images-public/tf-benchmarks-cpu:v20171202-bdab599-dirty-284af3 name: tensorflow ports: - containerPort: 2222 name: tfjob-port resources: limits: cpu: '1' workingDir: /opt/tf-benchmarks/scripts/tf_cnn_benchmarks restartPolicy: OnFailure Worker: replicas: 4 template: metadata: creationTimestamp: null labels: pod-group.scheduling.sigs.k8s.io/name: tf-smoke-gpu pod-group.scheduling.sigs.k8s.io/min-available: "5" spec: containers: - args: - python - tf_cnn_benchmarks.py - --batch_size=32 - --model=resnet50 - --variable_update=parameter_server - --flush_stdout=true - --num_gpus=1 - --local_parameter_device=cpu - --device=gpu - --data_format=NHWC image: registry.cn-hangzhou.aliyuncs.com/kubeflow-images-public/tf-benchmarks-gpu:v20171202-bdab599-dirty-284af3 name: tensorflow ports: - containerPort: 2222 name: tfjob-port resources: limits: nvidia.com/gpu: 2 workingDir: /opt/tf-benchmarks/scripts/tf_cnn_benchmarks restartPolicy: OnFailure

- 

不使用Gang scheduling功能

执行以下命令查看Pod状态。

kubectl get pods

系统输出类似以下结果，表示集群中只有2个Worker类型的Pod处于Running状态，剩余2个Worker类型的Pod处于Pending状态。

NAME READY STATUS RESTARTS AGE tf-smoke-gpu-ps-0 1/1 Running 0 6m43s tf-smoke-gpu-worker-0 1/1 Running 0 6m43s tf-smoke-gpu-worker-1 1/1 Running 0 6m43s tf-smoke-gpu-worker-2 0/1 Pending 0 6m43s tf-smoke-gpu-worker-3 0/1 Pending 0 6m43s

执行以下命令查看其中正在运行的Worker类型Pod的日志。

kubectl logs -f tf-smoke-gpu-worker-0

系统输出类似以下结果，表示已启动的两个Worker类型的Pod处于等待剩余两个Worker类型的Pod启动的状态，已启动的两个Worker类型的Pod占用GPU却没有使用。

INFO|2020-05-19T07:02:18|/opt/launcher.py|27| 2020-05-19 07:02:18.199696: I tensorflow/core/distributed_runtime/master.cc:221] CreateSession still waiting for response from worker: /job:worker/replica:0/task:3 INFO|2020-05-19T07:02:28|/opt/launcher.py|27| 2020-05-19 07:02:28.199798: I tensorflow/core/distributed_runtime/master.cc:221] CreateSession still waiting for response from worker: /job:worker/replica:0/task:2

- 

使用Gang scheduling功能

执行以下命令查看Pod状态。

kubectl get pods

系统输出以下结果，表示因为集群的资源无法满足设定的最小数要求，PodGroup无法正常调度，所有的Pod一直处于Pending状态。

NAME READY STATUS RESTARTS AGE tf-smoke-gpu-ps-0 0/1 Pending 0 43s tf-smoke-gpu-worker-0 0/1 Pending 0 43s tf-smoke-gpu-worker-1 0/1 Pending 0 43s tf-smoke-gpu-worker-2 0/1 Pending 0 43s tf-smoke-gpu-worker-3 0/1 Pending 0 43s

当集群中新增4个GPU卡的资源时，当前集群的资源满足设定的最小数要求。此时PodGroup正常调度，4个Worker类型Pod开始运行。执行以下命令查看Pod状态。

kubectl get pods

预期输出：

NAME READY STATUS RESTARTS AGE tf-smoke-gpu-ps-0 1/1 Running 0 3m16s tf-smoke-gpu-worker-0 1/1 Running 0 3m16s tf-smoke-gpu-worker-1 1/1 Running 0 3m16s tf-smoke-gpu-worker-2 1/1 Running 0 3m16s tf-smoke-gpu-worker-3 1/1 Running 0 3m16s

执行以下命令查看其中一个Worker类型Pod的日志。显示训练任务已经开始。

kubectl logs -f tf-smoke-gpu-worker-0

系统输出类似以下结果，表示训练任务已经开始。

INFO|2020-05-19T07:15:24|/opt/launcher.py|27| Running warm up INFO|2020-05-19T07:21:04|/opt/launcher.py|27| Done warm up INFO|2020-05-19T07:21:04|/opt/launcher.py|27| Step Img/sec loss INFO|2020-05-19T07:21:05|/opt/launcher.py|27| 1 images/sec: 31.6 +/- 0.0 (jitter = 0.0) 8.318 INFO|2020-05-19T07:21:15|/opt/launcher.py|27| 10 images/sec: 31.1 +/- 0.4 (jitter = 0.7) 8.343 INFO|2020-05-19T07:21:25|/opt/launcher.py|27| 20 images/sec: 31.5 +/- 0.3 (jitter = 0.7) 8.142

## 错误信息

- 

错误信息："rejected by podgroup xxx"。

- 

原因：当集群中同时存在多个PodGroup调度时，由于调度器存在BackOff队列，可能存在一个PodGroup的所有Pod的调度没有完全聚合在一起的情况。此时已经预占资源的Pod可能会影响后续PodGroup的Pod调度，因此在后续PodGroup的Pod调度时，会拒绝上一个调度的PodGroup中已经预占资源的Pod。这是一种正常现象，通常不会持续很久，若持续时间超过二十分钟，您可以[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)进行排查。

## 相关文档

- 

kube-scheduler发布记录，请参见[kube-scheduler](products/ack/documents/product-overview/kube-scheduler.md)。

- 

通过Kubernetes原生的ResourceQuota方式进行固定资源分配，集群的整体资源利用率不高。阿里云借鉴Yarn Capacity Scheduling的设计思路，基于Scheduling Framework的扩展机制，在调度侧通过引入弹性配额组实现了Capacity Scheduling功能，在确保用户资源分配的基础上通过资源共享的方式来提升集群的整体资源利用率。详细信息，请参见[使用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-capacity-scheduling.md)[Capacity Scheduling](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-capacity-scheduling.md)。

[上一篇：任务调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/task-scheduling.md)[下一篇：使用Capacity Scheduling](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-capacity-scheduling.md)

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
