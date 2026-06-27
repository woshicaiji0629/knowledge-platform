# CDN静态缓存-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/what-is-caching

# 什么是缓存
您使用CDN加速静态资源时，CDN会将资源缓存到最近的节点上。当您访问该资源时，可直接从缓存节点获取，减少延迟，提高访问效率。当请求的内容在节点上不存在或已过期时，CDN会向源站请求最新数据。
## 缓存相关功能
通过缓存配置功能，您可以对域名执行如下操作。
| 功能 | 说明 |
| --- | --- |
| [配置](configure-the-cdn-cache-expiration-time.md) [CDN](configure-the-cdn-cache-expiration-time.md) [缓存过期时间](configure-the-cdn-cache-expiration-time.md) | 通过配置缓存过期时间规则，可以精细化控制 CDN 节点的资源缓存时长，以平衡内容更新、访问性能与回源成本。此文档介绍缓存规则的工作原理、配置方法、验证、排障流程及最佳实践。 |
| [配置状态码过期时间](create-a-cache-rule-for-http-status-codes.md) | CDN 节点从源站获取资源时，源站会返回响应状态码，您可以在阿里云 CDN 上配置状态码缓存时间，当客户端再次请求相同资源时，由 CDN 直接响应状态码，不会触发回源，减轻源站压力。当状态码超过设置的缓存时间，会重新触发回源。 |
| [配置状态码过期时间（源站优先）](../create-a-status-code-expiration-rule-that-honors-origin.md) | 如果您需要根据源站响应的不同状态码，设置静态资源在 CDN 节点上的缓存过期时间，则可以配置状态码过期时间（源站优先）功能。 |
| [修改出站响应头](create-a-custom-http-response-header.md) | 出站响应头是 HTTP 响应消息头的组成部分之一，可携带特定响应参数并传递给客户端，用来控制缓存行为。通过修改出站响应头，当用户请求加速域名下的资源时， CDN 返回的响应消息会携带您配置的响应头，从而实现跨域访问等特定功能。 |
| [配置自定义页面](create-a-custom-error-page.md) | 配置自定义错误页面后，当用户请求的内容不存在或出现错误时，CDN 节点会返回自定义的错误页面，而不是默认的错误页面。自定义错误页面可以提高用户体验，让用户看到更友好的错误提示。 |
| [重写访问](create-an-access-url-rewrite-rule.md) [URL](create-an-access-url-rewrite-rule.md) | 如果源站资源路径变化， CDN 节点资源路径也会变化。用户请求的 URL 路径不变时， CDN 节点需要重写请求的 URL，将其重定向到目标路径，以减少回源并提升客户端访问性能。 |
| [自定义](create-custom-cache-keys.md) [Cache Key](create-custom-cache-keys.md) | 您可以将访问同一个文件的一类请求转化为统一的 Cachekey，避免不同请求缓存为不同文件的问题，降低回源频率。 配置自定义缓存键（Cache Key），开发者可以根据 HTTP 请求的不同部分（例如 URI、请求参数、HTTP 请求头或自定义变量等）制定规则来生成 Cache Key，将访问同一个文件的一类请求转化为统一的 Cache Key，提高缓存命中率，降低回源率，减少请求的响应时间和带宽消耗。 |
| [配置共享缓存](configure-shared-cache.md) | 同一阿里云账号下多个 CDN 加速域名默认拥有独立缓存空间，多个域名独立缓存会导致源站被重复回源。为多个域名配置共享缓存，可使多个域名在 CDN 节点共用缓存资源，公共资源只需从源站下载一次，后续访问直接从共享缓存中获取资源，从而提升缓存命中率、减少回源。 |
| [配置跨域资源共享](configure-cors.md) | 当您的业务接入阿里云 CDN 后，需要跨域共享或者访问资源时，您可以通过节点 HTTP 响应头来实现跨域访问。 |
## 常见问题
[CDN](cache-related-faq.md)[缓存清理机制是什么？](cache-related-faq.md)
[CDN](cache-related-faq.md)[默认的缓存规则是什么？](cache-related-faq.md)
[如何判断](cache-related-faq.md)[CDN](cache-related-faq.md)[缓存是否成功？](cache-related-faq.md)
[如何解决](cache-related-faq.md)[URL](cache-related-faq.md)[的传递参数为变量导致](cache-related-faq.md)[CDN](cache-related-faq.md)[缓存命中率低的问题？](cache-related-faq.md)
[如何设置文件不缓存直接回源？](cache-related-faq.md)
[在](cache-related-faq.md)[CDN](cache-related-faq.md)[控制台缓存过期时间设置为](cache-related-faq.md)[0，为何访问到的资源仍然不是最新内容？](cache-related-faq.md)
[源站变更文件后，CDN](cache-related-faq.md)[节点上的缓存会主动、实时更新吗？](cache-related-faq.md)
[影响](cache-related-faq.md)[CDN](cache-related-faq.md)[缓存命中率下降的因素有哪些？](cache-related-faq.md)
[如何排查](cache-related-faq.md)[CDN](cache-related-faq.md)[缓存命中率较低的问题？](cache-related-faq.md)
[如何提高](../use-cases/increase-the-cache-hit-ratios-of-alibaba-cloud-cdn.md)[CDN](../use-cases/increase-the-cache-hit-ratios-of-alibaba-cloud-cdn.md)[缓存命中率？](../use-cases/increase-the-cache-hit-ratios-of-alibaba-cloud-cdn.md)
[如何设置缓存全局生效？](cache-related-faq.md)
[设置](set-the-nginx-cache-policy.md)[Nginx HTTP](set-the-nginx-cache-policy.md)[缓存策略](set-the-nginx-cache-policy.md)
[设置](set-apache-caching-policy.md)[Apache](set-apache-caching-policy.md)[缓存策略](set-apache-caching-policy.md)
[设置](set-the-iis-cache-policy.md)[IIS](set-the-iis-cache-policy.md)[缓存策略](set-the-iis-cache-policy.md)
[CDN](specify-a-ttl-value-for-pops-when-using-alibaba-cloud-cdn-to-accelerate-the-delivery-of-static-content.md)[加速静态资源时如何设置服务器端的缓存过期时间？](specify-a-ttl-value-for-pops-when-using-alibaba-cloud-cdn-to-accelerate-the-delivery-of-static-content.md)
[通过](the-results-obtained-by-accessing-the-source-site-through-alibaba.md)[CDN](the-results-obtained-by-accessing-the-source-site-through-alibaba.md)[访问与直接访问源站得到的结果不一样](the-results-obtained-by-accessing-the-source-site-through-alibaba.md)
[缓存配置为什么没有生效？](cache-related-faq.md)
[通过](configure-cors.md)[HTTP](configure-cors.md)[响应头配置](configure-cors.md)[CDN](configure-cors.md)[跨域资源共享（CORS）及注意事项](configure-cors.md)
[为什么已经配置了响应头](cache-related-faq.md)[Access-Control-Allow-Origin，但是访问资源仍提示跨域问题，response header](cache-related-faq.md)[中没有配置的响应头？](cache-related-faq.md)
[异常状态码缓存规则是什么？](cache-related-faq.md)
[出站响应头和入站响应头有什么区别？](cache-related-faq.md)
[如何配置整个域名不缓存？](cache-related-faq.md)
[CDN](cache-related-faq.md)[是否支持多副本缓存？如何实现](cache-related-faq.md)[CDN](cache-related-faq.md)[的多副本缓存？](cache-related-faq.md)
[CDN](cache-related-faq.md)[如何配置子目录访问首页？](cache-related-faq.md)
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
