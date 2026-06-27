# 为Pod动态添加IP到RDS白名单-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/dynamically-add-the-ip-addresses-of-pods-to-the-whitelists-of-alibaba-cloud-services

# 为Pod动态配置阿里云产品白名单
在对权限要求相对较高的云上的场景中，您需要将Pod的IP地址动态地加入或移出指定的RDS白名单，以实现对权限最细粒度的控制。您可以通过ack-kubernetes-webhook-injector组件为Pod添加Annotation（注解），动态地将Pod的IP地址加入或移出指定的RDS白名单。本文介绍如何安装并使用ack-kubernetes-webhook-injector组件为Pod动态配置阿里云产品白名单，以及如何配置访问云产品内网Endpoint。
## 前提条件
已创建Kubernetes托管版集群，具体操作，请参见[创建](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[ACK](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。
已通过kubectl工具连接Kubernetes集群。具体操作，请参见[获取集群](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[KubeConfig](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[并通过](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[工具连接集群](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)。
集群使用Terway网络模式。更多信息，请参见[使用](../../ack-managed-and-ack-dedicated/user-guide/work-with-terway.md)[Terway](../../ack-managed-and-ack-dedicated/user-guide/work-with-terway.md)[网络插件](../../ack-managed-and-ack-dedicated/user-guide/work-with-terway.md)。
## 组件介绍
在云计算的使用场景中，某些资源需要配置相应的安全策略才能被外部访问，例如实例需要配置SLB访问控制策略，或者RDS数据库需要配置访问客户端的源IP地址白名单。虽然在创建ACK集群时可以将集群节点的IP网段加入到指定RDS的白名单中，但此方案有如下缺点：
白名单规则粒度太粗，加入白名单的IP网段覆盖了集群所有节点和Pod的IP地址。
集群删除后白名单规则需手动清理。
为了解决上述问题，容器服务 Kubernetes 版开发了ack-kubernetes-webhook-injector，支持将指定Pod的IP地址动态加入RDS白名单中，并且在Pod被删除时，将其IP地址从白名单中移除，实现对安全策略的细粒度控制。
目前，ack-kubernetes-webhook-injector支持以下功能：
随着Pod的创建与删除，自动将Pod的IP加入或移出指定的SLB访问控制策略组。
随着Pod的创建与删除，自动将Pod的IP加入或移出指定的阿里云Redis白名单。
随着Pod的创建与删除，自动将Pod的IP加入或移出指定的RDS白名单。
## 安装ack-kubernetes-webhook-injector
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择市场>应用市场。
选择并单击ack-kubernetes-webhook-injector，然后单击右上角的一键部署。
在面板中，选择安装组件的目标集群和命名空间，并设置名称，然后单击下一步。
在参数区域，填写openapi字段下的ak、sk为您的AK信息，然后在页面下方单击确定。
关于如何获取AK信息，请参见[获取](https://help.aliyun.com/zh/document_detail/175967.html#task-354412)[AccessKey](https://help.aliyun.com/zh/document_detail/175967.html#task-354412)。
## 使用ack-kubernetes-webhook-injector动态添加RDS白名单示例
在Pod副本控制器的Pod Spec中，您可以使用Annotation指定Pod需加入的RDS实例ID和RDS白名单分组名称。Pod创建时，ack-kubernetes-webhook-injector会将Pod的IP地址加入到白名单中，并且在Pod删除时移除规则。
Pod的Annotation需包括的RDS白名单如下：
RDS实例ID：ack.aliyun.com/rds_id
RDS白名单分组名称：ack.aliyun.com/white_list_name
本文以自动添加RDS白名单规则为例，展示如何使用ack-kubernetes-webhook-injector为Pod动态添加安全规则。
使用以下YAML示例创建一个Deployment，在其中的Pod定义中加入RDS实例ID和RDS白名单分组名称的Annotation。
apiVersion: apps/v1 kind: Deployment metadata: labels: app: inject-test name: inject-test spec: replicas: 1 selector: matchLabels: app: inject-test template: metadata: annotations: ack.aliyun.com/rds_id: <rm-wz9nanjcud75b****> ack.aliyun.com/white_list_name: <rds_group> labels: app: inject-test spec: containers: - command: - sleep - "3600" image: alpine:latest name: inject-test
执行以下命令，查看Pod的IP地址。
kubectl --kubeconfig .kube/config_sts_test -n inject-test get pod -o wide
预期输出：
NAME READY STATUS RESTARTS AGE IP NODE inject-test-68cc8f9bbf-gj86n 1/1 Running 0 22s 172.25.0.28 cn-hangzhou.xxx
预期输出中，Pod的IP地址为172.25.0.28。
登录[RDS](https://rdsnext.console.aliyun.com/?spm=5176.2020520152.nav-right.2.469016ddzrU6KW#/detail/rm-bp12685y16w4zjz9d/security/whiteList?region=cn-hangzhou)[控制台](https://rdsnext.console.aliyun.com/?spm=5176.2020520152.nav-right.2.469016ddzrU6KW#/detail/rm-bp12685y16w4zjz9d/security/whiteList?region=cn-hangzhou)，查看Annotation中RDS实例中的白名单。有关如何查看RDS的白名单，请参见[高安全白名单模式](../../../../rds/documents/apsaradb-rds-for-postgresql/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance.md)[IP](../../../../rds/documents/apsaradb-rds-for-postgresql/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance.md)[白名单](../../../../rds/documents/apsaradb-rds-for-postgresql/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance.md)。
此时，控制台显示规则已经自动添加。
将[步骤](dynamically-add-the-ip-addresses-of-pods-to-the-whitelists-of-alibaba-cloud-services.md)[1](dynamically-add-the-ip-addresses-of-pods-to-the-whitelists-of-alibaba-cloud-services.md)中的Deployment的副本数设置为0，再次查看RDS白名单。
此时，控制台显示已创建的规则被自动删除。
## 配置访问云产品内网Endpoint
ack-kubernetes-webhook-injector默认使用云产品公网Endpoint。如果您的集群未开启公网访问能力，可以通过修改配置，选择访问云产品内网Endpoint。
说明
部分云产品在特定地域没有内网Endpoint。配置前，请在[OpenAPI](https://next.api.aliyun.com/home)[门户](https://next.api.aliyun.com/home)查询目标产品的地域下是否提供内网Endpoint。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>无状态。
在页面顶部命名空间下拉列表中，选择kube-system命名空间，找到kubernetes-webhook-injector对应的Deployment，然后单击目标Deployment右侧操作列下的更多 > 查看Yaml。
在spec.template.spec.containers.command下方增加- '--intranet-access'一行，然后单击更新。
## 更多安全策略配置规则
ack-kubernetes-webhook-injector也支持以下安全策略配置：
SLB访问控制：ack.aliyun.com/access_control_policy_id。
阿里云Redis白名单配置：
Redis ID：ack.aliyun.com/redis_id。
Redis白名单分组：ack.aliyun.com/redis_white_list_name。
## 卸载ack-kubernetes-webhook-injector
如果您不再使用ack-kubernetes-webhook-injector，可以在ACK发布功能中将其删除。具体操作，请参见[基于](../../manage-releases-by-using-helm.md)[Helm](../../manage-releases-by-using-helm.md)[的发布管理](../../manage-releases-by-using-helm.md)。同时，请执行以下命令清理配置信息。
kubectl -n kube-system delete secret kubernetes-webhook-injector-certs kubectl delete mutatingwebhookconfigurations.admissionregistration.k8s.io kubernetes-webhook-injector
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
