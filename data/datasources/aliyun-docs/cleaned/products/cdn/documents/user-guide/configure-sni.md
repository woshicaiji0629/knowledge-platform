# 什么是SNI以及如何配置回源SNI-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-sni

# 配置默认回源SNI
如果您的源站IP绑定了多个域名，且回源协议为HTTPS时，需通过配置回源SNI指明所请求的具体域名，源站根据配置的SNI名称返回对应域名的SSL证书，以确保正常回源。
## 背景信息
SNI（Server Name Indication）是对SSL/TLS协议的扩展，允许服务器在单个IP地址上承载多个SSL证书，可解决一个HTTPS服务器拥有多个域名但是无法预知客户端到底请求的是哪一个域名的服务问题。开启SNI后，在CDN节点向源站发起TLS握手请求时，源站会根据TLS握手请求中携带的SNI信息来确认被请求的业务域名，返回正确的SSL证书给CDN节点。
重要
源站的服务端需要支持解析TLS握手请求中包含的SNI信息。
如果加速域名配置了多个源站，通过控制台配置SNI功能，所有源站地址会共用一个回源SNI值，那么回源请求都会指向SNI值对应的域名。如果您希望不同的源站，配置不同的SNI值，您可以[填写信息](https://page.aliyun.com/form/act2017566026/index.htm)申请。
回源SNI的工作原理如下图所示。
回源SNI的工作流程如下：
当CDN节点以HTTPS协议访问源站时，需要在SNI中指定访问的具体域名（如：example.com）。
源站接收到请求后，根据SNI中记录的域名，返回对应域名的证书（即example.com的证书）。
CDN节点收到证书，与服务器端建立安全连接。
重要
建议将[回源](configure-the-default-origin-host.md)[HOST](configure-the-default-origin-host.md)和回源SNI设置为相同的域名（通常为源站域名或加速域名）。回源HOST（HTTP Host头）和回源SNI（TLS握手阶段指定的域名）配置不一致时（例如回源HOST设为源站域名但SNI设为加速域名），可能导致SSL握手失败或源站返回错误。两者需在控制台分别配置，请确保匹配源站证书和虚拟主机配置。
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击回源配置。
在配置页签下找到默认回源SNI，单击修改配置。
在默认回源SNI对话框，打开回源SNI开关，输入您希望客户端从哪个域名获取资源（例如：example.com）。
说明
回源SNI配置的值只能是精确域名，不能是泛域名。
单击确定，完成配置。
## 相关文档
| 文档 | 描述 |
| --- | --- |
| [配置回源协议](configure-the-origin-protocol-policy.md) | 配置回源协议后，CDN 节点将根据指定的协议回源到源站的 80（HTTP）或 443（HTTPS）端口请求资源。 |
| [Common Name](common-name-whitelist.md) [白名单](common-name-whitelist.md) | 开启 Common Name 白名单功能后，CDN 节点以 HTTPS 协议与源站建连时，若请求的 SNI 信息和返回证书的 CommonName 不匹配时，如果证书的 Common Name 在白名单中，则可成功建联。 |
| [批量配置域名](../developer-reference/api-cdn-2018-05-10-batchsetcdndomainconfig.md) | 通过 API 配置回源 SNI。 |
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
