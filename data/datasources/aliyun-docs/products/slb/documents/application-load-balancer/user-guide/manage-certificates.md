# ALB配置证书-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/user-guide/manage-certificates

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/slb/documents/application-load-balancer/product-overview.md)

- [快速入门](products/slb/documents/application-load-balancer/getting-started.md)

- [操作指南](products/slb/documents/application-load-balancer/user-guide.md)

- [实践教程](products/slb/documents/application-load-balancer/use-cases.md)

- [开发参考](products/slb/documents/application-load-balancer/developer-reference.md)

- [服务支持](products/slb/documents/application-load-balancer/support.md)

[首页](https://help.aliyun.com/zh)

# 管理证书

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/slb)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在配置单向认证或双向认证业务时，您需要在阿里云证书中心购买证书，或者将所需的第三方签发的服务器证书和CA证书上传至阿里云证书中心，从证书中心获取该证书并使用。

## 背景信息

ALB支持单向认证和双向认证，请根据您的需要进行选择。

- 

单向认证：客户端需要认证服务端，而服务端不需要认证客户端。配置HTTPS监听和QUIC监听时，需要为监听绑定服务器证书。

- 

双向认证：客户端需要认证服务端，服务端也需要认证客户端，需要双方都通过认证，才能正常请求响应，以确保数据信息的安全。开启双向认证后，为监听绑定服务器证书的同时，还需要绑定CA证书来认证客户端。

## 使用限制

- 

基础版实例不支持双向认证。

- 

QUIC监听暂不支持双向认证。

- 

HTTP监听不支持单向认证和双向认证。

## 证书类型

ALB支持的证书类型包括国际标准证书（RSA/ECC）和国密证书（SM2）。

- 

国际标准证书：支持RSA和ECC算法，适用于通用HTTPS加密场景。

- 

国密证书：支持国密算法体系，包括 SM2（签名/密钥交换）、SM3（摘要）及 SM4（数据加密），适用于金融、政企及有等保三要求的行业客户。使用国密证书时，需要配合包含国密加密套件（ECC-SM2-WITH-SM4-SM3）的自定义TLS安全策略。

说明

- 

