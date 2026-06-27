# CDN源站配置-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-an-origin-server

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

# 配置源站

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

阿里云CDN支持的源站类型包括OSS域名、IP、源站域名和函数计算域名，每种源站类型都支持配置多个源站地址，多源站场景下，支持设置源站的主备优先级和权重，实现负载均衡。

## 注意事项

CDN回源从源站获取资源时，源站产生的流量宽带费用由源站来缴纳，比如源站是客户的IDC中心，产生的就是IDC中心的流量带宽费用；如果源站是OSS，产生的就是OSS的流量费。

## 新增或修改源站信息

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击域名管理。

- 

在域名管理页面，找到目标域名，单击操作列的管理。

- 

在源站信息区域，根据业务需求，选择新增或修改源站配置。

- 

单击新增源站信息，可以增加源站。

- 

单击已有源站信息后面的编辑，可以修改已有源站配置。

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

- 

| 参数 | 说明 |
| --- | --- |
| 源站信息 | 选择源站的类型，并填写源站地址。 OSS 域名 在下拉列表中选择同一账号下 OSS 的外网域名作为源站。 手动输入阿里云 OSS 的外网域名作为源站（不支持 OSS 内网域名作为源站），例如： ***.oss-cn-hangzhou.aliyuncs.com ，OSS 外网域名可前往 [OSS](https://oss.console.aliyun.com/) [控制台](https://oss.console.aliyun.com/) 查看。 说明 关于加速 OSS 资源的实践，请参见 [CDN](products/cdn/documents/use-cases/use-alibaba-cloud-cdn-to-accelerate-the-delivery-of-resources-from-oss-buckets.md) [加速](products/cdn/documents/use-cases/use-alibaba-cloud-cdn-to-accelerate-the-delivery-of-resources-from-oss-buckets.md) [OSS](products/cdn/documents/use-cases/use-alibaba-cloud-cdn-to-accelerate-the-delivery-of-resources-from-oss-buckets.md) [资源](products/cdn/documents/use-cases/use-alibaba-cloud-cdn-to-accelerate-the-delivery-of-resources-from-oss-buckets.md) 。 阿里云 CDN 回源阿里云 OSS 的流量优惠说明： 用户需要在 CDN 控制台上把源站类型设置为“OSS 域名”，这样阿里云 OSS 产品会将来自阿里云 CDN 产品的回源流量识别为“ CDN 回源流出流量”，从而享受到更优惠的价格。 如果用户在 CDN 控制台上把源站类型误设为“源站域名”，阿里云 OSS 产品会将来自阿里云 CDN 产品的回源流量识别为“外网流出流量”，这种情况下就享受不到优惠价格。 详细的费用说明，请参见 [CDN](products/cdn/documents/product-overview/billing-of-oss-content-acceleration.md) [加速](products/cdn/documents/product-overview/billing-of-oss-content-acceleration.md) [OSS](products/cdn/documents/product-overview/billing-of-oss-content-acceleration.md) [计费说明](products/cdn/documents/product-overview/billing-of-oss-content-acceleration.md) 。 采用阿里云 OSS 作为源站时，必须要 [配置默认回源](products/cdn/documents/user-guide/configure-the-default-origin-host.md) [HOST](products/cdn/documents/user-guide/configure-the-default-origin-host.md) ，并且默认回源 HOST 的值为 OSS Bucket 的公网地址域名，否则会无法访问源站。 采用阿里云 OSS 作为源站时，建议 [配置默认回源](products/cdn/documents/user-guide/configure-sni.md) [SNI](products/cdn/documents/user-guide/configure-sni.md) ，并且默认回源 SNI 的值为 OSS Bucket 的公网地址域名，否则可能会被 OSS 限流。 IP 支持配置单个或者多个 IP 作为源站地址，不支持内网 IP，支持 IPv4 地址和 IPv6 地址，不能全部配置 IPv6 地址，必须至少配置一个 IPv4 地址，使用阿里云 ECS 的外网 IP 作为源站地址可免审核。如果要配置 IPv6 源站地址，您需要提前开启 IPv6 回源功能，如果没有提前开启，那么配置的 IPv6 源站地址将无法生效，这会导致回源失败。详细信息，请参见 [配置](products/cdn/documents/user-guide/configure-back-to-origin-routing-over-ipv6.md) [IPv6](products/cdn/documents/user-guide/configure-back-to-origin-routing-over-ipv6.md) [回源](products/cdn/documents/user-guide/configure-back-to-origin-routing-over-ipv6.md) 。 关于源站类型为 IP 的配置实践，敬请参见 [CDN](products/cdn/documents/use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md) [加速](products/cdn/documents/use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md) [ECS](products/cdn/documents/use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md) [资源](products/cdn/documents/use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md) 。 源站域名 ：支持配置域名作为源站地址，可配置多个域名。 说明 关于源站类型为域名的配置实践，敬请参见 [CDN](products/cdn/documents/use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md) [加速](products/cdn/documents/use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md) [ECS](products/cdn/documents/use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md) [资源](products/cdn/documents/use-cases/use-alibaba-cloud-cdn-to-accelerate-the-retrieval-of-resources-from-an-ecs-instance.md) 。 源站域名不能与加速域名相同。若加速域名和源站域名一致，会导致请求反复解析到 CDN 节点上，造成循环解析，使得 CDN 节点无法回源。 阿里云 CDN 当前支持直接将阿里云 ALB 产品的实例地址（例如： example.hangzhou.alb.aliyuncs.com ）添加为 CDN 的源站。 CDN+ALB 架构下，域名解析和源站的配置方法如下： 在 DNS 服务商处将加速域名 CNAME 解析到 CDN 分配的 CNAME 地址。CNAME 地址可在 CDN 控制台的域名管理页面获取。 在 CDN 控制台将源站类型设置为 源站域名 ，源站地址填写 ALB 实例的域名。 配置完成后，用户请求的访问链路为：客户端→CDN→ALB→后端服务器。域名不能直接解析到 ALB，否则 CDN 加速不会生效。 源站域名格式： 域名长度为 1~67 个字符。 支持：小写英文字母（a~z）、数字（0~9）和短划线（-），例如 example.com。 不支持：中文、英文大写字母（A~Z）和除了短划线（-）以外的其他符号，且短划线（-）不能连续出现、不能单独使用、不能出现在开头和结尾。如果域名包含中文（例如：阿里云.网址），请以中文形式进行相关备案，再通过第三方工具 punycode 将中文域名转换成为英文域名（例如：xn--fiq **.xn--eq **）后填入。 函数计算域名 ：支持将您在同一账号下的函数计算产品上配置的函数计算域名，配置为源站地址。您需要选择函数计算 区域 和 域名 。操作方法，请参见 [配置自定义域名](https://help.aliyun.com/zh/functioncompute/fc-2-0/user-guide/configure-a-custom-domain-name#multiTask145) 。 |
| 优先级 | 源站优先级支持设置主备，主优先级大于备优先级。用户请求通过阿里云 CDN 回源时，会优先回源到优先级为主的源站地址。主源站出现故障（CDN 节点和源站 TCP 连接失败）的情况下，将会回源到备源站。源站优先级的取值范围为 0~127，数值越小，优先级越高。主源站的优先级默认值为 20，备源站的优先级默认值为 30。如需配置其他值，请提交工单申请。 例如，有 A、B 两个源站，A 源站的优先级为主，B 源站的优先级为备，则用户请求通过阿里云 CDN 回源时会优先回源到 A 源站，如果 A 源站出现故障（CDN 节点和源站 TCP 连接失败），将会回源到 B 源站，当 A 源站恢复正常后会从 B 源站切换回 A 源站。 |
| 权重 | 当多个源站的优先级相同时，阿里云 CDN 会按照源站的权重分配用户请求回源到不同源站的比例，实现按权重的负载均衡。您可以根据业务需求，自行设置权重值。 取值范围：1~100，数值越大，源站分配到的用户请求比例越高。 默认值：10。 例如：有 A、B 两个源站，两个源站的优先级都是主，A 源站的权重为 80，B 源站的权重为 20，则用户请求将会按照 8:2 的比例在 A、B 两个源站之间分配。 说明 在某些情况下，用户实际请求回源到不同源站的比例并不一定会与域名配置中源站的权重比例相同，例如： 回源 QPS 较低（例如不到 10QPS），回源到不同源站的概率分布不太均匀，因此会出现实际回源权重与源站配置的权重不一致的情况。 所有的请求均来自于某个 IP 地址（或者有限的某几个 IP 地址），由于同一个 IP 地址将会被调度到同一个 CDN 节点，并且 CDN 节点与源站之间存在 TCP 会话保持，因此很可能会出现大部分请求都回源到同一个源站的情况。 如果您希望验证用户请求回源权重大致等同于域名配置中的源站权重，您可以使用第三方拨测工具来发起探测任务，配置地理位置分布尽可能广、运营商分布尽可能多的探测客户端，并且探测任务需要持续一段时间，以便采集到足够多的有效探测数据。 |
| 端口 | 表示 CDN 节点回到源站哪个端口请求资源。默认为 80，根据您源站的支持情况，可自定义设置回源端口，允许设置的端口范围为 1~65535。 默认值：80。 端口值为 443 时，以 HTTPS 协议回源；80 或其他自定义端口，以 HTTP 协议回源。 说明 如果需要以 HTTPS 协议回源到其他自定义端口，请参见 [配置回源协议](products/cdn/documents/user-guide/configure-the-origin-protocol-policy.md) 。 如果配置了 回源协议 功能（默认为关闭状态），这里配置的端口会失效。关闭回源协议的方法，请参见 [配置回源协议](products/cdn/documents/user-guide/configure-the-origin-protocol-policy.md) 。 当源站选择 OSS 域名时，回源端口是否支持自定义端口，取决于 OSS 产品。 |


- 

单击确定，完成配置。

## 回源重试、回源超时、源站探测相关说明

- 

回源重试顺序：

- 

对域名基础信息的源站地址列表内的源站地址按优先级从高到低进行重试。

- 

如果有优先级相同的源站地址，则按权重比例进行重试。

- 

回源重试的颗粒度：

- 

重试是IP地址级别的，如果源站是域名，将会对域名解析出的所有IP地址进行重试，只有域名下的所有IP都连接失败后才会访问其他可用源站。

- 

重试时系统会自动过滤dead table中不可用的源站。

- 

回源重试状态码：

- 

CDN节点在收到源站响应的5xx状态码的时候进行重试。

- 

回源超时时间：在源站主动响应重试状态码时，CDN节点收到重试状态码之后就会重试。如果没有收到源站主动响应的重试状态码，则会遵循回源超时时间处理逻辑，达到超时时间之后就会触发CDN节点重试。

- 

源站TCP建连超时：10秒。

- 

源站写超时：默认为30秒（源站建连后写入内容超时）。

- 

源站读超时：默认为30秒（源站建连后在一定时间内没有把CDN节点请求的内容完整响应回去）。

- 

源站写超时时间和源站读超时时间可以通过配置回源HTTP请求超时时间来调整。

- 

源站探测逻辑：

- 

TCP连接异常：如果CDN节点与源站IP地址之间连续两次出现TCP连接不可用（建连失败或连接超时），CDN会从可用源站地址列表中剔除该源站IP地址，并将该IP地址加入dead table中，这样后续的回源请求就不会去访问这个源站IP地址；此后CDN节点会每隔5秒使用TCP建连去探测一次该源站IP地址，如果建连成功，则将该源站IP地址恢复到可用源站地址列表中。

- 

TCP连接正常：如果CDN节点与源站IP地址之间TCP连接正常，但收到源站响应的重试状态码（例如：5xx），此时虽然会触发重试的逻辑，但该源站IP地址仍然还在可用源站地址列表中，下次访问还会按权重去请求该源站（即TCP四层连接正常的情况下，七层HTTP请求异常不会主动屏蔽源站IP地址，如果需要在七层HTTP请求异常的情况下主动屏蔽源站IP地址，则需要提交工单申请配置）。

## 相关文档

- 

什么是源站，请参见[源站](products/cdn/documents/product-overview/terms.md)。

- 

当您使用多个源站进行加速时，可以通过设置不同的回源HOST来指定CDN节点回源到不同的源站，请参见[配置默认回源](products/cdn/documents/user-guide/configure-the-default-origin-host.md)[HOST](products/cdn/documents/user-guide/configure-the-default-origin-host.md)。

- 

如果您需要自定义HTTP或HTTPS回源协议，请参见[配置回源协议](products/cdn/documents/user-guide/configure-the-origin-protocol-policy.md)。

- 

如果您的源站使用的是阿里云对象存储OSS，并且OSS的Bucket被配置为私有模式，需要给加速域名开启OSS私有Bucket回源功能，请参见[OSS](products/cdn/documents/user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[私有](products/cdn/documents/user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[Bucket](products/cdn/documents/user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[回源](products/cdn/documents/user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)。

- 

如果您的源站IP绑定了多个域名，且CDN回源协议为HTTPS时，需配置回源SNI，请参见[配置默认回源](products/cdn/documents/user-guide/configure-sni.md)[SNI](products/cdn/documents/user-guide/configure-sni.md)。

[上一篇：配置全球资源计划](products/cdn/documents/user-guide/configure-global-resource-planning.md)[下一篇：配置条件源站](products/cdn/documents/user-guide/configure-a-conditional-origin.md)

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
