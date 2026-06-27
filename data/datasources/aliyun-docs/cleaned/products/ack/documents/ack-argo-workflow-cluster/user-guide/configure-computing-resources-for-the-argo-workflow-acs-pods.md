# 配置Argo工作流Pod的计算类型与算力质量-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-argo-workflow-cluster/user-guide/configure-computing-resources-for-the-argo-workflow-acs-pods

# 配置Argo工作流ACS Pod算力
工作流子任务在运行过程中，底层基于阿里云容器计算服务ACS以Serverless的方式运行Pod。实际业务场景可能对Pod算力规格有特殊需求，例如：需要更多的CPU核数和内存、高性能CPU、GPU、更大的临时存储、AMD机型等。本文介绍如何配置工作流子任务ACS Pod的算力规格。
## 配置Pod算力
### 计算类型（Compute Class）
ACS Pod支持下列算力计算类型：
| 计算类型 | 标签 | 适用场景 |
| --- | --- | --- |
| 通用型（默认） | general-purpose | 满足绝大部分无状态微服务应用 、Java Web 应用、计算类任务等。 |
| 性能型 | performance | 满足性能需求更强的业务场景，如 CPU Based AI/ML 训练和推理、HPC 批处理等。 |
| GPU 型 | gpu | 满足 AI/HPC 等异构计算场景，如 GPU 单卡、多卡推理，GPU 并行计算等。 |
| 高性能网络 GPU 型（gpu-hpn) | gpu-hpn | 满足 AI/HPC 等异构计算场景，如 GPU 分布式训练，分布式推理，GPU 高性能计算等。 |
通过使用Pod上的alibabacloud.com/compute-class标签指定实例的计算类型。下方示例分别演示了四种计算类型的配置方法：
关于ACS Pod计算类型的更多说明，请参见[ACS Pod](https://help.aliyun.com/zh/cs/user-guide/acs-pod-instance-overview)[实例概述](https://help.aliyun.com/zh/cs/user-guide/acs-pod-instance-overview)。
## 通用型（默认）
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: helloworld-- spec: entrypoint: helloworld templates: - name: helloworld metadata: labels: alibabacloud.com/acs: "true" # 默认配置可以省略 alibabacloud.com/compute-class: general-purpose # 默认配置可以省略 container: image: mirrors-ssl.aliyuncs.com/busybox:latest resources: # 默认配置可以省略 limits: cpu: 2 memory: "4Gi" requests: cpu: 2 memory: "4Gi" command: - sh - -c args: - echo "Hello, world!"; sleep 30;
## 性能型
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: helloworld-- spec: entrypoint: helloworld templates: - name: helloworld metadata: labels: alibabacloud.com/acs: "true" # 默认配置可以省略 alibabacloud.com/compute-class: performance container: image: mirrors-ssl.aliyuncs.com/busybox:latest resources: # 配置更大的CPU和内存 limits: cpu: 8 memory: "16Gi" requests: cpu: 8 memory: "16Gi" command: - sh - -c args: - echo "Hello, world!"; sleep 30;
## GPU
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: helloworld-- spec: entrypoint: helloworld templates: - name: helloworld metadata: labels: alibabacloud.com/acs: "true" # 默认配置可以省略 # 指定compute-class为gpu类型 alibabacloud.com/compute-class: "gpu" # 指定GPU型号为example-model，请按实际情况填写，如T4 alibabacloud.com/gpu-model-series: "T4" container: image: mirrors-ssl.aliyuncs.com/busybox:latest resources: limits: cpu: 4 memory: "8Gi" nvidia.com/gpu: "1" # 指定GPU数量，资源标签和数量请按实际情况填写 requests: cpu: 4 memory: "8Gi" nvidia.com/gpu: "1" # 指定GPU数量，资源标签和数量请按实际情况填写 command: - sh - -c args: - echo "Hello, world!"; sleep 30;
## 高性能网络GPU型
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: helloworld-- spec: entrypoint: helloworld templates: - name: helloworld metadata: labels: alibabacloud.com/acs: "true" # 默认配置可以省略 # 指定compute-class为gpu-hpn类型 alibabacloud.com/compute-class: "gpu-hpn" container: image: mirrors-ssl.aliyuncs.com/busybox:latest resources: limits: cpu: 4 memory: "8Gi" nvidia.com/gpu: "1" # 指定GPU数量，资源标签和数量请按实际情况填写 requests: cpu: 4 memory: "8Gi" nvidia.com/gpu: "1" # 指定GPU数量，资源标签和数量请按实际情况填写 command: - sh - -c args: - echo "Hello, world!"; sleep 30;如需在ACS使用高性能网络GPU，请先创建[GPU-HPN](https://help.aliyun.com/zh/cs/user-guide/gpu-hpn-capacity-reservation)[容量预留](https://help.aliyun.com/zh/cs/user-guide/gpu-hpn-capacity-reservation)，并在资源关联页面选择Argo工作流集群。
### 算力质量（Compute QoS）
不同的算力质量在资源供给上会有所区别，以适应不同的业务场景，ACS当前提供了2种算力质量：
| 算力质量 | 标签 | 特点 | 典型应用场景 |
| --- | --- | --- | --- |
| 默认型 | default | 有一定的算力扰动。 不存在强制的实例驱逐，实例故障通过热迁移或者通知用户触发驱逐完成。 | 微服务应用 Web 应用 计算类任务 |
| BestEffort 型 | best-effort | 有一定的算力扰动。 存在强制的实例抢占和驱逐，驱逐前 5 分钟会有事件通知。 | 大数据计算 音视频转码 批处理任务 |
通过使用Pod上的alibabacloud.com/compute-qos标签指定实例的算力质量。
BestEffort算力质量实例为动态库存，强烈建议在生产环境配置库存优先调度策略，在库存不足时由平台自动切换至默认型。更多信息，请参见[高级配置参数](https://help.aliyun.com/zh/cs/user-guide/custom-resource-priority-scheduling#095649ebeaybl)。
## 默认型
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: helloworld-- spec: entrypoint: helloworld templates: - name: helloworld metadata: labels: alibabacloud.com/acs: "true" # 默认配置可以省略 alibabacloud.com/compute-qos: default # 默认配置可以省略 container: image: mirrors-ssl.aliyuncs.com/busybox:latest resources: # 默认配置可以省略 limits: cpu: 2 memory: "4Gi" requests: cpu: 2 memory: "4Gi" command: - sh - -c args: - echo "Hello, world!"; sleep 30;
## BestEffort型
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: helloworld-- spec: entrypoint: helloworld templates: - name: helloworld metadata: labels: alibabacloud.com/acs: "true" alibabacloud.com/compute-qos: best-effort container: image: mirrors-ssl.aliyuncs.com/busybox:latest resources: # 配置更大的CPU和内存 limits: cpu: 2 memory: "4Gi" requests: cpu: 2 memory: "4Gi" command: - sh - -c args: - echo "Hello, world!"; sleep 30;
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
