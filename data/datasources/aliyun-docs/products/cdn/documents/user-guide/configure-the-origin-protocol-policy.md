# 配置CDN节点以HTTPS协议回源-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-the-origin-protocol-policy

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/cdn/documents/product-overview.md)

- [快速入门](products/cdn/documents/getting-started.md)

- [操作指南](products/cdn/documents/user-guide.md)

- [实践教程](products/cdn/documents/use-cases.md)

- [安全合规](products/cdn/documents/security-and-compliance.md)

- [开发参考](products/cdn/documents/developer-reference.md)

- [服务支持](products/cdn/documents/support.md)

- [视频专区](products/cdn/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# 配置回源协议

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

回源协议指CDN节点回源站请求资源时使用的协议。配置该功能后，CDN节点将根据指定的协议回源到源站请求资源，同时支持自定义HTTP和HTTPS协议端口。

## 功能介绍

回源协议功能默认关闭，关闭状态下的回源协议以[配置源站](products/cdn/documents/user-guide/configure-an-origin-server.md)中设置的回源端口为准：

- 

回源端口设置为443：以HTTPS协议回源。

- 

回源端口设置为80或其他：以HTTP协议回源。

配置回源协议后，CDN节点将根据指定的协议请求资源：

- 

HTTP：CDN节点固定使用HTTP协议回源到源站。

- 

HTTPS：CDN节点固定使用HTTPS协议回源到源站。

- 

跟随：

- 

用户使用HTTP协议访问CDN，CDN节点使用HTTP协议回源到源站。

- 

用户使用HTTPS协议访问CDN，CDN节点使用HTTPS协议回源到源站。

说明

HTTPS主要是为了保证信息在传输过程中不被改写或记录，HTTPS协议的加密处理需要额外消耗源站服务器的处理器资源。如果您仅需要对敏感数据（例如：用户身份验证数据）采用HTTPS协议传输，而对非敏感数据（例如：图片）采用HTTP协议传输，建议您配置回源协议为跟随。

回源Host与回源SNI关联说明：

当您将回源协议配置为HTTPS时，建议同时检查默认回源HOST和回源SNI的配置。在源站存在多域名监听的场景下（如源站一台服务器上部署了多个HTTPS站点），CDN节点发起HTTPS回源请求时需要正确的Host头部和SNI值来路由到目标站点：

- 

回源HOST：决定CDN回源时HTTP请求中的Host头部值。在默认回源HOST区域配置，可选加速域名、源站域名或自定义域名。

- 

回源SNI：决定CDN回源时TLS握手中发送的服务器名称指示（Server Name Indication）。在回源SNI区域配置，开启回源SNI开关后填写SNI值。

说明

建议：配置HTTPS回源（特别是443端口）时，将回源HOST和回源SNI均设置为加速域名或源站域名。如果两者配置不正确，可能导致Bad Request、502错误或回源失败。

## 操作步骤

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击域名管理。

- 

在域名管理页面，找到目标域名，单击操作列的管理。

- 

在指定域名的左侧导航栏，单击回源配置。

- 

在回源协议区域，打开回源协议开关。

- 

在静态协议跟随回源对话框，选择回源协议类型为：跟随、HTTP或HTTPS。

说明

- 

HTTP协议回源时，默认使用80端口，您可以通过配置HTTP端口自定义HTTP回源时使用的端口。

- 

HTTPS协议回源时，默认使用443端口，您可以通过配置HTTPS端口自定义HTTPS回源时使用的端口。

自定义回源端口使用说明：

- 

端口范围：HTTP端口和HTTPS端口的取值范围均为 1-65535。

- 

客户端访问端口限制：CDN客户端访问仅支持标准端口（HTTP 80和HTTPS 443），不支持通过非标准端口（如8080、60080等）直接访问CDN加速域名。自定义回源端口仅用于CDN节点与源站之间的回源连接。

- 

配置场景：当源站使用非标准端口监听HTTP或HTTPS服务时（如源站使用8150、60080等端口），您需要：

- 

在回源协议区域开启开关。

- 

将跳转类型设置为HTTP或HTTPS（与源站实际监听的协议一致）。

- 

在对应的端口输入框中填写源站实际监听的自定义端口号。

- 

注意事项：回源协议必须与源站实际监听的协议保持一致。例如，源站未配置HTTPS证书但CDN配置HTTPS回源，会导致连接失败。请确保源站在您配置的端口上监听了对应协议的请求。

- 

单击确定。

## 常见问题

### 配置HTTPS回源后访问报错502

问题现象：CDN加速后访问网站返回502错误。

可能原因：源站仅支持HTTP协议（未配置SSL证书或未开启HTTPS监听），但CDN回源协议配置为HTTPS，导致CDN节点尝试建立HTTPS连接时源站拒绝。

解决方法：

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)，在左侧导航栏单击域名管理。

