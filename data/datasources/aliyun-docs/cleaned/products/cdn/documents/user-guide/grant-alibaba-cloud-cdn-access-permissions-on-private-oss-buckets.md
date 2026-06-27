# OSS私有Bucket回源-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets

# OSS私有Bucket回源
如果加速域名的源站是阿里云对象存储OSS，并且OSS的Bucket为私有模式（可以起到访问鉴权的作用，避免非授权的请求盗刷流量），建议您给加速域名开启OSS私有Bucket回源功能，通过CDN加速OSS私有Bucket资源。
## 工作原理与优势
工作原理：功能开启后，CDN向您的私有OSS Bucket发起回源请求时，会自动在请求头（Header）中添加一个Authorization字段。该字段的值是根据您授权的身份信息（STS临时令牌或AccessKey）生成的有效签名，OSS服务会据此对请求进行鉴权。
安全访问：通过为CDN授予一个受限的只读权限，确保了回源请求的合法性，避免了将私有Bucket设置为公开所带来的安全风险。
成本优化：终端用户访问将命中CDN缓存，其流量费用远低于直接访问OSS产生的外网流出流量。同时，CDN回源到OSS的流量会计为CDN回源流量，其单价也低于OSS外网流出流量单价，有效降低总体成本。具体请参见[CDN](../product-overview/billing-of-oss-content-acceleration.md)[加速](../product-overview/billing-of-oss-content-acceleration.md)[OSS](../product-overview/billing-of-oss-content-acceleration.md)[计费说明](../product-overview/billing-of-oss-content-acceleration.md)
## 操作步骤
配置过程分为两步：首先为您的账号完成一次性授权，然后为指定的加速域名开启该功能。
授权CDN访问OSS。在首次为账号下域名配置该功能前，您必须先为CDN服务授予访问OSS的权限，此为账号级别的一次性操作。如果您没有出现授权提示，则直接跳过该步骤。
## （推荐）通过控制台一键授权
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，单击目标域名对应的管理。
在指定域名的左侧导航栏，单击回源配置。
在阿里云OSS私有Bucket回源区域，单击点击授权，在授权确认页中单击确认授权。
页面角色授权行提示"该账户未授权CDN服务访问您的OSS空间"，状态开关默认为关闭。
## （备用方案）通过RAM手动授权
登录[RAM](https://ram.console.aliyun.com/permissions)[控制台](https://ram.console.aliyun.com/permissions)。
在左侧导航栏，单击权限管理>权限策略。
在权限策略页面，单击创建权限策略。
在脚本编辑页签，输入以下策略内容。
{ "Version": "1", "Statement": [ { "Action": [ "oss:List*", "oss:Get*" ], "Resource": "*", "Effect": "Allow" } ] }
单击确定，在创建权限策略页面输入以下信息之后单击确定。
策略名称：AliyunCDNAccessingPrivateOSSRolePolicy
备注：用于CDN/DCDN回源私有OSS Bucket角色的授权策略，包含OSS的只读权限。
在左侧导航栏，单击身份管理>角色。
在角色页面，单击创建角色。
将信任主体类型设置为云账号，信任主体名称选择当前云账号，单击确定。
在创建角色阶段，输入以下信息。
角色名称：AliyunCDNAccessingPrivateOSSRole
角色创建完成之后，在角色页面列表中单击AliyunCDNAccessingPrivateOSSRole，进入角色编辑页面。
在信任策略页签，单击编辑信任策略，输入以下信息之后单击确定。
{ "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Principal": { "Service": [ "cdn.aliyuncs.com" ] } } ], "Version": "1" }
切换到权限管理页签，在授权页签中，单击新增授权。
资源范围：账号级别
授权主体：选择之前创建的AliyunCDNAccessingPrivateOSSRole
权限策略：选择自定义策略，选择之前创建的AliyunCDNAccessingPrivateOSSRolePolicy，单击确认新增授权。
确认新增授权之后，回到CDN控制台的回源配置页面，可以看到阿里云OSS私有Bucket回源功能已经完成授权，
开启阿里云OSS私有Bucket回源并配置回源类型。
找到阿里云OSS私有Bucket回源区域，打开其开关。
在弹出的阿里云OSS私有Bucket回源对话框中，选择回源类型，单击确定。
| 回源类型 | 推荐场景与说明 |
| --- | --- |
| 同账号回源 | （推荐） 适用于 CDN 和 OSS Bucket 在同一个阿里云账号下的场景。系统将自动使用 STS 临时安全令牌进行鉴权，配置简单，无需管理密钥，安全性更高。 STS 临时安全令牌也可以实现跨账号回源，详情请参见 [CDN](back-to-source-faq.md) [使用](back-to-source-faq.md) [STS](back-to-source-faq.md) [实现跨账号回源](back-to-source-faq.md) [OSS](back-to-source-faq.md) [私有](back-to-source-faq.md) [Bucket](back-to-source-faq.md) [操作指引](back-to-source-faq.md) 。 |
| 跨账号回源或同账号回源 | 适用于 CDN 和 OSS Bucket 分属不同阿里云账号的场景，也支持同账号。此方式需要您手动提供回源目标 OSS 私有 Bucket 所属阿里云账号的 AccessKey ID 和 AccessKey Secret。具体请参见 [创建](../../../ram/documents/user-guide/create-an-accesskey-pair.md) [AccessKey](../../../ram/documents/user-guide/create-an-accesskey-pair.md) 。 |
说明
访问范围说明：开启后，该加速域名将可以访问其源站私有Bucket内的所有资源，无法在CDN侧对Bucket内的部分资源做访问限制。
签名冲突说明：为避免OSS鉴权失败，请确保回源请求的URL参数中不携带签名信息。单个请求不能同时在Header和URL中携带签名。
功能冲突说明：本功能与OSS的静态网站托管功能的默认首页配置存在冲突。如需同时使用，请参考[说明文档](../you-are-forbidden-to-list-buckets-after-access-to-private-oss-buckets-is-enabled.md)。
## 安全加固建议
开启私有Bucket回源后，您的源站数据是安全的，但缓存在CDN边缘节点上的资源默认是公开访问的。为防止CDN流量被盗刷，强烈建议您结合使用CDN提供的其他安全功能：
[配置](configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[Referer](configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[黑/白名单](configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)：限制只有特定来源网站的请求才能访问您的CDN资源。
[配置](configure-url-signing.md)[URL](configure-url-signing.md)[鉴权](configure-url-signing.md)：为您的资源URL设置动态签名和过期时间，有效抵御恶意下载。
## 关闭OSS私有Bucket回源
如果您不希望加速域名能够访问您同账号下的私有Bucket内资源，您可以通过访问控制RAM（Resource Access Management）控制台，取消对应角色名称的授权，关闭CDN回源OSS私有Bucket的权限。
在CDN控制台关闭该功能。
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，单击目标域名对应的管理。
在指定域名的左侧导航栏，单击回源配置。
在阿里云OSS私有Bucket回源区域，关闭阿里云OSS私有Bucket回源开关。
在RAM控制台彻底删除授权。
登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。
在左侧导航栏，单击
在角色名称列表下，单击AliyunCDNAccessingPrivateOSSRole角色。
进入角色详情页，在权限管理页签下可查看到已授权的系统策略（备注：用于CDN回源私有OSS Bucket角色的授权策略，包含OSS的只读权限），资源范围为账号级别。操作列提供解除授权链接，页面右上角有删除角色按钮。
移除角色AliyunCDNAccessingPrivateOSSRole中的所有权限。
单击权限对应的解除授权。
在移除权限的确认对话框中，单击解除授权。
返回
单击AliyunCDNAccessingPrivateOSSRole角色对应的删除角色。
在删除角色的确认对话框中，单击删除角色。
返回
单击AliyunCDNAccessingPrivateOSSRolePolic策略对应的删除权限策略按钮。
在删除权限策略的确认对话框中，输入策略名称，单击删除权限策略。
## 常见问题
CDN访问OSS资源提示This request is forbidden by kms.错误如何解决？
如果您的OSS Bucket中使用了密钥管理服务KMS（Key Management Service）进行加密，您需要为CDN的回源角色额外授予使用KMS密钥的权限，否则CDN将无法解密和访问这些文件，出现This request is forbidden by kms.报错。
登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。
在左侧导航栏，选择
在角色名称列表下，找到AliyunCDNAccessingPrivateOSSRole角色。
单击新增授权，授权主体会自动填入。
在权限策略下选择系统策略，搜索AliyunKMSCryptoUserAccess，并单击AliyunKMSCryptoUserAccess，将其添加到已选择权限策略区域框中。
单击确认新增授权，显示已完成。
单击关闭。
使用[刷新和预热资源](refresh-and-prefetch-resources.md)功能，待刷新任务完成后，重新访问资源。
## 相关文档
[CDN](../use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)[加速](../use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)[OSS](../use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)[资源最佳实践](../use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)
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
