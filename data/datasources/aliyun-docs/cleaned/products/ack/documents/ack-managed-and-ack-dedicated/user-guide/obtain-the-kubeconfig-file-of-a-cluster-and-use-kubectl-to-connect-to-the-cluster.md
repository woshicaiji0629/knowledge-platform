# 获取集群KubeConfig并通过kubectl工具连接集群-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster

# 获取集群KubeConfig并通过kubectl工具连接集群
除容器服务控制台外，还可以使用Kubernetes命令行工具kubectl来管理集群与应用。通过kubectl连接集群时，需先获取包含当前用户身份信息的集群KubeConfig。
## 步骤一：安装并配置kubectl客户端
确定待安装kubectl的客户端机器，根据运行环境和集群版本[安装](https://kubernetes.io/docs/tasks/kubectl/install/)[kubectl](https://kubernetes.io/docs/tasks/kubectl/install/)。
## 步骤二：获取并使用KubeConfig
### 1. 选择KubeConfig类型
KubeConfig包含访问集群所需的认证信息，请根据安全需求和使用场景选择KubeConfig类型。
重要
根据[安全责任共担模型](../security-and-compliance/shared-responsibility-model.md)，KubeConfig凭证需自行负责和维护，请谨慎维护其合理性和有效性，定期轮换KubeConfig并遵循最小化权限策略，避免KubeConfig泄露带来的安全风险。
根据KubeConfig有效期：
临时KubeConfig：支持配置KubeConfig有效期（30分钟～3天），过期后自动失效，以降低KubeConfig泄露的安全风险。适用于日常运维、故障排查、CI/CD流水线等无需长期连接API Server的场景。
长期KubeConfig：默认有效期为3年，适用于无法频繁更新KubeConfig的自动化系统或长期监控服务。
根据访问集群的方式：
内网访问：获取内网访问的KubeConfig，此时kubectl客户端机器必须与集群位于同一VPC。通过阿里云内网连接时，延迟更低，更安全。
公网访问：获取公网访问的KubeConfig，通过公网中的任意机器作为客户端来连接集群。依赖[EIP](../../../../eip/documents/product-overview/what-is-eip.md)连接 API Server，适用于本地开发或远程运维。
EIP 绑定后，相关费用请参见[按量付费](../../../../eip/documents/pay-as-you-go.md)。
如使用ACK专有集群且已开启公网访问，可通过 SSH 从 Master 节点获取 KubeConfig 后在本地使用 kubectl 管理集群。详情请参见[通过](use-ssh-to-connect-to-the-master-nodes-of-a-dedicated-kubernetes-cluster.md)[SSH](use-ssh-to-connect-to-the-master-nodes-of-a-dedicated-kubernetes-cluster.md)[连接](use-ssh-to-connect-to-the-master-nodes-of-a-dedicated-kubernetes-cluster.md)[ACK](use-ssh-to-connect-to-the-master-nodes-of-a-dedicated-kubernetes-cluster.md)[专有版集群的](use-ssh-to-connect-to-the-master-nodes-of-a-dedicated-kubernetes-cluster.md)[Master](use-ssh-to-connect-to-the-master-nodes-of-a-dedicated-kubernetes-cluster.md)[节点](use-ssh-to-connect-to-the-master-nodes-of-a-dedicated-kubernetes-cluster.md)。
### 2. 获取KubeConfig并连接集群
在控制台获取 KubeConfig 后，kubectl 可依据该文件连接并管理集群。
RAM用户连接集群前，除容器服务的系统权限外，还需要被授予集群操作的权限，请参见[授权](authorization-overview.md)。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称或者目标集群右侧操作列下的详情。
在集群信息页面，单击连接信息页签，选择临时或长期KubeConfig。对于临时KubeConfig，需合理设置其有效期。
选择公网访问或内网访问页签，单击复制，将复制的KubeConfig内容粘贴至客户端的$HOME/.kube/config文件中，保存并退出。
如果$HOME/.kube/config文件不存在，可通过mkdir -p $HOME/.kube和touch $HOME/.kube/config来创建。
配置完成后，执行kubectl命令以验证集群连通性。
以查询命名空间为例。
kubectl get namespaces
预期输出：
NAME STATUS AGE default Active 4h39m kube-node-lease Active 4h39m kube-public Active 4h39m kube-system Active 4h39m
## 应用于生产环境
确保 KubeConfig 有效性：为防止 KubeConfig 过期导致集群访问中断，请及时更新。
长期 KubeConfig 有效期为3年，建议在临近过期的180天内，通过[容器服务管理控制台](https://cs.console.aliyun.com)或[DescribeClusterUserKubeconfig](../developer-reference/api-cs-2015-12-15-describeclusteruserkubeconfig.md)获取新KubeConfig。
新KubeConfig有效期仍为3年，旧 KubeConfig 在证书过期前仍然有效。
快速吊销KubeConfig：当KubeConfig疑似泄露时，应立即[吊销集群的](revoke-a-kubeconfig-credential.md)[KubeConfig](revoke-a-kubeconfig-credential.md)[凭证](revoke-a-kubeconfig-credential.md)。吊销后，系统会生成新的 KubeConfig 和授权绑定，所有基于旧KubeConfig的连接都将失效。
清理权限：在项目结束、员工离职等用户不再需要访问权限的场景中，使用“清理”功能来批量回收KubeConfig权限。清理后，系统不会生成新KubeConfig。具体操作请参见[清除](clear-kubeconfig.md)[KubeConfig](clear-kubeconfig.md)、[通过](revoke-the-permissions-of-the-specified-user-by-using-ack-ram-tool.md)[ack-ram-tool](revoke-the-permissions-of-the-specified-user-by-using-ack-ram-tool.md)[清理集群中指定用户的权限](revoke-the-permissions-of-the-specified-user-by-using-ack-ram-tool.md)。
为避免权限误删除，可[使用](using-the-kubeconfig-recycle-bin.md)[KubeConfig](using-the-kubeconfig-recycle-bin.md)[回收站](using-the-kubeconfig-recycle-bin.md)，恢复已清除的指定KubeConfig权限。
## 常见问题
如何获取KubeConfig中使用的证书所关联的身份信息？
执行如下命令获取。
grep client-certificate-data kubeconfig |awk '{print $2}' |base64 -d | openssl x509 -noout -text |grep Subject:请按实际情况修改kubeconfig路径。默认情况下，kubectl使用$HOME/.kube/config来连接集群。也可通过设置KUBECONFIG环境变量或设置--kubeconfig参数来指定其他KubeConfig文件。
预期输出类似如下：
Subject: O=system:users, OU=, CN=1***-1673419473
其中：
O：所属的Kubernetes用户组信息，示例中的组名为system:users。
CN：关联的用户信息。示例中的用户为1***-1673419473，其中1***关联的是账号下的某个阿里云用户ID。
如何获取KubeConfig所使用的证书的过期时间？
执行如下命令，获取名为KubeConfig的文件使用的证书所关联的过期时间。
grep client-certificate-data kubeconfig |awk '{print $2}' |base64 -d | openssl x509 -noout -enddate请按实际情况修改kubeconfig路径。默认情况下，kubectl使用$HOME/.kube/config来连接集群。也可通过设置KUBECONFIG环境变量或设置--kubeconfig参数来指定其他KubeConfig文件。
预期输出类似如下：
notAfter=Jan 10 06:44:34 2026 GMT
其中Jan 10 06:44:34 2026 GMT即为证书的过期时间。
支持在证书过期前180天内或证书过期后，通过控制台或者OpenAPI获取使用新过期时间的证书的KubeConfig。
如何获取客户端证书、客户端私钥和API Server信息？
可使用以下命令从KubeConfig文件中提取客户端证书、客户端私钥和API Server信息。
cat ./kubeconfig |grep client-certificate-data | awk -F ' ' '{print $2}' |base64 -d > ./client-cert.pem cat ./kubeconfig |grep client-key-data | awk -F ' ' '{print $2}' |base64 -d > ./client-key.pem APISERVER=`cat ./kubeconfig |grep server | awk -F ' ' '{print $2}'`请按实际情况修改kubeconfig路径。默认情况下，kubectl使用$HOME/.kube/config来连接集群。也可通过设置KUBECONFIG环境变量或设置--kubeconfig参数来指定其他KubeConfig文件。
如何解决通过kubectl连接集群时提示certificate is valid for错误的问题？
当为集群API Server的SLB绑定了新的IP，然后使用kubectl访问这个新的IP时，执行kubectl命令可能会失败并提示Error while proxying request: x509: certificate is valid for xxx或Unable to connect to the server: x509: certificate is valid for xxx错误。
ACK托管集群：将新的IP加入到API Server证书SAN中，请参见[自定义集群](../security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md)[API Server](../security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md)[证书](../security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md)[SAN](../security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md)。
ACK专有集群：配置kubectl，使用insecure-skip-tls-verify配置忽略此错误。
重要
此方式将导致客户端不再校验API Server证书，不建议在生产环境中使用。建议[热迁移](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[ACK](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[专有集群至](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[ACK](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[托管集群](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[Pro](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[版](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)，然后再将新IP加入到API Server证书SAN中来解决此问题。
方式一：执行kubectl命令时指定--insecure-skip-tls-verify参数。
kubectl -s https://<IP>:6443 --insecure-skip-tls-verify get ns
方式二：修改KubeConfig文件内容，新增insecure-skip-tls-verify: true配置，然后删除certificate-authority-data配置。
apiVersion: v1 clusters: - cluster: server: https://<IP>:6443 insecure-skip-tls-verify: true name: kubernetes contexts: ...
ACK托管集群能否提供集群根证书密钥用于自助生成KubeConfig证书？
ACK托管集群不对外提供集群根证书密钥，建议通过控制台或OpenAPI获取集群KubeConfig。
## 相关文档
可调用OpenAPI查询集群KubeConfig，请参见[DescribeClusterUserKubeconfig](../developer-reference/api-cs-2015-12-15-describeclusteruserkubeconfig.md)。
如需登录节点，请参见[选择](../../../../ecs/documents/user-guide/connect-to-instance.md)[ECS](../../../../ecs/documents/user-guide/connect-to-instance.md)[远程连接方式](../../../../ecs/documents/user-guide/connect-to-instance.md)。
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
