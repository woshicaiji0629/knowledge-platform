# 产品集成的开源组件生态概览-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/product-overview/open-source-projects

# 开源项目
开源项目扩展了Kubernetes集群的功能。本文介绍阿里云容器服务Kubernetes版主要使用的开源项目。
| 项目分类 | 项目名称 | 项目简介 | 项目地址 | 参考文档 |
| --- | --- | --- | --- | --- |
| 核心组件 | Kubernetes Cloud Controller Manager for Alibaba Cloud | 为 Kubernetes 应用创建负载均衡，管理节点路由条目。 | [Cloud-Provider-Alibaba-Cloud](https://github.com/kubernetes/cloud-provider-alibaba-cloud) | [Cloud Controller Manager](cloud-controller-manager.md) |
| 网络 | Terway CNI Network Plugin | Terway 网络插件是阿里云容器服务自研的网络插件，使用原生的弹性网卡分配给 Pod，实现 Pod 网络。 | [Terway](https://github.com/AliyunContainerService/terway) | [使用](../ack-managed-and-ack-dedicated/user-guide/work-with-terway.md) [Terway](../ack-managed-and-ack-dedicated/user-guide/work-with-terway.md) [网络插件](../ack-managed-and-ack-dedicated/user-guide/work-with-terway.md) |
| NGINX Ingress Controller | 作为反向代理服务器，提供 4 层和 7 层负载均衡能力。 | [Ingress-Nginx](https://github.com/AliyunContainerService/ingress-nginx) | [NGINX Ingress Controller](https://github.com/AliyunContainerService/ingress-nginx/blob/master/README.md) |  |
| ExternalDNS | 通过云产品 Private-Zone 提供动态 DNS 能力。 | [External-DNS](https://github.com/kubernetes-sigs/external-dns) | [ExternalDNS](https://github.com/kubernetes-sigs/external-dns/blob/master/README.md) |  |
| 存储 | Alibaba Cloud Kubernetes CSI Plugin | 容器存储接口，实现存储卷生命周期管理。 | [Alibaba-Cloud-CSI-Driver](https://github.com/kubernetes-sigs/alibaba-cloud-csi-driver) | [存储](../ack-managed-and-ack-dedicated/user-guide/csi-overview-1.md) [CSI](../ack-managed-and-ack-dedicated/user-guide/csi-overview-1.md) [概述](../ack-managed-and-ack-dedicated/user-guide/csi-overview-1.md) |
| 阿里云容器服务 Kubernetes Flexvolume 插件 | 提供挂载和卸载 Kubernetes 存储卷能力的组件（早期版）。 | [Flexvolume](https://github.com/AliyunContainerService/flexvolume) | [存储](../flexvolume-overview.md) [Flexvolume](../flexvolume-overview.md) [概述](../flexvolume-overview.md) |  |
| 阿里云盘 Volume Provision Controller | 提供创建和删除 Kubernetes 存储卷能力的组件（早期版）。 | [Alicloud-Storage-Provisioner](https://github.com/AliyunContainerService/alicloud-storage-provisioner) | [阿里云盘](https://github.com/AliyunContainerService/alicloud-storage-provisioner/blob/master/README.md) [Volume Provision Controller](https://github.com/AliyunContainerService/alicloud-storage-provisioner/blob/master/README.md) |  |
| 资源优化 | Node-Resource-Manager | 节点资源管理、上报组件。 | [Node-Resource-Manager](https://github.com/AliyunContainerService/node-resource-manager) | 无 |
| 弹性 | Kubernetes-CronHPA-Controller | Kubernetes 中的容器水平定时伸缩组件。 | [Kubernetes-CronHPA-Controller](https://github.com/AliyunContainerService/kubernetes-cronhpa-controller) | [容器定时伸缩（CronHPA）](../ack-managed-and-ack-dedicated/user-guide/cronhpa.md) |
| Kubernetes Autoscaler | Kubernetes 中的容器节点水平伸缩组件。 | [Autoscaler](https://github.com/kubernetes/autoscaler) | [节点自动伸缩](../ack-managed-and-ack-dedicated/user-guide/auto-scaling-of-nodes.md) |  |
| 安全 | KMS provider plugin for Alibaba Cloud | 基于阿里云 KMS 服务的密钥管理能力，实现 Kubernetes Secret 的落盘加密能力。 | [Ack-KMS-Plugin](https://github.com/AliyunContainerService/ack-kms-plugin) | [使用阿里云](../ack-managed-and-ack-dedicated/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2.md) [KMS](../ack-managed-and-ack-dedicated/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2.md) [进行](../ack-managed-and-ack-dedicated/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2.md) [Secret](../ack-managed-and-ack-dedicated/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2.md) [的落盘加密](../ack-managed-and-ack-dedicated/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2.md) |
| Kube2ram | 以 DaemonSet 的形式实现对 ECS 绑定 RAM 角色的访问代理，实现 Pod 维度的 RAM 角色权限隔离。 | [Kube2ram](https://github.com/AliyunContainerService/kube2ram) | [Kube2ram](https://github.com/AliyunContainerService/kube2ram/blob/master/README.md) |  |
| ACK RAM Authenticator for Kubernetes | 支持基于 RAM 角色扮演的 APIServer 认证方式。 | [ACK-RAM-Authenticator](https://github.com/AliyunContainerService/ack-ram-authenticator) | [使用](https://developer.aliyun.com/article/712178) [RAM Role](https://developer.aliyun.com/article/712178) [对](https://developer.aliyun.com/article/712178) [ACK](https://developer.aliyun.com/article/712178) [容器集群进行身份验证](https://developer.aliyun.com/article/712178) |  |
| ACK Secret Manager | 支持实时导入和同步阿里云 KMS 凭据管家服务中的密钥数据。 | [ACK Secret Manager](https://github.com/AliyunContainerService/ack-secret-manager) | [ACK Secret Manager](https://github.com/AliyunContainerService/ack-secret-manager/blob/master/README.md) |  |
| SGX-Device-Plugin | 在机密计算场景中，专用于 SGX 设备 EPC 加密内存资源扩展的 Kubernetes 设备插件。 | [SGX-Device-Plugin](https://github.com/AliyunContainerService/sgx-device-plugin) | [SGX-Device-Plugin](sgx-device-plugin.md) |  |
| 迁移 | Derrick | 开源 S2I 工具，通过探测的机制，一键生成 Dockerfile 与模板。 | [Derrick](https://github.com/alibaba/DERRICK) | [Derrick](https://github.com/alibaba/derrick/wiki) |
| Velero | Velero 是一个云原生的集群应用备份、恢复和迁移工具。 | [Velero-Plugin](https://github.com/AliyunContainerService/velero-plugin) | [Velero-Plugin](https://github.com/AliyunContainerService/velero-plugin/blob/master/README.md) |  |
| Image Build Specification of Alibaba Cloud Container Service for Kubernetes (ACK) | 快速制作符合 Kubernetes 集群节点要求的自定义镜像的工具。 | [ACK-Image-Builder](https://github.com/AliyunContainerService/ack-image-builder) | [使用自定义镜像创建](../use-a-custom-image-to-create-an-ack-cluster.md) [ACK](../use-a-custom-image-to-create-an-ack-cluster.md) [集群](../use-a-custom-image-to-create-an-ack-cluster.md) |  |
| AI | Arena | Arena 是基于 Kubernetes 的机器学习轻量级解决方案，支持数据准备、模型开发、模型训练、模型预测的完整生命周期。 | [Arena](https://github.com/kubeflow/arena) | [Arena](https://github.com/kubeflow/arena/blob/master/README.md) |
| GPU Sharing Scheduler Extender in Kubernetes | 业界首个 GPU 共享调度器。 | [GPU Share-Scheduler-Extender](https://github.com/AliyunContainerService/gpushare-scheduler-extender) | [GPU Share-Scheduler-Extender](https://github.com/AliyunContainerService/gpushare-scheduler-extender/blob/master/README.md) |  |
| Fluid | Fluid 是一个开源的 Kubernetes 原生的分布式数据集编排和加速引擎。 | [Fluid](https://github.com/fluid-cloudnative/fluid) | [Fluid](https://github.com/fluid-cloudnative/fluid/blob/master/README.md) |  |
| 应用管理 | Kube-eventer | 开源 Kubernetes 事件收集工具，支持 Kafka、MySQL、钉钉、飞书等多种离线链路。 | [Kube-Eventer](https://github.com/AliyunContainerService/kube-eventer) | [事件监控](../ack-managed-and-ack-dedicated/user-guide/event-monitoring.md) |
| Alibaba-Cloud-Metrics-Adapter | Kubernetes 云指标转换组件，提供弹性自定义指标支持。 | [Alibaba-Cloud-Metrics-Adapter](https://github.com/AliyunContainerService/alibaba-cloud-metrics-adapter) | [Alibaba-Cloud-Metrics-Adapter](https://github.com/AliyunContainerService/alibaba-cloud-metrics-adapter/blob/master/README.md) |  |
| OpenKruise | Kubernetes 应用负载自动化，提供了原地升级、Sidecar 管理、高效稳定部署等能力。 | [Kruise](https://github.com/openkruise/kruise) | [What is OpenKruise?](https://openkruise.io/) |  |
| Open Application Model Specification | 开放应用模型，为云原生应用管理提供标准化、关注点分离的规范。 | [Open Application Model](https://github.com/oam-dev/spec) | [Open Application Model Specification](https://github.com/oam-dev/spec/blob/master/README.md) |  |
| KubeVela | 一个简单易用且高度可扩展的应用管理平台与核心引擎。 | [KubeVela](https://github.com/oam-dev/kubevela) | [Quick Start](https://kubevela.io/#/en/quick-start) |  |
| 调度 | Scheduler Plugins | 基于 Scheduling Framework 扩展并且支持 AI、大数据等复杂场景的调度器。 | [Scheduler Plugins](https://github.com/kubernetes-sigs/scheduler-plugins) | [Scheduler Plugins](https://github.com/kubernetes-sigs/scheduler-plugins/blob/master/README.md) |
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
