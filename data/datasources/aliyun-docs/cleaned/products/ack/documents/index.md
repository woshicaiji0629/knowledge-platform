# 企业级容器化应用生命周期管理-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/

# 容器服务 Kubernetes 版 ACK
容器服务 Kubernetes 版（Container Service for Kubernetes，简称容器服务 ACK）提供高性能可伸缩的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理。
[功能发布](https://help.aliyun.com/document_detail/98310.html)[免费试用](https://free.aliyun.com/?spm=5176.7946893.J_5253785160.5.42073dafM4T6qr&pipCode=csk)[常见问题](https://help.aliyun.com/knowledge_detail/148453.html)[管理控制台](https://cs.console.aliyun.com/)[相关技术圈](https://developer.aliyun.com/group/kubernetes/)
## 文档导航
### [ACK托管与专有集群](ack-managed-and-ack-dedicated.md)
[通过Kubernetes一致性认证，提供高性能容器应用管理服务，支持企业级容器化应用的生命周期管理和云端容器化应用运行。](ack-managed-and-ack-dedicated.md)
### [ACK Edge集群](ack-edge.md)
[针对边缘计算场景的云边一体化协同托管方案，提供云端标准、安全、高可用的集群，整合阿里云存储、网络等能力。](ack-edge.md)
### [ACK灵骏集群](ack-lingjun-managed-clusters.md)
[针对智能计算灵骏场景，提供全托管、高可用控制面板的标准Kubernetes集群服务，以灵骏计算节点作为集群工作节点。](ack-lingjun-managed-clusters.md)
### [云原生AI套件](cloud-native-ai-suite.md)
[云原生AI技术和产品方案，支持在Kubernetes容器平台上快速定制化构建AI生产系统，并为AI/ML应用和系统提供全栈优化。](cloud-native-ai-suite.md)
### [分布式云容器平台ACK One](distributed-cloud-container-platform-for-kubernetes.md)
[面向混合云、多集群、分布式计算、容灾等场景推出的企业级云原生平台，支持对计算、网络、存储等统一运维管控。](distributed-cloud-container-platform-for-kubernetes.md)
### [容器Argo工作流集群](ack-argo-workflow-cluster/product-overview.md)
[采用Serverless无服务器模式，使用阿里云容器计算服务ACS运行工作流，通过优化开源工作流引擎性能及Kubernetes集群参数，实现大规模工作流的高效弹性调度。](ack-argo-workflow-cluster/product-overview.md)
### [ACK Serverless集群](serverless-kubernetes.md)
[无服务器Kubernetes容器服务，提供完善的Kubernetes兼容能力，降低Kubernetes使用门槛，让您更专注于应用程序，而非底层基础设施管理。](serverless-kubernetes.md)
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
