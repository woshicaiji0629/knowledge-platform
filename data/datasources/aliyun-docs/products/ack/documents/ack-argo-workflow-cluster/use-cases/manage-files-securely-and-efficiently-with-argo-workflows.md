# 如何使用Argo Workflow安全高效管理文件-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-argo-workflow-cluster/use-cases/manage-files-securely-and-efficiently-with-argo-workflows

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-argo-workflow-cluster/product-overview.md)

- [服务支持](products/ack/documents/ack-argo-workflow-cluster/support.md)

- [实践教程](products/ack/documents/ack-argo-workflow-cluster/use-cases.md)

- [操作指南](products/ack/documents/ack-argo-workflow-cluster/user-guide.md)

[首页](https://help.aliyun.com/zh)

# 如何使用Argo Workflow安全高效管理文件

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

工作流集群是一个全托管的Argo服务，专注于高效安全的文件管理，并提供了一些增强功能。它在批处理、数据处理和持续集成等场景中比标准的Argo Workflows更具优势。本文将介绍工作流集群如何实现高效安全的文件管理。

## 复杂工作流编排的存储难题

[Argo Workflows](https://github.com/argoproj/argo-workflows)是一个开源的云原生工作流引擎，也是CNCF的毕业项目。Argo Workflows可以自动化管理Kubernetes上的复杂工作流程，适用于多种场景，如定时任务、机器学习、ETL和数据分析、模型训练、数据流Pipeline以及CI/CD等。

在使用Argo Workflows进行任务编排时，尤其是在数据量大的场景下，如模型训练、数据处理、生物信息学分析等，如何高效管理和存储Artifacts是非常重要的一环。然而，采用开源方案可能面临以下挑战。

- 

超大文件无法上传：对于超过5 GiB的文件，因客户端上传限制而导致上传失败。

- 

缺乏文件清理机制：随着工作流执行的推进，中间产生的临时文件或已完成任务的输出结果若未及时清理，会导致OSS存储空间的浪费。

- 

Argo Server磁盘占用过高：在使用Argo Server下载文件时，需要先落盘再传输，高磁盘占用不仅影响服务器性能，还可能导致服务中断或数据丢失。

Argo工作流集群作为一款完全遵循社区规范的全托管式Argo Workflows服务，专注于解决大规模、高安全性的文件管理工作挑战。其一系列重要增强功能包括超大文件分片上传、Artifacts垃圾回收（GC）以及Artifacts流式传输。这些特性旨在帮助用户在阿里云环境下实现对OSS文件的高效、安全和精细管理。

Argo工作流集群作为全托管的Argo工作流服务，在Artifacts文件管理上相比于开源方案具有以下优势：

| OSS 文件管理能力 | 分布式工作流 Argo 集群 | 开源 Argo Workflows |
| --- | --- | --- |
| 文件上传 | 支持超大文件分片上传 | 仅支持 < 5 GiB，超大文件暂不支持 |
| 文件回收 | 支持 Artifacts 垃圾回收（GC） | 不支持文件回收 |
| 文件下载 | 支持流式传输 | 需要落盘，过程繁琐 |


## 支持超大文件上传

Argo开源方案不支持超大文件上传，限制了其在数据密集型任务中的应用。为解决这一问题，分布式工作流Argo集群优化了超大文件上传至OSS的逻辑，支持分片和断点续传，显著提升了大文件处理效率和可靠性。优化后的方案还能独立校验每个分片完整性，进一步增强数据完整性和系统容错能力。

### 使用示例

该功能在工作流集群中默认开通，在[配置](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/configure-artifacts.md)[Artifacts](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/configure-artifacts.md)后，提交示例工作流，即可在OSS上获得一个大小为20 GiB的文件testfile.txt，证明超大文件已上传。

apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: artifact- spec: entrypoint: main templates: - name: main metadata: annotations: k8s.aliyun.com/eci-extra-ephemeral-storage: "20Gi" # 自定义设置要增加的临时存储空间大小。 k8s.aliyun.com/eci-use-specs : "ecs.g7.xlarge" container: image: alpine:latest command: - sh - -c args: - | mkdir -p /out dd if=/dev/random of=/out/testfile.txt bs=20M count=1024 # 生成20 GiB的文件。 echo "created files!" outputs: # 触发文件上传到OSS。 artifacts: - name: out path: /out/testfile.txt

## 配置文件清理机制

开源的Argo方案无法实现OSS文件的自动回收，增加了用户的使用和运维成本。Argo Workflows的Artifacts垃圾回收（GC）机制主要用于在工作流结束后清理不再需要的文件，如中间结果、日志等，从而节省存储空间和成本，避免存储资源的无限制地被消耗。

工作流集群优化了OSS上的文件清理方法，用户只需配置简单的回收逻辑，就可以实现以下功能：

- 

自动清理：在工作流完成后，或在管理员手动清理工作流相关资源一定时间后，自动回收上传至OSS的文件。

- 

灵活配置回收：您可以选择只为成功的工作流任务配置回收策略，避免清理失败日志，便于后续追踪定位问题，或者选择只为失败的工作流任务配置回收策略，清除无效的中间产出。

- 

生命周期管理策略：利用OSS提供的生命周期管理策略，您可以设置规则，根据时间、前缀等参数，自动删除旧的Artifacts，或将早期的Artifacts归档至冷存储。这样不仅能够确保数据完整性，也可以有效降低存储成本。

### 使用示例

通过配置Artifacts垃圾回收（GC）策略，可以启用该功能。以下示例中，工作流整体的Artifacts垃圾回收（GC）策略为删除后回收，其中on-completion.txt文件的回收策略为完成时回收。提交该工作流后，可以在OSS上观察到，工作流完成时on-completion.txt文件被回收，删除工作流后on-deletion.txt文件也会被回收。

apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: artifact-gc- spec: entrypoint: main artifactGC: strategy: OnWorkflowDeletion # 全局回收策略，在Workflow被删除时回收Artifact，可被覆盖。 templates: - name: main container: image: mirrors-ssl.aliyuncs.com/argoproj/argosay:v2 command: - sh - -c args: - | echo "hello world" > /tmp/on-completion.txt echo "hello world" > /tmp/on-deletion.txt outputs: # 上传文件到OSS。 artifacts: - name: on-completion path: /tmp/on-completion.txt artifactGC: strategy: OnWorkflowCompletion # 覆盖全局回收策略，在Workflow完成时回收Artifact。 - name: on-deletion path: /tmp/on-deletion.txt

## 支持流式传输机制

使用开源方案时，Argo Server在下载文件时需要先写入磁盘再传输，这可能导致较高的磁盘占用率，从而影响服务器性能，甚至可能导致服务中断或数据丢失。

工作流集群实现了OSS的OpenStream接口，当您在Argo Workflows UI界面下载文件时，Argo Server可以直接将OSS服务端的文件流式传输给用户，并非将文件完整下载到服务器本地再提供给用户。这种流式传输机制特别适合处理大规模数据传输和存储的工作流任务，具有以下优势。

- 

提升下载性能：通过流式传输文件直接从OSS服务端传输，无需等待整个文件下载到Argo Server，从而减少下载开始的延迟，提升响应速度，提供更流畅的体验。

- 

减少资源占用以增强并发能力：流式处理降低了Argo Server对内存和磁盘的需求，使其能在相同硬件资源下处理更多的并行文件传输请求，提高了系统的并发处理能力。随着使用者数量增加或文件大小增大，直接通过流式传输可以更好地扩展服务来处理这种增长，不必担心Argo Server的磁盘空间限制。

- 

提升安全合规性：避免了数据在Argo Server空间中的临时存储，减小了安全风险和数据泄露的可能性，更有效地遵循数据保护和合规性要求。

通过流式传输Artifacts文件，Argo Server能够减轻单点压力，同时提升UI文件下载的性能，从而有效转型为轻量级的数据流转中心，而非存储和计算的重负载中心。

## 联系我们

如果您对于容器Argo工作流集群有任何疑问，欢迎使用钉钉搜索钉钉群号35688562加入钉钉群。

[上一篇：使用Argo Workflow编排动态DAG Fan-out/Fan-in任务](products/ack/documents/ack-argo-workflow-cluster/use-cases/use-argo-workflows-to-orchestrate-dynamic-dag-fan-out-fan-in-tasks.md)[下一篇：使用Python SDK构建大规模Argo Workflows](products/ack/documents/ack-argo-workflow-cluster/use-cases/use-pythonsdk-to-build-large-scale-argo-workflows.md)

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
