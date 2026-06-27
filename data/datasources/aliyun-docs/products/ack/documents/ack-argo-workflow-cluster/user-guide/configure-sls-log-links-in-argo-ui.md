# 通过配置workflow-controller-configmap，Argo UI可嵌入指向内部系统（如日志服务）的自定义链接，提升工作流和Pod的可观测性。-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-argo-workflow-cluster/user-guide/configure-sls-log-links-in-argo-ui

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

# 在Argo UI配置日志链接

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Argo UI支持在工作流（Workflow）和每个工作流Pod的用户界面（UI）中嵌入指向日志服务SLS的链接，以实现日志的快速访问。

## 适用范围

- 

已开通[日志服务](products/sls/documents/what-is-log-service.md)。

- 

已[开启](products/ack/documents/ack-argo-workflow-cluster/user-guide/enable-argo-server-for-a-workflow-cluster.md)[Argo Server](products/ack/documents/ack-argo-workflow-cluster/user-guide/enable-argo-server-for-a-workflow-cluster.md)[并访问工作流控制台](products/ack/documents/ack-argo-workflow-cluster/user-guide/enable-argo-server-for-a-workflow-cluster.md)。

## 操作步骤

- 

登录[容器](https://csnew.console.aliyun.com/#/next/argowf)[Argo](https://csnew.console.aliyun.com/#/next/argowf)[工作流集群控制台](https://csnew.console.aliyun.com/#/next/argowf)，单击目标集群名称。

- 

在左侧导航栏选择配置管理，单击workflow controller配置（YAML）。

- 

替换下方模板中的clusterid为集群ID，region为集群所在地域（例如：cn-hangzhou），然后在编辑workflow controller配置页面，填入YAML文件中data部分：

- 

NAMESPACE: 当前工作流 / Pod / 事件源（Event Source） / 传感器（Sensor）所在的 Kubernetes 命名空间。

- 

NAME: 当前工作流 / Pod / 事件源 / 传感器的名称。

- 

${status.startedAt}: 工作流 / Pod 的开始时间戳，格式为2021-01-01T10:35:56Z。

- 

${status.finishedAt}: 工作流 / Pod 的结束时间戳，格式为2021-01-01T10:35:56Z。

如果工作流或 Pod 仍在运行，该变量的值将为null。

links:| # Adds a button to the workflow page. E.g. linking to you logging facility. - name: Workflow Logs scope: workflow url: https://sls.console.aliyun.com/lognext/project/k8s-log-{clusterid}/logsearch/workflow-controller-{clusterid}?slsRegion={region}&queryTimeType=3&queryString=NAME# Adds a button next to the pod. E.g. linking to you logging facility but for the pod only. - name: Pod Logs scope: pod url: https://sls.console.aliyun.com/lognext/project/k8s-log-{clusterid}/logsearch/workflow-logstore?slsRegion={region}&queryTimeType=3&queryString=_pod_name_=NAMEand _namespace_=NAMESPACE

- 

在工作流集群中重启Argo Server，使配置生效。

kubectl rollout restart deployment/argo-server -n {clusterid}

- 

登录Argo UI查看，UI中已添加日志服务链接。

[上一篇：使用日志服务](products/ack/documents/ack-argo-workflow-cluster/user-guide/configure-log-service.md)下一篇：无

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
