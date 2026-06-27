# TLS安全策略-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/user-guide/tls-security-policies

# TLS安全策略
为ALB配置HTTPS监听时，TLS安全策略决定了ALB与客户端进行TLS协商时支持的TLS协议版本和加密算法套件。ALB预置了部分常用的系统默认策略供用户直接选择。对于有定制安全策略的特定需求场景，可以使用自定义TLS安全策略。
## 工作原理
TLS安全策略配置在ALB侧，用于定义其在TLS协商中支持的TLS协议版本和加密算法套件。在握手过程中，客户端通过Client Hello发送支持的协议版本和加密套件列表，ALB根据策略从列表中选择双方都支持的协议版本和加密套件组合并以Server Hello响应，后续步骤（如密钥交换、会话密钥生成）均基于此方案进行。
## 系统默认策略
各类信息安全标准可能对ALB的TLS安全策略提出要求，用户可展开下表查看系统默认策略支持的TLS协议版本和加密算法套件，并按需配置。如系统默认策略无法满足需求，可创建[自定义策略](tls-security-policies.md)。
策略详情
| 策略名称 | tls_cipher_policy_1_0 | tls_cipher_policy_1_1 | tls_cipher_policy_1_2 | tls_cipher_policy_1_2_strict | tls_cipher_policy_1_2_strict_with_1_3 | tls_cipher_policy_1_0_to_1_3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TLS 协议版本 | v1.0 | 支持 | 不支持 | 不支持 | 不支持 | 不支持 | 支持 |
| v1.1 | 支持 | 支持 | 不支持 | 不支持 | 不支持 | 支持 |  |
| v1.2 | 支持 | 支持 | 支持 | 支持 | 支持 | 支持 |  |
| v1.3 | 不支持 | 不支持 | 不支持 | 不支持 | 支持 | 支持 |  |
| 加密算法套件 | ECDHE-ECDSA-AES128-GCM-SHA256 | 支持 | 支持 | 支持 | 支持 | 支持 | 支持 |
| ECDHE-ECDSA-AES256-GCM-SHA384 | 支持 | 支持 | 支持 | 支持 | 支持 | 支持 |  |
| ECDHE-ECDSA-AES128-SHA256 | 支持 | 支持 | 支持 | 支持 | 支持 | 不支持 |  |
| ECDHE-ECDSA-AES256-SHA384 | 支持 | 支持 | 支持 | 支持 | 支持 | 不支持 |  |
| ECDHE-RSA-AES128-GCM-SHA256 | 支持 | 支持 | 支持 | 支持 | 支持 | 支持 |  |
| ECDHE-RSA-AES256-GCM-SHA384 | 支持 | 支持 | 支持 | 支持 | 支持 | 支持 |  |
| ECDHE-RSA-AES128-SHA256 | 支持 | 支持 | 支持 | 支持 | 支持 | 不支持 |  |
| ECDHE-RSA-AES256-SHA384 | 支持 | 支持 | 支持 | 支持 | 支持 | 不支持 |  |
| AES128-GCM-SHA256 | 支持 | 支持 | 支持 | 不支持 | 不支持 | 不支持 |  |
| AES256-GCM-SHA384 | 支持 | 支持 | 支持 | 不支持 | 不支持 | 不支持 |  |
| AES128-SHA256 | 支持 | 支持 | 支持 | 不支持 | 不支持 | 不支持 |  |
| AES256-SHA256 | 支持 | 支持 | 支持 | 不支持 | 不支持 | 不支持 |  |
| ECDHE-ECDSA-AES128-SHA | 支持 | 支持 | 支持 | 支持 | 支持 | 不支持 |  |
| ECDHE-ECDSA-AES256-SHA | 支持 | 支持 | 支持 | 支持 | 支持 | 不支持 |  |
| ECDHE-RSA-AES128-SHA | 支持 | 支持 | 支持 | 支持 | 支持 | 不支持 |  |
| ECDHE-RSA-AES256-SHA | 支持 | 支持 | 支持 | 支持 | 支持 | 不支持 |  |
| AES128-SHA | 支持 | 支持 | 支持 | 不支持 | 不支持 | 不支持 |  |
| AES256-SHA | 支持 | 支持 | 支持 | 不支持 | 不支持 | 不支持 |  |
| DES-CBC3-SHA | 支持 | 支持 | 支持 | 不支持 | 不支持 | 不支持 |  |
| TLS_AES_128_GCM_SHA256 | 不支持 | 不支持 | 不支持 | 不支持 | 支持 | 支持 |  |
| TLS_AES_256_GCM_SHA384 | 不支持 | 不支持 | 不支持 | 不支持 | 支持 | 支持 |  |
| TLS_CHACHA20_POLY1305_SHA256 | 不支持 | 不支持 | 不支持 | 不支持 | 支持 | 支持 |  |
| TLS_AES_128_CCM_SHA256 | 不支持 | 不支持 | 不支持 | 不支持 | 支持 | 支持 |  |
| TLS_AES_128_CCM_8_SHA256 | 不支持 | 不支持 | 不支持 | 不支持 | 支持 | 支持 |  |
| ECDHE-ECDSA-CHACHA20-POLY1305 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 |  |
| ECDHE-RSA-CHACHA20-POLY1305 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 |  |
扩展版ALB实例仅支持tls_cipher_policy_1_0_to_1_3，且其他版本实例不支持该策略。
对于面向公网且无特殊兼容性要求的应用，建议使用tls_cipher_policy_1_2及以上策略。
## 控制台
前往ALB控制台的[TLS](https://slb.console.aliyun.com/alb/cn-hangzhou/tls)[安全策略](https://slb.console.aliyun.com/alb/cn-hangzhou/tls)页面，在系统默认策略页签查看策略的详细信息。
## API
调用[ListSystemSecurityPolicies](../developer-reference/api-alb-2020-06-16-listsystemsecuritypolicies.md)接口查询系统默认策略。
## 自定义策略
仅标准版和WAF增强版ALB实例支持自定义策略；基础版和扩展版ALB实例不支持。
### 创建自定义策略
## 控制台
前往ALB控制台的[TLS](https://slb.console.aliyun.com/alb/cn-hangzhou/tls)[安全策略](https://slb.console.aliyun.com/alb/cn-hangzhou/tls)页面，选择ALB实例所在地域。
单击创建自定义策略，参考以下信息进行配置，配置完成后单击创建。
选择最低版本：如业务无特殊兼容性要求，建议选择TLS 1.2及以上保障安全性。
启用TLS 1.3版本：为保障网络通信的安全性与效率，建议在业务兼容的前提下启用。
选择加密算法套件：需要与TLS协议版本匹配。
创建完成后，即可在[为监听配置](tls-security-policies.md)[TLS](tls-security-policies.md)[安全策略](tls-security-policies.md)中选择该自定义策略。
## API
调用[CreateSecurityPolicy](../developer-reference/api-alb-2020-06-16-createsecuritypolicy.md)创建自定义策略。注意自定义策略的地域必须与ALB实例的地域保持一致。
如需使用国密证书实现HTTPS加密通信，请在创建自定义策略时选择国密加密套件（ECC-SM2-WITH-SM4-SM3），详见[ALB](../use-cases/configure-gm-https-for-alb.md)[配置国密](../use-cases/configure-gm-https-for-alb.md)[HTTPS](../use-cases/configure-gm-https-for-alb.md)[实现安全通信](../use-cases/configure-gm-https-for-alb.md)。
### 更新自定义策略的TLS协议版本和加密算法套件
## 控制台
前往ALB控制台的[TLS](https://slb.console.aliyun.com/alb/cn-hangzhou/tls)[安全策略](https://slb.console.aliyun.com/alb/cn-hangzhou/tls)页面，选择自定义策略的地域。
找到目标自定义策略，单击操作列的编辑，在编辑 TLS 安全策略对话框更新TLS协议版本和加密算法套件。
## API
调用[UpdateSecurityPolicyAttribute](../developer-reference/api-alb-2020-06-16-updatesecuritypolicyattribute.md)更新自定义策略属性。
### 复制自定义策略到其他地域
## 控制台
前往ALB控制台的[TLS](https://slb.console.aliyun.com/alb/cn-hangzhou/tls)[安全策略](https://slb.console.aliyun.com/alb/cn-hangzhou/tls)页面，选择自定义策略的地域。
找到目标自定义策略，单击操作列的复制到其他地域，选择目标地域并确定。
## API
调用[ListSecurityPolicies](../developer-reference/api-alb-2020-06-16-listsecuritypolicies.md)获取自定义策略的TLSVersions和Ciphers等参数，在调用[CreateSecurityPolicy](../developer-reference/api-alb-2020-06-16-createsecuritypolicy.md)创建自定义策略时传入。
### 删除自定义策略
若自定义策略已被监听使用，请先修改监听的TLS安全策略或删除监听，方可删除自定义策略。
## 控制台
前往ALB控制台的[TLS](https://slb.console.aliyun.com/alb/cn-hangzhou/tls)[安全策略](https://slb.console.aliyun.com/alb/cn-hangzhou/tls)页面，选择自定义策略的地域。
找到目标自定义策略，单击操作列的删除并确定。
## API
调用[DeleteSecurityPolicy](../developer-reference/api-alb-2020-06-16-deletesecuritypolicy.md)删除自定义策略。
## 为监听配置TLS安全策略
扩展版ALB实例暂时仅支持选择系统默认策略tls_cipher_policy_1_0_to_1_3。
## 控制台
[创建](add-an-https-listener.md)[HTTPS](add-an-https-listener.md)[监听](add-an-https-listener.md)时，在配置SSL证书页签选择TLS安全策略；[快速创建](add-an-https-listener.md)[HTTPS](add-an-https-listener.md)[监听](add-an-https-listener.md)时，在快速创建监听对话框中选择TLS安全策略。
[修改](../../manage-listeners.md)[TLS](../../manage-listeners.md)[安全策略](../../manage-listeners.md)：在实例详情页的监听页签，单击目标HTTPS监听ID进入监听详情页，在SSL 证书区域修改TLS安全策略。
## API
调用[CreateListener](../developer-reference/api-alb-2020-06-16-createlistener.md)创建HTTPS监听或调用[UpdateListenerAttribute](../developer-reference/api-alb-2020-06-16-updatelistenerattribute.md)更新HTTPS监听配置时，SecurityPolicyId字段传入TLS安全策略。
可调用[ListSystemSecurityPolicies](../developer-reference/api-alb-2020-06-16-listsystemsecuritypolicies.md)查询系统默认策略的SecurityPolicyId。
可调用[ListSecurityPolicies](../developer-reference/api-alb-2020-06-16-listsecuritypolicies.md)查询自定义策略的SecurityPolicyId。
## 计费说明
TLS安全策略不产生费用，但您需要为ALB实例本身[付费](../product-overview/alb-billing-rules.md)。
## 应用于生产环境
后端流量安全：为确保端到端安全，建议将ALB和后端服务器部署在同一 VPC 内，并通过安全组等策略严格限制访问。
TLS协议版本：如应用无特殊兼容性要求，建议使用TLS 1.2和TLS 1.3保障安全性。
变更回滚：调整TLS安全策略后，若出现异常，可立即通过修改监听配置回滚。建议在业务低峰期进行变更。
密钥交换算法：如应用无特殊兼容性要求，生产环境不建议使用以下RSA密钥交换算法套件：AES128-GCM-SHA256、AES256-GCM-SHA384、AES128-SHA256、AES256-SHA256、AES128-SHA、AES256-SHA、DES-CBC3-SHA。此类套件不支持前向保密（PFS），且存在侧信道攻击风险。建议优先选择包含ECDHE或DHE密钥交换的套件。
## 配置TLS安全策略后仍提示不安全的排查
配置了较高版本的TLS安全策略（如tls_cipher_policy_1_2_strict_with_1_3）后，客户端访问站点时仍可能提示证书不安全或连接不安全。此时可从以下方面排查。
客户端或浏览器不兼容所选TLS版本：部分旧版浏览器或操作系统不支持TLS 1.2及以上版本，会导致握手失败并提示不安全。建议使用最新版Chrome或Firefox等主流浏览器进行测试，排除客户端兼容性问题。macOS上的Safari在某些版本中对TLS 1.3的支持存在差异，可切换到Chrome验证。
证书过期或域名不匹配：TLS安全策略仅控制协议版本和加密套件的协商，不影响证书本身的有效性。若证书已过期、或证书中的域名与实际访问域名不一致，浏览器同样会提示不安全。请检查ALB监听绑定的证书是否在有效期内，且证书的CN或SAN字段覆盖了当前访问的域名。
客户端缓存了旧的TLS连接信息：浏览器可能缓存了之前使用低版本TLS协议建立的会话信息，导致短期内仍显示旧的安全状态。可清除浏览器缓存和SSL状态后重新访问，或使用无痕模式打开页面进行验证。
使用在线检测工具验证实际协商结果：通过SSL Labs（https://www.ssllabs.com/ssltest/）等在线检测工具扫描站点域名，可查看ALB实际支持的TLS协议版本、加密套件及证书链信息，确认策略是否已正确生效。
## TLS加密算法套件名称对照表
下表提供了各加密算法套件在OpenSSL格式、IANA标准格式和十六进制之间的对照关系。
对照表详情
| OpenSSL 格式 | IANA 标准格式 | 十六进制 |
| --- | --- | --- |
| ECDHE-ECDSA-AES128-GCM-SHA256 | TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 | 0xC02B |
| ECDHE-ECDSA-AES256-GCM-SHA384 | TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 | 0xC02C |
| ECDHE-ECDSA-AES128-SHA256 | TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 | 0xC023 |
| ECDHE-ECDSA-AES256-SHA384 | TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384 | 0xC024 |
| ECDHE-RSA-AES128-GCM-SHA256 | TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 | 0xC02F |
| ECDHE-RSA-AES256-GCM-SHA384 | TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 | 0xC030 |
| ECDHE-RSA-AES128-SHA256 | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 | 0xC027 |
| ECDHE-RSA-AES256-SHA384 | TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 | 0xC028 |
| AES128-GCM-SHA256 | TLS_RSA_WITH_AES_128_GCM_SHA256 | 0x009C |
| AES256-GCM-SHA384 | TLS_RSA_WITH_AES_256_GCM_SHA384 | 0x009D |
| AES128-SHA256 | TLS_RSA_WITH_AES_128_CBC_SHA256 | 0x003C |
| AES256-SHA256 | TLS_RSA_WITH_AES_256_CBC_SHA256 | 0x003D |
| ECDHE-ECDSA-AES128-SHA | TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA | 0xC009 |
| ECDHE-ECDSA-AES256-SHA | TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA | 0xC00A |
| ECDHE-RSA-AES128-SHA | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA | 0xC013 |
| ECDHE-RSA-AES256-SHA | TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA | 0xC014 |
| AES128-SHA | TLS_RSA_WITH_AES_128_CBC_SHA | 0x002F |
| AES256-SHA | TLS_RSA_WITH_AES_256_CBC_SHA | 0x0035 |
| DES-CBC3-SHA | TLS_RSA_WITH_3DES_EDE_CBC_SHA | 0x000A |
| TLS_AES_256_GCM_SHA384 | TLS_AES_256_GCM_SHA384 | 0x1302 |
| TLS_CHACHA20_POLY1305_SHA256 | TLS_CHACHA20_POLY1305_SHA256 | 0x1303 |
| TLS_AES_128_CCM_SHA256 | TLS_AES_128_CCM_SHA256 | 0x1304 |
| TLS_AES_128_CCM_8_SHA256 | TLS_AES_128_CCM_8_SHA256 | 0x1305 |
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
