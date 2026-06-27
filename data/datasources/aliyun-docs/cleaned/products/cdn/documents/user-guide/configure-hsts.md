# 配置HSTS强制使用HTTPS-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-hsts

# 配置HSTS
通过开启HSTS（HTTP Strict Transport Security）功能，您可以强制客户端（例如：浏览器）使用HTTPS与CDN节点创建连接，提高安全性。
## 前提条件
执行该操作前，请您确保已成功配置HTTPS证书，操作方法请参见[配置](configure-an-ssl-certificate.md)[HTTPS](configure-an-ssl-certificate.md)[证书](configure-an-ssl-certificate.md)。
## 背景信息
HSTS（HTTP Strict Transport Security，HTTP 严格传输安全），是一种网站用来声明他们只能使用安全连接（HTTPS）访问的方法。
配置HSTS后，客户端第一次使用HTTPS与CDN节点连接时，CDN节点通过使用响应头来告知客户端后续一段时间内访问时只能使用HTTPS访问，并阻止HTTP请求，HSTS响应头结构为：Strict-Transport-Security:max-age=expireTime [;includeSubDomains] [;preload]，参数说明如下表所示。
| 参数 | 说明 |
| --- | --- |
| max-age | HSTS Header 的过期时间，单位为秒，客户端在此时间段内强制使用 HTTPS 访问。 |
| includeSubDomains | 可选参数。如果包含这个参数，说明该域名及其所有子域名均开启 HSTS。 |
| preload | 可选参数。当您申请将域名加入到浏览器内置列表时需要使用 preload 列表。 |
客户端会记录域名在max-age到期前强制执行HSTS策略，客户端发起HTTP请求时将被强制转换为HTTPS请求，HTTP请求将被阻止。
说明
配置HSTS后，如果客户端第一次访问时使用HTTP，此时由于HSTS策略未同步至客户端，CDN节点会将该HTTP请求301重定向到HTTPS，从而避免此安全隐患。
## 约束限制
配置HSTS后，客户端只能使用HTTPS协议访问CDN节点，请勿同时配置HTTPS强制跳转HTTP。
HSTS策略仅对域名有效，对IP无效。
由于HSTS策略在客户端生效，关闭HSTS后无法立即生效，需要执行刷新使HSTS策略在客户端下一次HTTPS请求时下发给客户端。
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击HTTPS配置。
在HSTS区域，单击修改配置。
在HSTS设置对话框，打开HSTS开关，同时配置过期时间和包含子域名。
过期时间：HSTS响应头在浏览器的缓存时间，建议填入60天。配置为0时，HSTS关闭。
包含子域名：请谨慎开启，开启前，请确保该加速域名的所有子域名都已开启HTTPS，否则会导致子域名自动跳转到HTTPS后无法访问。
单击确定。
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
