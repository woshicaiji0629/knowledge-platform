# 在ACK Edge集群中部署和管理ack-kserve组件-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/user-guide-for-ack-kserve

# 在ACK Edge集群中部署和管理ack-kserve组件
KServe是一个开源项目，旨在通过YAML文件提供声明式API，简化Kubernetes上机器学习模型的部署和管理。ack-kserve基于开源KServe进行深度优化，并与阿里云生态（如存储、日志、网络等）深度集成，简化了KServe的部署和运维流程。本文介绍如何在ACK集群中部署和管理ack-kserve组件。
## 前提条件
已创建ACK Edge集群，且集群版本为1.22及以上。具体操作，请参见[创建](create-an-ack-edge-cluster-1.md)[ACK Edge](create-an-ack-edge-cluster-1.md)[集群](create-an-ack-edge-cluster-1.md)。
已安装Nginx Ingress Controller组件。具体操作，请参见[如何在](edge-cluster-ingress-overview.md)[ACK Edge](edge-cluster-ingress-overview.md)[集群部署](edge-cluster-ingress-overview.md)[Ingress Controller](edge-cluster-ingress-overview.md)。
## 步骤一： 安装cert-manager组件
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择应用>Helm。
单击左上方创建，在基本信息页面填写应用名，在Chart区域搜索选中cert-manager，然后单击下一步。
在参数配置页面，确认Chart 版本和参数信息后，单击确定。
部署成功后，可以在Helm页面查看cert-manager的Helm组件信息。
## 步骤二：安装ack-kserve组件
ack-kserve组件默认采用RawDeployment模式部署，并与Nginx Ingress Controller组件集成。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择应用>Helm。
单击左上方创建，在基本信息页面填写应用名，在Chart区域搜索选中ack-kserve，然后单击下一步。
在参数配置页面，确认Chart 版本和参数信息后，单击确定。
部署成功后，可以在Helm页面查看ack-kserve的Helm组件信息。
修改kserve中inferenceservice-config配置项。
在Helm页面，单击kserve，然后单击inferenceservice-config，单击YAML 编辑，修改YAML文件中的ingressClassName字段，使其与[安装](edge-cluster-ingress-overview.md)[Nginx Ingress Controller](edge-cluster-ingress-overview.md)时指定的ingressClassResource.name一致。
校验ack-kserve是否运行。
执行以下命令，查看Pod运行状态。
kubectl get pod -n kserve
如果预期输出的STATUS为running状态，表明ack-kserve组件已经安装成功。
## （可选）步骤三：查看或更新ack-kserve️组件
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择应用>Helm。
查看ack-kserve️组件详情。
在Helm页面，单击ack-kserve组件操作列的详情，即可查看组件的基本信息、参数配置及历史版本。
更新ack-kserve️组件信息。
在Helm页面，单击ack-kserve组件操作列的更新，即可更新组件的版本及参数。
## （可选）步骤四：清理资源和卸载组件
为避免资源浪费，请在卸载ack-kserve️组件前删除集群内的KServe CR（Custom Resource ）及CRD（Custom Resource Definition）资源。
重要
删除CR和CRD资源之前，请确认业务不再使用CR和CRD资源。删除CRD资源会同步删除对应的CR资源，CR资源一旦删除将无法恢复。
确认业务不再使用后，再删除集群内所有的KServe CR资源。删除CR资源可能涉及以下命令：
# 查看集群内所有isvc资源。 kubectl get isvc --all-namespaces # 保存集群内所有isvc资源。 kubectl get isvc --all-namespaces -oyaml > isvc.yaml.bak # 确认业务不再使用后删除isvc资源。 kubectl delete isvc --all
删除集群内的KServe CRD资源。
在删除CRD之前，应确保先删除所有依赖于该CRD的CR，否则会导致CRD删除失败。
kubectl delete crd clusterservingruntimes.serving.kserve.io kubectl delete crd clusterstoragecontainers.serving.kserve.io kubectl delete crd inferencegraphs.serving.kserve.io kubectl delete crd inferenceservices.serving.kserve.io kubectl delete crd predictors.serving.kserve.io kubectl delete crd servingruntimes.serving.kserve.io kubectl delete crd trainedmodels.serving.kserve.io
卸载ack-kserve组件。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择应用>Helm。
在Helm页面，单击ack-kserve组件操作列的删除，即可根据页面提示卸载ack-kserve组件。
卸载cert-manager组件。
警告
卸载cert-manager组件前，请先确认集群中没有其他组件使用cert-manager组件，否则会导致业务不可用。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择应用>Helm。
在Helm页面，单击cert-manager组件操作列的删除，即可根据页面提示卸载cert-manager组件。
执行以下命令，删除集群内cert-manager的CRD资源。
kubectl delete crd certificaterequests.cert-manager.io kubectl delete crd certificates.cert-manager.io kubectl delete crd challenges.acme.cert-manager.io kubectl delete crd clusterissuers.cert-manager.io kubectl delete crd issuers.cert-manager.io kubectl delete crd orders.acme.cert-manager.io
## 常见问题及解决方案
常见问题：安装ack-kserve组件时出现报错failed to call webhook: Post "https://cert-manager-webhook.cert-manager.svc:443/validate?timeout=30s": tls: failed to verify certificate: x509: certificate signed by unknown authority。
问题原因：ack-kserve组件强依赖于cert-manager组件，如果当前集群中未安装cert-manager组件或者cert-manager组件未就绪，此时安装ack-kserve组件就会出现上述报错。
解决方案：
执行以下命令，确认集群中是否已经安装cert-manager组件。
kubectl get crd |grep certificates.cert-manager.io
预期输出如下所示，表明集群中已经安装cert-manager组件。
certificates.cert-manager.io 2024-05-06T07:09:17Z
如集群中没有cert-manager的CRD资源，请参见[步骤一](../../cloud-native-ai-suite/user-guide/installing-ack-kserve-components.md)安装cert-manager组件。
执行以下命令，确认cert-manager组件是否已经就绪。
kubectl -n cert-manager get po
预期输出如下所示，表明cert-manager组件的Pod均已就绪。
NAME READY STATUS RESTARTS AGE cert-manager-7f4bb44d5b-jrrfn 1/1 Running 0 23h cert-manager-cainjector-79544456cc-qp5pp 1/1 Running 0 23h cert-manager-webhook-f74ccb647-7m5dt 1/1 Running 0 23h
如果所有Pod均为Ready状态，请参见上文先卸载ack-kserve组件，然后再重新安装即可解决报错。
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