- 

找到目标域名，单击管理。

- 

在左侧导航栏选择回源配置。

- 

在回源协议区域，单击修改配置。

- 

将跳转类型改为HTTP，HTTP端口保持默认的80（或源站实际监听的自定义端口），单击确定。

- 

如果缓存了502响应，建议执行URL刷新操作清除缓存。

### 配置HTTP回源时出现301重定向循环

问题现象：CDN加速后部分图片或资源无法加载，浏览器F12控制台显示301重定向报错。

可能原因：源站配置了HTTP到HTTPS的强制跳转（如宝塔面板或WAF配置了301重定向），而CDN使用HTTP协议回源到默认80端口，源站返回301跳转到HTTPS，CDN缓存该301响应后导致重定向循环。

解决方法：

- 

将回源端口改为443，回源协议改为HTTPS：

- 

在协议跟随回源区域，单击修改配置。

- 

将跳转类型改为HTTPS，HTTPS端口为443，单击确定。

- 

配置状态码缓存规则，忽略301和302响应：

- 

在左侧导航栏选择缓存配置。

- 

配置根目录缓存规则，设置/ 301=0, 302=0（缓存时间为0，即不缓存）。

- 

执行目录刷新操作，清除边缘节点已缓存的异常301响应：

- 

在左侧导航栏选择刷新预热。

- 

刷新类型选择目录刷新，输入http://您的加速域名/（注意提交地址前后不要有空格），单击提交。

说明

如果您使用的是宝塔面板等建站工具，源站无需开启强制HTTPS访问，只需确保CDN回源协议与源站监听协议一致即可。

### CDN回源404但源站正常

问题现象：通过CDN访问资源返回404，但直接访问源站正常。

可能原因：

- 

源站仅开启80端口未开启443端口，但CDN回源协议配置为HTTPS。

- 

回源HOST未正确设置（源站为域名时需将回源HOST修改为源站域名）。

- 

旧缓存未清除。

解决方法：

- 

确认源站监听的协议和端口。如果源站仅支持HTTP 80端口，需将回源协议改为HTTP，端口为80。

- 

如果源站为域名，需配置回源HOST：

- 

在默认回源HOST区域，单击修改配置。

- 

打开回源HOST开关，域名类型选择源站域名，从源站列表中选择对应的域名。

- 

执行目录刷新操作清除旧缓存。

### 配置回源协议为HTTPS时，源站是否也需要配置SSL证书？

是的，取决于您的回源方式：

- 

HTTPS回源（443端口或其他HTTPS端口）：CDN节点通过HTTPS协议连接源站，会校验源站的SSL证书。此时源站必须配置有效的SSL证书，否则回源连接失败。

- 

HTTP回源（80端口或其他HTTP端口）：CDN节点通过HTTP协议连接源站，不会校验源站证书。此时源站无需配置SSL证书，您只需维护CDN侧加速域名的证书即可。

说明

建议：如果您仅需要在客户端到CDN节点之间使用HTTPS加密，而源站到CDN节点之间的网络可信，可将回源协议改为HTTP，这样只需维护CDN侧证书，简化源站管理。

### 配置回源协议为"跟随"时，如果源站不支持HTTPS会导致访问失败，如何处理？

问题说明：选择跟随模式时，CDN回源协议与客户端访问协议一致——客户端使用HTTP访问时CDN以HTTP回源，客户端使用HTTPS访问时CDN以HTTPS回源。如果您的源站不支持HTTPS，当客户端通过HTTPS访问CDN时，CDN尝试以HTTPS回源将导致连接失败。

解决方法：

- 

方案一：将回源协议从跟随改为HTTP。

- 

在回源协议区域，单击修改配置。

- 

将跳转类型改为HTTP，单击确定。

- 

这样无论客户端使用何种协议访问，CDN均以HTTP协议回源。

- 

方案二：为源站配置HTTPS证书，使源站支持HTTPS访问。

## 相关文档

- 

[批量配置域名](products/cdn/documents/developer-reference/api-cdn-2018-05-10-batchsetcdndomainconfig.md)

[上一篇：重写回源请求](products/cdn/documents/user-guide/rewrite-origin-requests.md)[下一篇：重写回源路径](products/cdn/documents/user-guide/rewrite-urls-in-back-to-origin-requests.md)

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
