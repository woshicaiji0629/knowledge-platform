# CDN边缘可编程定制配置-EdgeScript-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/user-guide/edgescript-overview

# EdgeScript概述
边缘脚本（EdgeScript，简称ES）是一个可供您快速实现CDN定制配置的工具箱，当CDN控制台上的标准配置无法满足您的业务需求时，可以尝试使用边缘脚本简单编程实现。
边缘脚本通过简单易学的语法和庞大的函数库，能够像积木式地组合出个性化的CDN定制配置。
边缘脚本内置了CDN节点可以识别的变量、简单的判断语句，同时提供了大量阿里云CDN封装好的函数供您直接调用。通过简单的变量判断并调用现成的函数，即可满足您绝大部分定制的鉴权、缓存、限速、请求头增减等定制配置需求，可以有效地帮您解决定制化配置需求无法实现、业务变更不敏捷的问题。
变量信息，请参见[EdgeScript](edgescript-built-in-variables.md)[内置变量表](edgescript-built-in-variables.md)。
函数信息，请参见[EdgeScript](tag-overview.md)[内置函数库](tag-overview.md)。
条件判断，请参见[条件判断相关](logical-functions.md)。
## 使用费用
边缘脚本功能目前不收费。
## 应用场景
| 场景 | 描述 |
| --- | --- |
| 定制化鉴权逻辑 | 鉴权场景在视频点播、视频直播中的防盗链需求中十分普遍。基于请求参数、Cookie 或其他复杂算法等各类鉴权需求，帮您快速实现鉴权需求，从而完成对资源的保护。 |
| 请求头&响应头控制 | 可以使用边缘脚本对请求参数、请求头等变量进行灵活修改。 |
| 改写&重定向 | 多应用在多语言版本的网站之上，比如中文网站可能会 302 重定向到 1 个位置，英文网站或者德文网站，可能会 302 重定向到不同的位置。 |
| A/B Test | 当源站上一个新功能时，可能会有 A/B Test 的需求，很可能需要 CDN 侧做支持。通过 CDN 携带不同的回源请求头或不同的 URL，去区分触发源站的不同功能，从而来实现这个全链路的 A/B Test。 |
| 缓存控制 | 在某些自定义业务场景下，标准功能的缓存时长或者缓存策略不能够满足需求时，可以通过边缘脚本去完成缓存业务定制化。 |
| 限速控制 | 当需要对免费客户和付费客户进行限速的区分。可以通过边缘脚本来实现。 |
| 封禁拦截 | 针对某些地区、某些特殊的逻辑或者特殊的客户端 IP 去进行封禁拦截，都可以通过边缘脚本来实现定制化。同时，还可以针对防爬策略的实现，防止爬虫爬取资源。 |
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
