# CDN概览页-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/cdn-overview-dashboard

# CDN概览页
概览页提供了新手配置向导、访问数据、状态码和计费方式四个常用功能面板。
## 新手指引向导
说明
当域名管理中的域名数量超过30个之后，该模块会自动隐藏。
### 账户域名看板
按照正常运行、已停止和配置中三种分类，展示该账号中三种状态的域名数量和总域名数量。
### 【正在运行】域名看板
在所有正在运行状态的域名中，以CNAME、缓存过期时间、SSL证书三个配置为维度，统计每个配置未配置和已配置的数量。鼠标悬浮于统计数字上时，会显示对应配置状态的域名。
| 配置项 | 是否为必要配置 | 说明 |
| --- | --- | --- |
| CNAME | 必配 | [CNAME](../getting-started/quick-access-to-alibaba-cloud-cdn.md) 是一种 DNS 记录类型，在阿里云 CDN 中是保证加速域名正常运行的必要配置。 |
| 缓存过期时间 | 推荐 | [缓存过期时间](configure-the-cdn-cache-expiration-time.md) 指源站资源在阿里云 CDN 节点缓存的时长，达到预设时间，资源将会被节点标记为失效资源。合理的配置缓存过期时间可以提高阿里云 CDN 的缓存命中率，提升用户体验。 |
| SSL 证书 | 推荐 | [SSL](configure-an-ssl-certificate.md) [证书](configure-an-ssl-certificate.md) 是可以实现客户端与阿里云 CDN 节点之间的数据加密，使加速域名可以使用 HTTPS 协议访问。 |
## 访问数据
该模块按照不同时间维度（如今天、昨天、近七天等），展示账号下所有加速域名的带宽、流量和请求数的数据统计。
点击时间维度的>按钮，即可在[用量查询](query-resource-usage-1.md)页面中查询单个加速域名的数据或者自定义时间内更详细的访问数据。
## 状态码
该模块按照不同时间维度（如今天、昨天、近七天等），展示客户端收到的HTTP状态码统计数据，包括2xx成功、4xx 客户端错误和5xx 服务器错误的响应数量及占比。
例如，4xx 客户端错误边缘响应的占比为4xx 客户端错误边缘响应数量占边缘总响应数量的比例。
点击时间维度的>按钮，即可在[资源监控](resource-monitoring.md)页面中查询单个加速域名的数据或者自定义时间内更详细的HTTPCODE数据。
2xx成功-边缘响应：表示客户端访问阿里云CDN节点时，请求已被服务器成功处理，并返回了相应的资源或确认信息。
4xx 客户端错误-边缘响应：表示客户端访问阿里云CDN节点时，由于客户端发送的请求有问题（例如，权限不足），阿里云CDN节点无法处理，请修改客户端请求内容后重新发送。
4xx 客户端错误-回源响应：表示阿里云CDN节点访问源站时，由于阿里云CDN节点发送的请求有问题（例如，请求的资源不存在），源站服务器无法处理，请修改客户端请求内容或调整CDN域名配置后重新发送。
5xx 服务器错误-边缘响应：表示客户端访问阿里云CDN节点时，阿里云CDN节点的服务器出现了内部错误（例如，阿里云CDN节点负载过高），请检查源站配置（例如，源站的网络设置）。
5xx 服务器错误-回源响应：表示阿里云CDN节点访问源站时，源站服务器出现了内部错误（例如：源站服务器负载过高），请检查源站配置（例如，源站的服务器负载）。
## 计费方式
### 计费方式展示
该模块显示当前账号阿里云CDN[基础服务计费](../product-overview/billing-rules-of-basic-services.md)（流量）和[静态](../product-overview/billing-of-https-requests-for-static-content.md)[HTTPS](../product-overview/billing-of-https-requests-for-static-content.md)[请求数](../product-overview/billing-of-https-requests-for-static-content.md)的计费方式。
基础服务计费（流量）默认采用按流量计费模式，如果自身业务场景需要更换计费方式，点击变更按钮可以[变更计费方式](../product-overview/change-the-metering-method.md)；静态HTTPS请求数的计费方式为按流量计费，小时出账，且计费方式无法更改。
### 资源包信息
重要
当基础服务计费（流量）的计费方式为按流量计费时，才会展示资源包详细的使用信息。
当基础服务计费（流量）的计费方式为非按流量计费时，即使购买了资源包，也不会使用资源包进行流量抵扣。此时会扣减账户余额来抵扣产生的资源费用，详情请参考[购买了资源包为什么仍会扣费或欠费？](../product-overview/why-am-i-still-charged-for-resources-after-i-purchase-resource-plans-of-alibaba-cloud-cdn.md)
该模块展示当前账号下，在阿里云CDN中购买的在有效期内、可抵扣余量大于0的资源包信息。
| 表格项 | 说明 | 示例 |
| --- | --- | --- |
| 资源包类型 | [阿里云](../product-overview/resource-plan-overview.md) [CDN](../product-overview/resource-plan-overview.md) [支持的资源包](../product-overview/resource-plan-overview.md) | 下行流量（GB） 、静态 HTTPS 请求数（万次）等 。 |
| 加速区域 | 下行流量包允许抵扣的加速区域 | 全国通用（中国内地）、亚太 1、亚太 2、亚太 3、北美、欧洲、中东/非洲、南美。 |
| 当月用量 | 资源包当月已经使用的用量 | 下行流量：单位 GB，保留两位小数。 静态 HTTPS 请求数：单位万次，保留两位小数。 |
| 可抵扣资源包 | 资源包数量 | 当月用量不等于 0，且有可抵扣资源包，显示 可抵扣资源包 的数量。 当月用量不等于 0，且无可抵扣资源，提示 无可抵扣，后付费 。 当月用量等于 0，有可抵扣资源包，显示 可抵扣资源包 的数量。 当月用量等于 0，无可抵扣资源包，提示 无需抵扣 。 |
点击下方的资源包管理按钮，可以查看更多关于资源包的总量、剩余量、失效时间等详情信息，详细信息请参考[资源包管理详情](query-the-details-of-resource-plans.md)。
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
