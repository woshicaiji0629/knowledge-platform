# 排查并解决边缘节点接入与升级失败-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/diagnose-edge-node-problems

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

# 诊断边缘节点问题

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在管理边缘节点过程中，可能会遇到一些问题，包括接入失败和升级失败的问题。本文介绍边缘节点会遇到的常见问题和对应的解决方案。

## 如何处理边缘节点接入失败的问题？

当脚本执行时出现问题，请参考以下常见问题列表进行处理。若出现以下表格中不存在的问题，请收集节点诊断信息后，[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)排查处理。关于如何收集边缘节点诊断信息，请参见[如何收集](products/ack/documents/ack-edge/user-guide/diagnose-edge-node-problems.md)[ACK Edge](products/ack/documents/ack-edge/user-guide/diagnose-edge-node-problems.md)[集群节点的诊断信息？](products/ack/documents/ack-edge/user-guide/diagnose-edge-node-problems.md)

- 

- 

- 

- 

- 

- 

- 

- 

| 接入失败信息 | 失败原因 | 处理建议 |
| --- | --- | --- |
| The os XXX unsupport | 当前边缘节点的系统版本不支持。 | 关于支持的边缘节点的系统列表，请参见 [添加边缘节点](products/ack/documents/ack-edge/user-guide/add-an-edge-node.md) 。 |
| invalid nodeName | 节点名称不合法。 | 节点名称只能由英文小写字母、中划线（-）和半角句号（.）组成。 节点名称不能超过 253 个字符。 节点名称不能以 localhost 开头。 |
| Node route overlaps with service cidr | 节点的路由表网段与集群创建时配置的 Pod CIDR 或 Service CIDR 冲突。 | 重新创建集群，请注意配置 Pod CIDR 与 Service CIDR，需避免与边缘节点的 NameServer 地址以及路由表网段冲突。 |
| response error msg: TOKEN_EXPIRED | 接入 Token 过期。 | 重新生成节点接入脚本。 检查节点系统时间是否正常。 |
| A node named XXX is already exist in the cluster | 集群中已存在同名的节点。 | 下线集群中的同名节点。 |
| error run phase join-node: failed to get cluster info: failed to get cluster-info configmap, Get "https://xx.xxx.xx.xx:6443/api/v1/namespaces/kube-public/configmaps/cluster-info": dial tcp xx.xxx.xx.xx:6443: i/o timeout | 获取集群 cluster-info 失败。 | edgeadm 接入边缘节点时需要通过该地址访问 APIServer， 请检查 API Server 负载均衡（SLB）ACL 规则是否限制了该地址的访问。 |
| error run phase join-node: Install edge-hub failed: Copy file /tmp/edge-hub to /usr/bin/edge-hub fail: open /usr/bin/edge-hub: text file busy | 40009 | 40009 | 安装 edge-hub 失败，节点上已经存在 edge-hub 的二进制文件。 | 执行 edgeadm reset 命令清理节点后重新接入。 |
| error run phase post-check: timed out waiting for the condition | 系统组件启动失败。 | 请重新下载 edgeadm 工具，并执行 edgeadm reset 后重新接入，确保您使用的是最新版本的 edgeadm。 检查边缘节点是否能正常访问依赖的公网地址。相关地址列表请参见 [边缘节点访问域名和](products/ack/documents/ack-edge/user-guide/network-configuration-for-public-network-access.md) [IP](products/ack/documents/ack-edge/user-guide/network-configuration-for-public-network-access.md) [路由网段配置](products/ack/documents/ack-edge/user-guide/network-configuration-for-public-network-access.md) 。 收集边缘节点诊断信息，并 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 排查，关于如何收集诊断信息，请参见 [如何收集](products/ack/documents/ack-edge/user-guide/diagnose-edge-node-problems.md) [ACK Edge](products/ack/documents/ack-edge/user-guide/diagnose-edge-node-problems.md) [集群节点的诊断信息？](products/ack/documents/ack-edge/user-guide/diagnose-edge-node-problems.md) |


## 如何处理边缘节点升级失败的问题？

[升级边缘节点池](products/ack/documents/ack-edge/user-guide/upgrade-ack-edge-cluster.md)时，若未返回升级成功结果This node has been upgraded successfully，请参考以下内容排查处理。

- 

- 

- 

- 

- 

- 

| 升级失败信息 | 可能原因 | 处理建议 |
| --- | --- | --- |
| edgeadm version xxxx does not match cluster version | 升级工具版本与集群版本不匹配。 | 检查集群控制面是否已经完成升级。 检查 TARGET_CLUSTER_VERSION 参数是否填写正确。 |
| node has already been upgraded to xxx | 节点已经是升级后的目标版本。 | 如果确认节点上还有组件没有完成升级，请保留日志并 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 处理。 |
| kubelet target version xxxx does not match cluster version xxxx | 指定的 kubelet 升级的版本与集群控制面版本不匹配。 | 如果指定了 kubelet-version 参数，请检查该参数是否填写正确（与集群控制面版本一致）。 如果没有指定该参数，请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 处理。 |
| Parameter currentVersion cann't null | 使用了老版本的 edgeadm。 | 请检查 edgeadm 版本是否为最新版本。 当前支持的集群升级范围为 1.18 升级到 1.20 版本、1.20 升级到 1.22 版本。 |
| upgrade kubelet failed at phase install, recover to previous state. error run phase upgrade: xxxx | 升级失败，且已自动回滚到之前的状态，节点状态不受影响。 | 请保留日志并 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 处理。 |
| upgrade kubelet failed at phase install, recover to previous state recover kubelet failed, err: xxx error run phase upgrade: xxxx | 升级失败，且自动回滚失败，节点状态会受到影响。 | 请保留日志并 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 处理。 |


## 如何收集ACK Edge集群节点的诊断信息？

当ACK Edge集群的节点出现异常时，您可以参见以下步骤收集集群节点的诊断信息，以供数据分析使用。

- 

登录到ACK Edge集群的异常节点。

- 

执行如下命令，下载诊断脚本。

curl -o /usr/local/bin/diagnose_edge_node.sh https://aliacs-k8s-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/public/diagnose/diagnose_k8s.sh

- 

执行如下命令，给诊断脚本添加执行权限。

chmod u+x /usr/local/bin/diagnose_edge_node.sh

- 

执行如下命令，进入指定目录。

cd /usr/local/bin/

- 

执行如下命令，运行诊断脚本。

./diagnose_edge_node.sh

预期输出如下。每次执行诊断脚本产生的诊断信息文件名称不同，本示例以diagnose_1578310147.tar.gz为例，具体以实际环境为准。

...... + echo 'please get diagnose_1578310147.tar.gz for diagnostics' please get diagnose_1578310147.tar.gz for diagnostics + echo '请提交 diagnose_1578310147.tar.gz 给技术支持' 请提交 diagnose_1578310147.tar.gz 给技术支持

- 

执行ll命令，确认存在diagnose_1578310147.tar.gz诊断信息文件。

[上一篇：边缘节点离线运维](products/ack/documents/ack-edge/user-guide/edge-node-offline-operation-and-maintenance-tool.md)[下一篇：虚拟节点管理](products/ack/documents/ack-edge/user-guide/virtual-node-management.md)

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