国密证书功能默认不开放，用户可前往[配额中心](https://quotas.console.aliyun.com/white-list-products/alb/quotas)自主申请权益配额。

- 

仅[ALB](products/slb/documents/product-overview/alb.md)[升级实例](products/slb/documents/product-overview/alb.md)支持国密证书，升级前的ALB实例不支持。可通过[ALB](products/slb/documents/application-load-balancer/use-cases/quickly-copy-alb-configurations-by-cloning-an-alb-instance.md)[实例克隆](products/slb/documents/application-load-balancer/use-cases/quickly-copy-alb-configurations-by-cloning-an-alb-instance.md)将存量ALB实例业务手动迁移至ALB升级实例。

- 

仅标准版和WAF增强版ALB实例支持国密证书，基础版、扩展版不支持。

- 

国密证书不支持双向认证（CA证书不支持SM2类型）。

不同监听类型、证书类型与认证方式的支持情况如下表所示：

| 监听类型 | 证书类型 | 证书认证方式 |  |
| --- | --- | --- | --- |
| 单向认证 | 双向认证 |  |  |
| HTTPS | RSA、ECC、SM2 单证书配置 | 支持 | 支持（RSA、ECC） 不支持（SM2） |
| RSA 和 ECC 双证书配置 | 支持 | 支持 |  |
| RSA 和 SM2 双证书配置 | 支持 | 不支持 |  |
| ECC 和 SM2 双证书配置 | 支持 | 不支持 |  |
| RSA、ECC、SM2 三证书混合配置 | 支持 | 不支持 |  |
| QUIC | RSA 和 ECC 单证书配置 | 支持 | 不支持 |
| RSA 和 ECC 双证书配置 | 支持 | 不支持 |  |
| HTTP | 不支持配置证书 |  |  |


## 证书匹配逻辑

当监听配置了多个证书时，ALB使用支持SNI的智能证书选择算法。如果客户端提供的主机名与证书列表中的单个证书匹配，则ALB将选择此证书。如果客户端提供的主机名与证书列表中的多个证书匹配，则ALB将按照以下优先级选择最佳证书：

- 

域名匹配：精确匹配优先于通配符匹配。

- 

公钥算法：ECDSA（ECC）优先于RSA。

- 

哈希算法：SHA系列优先于MD5。

- 

密钥长度：优先选择密钥长度最大的证书。

- 

有效期：优先选择有效时间最长的证书。

说明

ALB会根据客户端TLS握手时携带的协议版本识别是否使用国密协议（TLCP）。

- 

如果客户端使用TLCP协议，ALB优先选择国密证书。

- 

如果客户端使用标准TLS协议，ALB优先选择国际标准证书（RSA/ECC）。

## 前提条件

- 

您已[创建](products/slb/documents/application-load-balancer/user-guide/create-and-manage-alb-instances.md)[ALB](products/slb/documents/application-load-balancer/user-guide/create-and-manage-alb-instances.md)[实例](products/slb/documents/application-load-balancer/user-guide/create-and-manage-alb-instances.md)（标准版或WAF增强版）。

- 

您已[创建可用的后端服务器组](products/slb/documents/application-load-balancer/user-guide/create-and-manage-a-server-group.md)。

- 

您已在证书中心[购买](https://help.aliyun.com/zh/ssl-certificate/purchase-an-ssl-certificate#task-q3j-zfp-ydb)或[上传](https://help.aliyun.com/zh/ssl-certificate/upload-an-ssl-certificate)服务器证书。

- 

您已在证书中心[购买及启用子](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468)[CA](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468)[证书](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468)，且私有子CA的证书剩余数量不为0；或已[上传](https://help.aliyun.com/zh/ssl-certificate/manage-private-certificates-by-using-a-certificate-application-repository#section-7ga-7sy-cv7)自签名根CA或自签名子根CA证书至证书中心。

## 添加证书

- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。

- 

在顶部菜单栏处，选择实例所属的地域。

- 

在实例页面，找到目标实例，单击实例ID。

- 

选择以下一种方法，打开监听配置向导。

- 

在实例页面，在目标实例操作列单击创建监听。

- 

在实例页面，单击目标实例ID。在监听页签，单击创建监听。

- 

在配置监听配置向导，完成以下配置，然后单击下一步。

本文仅列举强相关参数，更多信息，请参见[添加](products/slb/documents/application-load-balancer/user-guide/add-an-https-listener.md)[HTTPS](products/slb/documents/application-load-balancer/user-guide/add-an-https-listener.md)[监听](products/slb/documents/application-load-balancer/user-guide/add-an-https-listener.md)。

- 

- 

| 监听配置 | 说明 |
| --- | --- |
| 选择监听协议 | 选择监听的协议类型。 您可以根据需要选择 HTTPS 或 QUIC 。 说明 QUIC 监听暂不支持双向认证。 HTTP 监听不支持单向认证和双向认证。 本文选择 HTTPS 。 |
| 监听端口 | 输入用来接收请求并向后端服务器进行请求转发的监听端口，端口范围为 1~65535。通常 HTTP 协议使用 80 端口，HTTPS 协议使用 443 端口。 本文输入 443 。 |
| 监听名称 | 输入自定义监听名称。 |
| 高级配置 | 单击 修改 展开高级配置。 |


- 

在配置SSL证书配置向导，选择一个服务器证书。

如果没有可选的服务器证书，您可以在下拉框中单击创建SSL证书进入证书中心，在证书中心[购买](https://help.aliyun.com/zh/ssl-certificate/purchase-an-ssl-certificate#task-q3j-zfp-ydb)或[上传](https://help.aliyun.com/zh/ssl-certificate/upload-an-ssl-certificate)服务器证书。

- 

可选：打开启用双向认证，选择CA证书来源。

- 

选择CA证书来源为阿里云签发，在选择默认CA证书下拉框中选择一个CA证书。

如果没有可选的CA证书，您可以在下拉框中单击购买CA证书，以[创建新](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468)[CA](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468)[证书](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468)。

- 

选择CA证书来源为非阿里云签发，在选择默认CA证书下拉框中选择一个CA证书。

如果没有可选的自签名CA证书，您可以在下拉框中单击上传自签CA证书，在证书应用仓库页面，创建数据来源为上传CA证书的仓库，然后通过证书应用仓库[上传](https://help.aliyun.com/zh/ssl-certificate/create-and-manage-a-certificate-application-repository)自签名根CA或自签名子根CA证书。

说明

- 

仅标准版和WAF增强版的ALB实例支持双向认证，基础版ALB实例不支持双向认证。

- 

开启双向认证后，如果您后续需要关闭双向认证，请参考以下步骤。

- 

在实例页面，单击目标实例ID。

- 

在监听页签，单击目标HTTPS协议监听ID。

- 

在监听详情页签，在SSL 证书区域关闭双向认证开关。

- 

选择TLS安全策略，然后单击下一步。

如果没有可选的TLS安全策略，您可以在下拉框中单击创建 TLS 安全策略。

[TLS](products/slb/documents/application-load-balancer/user-guide/tls-security-policies.md)[安全策略](products/slb/documents/application-load-balancer/user-guide/tls-security-policies.md)包含HTTPS可选的TLS协议版本和配套的加密算法套件。

- 

在选择服务器组配置向导，选择服务器组，查看后端服务器信息，然后单击下一步。

- 

在配置审核配置向导，确认配置信息，然后单击提交。

## 更多操作

- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。

- 

在顶部菜单栏处，选择实例所属的地域。

- 

在实例页面，找到目标实例，单击实例ID。

- 

单击监听页签，在目标监听操作列单击管理证书。

- 

在监听证书页签，您可以根据需要进行如下操作。

说明

为避免证书过期对您的服务产生影响，请在证书过期前更换证书。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 证书类别 | 操作 | 说明 |
| --- | --- | --- |
| 服务器证书 | 更换监听默认服务器证书 | 在 服务器证书 页签，找到监听默认服务器证书，在 操作 列单击 更换 。 在弹出的对话框，选择服务器证书，单击 确定 。 如果没有可选的服务器证书，您可以在下拉框中单击 创建 SSL 证书 进入证书中心，在证书中心 [购买](https://help.aliyun.com/zh/ssl-certificate/purchase-an-ssl-certificate#task-q3j-zfp-ydb) 或 [上传](https://help.aliyun.com/zh/ssl-certificate/upload-an-ssl-certificate) 服务器证书。 |
| 添加服务器扩展证书 | 您可以通过添加扩展证书增加监听关联的证书。 在 服务器证书 页签，单击 添加扩展证书 。 在 添加扩展证书 对话框中，选择服务器证书，然后单击 确定 。 如果没有可选的服务器证书，您可以在右上角单击 购买证书 进入证书中心，在证书中心 [购买](https://help.aliyun.com/zh/ssl-certificate/purchase-an-ssl-certificate#task-q3j-zfp-ydb) 或 [上传](https://help.aliyun.com/zh/ssl-certificate/upload-an-ssl-certificate) 服务器证书。 |  |
| 删除服务器扩展证书 | 您可以删除不需要的服务器扩展证书，删除后该证书将不再认证后端服务器。 在 服务器证书 页签，找到目标扩展证书，在 操作 列单击 删除 。 在弹出的对话框中，单击 确定删除 。 |  |
| CA 证书 | 开启或关闭双向认证 | 开启双向认证 ：如果您创建的监听从未开启过双向认证，您可以通过以下方式开启双向认证。 单击 CA 证书 页签，打开 双向认证 开关或单击 点此开启双向认证 。 在 启用双向认证 对话框中，根据业务选择以下任一步骤完成操作。 选择 CA 证书来源为 阿里云签发 ，在 选择默认 CA 证书 下拉框中选择一个 CA 证书，然后单击 确定 。 如果没有可选的 CA 证书，您可以在下拉框中单击 购买 CA 证书 ，以 [创建新](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468) [CA](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468) [证书](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468) 。 选择 CA 证书来源为 非阿里云签发 ，在 选择默认 CA 证书 下拉框中选择一个 CA 证书，然后单击 确定 。 如果没有可选的自签名 CA 证书，您可以在下拉框中单击 上传自签 CA 证书 ，在 证书应用仓库 页面，创建数据来源为 上传 CA 证书 的仓库，然后通过证书应用仓库 [上传](https://help.aliyun.com/zh/ssl-certificate/create-and-manage-a-certificate-application-repository) 自签名根 CA 或自签名子根 CA 证书。 关闭双向认证 ：如果您创建的监听开启过双向认证，您可以单击 CA 证书 页签，然后关闭 双向认证 开关，关闭后该监听只支持单向认证。 |
| 更换 CA 证书 | 单击 CA 证书 页签，找到监听默认 CA 证书，在 操作 列单击 更换 。 在 更换默认 CA 证书 对话框中，根据业务选择以下任一步骤完成操作。 选择 CA 证书来源为 阿里云签发 ，在 选择默认 CA 证书 下拉框中选择一个 CA 证书，然后单击 确定 。 如果没有可选的 CA 证书，您可以在下拉框中单击 购买 CA 证书 ，以 [创建新](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468) [CA](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468) [证书](https://help.aliyun.com/zh/ssl-certificate/purchase-and-enable-a-private-ca#task-2060468) 。 选择 CA 证书来源为 非阿里云签发 ，在 选择默认 CA 证书 下拉框中选择一个 CA 证书，然后单击 确定 。 如果没有可选的自签名 CA 证书，您可以在下拉框中单击 上传自签 CA 证书 ，在 证书应用仓库 页面，创建数据来源为 上传 CA 证书 的仓库，然后通过证书应用仓库 [上传](https://help.aliyun.com/zh/ssl-certificate/create-and-manage-a-certificate-application-repository) 自签名根 CA 或自签名子根 CA 证书。 |  |


## 相关文档

## 产品教程

- 

[配置全链路](products/slb/documents/application-load-balancer/use-cases/end-to-end-data-transfer-over-https.md)[HTTPS](products/slb/documents/application-load-balancer/use-cases/end-to-end-data-transfer-over-https.md)[访问实现加密通信](products/slb/documents/application-load-balancer/use-cases/end-to-end-data-transfer-over-https.md)：ALB提供全链路HTTPS加密功能，可以实现客户端到ALB、ALB到后端服务器之间的全链路加密通信，提升敏感业务的安全性。

- 

[单](products/slb/documents/application-load-balancer/use-cases/configure-an-alb-instance-to-serve-multiple-domain-names-over-https.md)[ALB](products/slb/documents/application-load-balancer/use-cases/configure-an-alb-instance-to-serve-multiple-domain-names-over-https.md)[实例配置多域名](products/slb/documents/application-load-balancer/use-cases/configure-an-alb-instance-to-serve-multiple-domain-names-over-https.md)[HTTPS](products/slb/documents/application-load-balancer/use-cases/configure-an-alb-instance-to-serve-multiple-domain-names-over-https.md)[网站](products/slb/documents/application-load-balancer/use-cases/configure-an-alb-instance-to-serve-multiple-domain-names-over-https.md)：当您需要将不同域名的HTTPS访问请求转发至不同的后端服务器时，您可以通过ALB的HTTPS监听绑定多个证书，并配置基于域名的转发规则，实现多域名HTTPS网站的访问。

- 

[使用](products/slb/documents/application-load-balancer/use-cases/configure-mutual-authentication-on-an-https-listener.md)[ALB](products/slb/documents/application-load-balancer/use-cases/configure-mutual-authentication-on-an-https-listener.md)[部署](products/slb/documents/application-load-balancer/use-cases/configure-mutual-authentication-on-an-https-listener.md)[HTTPS](products/slb/documents/application-load-balancer/use-cases/configure-mutual-authentication-on-an-https-listener.md)[业务（双向认证）](products/slb/documents/application-load-balancer/use-cases/configure-mutual-authentication-on-an-https-listener.md)：在需要高安全性验证的场景（如金融、医疗等）下，可通过ALB的HTTPS双向认证功能，实现客户端与服务器之间的相互身份验证，确保数据传输的安全性。

## API文档

- 

[CreateListener](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-createlistener.md)：创建HTTP、HTTPS或QUIC监听。

- 

[AssociateAdditionalCertificatesWithListener](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-associateadditionalcertificateswithlistener.md)：为HTTPS和QUIC监听添加扩展证书。

- 

[DissociateAdditionalCertificatesFromListener](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-dissociateadditionalcertificatesfromlistener.md)：从HTTPS和QUIC监听移除扩展证书。

- 

[UpdateListenerAttribute](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-updatelistenerattribute.md)：修改HTTPS和QUIC监听的默认证书配置（更换默认证书，是否开启双向认证等）。

[上一篇：HTTP头字段](products/slb/documents/application-load-balancer/user-guide/http-headers.md)[下一篇：TLS安全策略](products/slb/documents/application-load-balancer/user-guide/tls-security-policies.md)

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
