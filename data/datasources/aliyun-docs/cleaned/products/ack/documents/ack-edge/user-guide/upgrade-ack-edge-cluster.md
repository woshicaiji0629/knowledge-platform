# ACK Edge集群升级方法与操作步骤-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/upgrade-ack-edge-cluster

# 升级ACK Edge集群
为避免过期版本集群潜在的安全性和稳定性风险，同时享有新集群版本的新功能，建议您随ACK Edge集群的版本发布节奏及时升级集群。ACK Edge集群采用原地升级方式进行升级，本文为您介绍ACK Edge集群升级的注意事项、升级流程和操作。
## 为什么需要升级集群版本
降低安全和稳定性风险：新版本修复发现的安全和稳定性漏洞，长期使用过期版本集群会给业务带来安全和稳定性风险。
享受更好的维护支持：对于过期版本，ACK Edge集群不再提供安全补丁和问题修复，也无法保证过期版本的技术支持质量。使用新版本能够让您享受更好的技术支持和答疑服务。
使用新版本的新功能：ACK Edge集群发布的新版本包含新的功能和改进，为您带来更好的开发和运维体验。
## 注意事项
ACK Edge集群支持的升级范围为1.18到1.24版本，且只能按照支持的版本依次升级，不支持跨版本升级，不支持回退。
例如，从1.18版本升级到1.22版本，需要进行两次升级操作，先从1.18升级到1.20版本，再从1.20升级到1.22版本。
说明
目前已支持从集群版本1.26开始的升级。若您升级范围为1.26到1.30版本，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)开通白名单。
边缘节点池和控制面最多只能相差两个次要版本，例如控制面为1.22版本，边缘节点池最低是1.20版本，否则会导致集群异常。
## 升级流程、方式及所需时间
### 升级流程
升级前准备
登录[容器服务管理控制台](https://cs.console.aliyun.com/)，进入集群列表页面，在集群列表的版本列查看当前ACK Edge集群的版本并确认升级版本。
仔细阅读ACK Edge集群发布的版本及各版本的功能特性，请参见[版本发布说明](release-notes-for-kubernetes-versions-supported-by-ack-edge.md)。
集群升级中
控制面和云端节点池升级前，均需通过前置检查，等待所有检查项均已通过或修复完成后，可进入后续的升级操作。
[控制面升级](upgrade-ack-edge-cluster.md)：采用滚动升级的方式。升级控制面组件，包括kube-apiserver、kube-controller-manager、kube-scheduler。
[云端节点池升级](node-pool-updates.md)：云端节点池升级包括kubelet和容器运行时的升级。按照分批策略执行分批升级。
根据节点池依次执行，同一时间只对一个节点池执行升级。
同一个节点池内采用分批升级。第一批升级的节点数为1，后续的批次以2的幂数进行增长。如果暂停后重新恢复升级，依然遵循该分批策略。您可以在节点池升级页面配置每批升级节点的最大数量，推荐设置为10。
[边缘节点池升级](upgrade-ack-edge-cluster.md)：需要您手动执行命令，将待升级边缘节点池下的所有节点依次进行升级。
升级所需时间
ACK Edge集群控制面升级时间约为5分钟。
云端节点池升级时内部节点分批升级，每批升级时间约为5分钟。
边缘节点池需要由您手动执行命令完成升级操作，操作时间和节点池下的节点数量有关。
集群升级后
核验集群版本信息，检查节点池运行是否正常，并检查集群业务运行是否正常。
## 操作步骤
### 步骤一：升级控制面
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择运维管理>集群升级。
在集群升级页面选择可升级的目标版本，然后单击前置检查，提前扫描集群升级可能存在的潜在风险。
检查完成后，您可以在前置检查结果区域查看检查结果。
结果正常时，升级检查成功，请继续进行集群升级操作。
结果提示异常时，不影响当前集群的运行及集群状态。您可以参见推荐的解决方案进行修复。关于典型修复方案，请参见[集群检查项及修复方案](../../ack-managed-and-ack-dedicated/user-guide/cluster-check-items-and-suggestions-on-how-to-fix-cluster-issues.md)。
说明
Kubernetes 1.20及以后版本的集群升级前检查时，会检查当前版本是否使用了废弃API，检查结果不会影响升级流程，仅作为提示信息。详细内容，请参见[废弃](../../ack-managed-and-ack-dedicated/user-guide/cluster-check-items-and-suggestions-on-how-to-fix-cluster-issues.md)[API](../../ack-managed-and-ack-dedicated/user-guide/cluster-check-items-and-suggestions-on-how-to-fix-cluster-issues.md)[说明](../../ack-managed-and-ack-dedicated/user-guide/cluster-check-items-and-suggestions-on-how-to-fix-cluster-issues.md)。
前置检查通过后，单击立即升级，按照页面提示进行控制面的升级。
升级过程中，您可以在页面右上角查看升级历史。
升级完成后，请在集群列表查看集群版本，确认升级是否成功。新扩容节点的版本也将遵循控制面版本。
### 步骤二：升级云端节点池
控制面升级完成后，请尽快在业务低峰期完成云端节点池的升级。云端节点池升级包括节点kubelet和容器运行时的升级。功能介绍、相关注意事项及操作步骤，请参见[云端节点池升级](node-pool-updates.md)。
### 步骤三：升级边缘节点池
重要
升级边缘节点池之前必须保证控制面已升级完成。
边缘集群节点池下的所有边缘节点都升级成功，边缘节点池才算升级完成。
## 含Docker运行时迁移的升级
升级ACK Edge集群至1.24版本，若其中包含使用Docker运行时的节点时，您需要将容器运行时从Docker迁移到containerd，因为1.24版本的Kubernetes已经不支持Docker运行时。您可以通过以下任一方式完成升级操作。
（推荐）新建containerd节点池轮转迁移：新建一个节点池，运行时选择containerd，扩容节点。通过设置老节点池禁止调度或者更新应用负载指定节点池调度的方式（例如Label），逐步将应用全部迁移至新的节点池，再将旧节点池进行下线处理。关于如何创建节点池，请参见[边缘节点池管理](edge-node-pool-management.md)；关于如何将节点设置为不可调度，请参见[节点排水和调度状态](../../ack-managed-and-ack-dedicated/user-guide/overview-of-node-management.md)。
原地升级：直接将节点上的运行时从containerd切换到Docker，在升级前也要进行节点排水，另外升级会导致节点上所有容器重启。
节点排水。
在待升级边缘节点池下的所有边缘节点上，依次执行如下命令，完成所有边缘节点的升级。
export REGION="" INTERCONNECT_MODE="" TARGET_CLUSTER_VERSION=""; export ARCH=$(uname -m | awk '{print ($1 == "x86_64") ? "amd64" : (($1 == "aarch64") ? "arm64" : "amd64")}') INTERNAL=$( [ "$INTERCONNECT_MODE" = "private" ] && echo "-internal" || echo "" ); wget http://aliacs-k8s-${REGION}.oss-${REGION}${INTERNAL}.aliyuncs.com/public/pkg/run/attach/${TARGET_CLUSTER_VERSION}/${ARCH}/edgeadm -O edgeadm; chmod u+x edgeadm;./edgeadm upgrade --interconnect-mode=${INTERCONNECT_MODE} --region=${REGION}
参数说明如下：
| 参数 | 说明 | 示例值 |
| --- | --- | --- |
| TARGET_CLUSTER_VERSION | 指定要升级到的目标集群版本。 说明 升级的目标集群版本就是控制面升级完成后的版本。 | 1.24.6-aliyunedge.1 ACK Edge 集群 发布的版本和具体版本号，请参见 [版本发布说明](release-notes-for-kubernetes-versions-supported-by-ack-edge.md) 。 |
| REGION | 指定集群所在地域的 Region ID。 | cn-hangzhou ACK Edge 集群 支持的地域及其 Region ID，请参见 [开服地域](../../product-overview/supported-regions.md) 。 |
| INTERCONNECT_MODE | 指定节点接入的网络类型。 basic：公网接入。 private：专线接入。 | basic |
返回如下执行结果，则说明当前边缘节点升级成功。
## 不含Docker运行时迁移的升级
在待升级边缘节点池下的所有边缘节点上，依次执行如下命令，完成所有边缘节点的升级。
export REGION="" INTERCONNECT_MODE="" TARGET_CLUSTER_VERSION=""; export ARCH=$(uname -m | awk '{print ($1 == "x86_64") ? "amd64" : (($1 == "aarch64") ? "arm64" : "amd64")}') INTERNAL=$( [ "$INTERCONNECT_MODE" = "private" ] && echo "-internal" || echo "" ); wget http://aliacs-k8s-${REGION}.oss-${REGION}${INTERNAL}.aliyuncs.com/public/pkg/run/attach/${TARGET_CLUSTER_VERSION}/${ARCH}/edgeadm -O edgeadm; chmod u+x edgeadm;./edgeadm upgrade --interconnect-mode=${INTERCONNECT_MODE} --region=${REGION}
参数说明如下：
| 参数 | 说明 | 示例值 |
| --- | --- | --- |
| TARGET_CLUSTER_VERSION | 指定要升级到的目标集群版本。 说明 升级的目标集群版本就是控制面升级完成后的版本。 | 1.24.6-aliyunedge.1 ACK Edge 集群 发布的版本和具体版本号，请参见 [版本发布说明](release-notes-for-kubernetes-versions-supported-by-ack-edge.md) 。 |
| REGION | 指定集群所在地域的 Region ID。 | cn-hangzhou ACK Edge 集群 支持的地域及其 Region ID，请参见 [开服地域](../../product-overview/supported-regions.md) 。 |
| INTERCONNECT_MODE | 指定节点接入的网络类型。 basic：公网接入。 private：专线接入。 | basic |
返回如下执行结果，则说明当前边缘节点升级成功。
## 升级常见问题
### 若一直不升级，后台是否会强制完成自动升级？
不会，ACK Edge集群目前只支持手动升级，若您一直不升级，将一直使用旧版本。建议您及时升级以获得更完整的功能特性和技术支持。
### 边缘节点升级失败如何处理？
升级边缘节点池时，若未返回升级成功结果This node has been upgraded successfully，请参见[如何处理边缘节点升级失败的问题？](diagnose-edge-node-problems.md)排查原因。
## 相关文档
在执行升级前置检查时，若检查结果异常，可参考[集群检查项及修复方案](../../ack-managed-and-ack-dedicated/user-guide/cluster-check-items-and-suggestions-on-how-to-fix-cluster-issues.md)排查异常原因。
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
