# 在Workbench或CloudShell上使用kubectl连接集群-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/use-kubectl-on-cloud-shell-to-manage-ack-clusters-1690962464408

# 在Workbench或CloudShell上使用kubectl连接集群
阿里云提供浏览器命令行工具Workbench和CloudShell用于连接集群和管理集群资源，无需额外安装软件。登录阿里云控制台后，您可以在任何浏览器内使用Workbench或CloudShell，ACK会在工具启动时根据当前用户信息自动加载集群的KubeConfig文件。
[Workbench](../../../../ecs/documents/user-guide/workbench-overview.md)：阿里云提供的ECS实例远程连接工具，无需额外安装软件。支持通过公网和内网连接集群。
[CloudShell](https://help.aliyun.com/zh/cloud-shell/what-is-the-cloud-command-line)：阿里云提供的Shell工具，相当于自动创建的一台Linux虚拟机，其中预装了多种语言及命令行工具。仅通过公网连接集群。
公网连接时，需要为集群API Server绑定阿里云EIP，实现集群的公网访问，请参见[实现从公网访问](control-public-access-to-the-api-server-of-a-cluster.md)[API Server](control-public-access-to-the-api-server-of-a-cluster.md)。
CloudShell创建的虚拟机使用期限为1小时，到期后会立即销毁。无交互式操作30分钟或关闭所有会话窗口，虚拟机将在15分钟后销毁。再次启动时，系统会重新创建新虚拟机。
## 准备工作
RAM用户连接集群前，除容器服务的系统权限外，还需要被授予集群操作的权限，请参见[授权](authorization-overview.md)。
RAM用户使用CloudShell前需要被授予AliyunCloudShellFullAccess权限，如需创建并绑定NAS文件系统，还需被授予AliyunNASFullAccess权限，请参见[为](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
## 操作步骤
根据集群的公网连接情况，集群信息页面右上角将展示通过Workbench或CloudShell连接集群。您可按页面提示进行选择。
## Workbench
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择集群信息。
在集群信息页面，单击右上方的通过 Workbench 管理集群。
在终端界面，执行kubectl命令以验证集群的连通性。
此命令以查询命名空间为例。
kubectl get namespace
预期输出：
NAME STATUS AGE default Active 3h14m kube-node-lease Active 3h14m kube-public Active 3h14m kube-system Active 3h14m
## CloudShell
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择集群信息。
在集群信息页面，单击右上方的通过 CloudShell 管理集群。
可选：单击，然后单击挂载存储空间，按照页面提示选择是否创建并绑定NAS文件系统。
关联并挂载NAS可持久化存储常用脚本及文件，防止实例释放时数据丢失。
执行kubectl命令以验证集群的连通性。
此命令以查询命名空间为例。
kubectl get namespaces
预期输出：
NAME STATUS AGE default Active 3h14m kube-node-lease Active 3h14m kube-public Active 3h14m kube-system Active 3h14m
## 相关文档
请按需对KubeConfig进行吊销、清除等操作，避免KubeConfig泄露带来的数据泄露等安全风险，请参见[管理](kubeconfig-operation-guide.md)[KubeConfig](kubeconfig-operation-guide.md)。
关于如何通过CloudShell传输文件，请参见[上传和下载文件](https://help.aliyun.com/zh/cloud-shell/user-guide/upload-and-download-files)。
关于Workbench的一些基础操作，例如文件的上传、查看、删除等，请参见[Workbench](../../../../ecs/documents/user-guide/basic-operations-in-workbench.md)[基础操作](../../../../ecs/documents/user-guide/basic-operations-in-workbench.md)。
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
