# 开启过滤参数解决URL可变参数导致的CDN缓存命中率低-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/the-passing-parameter-of-the-url-is-a-variable-resulting-in-a-low-alibaba-cloud-content-delivery-network-cache-hit-rate

# URL的传递参数为变量导致CDN缓存命中率低
## 问题描述
在使用阿里云CDN时，CDN的缓存命中率很低。在浏览器中，按F12键，在访问页面中，单击Network，然后在Name选项中，单击Headers，在Response Headers模块中，确认URL响应头信息中X-Cache为MISS，则表示没有命中CDN缓存。但是在页面中，对应文件的URL响应头信息的X-Cache为HIT。
说明：本案例以Chrome浏览器为例。
## 问题原因
没有开启CDN的过滤参数功能。
## 解决方案
以下是关于CDN缓存命中率的说明以及CDN命中率低的相关解决方案。
### CDN命中率说明
- CDN命中表示可以直接通过缓存获取到需要的数据。
- CDN没有命中表示无法直接通过缓存获取需要的数据，需要再次查询数据库或者执行其它的操作。一般情况下，可能是由于缓存中根本不存在所需数据，或者缓存已经过期。
### 开启过滤参数功能
- 可能由于没有开启CDN的过滤参数功能，导致URL中传递参数为变量。以如下URL为例，其对应的文件为ArrowScene.ccbi，但是每一次打开该文件时，URL中“?_t=”字段后的数字为变量，所以CDN并不会缓存该数据。http://example.com/movie/XSHD/res/ccb/ArrowScene.ccbi?_t=xxxxxxxxxxxxxx
- 登录CDN控制台，开启过滤参数功能。关于如何开启过滤参数功能，请参考[过滤参数](user-guide/ignore-parameters.md)。说明：开启该功能后，“?_t=”字段后的参数将被忽略。
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
