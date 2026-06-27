# 如何移除边缘节点-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/remove-edge-nodes

# 移除边缘节点
您需要从容器服务管理控制台的节点池页面进行标准化操作，移除ACK Edge集群不需要的节点，以免带来不符合预期的效果。本文介绍如何移除边缘节点。
## 前提条件
[已创建边缘托管版集群](create-an-ack-edge-cluster-1.md)
[已通过](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[连接](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[Kubernetes](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[集群](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)
## 注意事项
移除节点涉及Pod迁移，可能会影响业务，请在业务低峰期操作，并提前做好数据备份。
操作过程中，后台会把当前节点设置为不可调度状态。
移除节点仅移除Worker节点，不会移除Master节点。
ACK Edge集群存在云端节点和边缘节点两种类型的节点，这两种类型的节点可同时移除。
ACK Edge集群需至少保留一个云端节点。
请通过控制台进行操作。如果通过执行kubectl delete node命令行方式手动移除云端节点，需注意以下问题。
移除后的节点无法再添加到其他集群。
删除集群时，该节点所在的ECS实例会被释放。
## 操作步骤
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点池。
云端节点池和边缘节点池移除节点的方法不同。
## 边缘节点池
在节点池页面，单击目标边缘节点池名称。
在基本信息页签最下方，选中目标节点，单击移除节点。
在移除节点面板，仔细阅读注意事项之后，选中我已了解上述说明，确认移除节点。然后单击确定。
边缘型节点池不支持同时释放ECS和自动排空节点。
移除边缘节点之后，为确保边缘节点上的K8s组件被清理。您需要在边缘节点上，使用边缘节点接入工具Edgeadm的Reset子命令重置节点，命令如下。
wget http://aliacs-k8s-[region].oss-[region].aliyuncs.com/public/pkg/run/attach/[clusterVersion]/[arch]/edgeadm -O edgeadm; chmod u+x edgeadm; ./edgeadm reset
| 参数 | 说明 | 示例 |
| --- | --- | --- |
| region | 集群地域。 | cn-hangzhou |
| clusterVersion | 集群版本。 | 1.22.15-aliyunedge.1 |
| arch | 边缘节点的 CPU 架构。 | amd64 |
## 云端节点池
在节点池页面，单击目标云端节点池名称。
在节点管理页签中，选中目标节点，并单击页面下方的批量移除。
选择是否需要自动排空节点（drain）和同时释放 ECS，仔细阅读页面注意事项后按照页面提示完成操作。
关于自动排空节点（drain）和同时释放 ECS的注意事项，请参见上文的[功能说明](../../ack-managed-and-ack-dedicated/user-guide/remove-a-node-11.md)。
## 相关文档
[添加边缘节点](add-an-edge-node.md)
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
