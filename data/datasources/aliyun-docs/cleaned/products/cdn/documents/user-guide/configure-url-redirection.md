# 通过强制跳转功能实现HTTP强制跳转HTTPS-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-url-redirection

# 配置协议重定向
您可以通过配置强制跳转HTTPS功能，将客户端到CDN节点的请求强制重定向为更安全的HTTPS请求。
## 前提条件
执行该操作前，请您确保已成功配置HTTPS证书，操作方法请参见[配置](configure-an-ssl-certificate.md)[HTTPS](configure-an-ssl-certificate.md)[证书](configure-an-ssl-certificate.md)。
## 适用场景
已经配置了HTTPS证书的加速域名，可配置强制跳转，默认通过301重定向方式，将客户端到CDN节点的HTTP请求强制跳转为HTTPS请求，HTTPS请求更安全。
$ curl http://xxx xxx xxx/' -i HTTP/1.1 301 Moved Permanently Server: Tengine Date: Mon, 03 Jun 2019 13:26:01 GMT Content-Type: text/html Content-Length: 278 Connection: keep-alive Location: https://xxx xxx xxx/ Via: cache2.cn201[,0] Timing-Allow-Origin: * EagleId: 2a786b0215595683612635433e &lt;!DOCTYPE HTML PUBLIC &quot;-//IETF//DTD HTML 2.0//EN&quot;&gt; <html> <head><title>301 Moved Permanently</title></head> <body bgcolor="white"> <h1>301 Moved Permanently</h1> <p>The requested resource has been assigned a new permanent URI.</p> &lt;hr/&gt;Powered by Tengine</body> </html>
强制跳转功能默认使用301重定向方式，同时也支持308重定向方式，如果您需要修改重定向方式，可以通过[填写信息](https://page.aliyun.com/form/act2017566026/index.htm)申请。
| 编码 | 含义 | 处理方法 | 典型应用场景 |
| --- | --- | --- | --- |
| 301 | Moved Permanently | GET 方法不会发生变更，其他方法有可能会变更为 GET 方法。 | 网站重构。 |
| 308 | Permanent Redirect | 方法和消息主体都不发生变化。 | 网站重构，用于非 GET 方法。(with non-GET links/operations) |
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击HTTPS配置。
在协议重定向区域，单击修改配置。
在协议重定向对话框，选择跳转类型。
| 跳转类型 | 说明 |
| --- | --- |
| 默认 | 同时支持 HTTP 和 HTTPS 方式的请求。 |
| HTTPS -> HTTP | 将客户端到 CDN 节点的请求强制重定向为 HTTP 方式。 警告 配置 HTTPS 强制跳转 HTTP 后，请勿同时 [配置](configure-hsts.md) [HSTS](configure-hsts.md) ，否则会造成请求重定向循环，从而导致资源无法访问。 |
| HTTP -> HTTPS | 将客户端到 CDN 节点的请求强制重定向为 HTTPS 方式，以确保访问安全。 |
单击确定，完成配置。
## 相关功能
协议强制重定向仅支持 HTTP 与 HTTPS 之间的协议级跳转。如果需要按地域、按 URL 路径等条件将请求重定向到其他网站或域名，请使用重写访问 URL 功能，并结合规则引擎设置匹配条件。
例如，通过规则引擎的「客户端 IP 归属地」条件，可将非中国内地的访问请求重定向到海外站点。
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
