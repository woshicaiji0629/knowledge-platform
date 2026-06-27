# 集群运维FAQ-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/faq-about-container-security

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-edge/product-overview.md)

- [快速入门](products/ack/documents/ack-edge/quick-start.md)

- [操作指南](products/ack/documents/ack-edge/user-guide.md)

- [实践教程](products/ack/documents/ack-edge/use-cases.md)

- [安全合规](products/ack/documents/ack-edge/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-edge/developer-reference.md)

- [服务支持](products/ack/documents/ack-edge/support.md)

[首页](https://help.aliyun.com/zh)

# 容器安全FAQ

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍应用容器安全的常见问题及解决方案。

- 

[为什么容器之间网络不通？](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)

- 

[如何给](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)[Kubernetes](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)[集群指定安全组？](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)

- 

[集群审计功能是否可以取消或者在创建集群后再部署？](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)

- 

[Kubernetes](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)[专有版本集群如何更换证书有效期，以及如何更换各个组件的证书？](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)

- 

[Pod](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)[无法创建，报错详情：no providers available to validate pod request](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)

- 

[Secret](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)[在新建的](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)[Namespace](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)[下面无法使用](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)

- 

[无法挂载](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)[default-token](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)

- 

[审计日志查询方法](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)

- 

[如何收集](products/ack/documents/ack-edge/user-guide/diagnose-edge-node-problems.md)[ACK Edge](products/ack/documents/ack-edge/user-guide/diagnose-edge-node-problems.md)[集群节点的诊断信息？](products/ack/documents/ack-edge/user-guide/diagnose-edge-node-problems.md)

- 

[CentOS 7.6](https://help.aliyun.com/zh/document_detail/178340.html)[系统的](https://help.aliyun.com/zh/document_detail/178340.html)[Kubernetes](https://help.aliyun.com/zh/document_detail/178340.html)[集群中](https://help.aliyun.com/zh/document_detail/178340.html)[kubelet](https://help.aliyun.com/zh/document_detail/178340.html)[日志含有“Reason:KubeletNotReady Message:PLEG is not healthy:”信息](https://help.aliyun.com/zh/document_detail/178340.html)

## 为什么容器之间的网络不通？

您可以参考以下步骤解决容器服务Kubernetes集群由于安全组导致网络不通的问题。

- 

入方向授权对象为Pod 网络CIDR，且协议类型为全部的规则已被删除。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择集群信息。

- 

在集群信息页面，选择基本信息页签，单击控制面安全组右侧的链接进入ECS控制台的安全组页面。

- 

在安全组页面的入方向页签下，单击增加规则，在编辑安全组规则页面配置规则后，单击确定。

- 

授权策略：允许。

- 

优先级：默认。

- 

协议：选择所有流量。

- 

访问来源：填写为Pod的网段地址。Pod的网段地址（Pod网络CIDR）可在容器服务管理控制台集群详细信息页面的网络区域查看。

入方向访问来源为Pod网络CIDR，且协议为所有流量的规则已添加。

- 

新增ECS实例的安全组与集群所在的安全组不同。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择集群信息。

- 

在集群信息页面，选择基本信息页签，查看并记录安全组右侧的安全组ID。

- 

将目标ECS实例加入上一步查到的集群安全组中。将ECS实例加入指定安全组的相关操作，请参见[将实例加入、移出或更换安全组](products/ecs/documents/user-guide/manage-ecs-instances-in-security-groups.md)。

## 如何给Kubernetes集群指定安全组？

创建集群时指定安全组

创建Kubernetes集群时，容器服务ACK会自动创建一个默认安全组，您可以通过修改默认安全组的规则，达到指定安全组的效果。请参见[配置集群安全组](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-security-group-rules-to-enforce-access-control-on-ack-clusters.md)。

在已创建集群中修改关联的安全组

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择集群信息。

- 

在集群信息页面，选择基本信息页签，然后在网络区域单击控制面安全组后的编辑。

- 

在弹出的对话框中选中要切换的安全组，然后单击确定完成。

## 集群审计功能是否可以取消或者在创建集群后再部署？

可以。具体操作，请参见[使用集群](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/work-with-cluster-auditing.md)[API Server](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/work-with-cluster-auditing.md)[审计功能](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/work-with-cluster-auditing.md)。

## Kubernetes专有版本集群如何更换证书有效期，以及如何更换各个组件的证书？

- 

集群临近过期前两个月左右，您会收到站内和短信通知，收到通知后，在控制台集群列表页面单击证书更新按钮即可。具体操作，请参见[更新](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/renew-expiring-kubernetes-cluster-certificates.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/renew-expiring-kubernetes-cluster-certificates.md)[专有集群即将过期的证书](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/renew-expiring-kubernetes-cluster-certificates.md)。

- 

如果Kubernetes集群证书已过期，具体操作，请参见[更新](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/update-expired-certificates-of-a-kubernetes-cluster.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/update-expired-certificates-of-a-kubernetes-cluster.md)[专有集群已过期的证书](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/update-expired-certificates-of-a-kubernetes-cluster.md)。

## Pod无法创建，报错详情：no providers available to validate pod request

- 

如果您没有自定义PSP，出现该报错是因为您删除了默认的PSP，恢复使用默认的PSP规则即可。具体操作，请参见[【已弃用】使用](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md)[Pod](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md)[安全策略](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md)。

- 

如果您需要自定义PSP，具体操作，请参见[启用安全策略管理](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/configure-and-enforce-ack-pod-security-policies.md)。

## Secret在新建的Namespace下面无法使用

Secret是命名空间级别的，您需要在新建的Namespace下新建Secret。

## 无法挂载default-token

无法挂载default-token，具体报错信息如下：

Normal Scheduled 13m default-scheduler Successfully assigned dev/alibaba-demo-67fcdbfb8-zklnp to cn-hangzhou.10.7.3.16 Warning FailedMount 13m (x2 over 13m) kubelet, cn-hangzhou.10.7.3.16 MountVolume.SetUp failed for volume 'default-token-8twx9' : mount failed: exit status 1 Mounting command: systemd-run Mounting arguments: --description=Kubernetes transient mount for /var/lib/kubelet/pods/62d39b35-9a4d-11ea-9870-c24d56a0e904/volumes/kubernetes.io~secret/default-token-8twx9 --scope -- mount -t tmpfs tmpfs /var/lib/kubelet/pods/62d39b35-9a4d-11ea-9870-c24d56a0e904/volumes/kubernetes.io~secret/default-token-8twx9 Output: Failed to start transient scope unit: Argument list too long Warning FailedCreatePodContainer 3m40s (x49 over 13m) kubelet, cn-hangzhou.10.7.3.16 unable to ensure pod container exists: failed to create container for [kubepods burstable pod62d39b35-9a4d-11ea-9870-c24d56a0e904] : Argument list too long

Systemd版本太老旧。

- 

升级Systemd，具体操作，请参见[systemd](https://github.com/kubernetes/kubernetes/issues/57345#issuecomment-427349235)。

- 

执行sudo systemctl daemon-reload命令重启清零。更多信息，请参见[systemd](https://github.com/kubernetes/kubernetes/issues/57345#issuecomment-356179385)。

## 审计日志查询方法

### RBAC相关变更操作的审计日志查询方法

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择集群信息。

- 

在集群信息页面，选择基本信息页签，单击审计日志右侧的链接。

- 

在日志存储>日志库页面，选择对应的audit-<cluster_id>，单击页面右上角的查询 / 分析。

- 

在页面顶端的下拉列表中，选择需要查询的时间范围，例如最近15分钟。

说明

时间段覆盖的范围是正常到出现问题时的这段时间，例如3天、7天或15天。

- 

在查询 / 分析文本框中，输入以下SQL查询命令，然后单击页面右上角的查询 / 分析。

requestURI: "rbac.authorization.k8s.io" not (verb: get or verb: watch)

- 

单击图标，选择下载日志，在弹出的日志下载对话框，选中通过Cloud Shell下载，单击确认。

### ConfigMap相关变更操作的审计日志查询方法

在查询 / 分析文本框中输入以下SQL查询命令，然后单击查询 / 分析。更多操作，请参见[审计日志查询方法](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)。

requestURI: "configmaps" and <configmap_name> not (verb: get or verb: watch or verb: list)

说明

上述查询命令在查询时，需要将<configmap_name>替换为实际的ConfigMap名称。

### Deployment的Pod扩缩容相关操作的审计日志查询方法

在查询 / 分析文本框中输入以下SQL查询命令，然后单击查询 / 分析。更多操作，请参见[审计日志查询方法](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)。

requestURI: deployments and (verb: update or verb: patch) and replicas and deployments and <deployment_name> not deployment-controller

说明

上述查询命令在查询时，需要将<deployment_name>替换为实际的Deployment名称。

[上一篇：主机安全](products/ack/documents/ack-edge/security-and-compliance/host-security.md)[下一篇：开发参考](products/ack/documents/ack-edge/developer-reference.md)

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
