# 配置Argo工作流将日志与状态持久化到RDS数据库-容器服务Kubernetes版ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-argo-workflow-cluster/user-guide/use-rds-for-argo-workflow-persistence

# 使用RDS数据库持久化Argo工作流
Argo工作流在容器Argo工作流集群中被存储为Kubernetes资源，会被定期清理，如果需要对工作流的运行过程进行分析和回溯，可以通过配置持久化策略，将工作流持久化存储到数据库中。即使工作流被删除或者工作流运行的Pod被删除后，也可以查看工作流日志。本文以阿里云RDS MySQL数据库为例，介绍如何配置工作流持久化存储。
## 适用范围
已[获取集群](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[KubeConfig](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[并通过](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[kubectl](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[工具连接集群](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)。
已[创建](../../../../rds/documents/apsaradb-rds-for-mysql/step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)[RDS MySQL](../../../../rds/documents/apsaradb-rds-for-mysql/step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)[实例与配置数据库](../../../../rds/documents/apsaradb-rds-for-mysql/step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)。
重要
RDS MySQL实例需要和已创建的容器Argo工作流集群处于同一VPC，并将该VPC网段添加到RDS实例的白名单中。
操作过程中，请记录数据库名称、数据库的用户名和密码（需要具有数据库的读写权限）、RDS实例地址等信息，用于后续步骤。
Argo工作流持久化功能支持RDS MySQL数据库、RDS PostgreSQL数据库。
## 操作步骤
将下方的示例保存到rds-user.yaml，然后执行kubectl apply -f rds-user.yaml创建Secret。
apiVersion:v1stringData:username:DATABASE_USERNAME# 替换为数据库的用户名。password:DATABASE_PASSWORD# 替换为数据库的密码。kind:Secretmetadata:name:argo-mysql-confignamespace:defaulttype:Opaque
将下方命令中的CLUSTER_ID替换为集群ID，然后执行命令编辑ConfigMap， 添加持久化相关配置。
kubectl edit configmap -nCLUSTER_IDworkflow-controller-configmap
配置项：
host：设置为RDS MySQL实例的地址。
database：设置为数据库的名称。
archive：开启持久化功能，需要设置为true。
archiveTTL：持久化数据的保存时间。示例中设置为30d，表示工作流持久化到数据库中保存30天。
nodeStatusOffLoad：开启工作流状态卸载（Offload）功能，需设置为true。开启后，工作流节点状态将存储在数据库中而非etcd，从而支持包含大规模子任务的单体工作流。
persistence: | connectionPool: maxIdleConns: 100 maxOpenConns: 0 connMaxLifetime: 0s # 0 means connections don't have a max lifetime. archiveTTL: 30d archive: true nodeStatusOffLoad: true mysql: host: rm-xxx.mysql.cn-beijing.rds.aliyuncs.com port: 3306 database: argo-workflow tableName: argo_workflows userNameSecret: name: argo-mysql-config key: username passwordSecret: name: argo-mysql-config key: password
配置完成后，重启Argo Server，并确认Pod是否正常更新。
kubectl rollout restart deployment -nCLUSTER_IDargo-server
重要
如果重启Argo Server后，Pod出现反复重启状况，可能是由于网络连接出现问题。请检查集群和数据库实例是否处于同一个VPC，数据库白名单是否允许集群访问。
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
