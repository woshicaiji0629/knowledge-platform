# 清除KubeConfig-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/clear-kubeconfig

# 清除KubeConfig
容器服务 Kubernetes 版会为不同阿里云账号、RAM用户或角色签发带有其身份信息的KubeConfig凭证用于连接集群。KubeConfig管理功能支持从集群维度或用户维度获取所有已下发的KubeConfig状态，供您对有安全风险的KubeConfig进行清理和解除授权。
## KubeConfig介绍
KubeConfig用于在客户端配置集群的访问凭据，您可以通过[容器服务管理控制台](https://cs.console.aliyun.com)、[获取集群](../developer-reference/api-query-the-kubeconfig-file-of-a-cluster.md)[KubeConfig](../developer-reference/api-query-the-kubeconfig-file-of-a-cluster.md)[接口](../developer-reference/api-query-the-kubeconfig-file-of-a-cluster.md)等方式获取。请妥善管理集群的KubeConfig凭据，避免KubeConfig泄露带来的数据泄露等安全风险。
重要
获取的KubeConfig具备特定的生效时间，到期之后将自动失效。关于KubeConfig有效期时间查询，请参见[如何获取](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[KubeConfig](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[所使用的证书的过期时间？](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)
### KubeConfig状态
容器服务 Kubernetes 版的KubeConfig具备以下四个状态。
| 状态 | 说明 |
| --- | --- |
| 未颁发 | 对当前 RAM 用户或 RAM 角色从未下发过该集群的 KubeConfig。 |
| 生效 | 当前 RAM 用户或 RAM 角色的集群 KubeConfig 存在且未过期。 |
| 当前 RAM 用户或 RAM 角色的集群 KubeConfig 已被清除，但仍然存在残留的 RBAC 权限。 |  |
| 过期 | 当前 RAM 用户或 RAM 角色的集群 KubeConfig 存在，但已过期。 |
| 已清除 | 当前 RAM 用户或 RAM 角色下发过集群的 KubeConfig，但是目前 KubeConfig 已经被清除。 清除 KubeConfig 即删除集群的 KubeConfig 信息和该 RAM 用户或 RAM 角色的 RBAC Binding。 |
如需清除正在生效的KubeConfig，请您谨慎核对凭据下发的合理性和有效性。例如，离职员工请逐一清除其持有的KubeConfig，避免正在合理使用的KubeConfig过期。同时建议您[通过](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)[ack-ram-authenticator](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)[完成](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)[ACK](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)[托管集群](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)[API Server](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)[的](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)[Webhook](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)[认证](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)实现更加灵活可控的RBAC授权体验，实现删除RAM用户或RAM角色时数据面KubeConfig凭据的自动吊销。
重要
请务必确认不存在风险后，再执行KubeConfig清除操作，否则，您将无法使用该用户的KubeConfig访问集群API Server。
KubeConfig的运维和管理是用户的职责，请您务必及时清除有安全风险的KubeConfig。
### KubeConfig管理
| 管理维度 | 适用场景 | 使用所需权限 | 使用示例 |
| --- | --- | --- | --- |
| 集群维度 | 管理目标集群下所有用户的 KubeConfig。 | 阿里云账号 具有 [AliyunCSFullAccess](https://ram.console.aliyun.com/policies/AliyunCSFullAccess/System/content) 以及 [AliyunRAMReadOnlyAccess](https://ram.console.aliyun.com/policies/AliyunRAMReadOnlyAccess/System/content) RAM 权限的 RAM 用户或 RAM 角色，且该用户或角色需具有 RBAC 管理员权限。具体操作，请参见 [将](grant-rbac-permissions-to-ram-users-or-ram-roles.md) [RAM](grant-rbac-permissions-to-ram-users-or-ram-roles.md) [用户或](grant-rbac-permissions-to-ram-users-or-ram-roles.md) [RAM](grant-rbac-permissions-to-ram-users-or-ram-roles.md) [角色设置为权限管理员](grant-rbac-permissions-to-ram-users-or-ram-roles.md) 。 | [集群维度](clear-kubeconfig.md) [KubeConfig](clear-kubeconfig.md) [管理示例](clear-kubeconfig.md) |
| RAM 用户或 RAM 角色维度 | 管理指定用户所拥有的集群 KubeConfig。 | 阿里云账号 具有 [AliyunCSFullAccess](https://ram.console.aliyun.com/policies/AliyunCSFullAccess/System/content) 以及 [AliyunRAMReadOnlyAccess](https://ram.console.aliyun.com/policies/AliyunRAMReadOnlyAccess/System/content) RAM 权限的 RAM 用户或 RAM 角色，且该用户或角色需具有 RBAC 管理员权限。具体操作，请参见 [将](grant-rbac-permissions-to-ram-users-or-ram-roles.md) [RAM](grant-rbac-permissions-to-ram-users-or-ram-roles.md) [用户或](grant-rbac-permissions-to-ram-users-or-ram-roles.md) [RAM](grant-rbac-permissions-to-ram-users-or-ram-roles.md) [角色设置为权限管理员](grant-rbac-permissions-to-ram-users-or-ram-roles.md) 。 | [RAM](clear-kubeconfig.md) [用户或](clear-kubeconfig.md) [RAM](clear-kubeconfig.md) [角色维度](clear-kubeconfig.md) [KubeConfig](clear-kubeconfig.md) [管理示例](clear-kubeconfig.md) |
| 已失效 RAM 用户或 RAM 角色维度 | 账号中存在已删除的 RAM 用户或 RAM 角色，但 KubeConfig 仍在生效中。 | 阿里云账号 具有 [AliyunCSFullAccess](https://ram.console.aliyun.com/policies/AliyunCSFullAccess/System/content) 以及 [AliyunRAMReadOnlyAccess](https://ram.console.aliyun.com/policies/AliyunRAMReadOnlyAccess/System/content) RAM 权限的 RAM 用户或 RAM 角色，且该用户或角色需具有 RBAC 管理员权限。具体操作，请参见 [将](grant-rbac-permissions-to-ram-users-or-ram-roles.md) [RAM](grant-rbac-permissions-to-ram-users-or-ram-roles.md) [用户或](grant-rbac-permissions-to-ram-users-or-ram-roles.md) [RAM](grant-rbac-permissions-to-ram-users-or-ram-roles.md) [角色设置为权限管理员](grant-rbac-permissions-to-ram-users-or-ram-roles.md) 。 | [清除失效用户](clear-kubeconfig.md) [KubeConfig](clear-kubeconfig.md) [示例](clear-kubeconfig.md) |
## 集群维度KubeConfig管理示例
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择授权管理。
单击KubeConfig 管理页签，单击目标集群右侧的KubeConfig 管理，查看拥有该集群KubeConfig或KubeConfig过去被清除但仍残留RBAC授权的用户列表。
如果您的账号下存在RAM用户或角色已删除，但其KubeConfig仍在生效中的情况，控制台会有对应提示。
用户信息：用户名、用户ID、账号类型以及账号状态。
KubeConfig证书信息：KubeConfig过期时间、KubeConfig状态等。
确认待清除用户的KubeConfig没有被任何业务应用依赖使用后，单击目标用户右侧操作列下的清除 KubeConfig，清除目标用户在该集群下的KubeConfig。
重要
请务必确认不存在风险后，再执行KubeConfig清除操作，否则，您将无法使用该用户的KubeConfig访问集群API Server。
KubeConfig的运维和管理是用户的职责，请您务必及时清除有安全风险的KubeConfig。
单击清除 KubeConfig时，将会对待删除的KubeConfig进行七天内在指定集群API Server审计日志的访问记录检查，此辅助检查使用前提为对应集群[已开启集群的](../security-and-compliance/work-with-cluster-auditing.md)[API Server](../security-and-compliance/work-with-cluster-auditing.md)[审计功能](../security-and-compliance/work-with-cluster-auditing.md)。
## RAM用户或RAM角色维度KubeConfig管理示例
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择授权管理。
在授权管理页面，单击RAM 用户页签，然后单击目标用户右侧的管理 KubeConfig进入该用户的管理 KubeConfig页面。
可查看该用户各个集群KubeConfig的下发状态列表。
集群信息：集群名称和ID。
KubeConfig证书信息：KubeConfig过期时间和状态、七天日志检查（即证书访问记录）。
单个或批量清除该用户对应集群的KubeConfig。清除前，请确认待清除用户的KubeConfig没有被任何业务应用依赖使用。
单个清除：单击目标集群右侧操作列下的清除 KubeConfig，清除当前用户在该集群下的KubeConfig。
批量清除：在集群名称列选择多个待清除的集群，然后在页面左下角单击清除 KubeConfig。
重要
请务必确认不存在风险后，再执行KubeConfig清除操作，否则，您将无法使用该用户的KubeConfig访问集群API Server。
KubeConfig的运维和管理是用户的职责，请您务必及时清除有安全风险的KubeConfig。
单击清除 KubeConfig时，将会对待删除的KubeConfig进行七天内在指定集群API Server审计日志的访问记录检查，此辅助检查使用前提为对应集群[已开启集群的](../security-and-compliance/work-with-cluster-auditing.md)[API Server](../security-and-compliance/work-with-cluster-auditing.md)[审计功能](../security-and-compliance/work-with-cluster-auditing.md)。
## 清除失效用户KubeConfig示例
### 控制台
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择授权管理。
在授权管理页面，如果您的账号中存在已删除的失效用户的KubeConfig残留，该页面会显示提示信息。
单击红色提示框中的处理与失效账号关联的 KubeConfig，进入清除已删除 RAM 用户/角色的 KubeConfig页面。
该页面可查看KubeConfig 以及 RBAC 授权仍在生效的已删除的 RAM用户或RAM角色列表。
确认待清除用户的KubeConfig没有被任何业务应用依赖使用后，单击已失效用户右侧的清除 KubeConfig，清除该失效用户的KubeConfig。
重要
请务必确认不存在风险后，再执行KubeConfig清除操作，否则，您将无法使用该用户的KubeConfig访问集群API Server。
KubeConfig的运维和管理是用户的职责，请您务必及时清除有安全风险的KubeConfig。
单击清除 KubeConfig时，将会对待删除的KubeConfig进行七天内在指定集群API Server审计日志的访问记录检查，此辅助检查使用前提为对应集群[已开启集群的](../security-and-compliance/work-with-cluster-auditing.md)[API Server](../security-and-compliance/work-with-cluster-auditing.md)[审计功能](../security-and-compliance/work-with-cluster-auditing.md)。
### ack-ram-tool工具
关于如何使用ack-ram-tool工具清除KubeConfig，请参见[通过](revoke-the-permissions-of-the-specified-user-by-using-ack-ram-tool.md)[ack-ram-tool](revoke-the-permissions-of-the-specified-user-by-using-ack-ram-tool.md)[清理集群中指定用户的权限](revoke-the-permissions-of-the-specified-user-by-using-ack-ram-tool.md)。
## 常见问题
### 清除KubeConfig时，什么是七天日志检查？
七天日志检查是一种辅助检查手段，用于查看KubeConfig在最近七天是否访问过集群。但此检查仅作辅助检查供您参考，您仍需要自行确保KubeConfig未被任何业务应用依赖使用。
使用此功能需[已开启集群的](../security-and-compliance/work-with-cluster-auditing.md)[API Server](../security-and-compliance/work-with-cluster-auditing.md)[审计功能](../security-and-compliance/work-with-cluster-auditing.md)。
### 如何解读七天日志检查的结果？
| 检查结果 | 结果类型 | 可能原因 |
| --- | --- | --- |
| 成功 | 未发现访问记录 | 近七天内用户可能并未使用该 KubeConfig 访问集群 API Server。 |
| 存在访问记录 | 近七天内用户使用过该 KubeConfig 访问集群 API Server。 |  |
| 失败 | 无法查找访问记录 | 集群未开通日志审计，无法自动进行检查。 |
| 其他错误原因，例如集群连接失败、网络问题等。 |  |  |
### 不能清除KubeConfig的场景有哪些？
集群状态异常：删除失败、删除中、已删除、失败四种状态的集群无法进行KubeConfig清除。
KubeConfig或证书状态异常：集群KubeConfig处于未颁发、已清除、未知状态的用户无法进行 KubeConfig清除。
用户无法清除自己的KubeConfig。
用户无法清除阿里云账号的KubeConfig。
### KubeConfig误清除可以恢复吗？可以恢复指定版本的KubeConfig吗？
如果您需要恢复误清除的KubeConfig，或回滚某个历史版本的KubeConfig，您可以通过KubeConfig回收站功能来实现。更多信息，请参见[使用](using-the-kubeconfig-recycle-bin.md)[KubeConfig](using-the-kubeconfig-recycle-bin.md)[回收站](using-the-kubeconfig-recycle-bin.md)。
### KubeConfig管理的最佳安全实践是什么？
您应自行管理账号和容器服务集群的访问凭据，妥善保管账号和容器服务集群的访问凭据，例如RAM AK、Token和容器服务集群KubeConfig客户端等。您自行管理账号和容器服务集群的授权范围，应遵循权限的最小化原则，并及时更新清除不恰当、失效的授权，例如，已离职员工不应再持有容器服务集群的访问权限。同时，建议您[通过](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)[ack-ram-authenticator](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)[完成](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)[ACK](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)[托管集群](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)[API Server](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)[的](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)[Webhook](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)[认证](use-ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)实现更加灵活的RBAC授权体验，实现删除RAM用户或角色时数据面KubeConfig凭据的自动吊销。
重要
因您运维不当导致的访问凭据（例如RAM凭据、KubeConfig）泄露或过期引起的一切损失和后果均由您自行承担，请仔细阅读并遵循[安全责任共担模型](../security-and-compliance/shared-responsibility-model.md)的要求。
## 相关文档
当企业内部员工离职或是某签发KubeConfig疑似泄露等情况发生时，您可以吊销该集群的KubeConfig，生成新的KubeConfig。具体操作，请参见[吊销集群的](revoke-a-kubeconfig-credential.md)[KubeConfig](revoke-a-kubeconfig-credential.md)[凭证](revoke-a-kubeconfig-credential.md)。
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
