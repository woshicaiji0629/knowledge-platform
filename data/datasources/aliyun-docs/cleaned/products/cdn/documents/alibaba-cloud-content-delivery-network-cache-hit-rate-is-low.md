# CDN缓存命中率低的原因分析与排查方法-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/alibaba-cloud-content-delivery-network-cache-hit-rate-is-low

# CDN缓存命中率较低排查方法
## 概述
阿里云CDN控制台上显示的缓存命中率一直不高，且源站收到较多来自CDN的回源请求，对源站造成一定的负载压力。现需要排查缓存命中率不高的原因。
## 详细信息
如果发生命中率过低的情况意味用户的每次请求都会通过CDN回源，公网链路的不稳定可能导致加速的效果反而变差。如何解决命中率过低的问题，可以通过预热URL、配置资源缓存规则、过滤URL中可变参数优化缓存命中率，具体操作请参见[优化CDN缓存命中率](use-cases/increase-the-cache-hit-ratios-of-alibaba-cloud-cdn.md)。首先参见以下操作分析具体原因：
### CDN控制台查看命中率和流量情况
CDN控制台中的命中率和流量的说明及分析如下：
- CDN控制台统计的缓存命中率仅仅是CDN L1节点的命中率，实际L1节点的缓存数据也是从CDN L2节点获取，并不会从源站获取数据，所以真实的CDN命中率是略高于CDN控制台显示的命中率。说明：CDN数据流向为客户端>CDN的1级节点>CDN的2级节点>源站。
- 查看提交的CDN加速域名的流量情况。在加速域名流量不高的情况下，即便MISS状态的URL不多，但是对命中率的统计计算影响很大。例如，某CDN加速域名一共对外提供了10个可以访问的URL，其中有一个URL源站上设置了no-cache，导致不缓存，在其他URL访问都命中的情况下，命中率也仅有90%。说明：CDN加速域名的流量带宽可以在CDN控制台获取。
- 检查业务QPS是否正常。CDN的缓存规则默认是按照配置的缓存时间进行缓存。但节点的磁盘空间是有限的，在高频用户访问的情况下，缓存文件会按照冷文件的冷热程度汰换，访问频率较低的文件会被访问热点的文件汰换掉造成回源。遇到这种情况一般都是只有十几个QPS的域名，建议您定义对自己域名下的资源进行预热，保证是命中在节点。
### 缓存配置检查
检查是否因部分参数配置不合理导致缓存命中率低，具体操作如下：
- 检查是否开启强制Range回源，详情请参见[配置Range回源](user-guide/object-chunking.md)。此功能开启后，所有回源请求将按照设定的Range size切片回源。 Range的功能也有两面性，对于源站是大文件的（超过50M） 场景，Range分片可以有效的降低大文件下载时遇到的网络拥塞，以及源站为窄带的情况。但如果源站的文件平均size相对较小，比如在10M以内的文件，开启强制Range回源没有优化效果，反而降低回源的效率，扩大回源，使命中率降低。
- 检查CDN的加速URL中是否带有可变参数。当您的业务经常使用uri带有变量，并且不同用户请求都有不同的parameter变量时，CDN会按照URL hash后的值存储，每一条不同的uri都会触发回源，CDN就变成透传的组件失去了缓存的意义。遇到这种情况，建议可以开启CDN忽略参数缓存的功能，将uri、"?"以后的资源去掉后再进行CDN缓存。但如果源站或者用户对"?"后的参数强依赖，建议切换到全站加速（DCDN）产品，通过智能选路回源更灵活，CDN是固定边缘节点、中心节点双层回源，对于强依赖"?"变量的访问效果略低于全站加速（DCDN），智能选路是动态的网络质量检测规划回源路径，可能是边缘节点直接回源，也可以是边缘节点回到中心节点再回源。说明：例如URL地址为http://example.aliyundoc.com/1.txt?timestamp=14378923，其中timestamp值为时间戳，每次访问此值均不同。CDN针对第一次访问的URL，即之前未预热的URL，无论该URL是否符合CDN的缓存规则，由于节点上还没有这个文件，第一次访问肯定都是MISS状态。但是timestamp参数会变化，所以每次访问都是一个全新的URL，则每次都返回MISS状态，从而影响命中率。
检查源站是否开启多副本缓存。多副本缓存是服务端（源站） 针对用户请求带有不同Accept-Encoding头，源站能响应不同的Vary头，且CDN会按按照不同的Vary头进行缓存。带有不同vary头的请求会增加回源的次数，导致命中率降低。
- 检查缓存配置是否合理。源站上缓存Header设置不当，或者缺少必要的Header，如果CDN的缓存规则是不缓存，那么每次访问都是MISS状态，影响命中率：
- 缓存Header设置不当，主要是Cache-Control或者Pragma配置，即源站上设置了Cache-Control为no-cache、no-store、max-age=0、private，或者Pragma设置为no-cache等情况下，均会被CDN当做最高优先级执行不缓存操作。
- 缺少必要的Header，指源站的Response头部信息中不包含ETag和Last-modified，这种情况也会导致不进行缓存。
- 源是否设置过缓存头，CDN默认按照源站的缓存头优先级缓存，如果源站设置了不合理的缓存头，比如max-age=0，则覆盖CDN 的缓存。
- 检查CDN控制台是否设置了不缓存的规则，即某目录或者某种后缀的文件设置的缓存时间为0秒。
- 检查源站动态内容是否较多，目前CDN主要是加速静态资源，例如CSS、JS、HTML、图片、TXT、视频等资源，针对动态资源PHP、JSP、包含内部逻辑处理甚至Cookie等资源都会回源数据。
- 刷新操作频繁。CDN控制台有定时刷新功能，每次刷新都会导致所有已经在CDN上缓存的URL失效，所以在刷新之后访问同样的URL时，就是MISS状态，从而影响命中率。
- 文件热度不够。不经常被用户访问到的URL，即使符合所有缓存规则，但是经常有被节点去除缓存的风险。CDN节点上缓存的文件，可以理解为按照热度属性采取末尾淘汰制，热度就是该文件在该节点上被访问的频率，文件热度不够，其实一定程度上跟这个域名本身的流量不高有关系。
## 相关文档
CDN缓存相关文档如下：
- [CDN缓存命中率下降的因素](cache-hit-ratio-of-an-alibaba-cloud-cdn-pop-decreases.md)
- [URL的传递参数为变量导致CDN缓存命中率低](the-passing-parameter-of-the-url-is-a-variable-resulting-in-a-low-alibaba-cloud-content-delivery-network-cache-hit-rate.md)
- [CDN缓存规则](user-guide/what-is-caching.md)
## 适用于
- CDN
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
