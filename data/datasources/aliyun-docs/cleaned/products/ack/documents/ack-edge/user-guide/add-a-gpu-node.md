# 添加GPU节点-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/add-a-gpu-node

# 添加GPU节点
ACK Edge集群的边缘节点池支持管理线下GPU资源。本文介绍如何在ACK Edge集群中的边缘节点池中添加GPU节点。
## 前提条件
已[创建](create-an-ack-edge-cluster-1.md)[ACK Edge](create-an-ack-edge-cluster-1.md)[集群](create-an-ack-edge-cluster-1.md)。
在接入节点前，需要先安装好GPU驱动，驱动版本相关信息请参见[ACK](../../ack-managed-and-ack-dedicated/user-guide/ack-supported-nvidia-driver-version-list.md)[支持的](../../ack-managed-and-ack-dedicated/user-guide/ack-supported-nvidia-driver-version-list.md)[NVIDIA](../../ack-managed-and-ack-dedicated/user-guide/ack-supported-nvidia-driver-version-list.md)[驱动版本列表](../../ack-managed-and-ack-dedicated/user-guide/ack-supported-nvidia-driver-version-list.md)。
## 使用限制
请确保您的集群配额充足。如需添加更多节点，请[到配额平台提交申请](https://quotas.console.aliyun.com/products/csk/quotas)扩大配额。关于ACK Edge集群的配额限制，请参见[配额与限制](../../product-overview/limits.md)。
添加GPU节点时会访问部分域名地址，需要节点侧网络安全组放开限制允许访问。具体信息，请参见[节点接入访问域名和](network-configuration-for-public-network-access.md)[IP](network-configuration-for-public-network-access.md)[路由网段配置](network-configuration-for-public-network-access.md)。
## 操作步骤
## 1.26及以上版本集群
ACK Edge集群从1.26版本开始，接入Nvidia GPU时，无需配置gpuVersion参数直接接入，由接入工具自动检查GPU型号并安装相关组件。
添加GPU节点的操作与其他边缘节点操作一致，具体操作，请参见[添加边缘节点](add-an-edge-node.md)。
说明
1.26及以上版本的ACK Edge集群支持全系列NVIDIA官方发布的生产级（Production Grade）GPU显卡，包括Tesla系列、Hopper（H系列）、Ada Lovelace（A系列）以及L系列。
## 1.26以下版本集群
在1.26以下版本ACK Edge集群中添加GPU节点时，需要选择以下支持的GPU型号。如果有其他GPU型号需求，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)处理。
| 系统架构 | GPU 型号 | 边缘 Kubernetes 集群版本 |
| --- | --- | --- |
| AMD64/x86_64 | Nvidia_Tesla_T4 | ≥1.16.9-aliyunedge.1 |
| AMD64/x86_64 | Nvidia_Tesla_P4 | ≥1.16.9-aliyunedge.1 |
| AMD64/x86_64 | Nvidia_Tesla_P100 | ≥1.16.9-aliyunedge.1 |
| AMD64/x86_64 | Nvidia_Tesla_V100 | ≥1.18.8-aliyunedge.1 |
| AMD64/x86_64 | Nvidia_Tesla_A10 | ≥1.20.11-aliyunedge.1 |
| AMD64/x86_64 | Nvidia_L40 | ≥1.26.3-aliyun.1 |
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点池。
在节点池页面，选择目标节点池右侧操作列的> 添加已有节点。
进入添加节点页面，单击手动添加，添加现有实例。
单击下一步进入实例信息页面，您可以在此处填写节点接入配置，具体的配置参数，请参见[参数列表](add-an-edge-node.md)。
{ "gpuVersion": "Nvidia_Tesla_T4", "enableIptables": true, "quiet": true, "manageRuntime": true, "allowedClusterAddons": [ "kube-proxy", "flannel", "coredns" ] }
说明
生成节点接入脚本时，需配置gpuVersion参数。当前支持的GPU版本如下请参见[使用限制](add-a-gpu-node.md)。
该参数配置完成后，接入工具会自动安装nvidia-containerd-runtime，关于nvidia-containerd-runtime更多信息，请参见[nvidia-containerd-runtime](https://developer.nvidia.com/nvidia-container-runtime)。
配置完成后单击下一步，进入添加完成页面，单击复制，到您的边缘节点上粘贴并执行该脚本。
添加节点成功的结果如下所示。
I0410 10:54:25.801554 19419 join-node.go:241] [join-node] Config the kubelet service configuration successfully. I0410 10:54:25.801590 19419 join-node.go:246] [join-node] Adding edge hub static yaml I0410 10:54:25.801662 19419 join-node.go:279] [join-node] Add edge hub static yaml is ok I0410 10:54:25.801666 19419 join-node.go:384] [join-node] Start to joining node to cluster. I0410 10:54:27.338166 19419 join-node.go:393] [join-node] Join node to cluster successfully. I0410 10:54:27.338214 19419 install.go:151] [install-edgehub] Checking edgehub status I0410 10:54:37.357405 19419 install.go:156] [install-edgehub] Edgehub is ok I0410 10:54:37.357421 19419 install.go:86] [install-edgehub] Reconfiguring the kubelet configuration files. I0410 10:54:37.364387 19419 install.go:103] [install-edgehub] Reconfigure the kubelet configuration files successfully. I0410 10:54:37.364400 19419 install.go:104] [install-edgehub] Restarting the kubelet. I0410 10:54:52.626540 19419 install.go:127] [install-edgehub] Restart the kubelet successfully. I0410 10:54:52.626613 19419 postcheck.go:77] [post-check] Checking docker status I0410 10:54:52.629194 19419 postcheck.go:86] [post-check] docker is ok I0410 10:54:52.629208 19419 postcheck.go:92] [post-check] Checking kubelet status I0410 10:54:52.631661 19419 postcheck.go:100] [post-check] Kubelet is ok I0410 10:54:52.631671 19419 postcheck.go:106] [post-check] Checking edgehub status I0410 10:54:52.642345 19419 postcheck.go:113] [post-check] Edgehub is ok I0410 10:54:52.642356 19419 postcheck.go:129] [post-check] Checking addon kube-proxy status. I0410 10:54:52.683227 19419 postcheck.go:133] [post-check] kube-proxy is OK. I0410 10:54:52.683243 19419 postcheck.go:129] [post-check] Checking addon flannel status. I0410 10:54:52.724501 19419 postcheck.go:133] [post-check] flannel is OK. I0410 10:54:52.724518 19419 postcheck.go:129] [post-check] Checking addon coredns status. I0410 10:54:52.764745 19419 postcheck.go:133] [post-check] coredns is OK. I0410 10:54:52.764763 19419 postcheck.go:165] [post-check] Callback to the OpenAPI. I0410 10:54:53.014706 19419 postcheck.go:178] [post-check] Callback to the OpenAPI successfully. I0410 10:54:53.014760 19419 postcheck.go:66] This node joined into the cluster successfully.
## 相关文档
如果您在添加边缘节点时遇到问题，请参见[诊断边缘节点问题](diagnose-edge-node-problems.md)。
如果您需要移除不使用的边缘节点，请参见[移除边缘节点](remove-edge-nodes.md)。
如果您需要实现边缘节点的自主管理，当云边网络断开时，边缘节点上的业务仍然可以持续稳定地运行。具体操作，请参见[设置边缘节点自治](configure-node-autonomy.md)。
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
