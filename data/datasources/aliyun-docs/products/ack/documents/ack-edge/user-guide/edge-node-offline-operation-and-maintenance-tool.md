# 对离线边缘节点进行本地运维修改Pod等资源-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/edge-node-offline-operation-and-maintenance-tool

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

# 边缘节点离线运维

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在云边场景下，边缘节点可能会因为网络不稳定而处于离线状态。离线的边缘节点如果设置了节点自治，节点上的业务可以不受影响持续运行，但您无法再通过云端控制面对边缘节点上的业务做运维变更。ACK Edge集群提供了边缘节点离线运维工具，用于支持用户在紧急情况下，对离线节点上的业务进行运维操作，例如业务回滚，资源变配，业务配置修改等。本文为您介绍如何使用边缘节点离线运维工具。

## 前提条件

- 

已创建ACK Edge集群，并且集群版本在1.26及以上。具体操作，请参见[创建](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster-1.md)[ACK Edge](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster-1.md)[集群](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster-1.md)。

- 

ACK Edge集群中已经添加了边缘节点。具体操作，请参见[添加边缘节点](products/ack/documents/ack-edge/user-guide/add-an-edge-node.md)。

## 注意事项

- 

该运维工具只能在边缘节点离线的情况下作为紧急运维方式来使用。

- 

该工具只支持修改Pod、ConfigMap、Secret三类资源。

- 

该工具只能修改本节点上的资源，例如当您修改了ConfigMap的内容，只在本节点生效，其他节点使用了该ConfigMap也不受影响。

- 

该运维工具所做的操作不会同步到云端，当节点状态恢复正常之后，该工具所做的改动会被云端的内容重新覆盖。若您需要修改永久生效，需要在集群云端中重新修改。

## 获取edgeadm运维工具

执行以下命令获取离线运维工具：

export REGION="" INTERCONNECT_MODE="" CLUSTER_VERSION=""; export ARCH=$(uname -m | awk '{print ($1 == "x86_64") ? "amd64" : (($1 == "aarch64") ? "arm64" : "amd64")}') INTERNAL=$( [ "$INTERCONNECT_MODE" = "private" ] && echo "-internal" || echo "" ); wget http://aliacs-k8s-${REGION}.oss-${REGION}${INTERNAL}.aliyuncs.com/public/pkg/run/attach/${CLUSTER_VERSION}/${ARCH}/edgeadm -O edgeadm; chmod u+x edgeadm;

参数说明如下：

- 

- 

| 参数 | 说明 | 示例值 |
| --- | --- | --- |
| CLUSTER_VERSION | ACK Edge 集群 发布的版本和具体版本号，请参见 [版本发布说明](products/ack/documents/ack-edge/user-guide/release-notes-for-kubernetes-versions-supported-by-ack-edge.md) 。 | 1.26.3-aliyun.1 |
| REGION | ACK Edge 集群 支持的地域及其 Region ID，请参见 [开服地域](products/ack/documents/product-overview/supported-regions.md) 。 | cn-hangzhou |
| INTERCONNECT_MODE | 指定节点接入的网络类型。 basic：公网接入。 private：专线接入。 | basic |


## 常见运维操作

在下述场景中，需要替换执行命令中的变量信息。变量信息和获取方式如下表。

| 变量 | 说明 | 获取方式 |
| --- | --- | --- |
| {pod-name} | 替换为要修改的 Pod 的名称。 | 在节点上执行 crictl pods 查看。 |
| {namespace} | 替换为 Pod 所在的 Namespace 名称。 |  |
| {pod-id} | 替换为该 Pod 对应的 ID。 |  |
| {configmap-name} | 替换为要修改的 ConfigMap 名称。 | 在节点上执行 ls /etc/kubernetes/cache/kubelet/configmaps.v1.core/{namespace} 查看。 |
| {secret-name} | 替换要修改的 Secret 的名称。 | 在节点上执行 ls /etc/kubernetes/cache/kubelet/secrets.v1.core/{namespace} 查看。 |


### 场景一：修改Pod模板

- 

在Pod所在的边缘节点上执行如下命令，打开编辑界面。

edgeadm -n {namespace} edit pod {pod-name}

- 

进入编辑模式，修改Pod模板内容，保存并退出。

- 

修改成功后，Pod会自动重启，可以通过如下命令查询Pod配置，验证修改是否生效。

crictl inspectp {pod-id}

### 场景二：修改指定Pod的ConfigMap

- 

在Pod所在的边缘节点上执行如下命令，打开编辑界面。

edgeadm -n {namespace} -p {pod-name} edit configmap {configmap-name}

- 

进入编辑模式，修改ConfigMap模板内容，保存并退出。

- 

修改成功后，指定的Pod会自动重启并使用修改后的ConfigMap。如果节点上还有其他Pod使用该ConfigMap，您可以通过如下命令手动重启Pod使修改生效。

crictl stopp {pod-id}

说明

该命令只会停止Pod，Pod停止后会被kubelet自动重启。

### 场景三：修改指定Pod的Secret

- 

在Pod所在的边缘节点上执行如下命令，打开编辑界面。

edgeadm -n {namespace} -p {pod-name} edit secret {secret-name}

- 

进入编辑模式，修改Secret模板内容，保存并退出。

- 

修改成功后，指定的Pod会自动重启并使用修改后的Secret。如果节点上还有其他Pod使用该Secret，您可以通过如下命令手动重启Pod使修改生效。

crictl stopp {pod-id}

[上一篇：设置边缘节点自治](products/ack/documents/ack-edge/user-guide/configure-node-autonomy.md)[下一篇：诊断边缘节点问题](products/ack/documents/ack-edge/user-guide/diagnose-edge-node-problems.md)

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
