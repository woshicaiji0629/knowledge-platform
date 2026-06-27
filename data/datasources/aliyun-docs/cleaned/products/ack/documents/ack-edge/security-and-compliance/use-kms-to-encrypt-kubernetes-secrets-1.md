# 在ACK Edge集群中使用阿里云KMS进行Secret的落盘加密-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-1

# 在ACK Edge集群中使用阿里云KMS进行Secret的落盘加密
在ACK Edge集群Pro版中，您可以使用在阿里云密钥管理服务KMS（Key Management Service）中创建的密钥加密Kubernetes Secret密钥，提升加密数据保护能力。本文主要介绍如何使用KMS中管理的密钥对ACK Edge集群Pro版中的Kubernetes Secret密钥数据进行落盘加密。
## 前提条件
| 条件项 | 说明 |
| --- | --- |
| KMS 密钥 | 已在 [密钥管理服务控制台](https://yundun.console.aliyun.com/?p=kms#/keyList/base) 创建 KMS 密钥，且密钥地域与目标 ACK Pro 集群所在地域保持统一。 ACK Pro 集群支持默认密钥、软件密钥和硬件密钥，您可以按业务需求选择。关于 KMS 密钥管理的更多信息和相关操作，请参见 [密钥管理快速入门](../../../../kms/documents/key-management-service/getting-started/getting-started-with-key-management.md) ；关于 KMS 服务计费的详细说明，请参见 [产品计费](../../../../kms/documents/key-management-service/product-overview/kms-billing.md) 。 重要 开启落盘加密功能时，请勿使用 KMS 的控制台或 OpenAPI 禁用或删除集群 Secret 加解密选择的密钥，否则会导致集群 API Server 不可用，继而无法正常获取 Secret 和 ServiceAccount 等对象，影响业务应用的正常运行。 |
| 集群网络 ACL 规则配置 | 开启落盘加密功能时，控制面的 KMS 插件需要访问阿里云 KMS OpenAPI 完成 Secrets 实例的加解密。因此，需要确保集群使用的安全组的 出方向 、VPC 网络 ACL 的 出入方向规则 中均放行了阿里云云产品网段（ 100.64.0.0/10 ），否则会导致集群控制面不可用。请参见 [普通安全组](../../ack-managed-and-ack-dedicated/user-guide/configure-security-group-rules-to-enforce-access-control-on-ack-clusters.md) 。 |
| 授权 | 根据您使用账号类型的不同，确认已完成如下授权操作。 阿里云账号：已授权容器服务账号使用 AliyunCSManagedSecurityRole 系统角色的权限。如果您使用的账号未授权，开启 Secret 落盘加密时，ACK 控制台会提示您进行 KMS 安全系统角色授权。您可以根据控制台指引完成授权，也可以通过 [访问控制快速授权页面](https://ram.console.aliyun.com/role/authorization?request=%7B%22Services%22%3A%5B%7B%22Service%22%3A%22CS%22%2C%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunCSManagedSecurityRole%22%2C%22TemplateId%22%3A%22AliyunCSManagedSecurityRole%22%7D%5D%7D%5D%2C%22ReturnUrl%22%3A%22https%3A%2F%2Fcs.console.aliyun.com%2F%22%7D) 完成授权。 RAM 用户或 RAM 角色： 已确保对该集群有 RBAC 的管理员或运维人员权限。具体操作，请参见 [使用](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md) [RBAC](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md) [为集群内资源操作授权](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md) 。 已授予 AliyunKMSCryptoAdminAccess 系统权限。具体操作，请参见 [为](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md) [RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md) [用户或](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md) [RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md) [角色授权](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md) 。 |
## Secret加密介绍
在Kubernetes集群中，通常使用Secret密钥模型存储和管理业务应用涉及的敏感信息，例如应用密码、TLS证书、Docker镜像下载凭据等敏感信息。Kubernetes会将所有的Secret密钥对象数据存储在集群对应的etcd中。关于密钥的更多信息，请参见[Secrets](https://kubernetes.io/zh/docs/concepts/configuration/secret/)。
在ACK Edge集群Pro版中，您可以使用在KMS中创建的密钥加密Kubernetes Secret密钥。KMS加密过程基于Kubernetes提供的KMS Encryption Provider机制，使用信封加密的方式对存储在etcd中的Kubernetes Secret密钥进行自动加密和解密。Kubernetes Secret密钥加密和解密的过程如下。
当一个业务密钥需要通过Kubernetes Secret API存储时，数据会首先被API Server生成的一个随机的数据加密密钥加密，然后该数据密钥会被指定的KMS密钥加密为一个密文密钥存储在etcd中。
解密Kubernetes Secret密钥时，系统会首先调用KMS的解密OpenAPI进行密文密钥的解密，然后使用解密后的明文密钥对Secret数据解密，并最终返回给您。
更多信息，请参见[KMS Encryption Provider](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/)[机制](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/)、[使用](../../../../kms/documents/key-management-service/use-cases/use-envelope-encryption.md)[KMS](../../../../kms/documents/key-management-service/use-cases/use-envelope-encryption.md)[密钥进行信封加密](../../../../kms/documents/key-management-service/use-cases/use-envelope-encryption.md)。
## 在ACK Edge集群Pro版中开启Secret落盘加密
## 新创建集群
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面中，单击页面右上角的创建集群。
单击ACK Edge 集群页签，在页签最下方展开高级选项（选填），找到Secret 落盘加密，选中选择 KMS 密钥，在下拉框中选择KMS密钥ID。
如果您未创建KMS密钥，请单击创建密钥，前往[密钥管理服务控制台](https://kms.console.aliyun.com)创建密钥。具体操作，请参见[创建密钥](../../../../kms/documents/key-management-service/support/create-a-cmk.md)。
关于创建ACK Edge集群Pro版的其他配置信息，请参见[创建集群](../user-guide/create-an-ack-edge-cluster-1.md)。
登录[操作审计控制台](https://actiontrail.console.aliyun.com)，在左侧导航栏单击事件查询，在事件查询页面有使用aliyuncsmanagedsecurityrole系统角色的加密和解密事件日志，则说明该集群后台已成功开启Secret落盘加密特性。
## 已创建集群
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏单击集群列表。
在集群列表页面，单击目标集群名称，然后在集群详情页面单击基本信息页签，在安全与审计区域打开Secret 落盘加密开关。
首次开启时，请根据提示单击前往RAM进行授权进入访问控制快速授权页面，然后单击确认授权完成授权。
说明
如需开启落盘加密功能，请确保当前登录的RAM用户或RAM角色对该集群有RBAC的管理员或运维人员权限。具体操作，请参考[使用](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[RBAC](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[为集群内资源操作授权](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)。
如需授权aliyuncsmanagedsecurityrole角色，请确保已使用阿里云账号（主账号）或拥有RAM管理权限的RAM用户或RAM角色登录。
在弹出的Secret 落盘加密对话框，选择已有的KMS密钥，然后单击确定。
如果您未创建KMS密钥，请单击创建密钥，前往[密钥管理服务控制台](https://kms.console.aliyun.com)创建密钥。具体操作，请参见[创建密钥](../../../../kms/documents/key-management-service/support/create-a-cmk.md)。
当集群状态由更新中变为运行中时，表明该集群的Secret落盘加密特性已开启。
当您不需要使用Secret落盘加密功能时，可在安全与审计区域关闭Secret 落盘加密开关。
## 使用自动轮转密钥开启Secret落盘加密
您可以使用KMS自动轮转密钥功能进行Secret的落盘加密。当密钥发生自动轮转时，存量的Secret仍旧使用轮转前的密钥版本进行加密，新增的Secret将使用轮转后的新密钥版本进行加密。关于自动轮转密钥具体操作，请参见[密钥轮转](../../../../kms/documents/key-management-service/user-guide/configure-key-rotation.md)。
如需确保存量的Secret也使用新的密钥版本进行加密，请在密钥发生自动轮转后，执行以下命令强制使用新的密钥版本重新加密所有的存量Secret。
kubectl get secrets --all-namespaces -o json | kubectl annotate --overwrite -f - encryption-key-rotation-time="$(date -u +'%Y-%m-%dT%H:%M:%S%z')"
## 常见问题
### 开启Secret落盘加密后，通过kubectl命令获取到的Secret是加密后的密文吗？
不是。Secret落盘加密功能所加密的是etcd中存储的原始数据，即开启Secret落盘加密后，etcd中存储的Secret数据将是加密后的密文数据。但客户端通过API Server提供的Secret API获取到的Secret数据仍旧是原始的明文数据。
### 如何禁止RAM用户或RAM角色在已创建的ACK Edge集群中开启或关闭Secret落盘加密功能
您可以通过为RAM用户或RAM角色授予如下拒绝操作的RAM权限策略，禁止该RAM用户或RAM角色在已创建的ACK Edge集群中开启或关闭Secret落盘加密功能。具体操作，请参见[使用](../../ack-managed-and-ack-dedicated/user-guide/create-a-custom-ram-policy.md)[RAM](../../ack-managed-and-ack-dedicated/user-guide/create-a-custom-ram-policy.md)[授予集群及云资源访问权限](../../ack-managed-and-ack-dedicated/user-guide/create-a-custom-ram-policy.md)。
{ "Action": [ "cs:UpdateKMSEncryption" ], "Effect": "Deny", "Resource": [ "*" ] }
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
