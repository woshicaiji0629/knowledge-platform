# 什么是QUIC协议以及如何开通和收费-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/what-is-the-quic-protocol

# 配置QUIC协议
QUIC协议提供与TLS/SSL相当的安全性，同时具有更低的连接和传输延迟。如果您需要提高资源访问效率，且保证数据传输的安全性，则开启QUIC协议。
## HTTP/3和QUIC
### 什么是HTTP/3
HTTP/3是HTTP协议的第三个版本，其底层传输协议由传统的TCP、TLS改变为QUIC，HTTP/3保留了HTTP/2的许多特性，如头部压缩、多路复用等，同时能更好地处理网络拥塞从而降低访问延迟。
### 什么是QUIC
QUIC（Quick UDP Internet Connections）是一种实验性传输层网络协议，提供与TLS/SSL相当的安全性，同时具有更低的连接和传输延迟。QUIC基于UDP，因此拥有极佳的弱网性能，在丢包和网络延迟严重的情况下仍可提供可用的服务。QUIC在应用程序层面就能实现不同的拥塞控制算法，不需要操作系统和内核支持，这相比于传统的TCP协议，拥有了更好的改造灵活性，非常适合在TCP协议优化上遇到瓶颈的业务。
目前，阿里云CDN开放使用的是七层协议的QUIC。
QUIC的类型
阿里云CDN支持互联网标准版本 IETF QUIC。
对客户端的要求
QUIC协议对客户端的要求如下：
如果您使用Chrome浏览器，当前阿里云CDN已经支持HTTP/3的标准协议，Chrome支持直接对阿里云CDN发起QUIC请求。
如果您使用自研App，则App必须集成支持QUIC协议的网络库，例如：lsquic-client、cronet网络库、ngtcp2和quiche等。
## 工作原理
在阿里云CDN中使用QUIC的工作原理如下图所示。
## QUIC计费规则
QUIC协议属于增值服务，会对QUIC请求数进行额外计费。详细信息，请参见[CDN](https://www.aliyun.com/price/product#/cdn/detail/cdn)[定价详情](https://www.aliyun.com/price/product#/cdn/detail/cdn)的QUIC部分。
重要
QUIC协议的请求判断标准为是否基于UDP协议。
协议头为HTTPS的QUIC协议请求计费规则为：如果是QUIC协议请求，则匹配QUIC请求数计费；如果不是，则匹配HTTPS请求数计费。
## QUIC计费方式
| 计费项目 | 计费规则 | 付费方式 | 计费周期 |
| --- | --- | --- | --- |
| 静态 QUIC 请求数 | 域名请求次数+域名关联的静态资源加载次数 | 按量后付费。 | 按小时结算，出账存在 3~4 个小时的延迟。 |
## 开启QUIC协议
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击QUIC协议，打开QUIC协议开关。
## 如何判断客户端发起的是QUIC协议还是HTTP协议
下文以Chrome浏览器验证为例为您介绍查看方法。
操作步骤：网站空白处右键，选择检查>网络，Protocol列显示h3-29表示QUIC请求。
说明
如果没有Protocol列，可尝试刷新网页后，右键勾选标头选项>协议即可。
## 视频讲解
本视频主要从以下几个方面为您介绍QUIC功能：
QUIC功能的诞生与演进历程。
QUIC在CDN中的应用。
QUIC在首屏时间、卡顿时间上的优势。
QUIC的拥塞控制与弱网改进。
QUIC在阿里的几个落地应用场景与优势总结。
如何在CDN上开通和使用QUIC。
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
