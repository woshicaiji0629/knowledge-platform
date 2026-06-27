# 复制CDN加速域名配置并批量应用到其他加速域名-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/copy-configurations-to-domain-names

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

# 复制配置

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

如果您需要将一个域名的配置批量应用到其他域名，可以使用复制配置功能，使得不同域名的配置项保持一致，节约人工配置时间，如：使用多个域名加速同一个源站资源，要求源站信息配置相同，可使用该功能复制已有域名的源站信息配置到目标域名。

## 注意事项

- 

复制配置操作不可逆。请您务必确认域名配置复制正确。

- 

对于流量或带宽较大的域名，请您在复制配置时谨慎操作，以免带来经济损失。

- 

无法复制通过提交工单申请添加的后端特殊配置。

- 

使用批量配置功能时，一次最多可配置 20 个域名，并且域名个数乘以功能函数个数需小于等于 50。

- 

以下配置项不支持复制：HTTPS 证书、HTTP/2、OCSP Stapling、TLS 加密套件与协议版本。请在复制完成后前往目标域名的对应配置页面单独设置。

## 常见问题

### CDN 控制台复制域名配置时报错失败怎么办？

如果使用复制配置功能时遇到报错（超时或失败），请按以下步骤排查：

- 

尝试去掉部分勾选的功能（如页面优化、Gzip 压缩、过滤参数）后，再次执行复制操作。

- 

若去掉部分功能后复制成功，后续可以在域名管理中找到目标域名，逐一手动添加之前去掉的功能配置，不影响最终效果。

## 操作步骤

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击域名管理。

- 

在域名管理页面，选择您需要复制配置的域名，单击复制配置。

- 

选中您需要复制的配置项，单击下一步。

说明

- 

源站信息和基础信息（CNAME地址、业务类型、加速区域）无法同时复制。

- 

回源HTTP请求头和自定义HTTP响应头为增量复制。例如，您的A域名有2条回源头配置，您从B域名复制了5条内容，则A将有7条回源头配置。

- 

回源HTTP请求头（新）和回源HTTP响应头复制后，将覆盖原有配置。例如，您的A域名配置了cache_control为private，您的B域名配置为public，从B复制到A后，您的cache_control为public。

- 

开关类配置、Referer或IP黑白名单复制后，将覆盖域名原有配置。

在复制配置页面，第1步选择配置项：页面以表格形式列出可复制的配置项及其当前配置状态（例如源站信息为已设置、Range回源为开启、拖拽播放为未开启），勾选需要复制的配置项后单击下一步。

- 

选中您想要批量配置的目标域名，单击下一步。

您可以输入关键词查找域名。域名列表中最多允许选择50个目标域名，可通过搜索框按域名筛选。

- 

在复制配置对话框，单击确定。

[上一篇：域名管理](products/cdn/documents/user-guide/domain-name-management.md)[下一篇：域名迁移](products/cdn/documents/user-guide/domain-name-transfer-1.md)

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
