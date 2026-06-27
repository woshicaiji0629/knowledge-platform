# 云上资源的访问控制管理-身份管理-专有网络VPC-阿里云

Source: https://help.aliyun.com/zh/vpc/identity-management

# 身份管理
为确保您的阿里云账号及云资源使用安全，如非必要都应避免直接使用阿里云主账号来访问专有网络 VPC。推荐的做法是使用访问控制 RAM（Resource Access Management）提供的身份，包括RAM用户和RAM角色来访问VPC。
## RAM用户
RAM用户需要由阿里云账号（即主账号）或拥有管理员权限的RAM用户、RAM角色来创建，且必须在获得授权后才能登录控制台或使用API访问阿里云账号下的资源。
对于RAM用户的使用，建议您：
使用阿里云账号创建一个RAM用户，并为RAM用户授予管理员权限，后续使用有管理员权限的RAM用户创建并管理其他RAM用户。
将人员用户和程序用户分离。
创建RAM用户时，支持设置控制台访问和使用永久AccessKey访问两种访问方式。
控制台用户使用账号和密码访问云产品控制台，API用户使用访问密钥AK（AccessKey）调用API访问云资源。建议您将两个不同的使用场景分离，避免误操作导致服务受到影响。对于通过控制台访问的用户，推荐为其开启MFA多因素认证。
按需为RAM用户分配最小权限。
最小权限是指授予用户执行某项任务所需的权限，不授予其他无需用到的权限。最小授权可以避免用户操作权限过大，提高数据安全性，减少因权限滥用导致的安全风险。
不要把RAM用户的AccessKey ID和AccessKey Secret保存在工程代码中，否则可能导致AK泄露，威胁您账号下所有资源的安全。建议您使用STS或环境变量等方式获取访问授权。
满足条件时对RAM用户设置SSO单点登录功能，实现直接使用企业自有的身份登录并访问阿里云资源。
### RAM用户相关操作
[RAM](../../ram/documents/user-guide/overview-of-ram-users.md)[用户管理](../../ram/documents/user-guide/overview-of-ram-users.md)
[AK](https://help.aliyun.com/zh/openapi/accesskey-security-solution)[安全方案](https://help.aliyun.com/zh/openapi/accesskey-security-solution)
[RAM](../../ram/documents/overview-of-user-based-sso.md)[用户](../../ram/documents/overview-of-user-based-sso.md)[SSO](../../ram/documents/overview-of-user-based-sso.md)[管理](../../ram/documents/overview-of-user-based-sso.md)
## RAM用户组
当您的阿里云账号下有多个RAM用户时，可以通过创建用户组对职责相同的RAM用户进行分组管理和批量授权，高效地管理RAM用户及其权限。
对于RAM用户组的使用，建议您：
在对RAM用户组授权时遵循最小权限策略原则。
在RAM用户职责发生变化时将其从不再归属的用户组中移除，避免权限滥用。
在某个用户组不再需要某些权限时移除用户组对应的权限。
### RAM用户组相关操作
[RAM](../../ram/documents/user-guide/overview-of-a-ram-user-group.md)[用户组](../../ram/documents/user-guide/overview-of-a-ram-user-group.md)
## RAM角色
RAM角色是一种虚拟用户，可以被授予一组权限策略。与RAM用户不同，RAM角色没有永久身份凭证（登录密码或访问密钥），需要被一个可信实体扮演。扮演成功后，可信实体将获得RAM角色的临时身份凭证，即安全令牌（STS Token），使用该安全令牌就能以RAM角色身份访问被授权的资源。
以下是使用RAM角色的安全建议：
创建RAM角色后，请勿随意变更RAM角色的可信实体。修改RAM角色信任策略中的可信实体，可能会导致原受信对象权限缺失，影响业务正常运行。也可能会因增加受信对象，带来过度授权的风险。特殊情况必须修改时请务必在测试账号充分测试，确保功能正常使用后，再应用到正式生产账号。
可信实体的RAM用户获得相关授权后即可以调用[AssumeRole - 获取扮演角色的临时身份凭证](../../ram/documents/developer-reference/api-sts-2015-04-01-assumerole.md)接口获取RAM角色的STS Token。STS Token自颁发后将在一段时间内有效，建议您设置合理的Token有效期，避免有效期过长带来安全风险。
说明
STS Token有效期的最大值为角色的最大会话时间。从安全的角度考虑，应将角色最大会话时间也设置在合理范围。
满足条件时对RAM角色设置SSO单点登录功能，实现直接使用企业自有的身份登录并访问阿里云资源。
### RAM角色相关操作
[RAM](../../ram/documents/user-guide/ram-role-overview.md)[角色管理](../../ram/documents/user-guide/ram-role-overview.md)
[扮演](../../ram/documents/user-guide/assume-a-ram-role.md)[RAM](../../ram/documents/user-guide/assume-a-ram-role.md)[角色](../../ram/documents/user-guide/assume-a-ram-role.md)
[设置](../../ram/documents/user-guide/specify-the-maximum-session-duration-for-a-ram-role.md)[RAM](../../ram/documents/user-guide/specify-the-maximum-session-duration-for-a-ram-role.md)[角色最大会话时间](../../ram/documents/user-guide/specify-the-maximum-session-duration-for-a-ram-role.md)
[角色](../../ram/documents/role-based-sso.md)[SSO](../../ram/documents/role-based-sso.md)[管理](../../ram/documents/role-based-sso.md)
## 身份管理相关文档
[阿里云身份与权限](https://help.aliyun.com/zh/document_detail/469087.html)
[RAM](../../ram/documents/terms.md)[基本概念](../../ram/documents/terms.md)
[RAM](../../ram/documents/product-overview/limits.md)[相关使用限制](../../ram/documents/product-overview/limits.md)
[专有网络](vpc-1694081077178.md)[VPC](vpc-1694081077178.md)[系统权限策略参考](vpc-1694081077178.md)
[专有网络](vpc-custom-permission-policy-reference.md)[VPC](vpc-custom-permission-policy-reference.md)[自定义权限策略参考](vpc-custom-permission-policy-reference.md)
[RAM](security-and-compliance/grant-permissions-to-ram-user.md)[鉴权](security-and-compliance/grant-permissions-to-ram-user.md)
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
