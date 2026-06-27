# 日志服务不同网络类型的服务入口-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/developer-reference/service-entrance

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [开始使用](products/sls/documents/start-using-sls.md)

- [资源管理](products/sls/documents/resource-management.md)

- [数据采集](products/sls/documents/data-collection-1.md)

- [数据处理](products/sls/documents/data-processing-sls.md)

- [数据存储](products/sls/documents/data-storage.md)

- [查询与分析](products/sls/documents/index-and-query.md)

- [数据监控](products/sls/documents/data-monitoring.md)

- [数据输出与集成](products/sls/documents/sls-log-output-and-integration.md)

- [技术解决方案](products/sls/documents/sls-technical-solutions.md)

- [开发参考](products/sls/documents/developer-reference.md)

- [安全合规](products/sls/documents/security-compliance.md)

- [常见问题](products/sls/documents/faq-15.md)

[首页](https://help.aliyun.com/zh)

# 服务入口

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍日志服务不同网络类型的服务入口。

## 查看服务入口

重要

使用SLS的公共云私网Endpoint时，必须使用阿里云的云上私网DNS地址（100.100.2.136和100.100.2.138），否则可能获取不到正确的私网Endpoint对应的VIP地址，导致您无法访问SLS。

服务入口（Endpoint）表示日志服务对外服务的访问域名。日志服务提供私网域名和公网域名，不同网络的接入方式请参见[使用](https://yq.aliyun.com/articles/59236)[Logtail](https://yq.aliyun.com/articles/59236)[收集各网络日志数据](https://yq.aliyun.com/articles/59236)。

- 

在Project列表区域，单击目标Project。

- 

在Project的项目概览页面，查看该Project所在地域的服务入口。在项目概览Tab 页的访问域名区域，可查看私网域名（cn-shanghai-intranet.log.aliyuncs.com）、公网域名（cn-shanghai.log.aliyuncs.com）和跨域域名（cn-shanghai-share.log.aliyuncs.com）。

## 如何选择服务入口

私网域名和公网域名对外提供的服务都是一致的，但其在网络延时、计费规则方面有少许差异。

| 对比项 | 私网域名 | 公网域名 |
| --- | --- | --- |
| 请求协议 | HTTP、HTTPS | HTTP、HTTPS |
| 使用场景 | 阿里云产品内部相互通信。例如同地域 ECS 访问日志服务。 建议优先使用私网域名。 | 通过公网（互联网）访问日志服务。例如通过本地公网的 API、SDK 访问日志服务。 |
| 相关计费 | 按照日志服务计费项正常计费。更多信息，请参见 [日志服务计费项](products/sls/documents/billable-items.md) 。 | 相比私网计费，增加了外网读取流量。更多信息，请参见 [日志服务计费项](products/sls/documents/billable-items.md) 。 |


## 公网

服务入口是访问一个项目（Project）及其内部日志数据的URL。服务入口与Project所在的地域相关。目前，日志服务已经在多个地域开通，在各地域内的公网服务入口如下表所示。

| 地域 | 服务入口 |
| --- | --- |
| 华东 1（杭州） | cn-hangzhou.log.aliyuncs.com |
| 华东 2（上海） | cn-shanghai.log.aliyuncs.com |
| 华东 5（南京-本地地域-关停中） | cn-nanjing.log.aliyuncs.com |
| 华东 6（福州-本地地域-关停中） | cn-fuzhou.log.aliyuncs.com |
| 华北 1（青岛） | cn-qingdao.log.aliyuncs.com |
| 华北 2（北京） | cn-beijing.log.aliyuncs.com |
| 华北 3（张家口） | cn-zhangjiakou.log.aliyuncs.com |
| 华北 5（呼和浩特） | cn-huhehaote.log.aliyuncs.com |
| 华北 6（乌兰察布） | cn-wulanchabu.log.aliyuncs.com |
| 华南 1（深圳） | cn-shenzhen.log.aliyuncs.com |
| 华南 2（河源） | cn-heyuan.log.aliyuncs.com |
| 华南 3（广州） | cn-guangzhou.log.aliyuncs.com |
| 西南 1（成都） | cn-chengdu.log.aliyuncs.com |
| 中国（香港） | cn-hongkong.log.aliyuncs.com |
| 日本（东京） | ap-northeast-1.log.aliyuncs.com |
| 韩国（首尔） | ap-northeast-2.log.aliyuncs.com |
| 新加坡 | ap-southeast-1.log.aliyuncs.com |
| 马来西亚（吉隆坡） | ap-southeast-3.log.aliyuncs.com |
| 印度尼西亚（雅加达） | ap-southeast-5.log.aliyuncs.com |
| 菲律宾（马尼拉） | ap-southeast-6.log.aliyuncs.com |
| 泰国（曼谷） | ap-southeast-7.log.aliyuncs.com |
| 阿联酋（迪拜） | me-east-1.log.aliyuncs.com |
| 美国（硅谷） | us-west-1.log.aliyuncs.com |
| 德国（法兰克福） | eu-central-1.log.aliyuncs.com |
| 美国（弗吉尼亚） | us-east-1.log.aliyuncs.com |
| 英国（伦敦） | eu-west-1.log.aliyuncs.com |


## 私网

如果在阿里云ECS机器环境使用日志服务API，还可以使用私网服务入口，各个地域服务入口如下表所示。

说明

- 

日志服务API在如下服务入口仅支持HTTP协议、HTTPS协议。

- 

使用私网服务入口访问日志服务不消耗ECS公网流量，可以节约ECS公网带宽。

| 地域 | 服务入口 |
| --- | --- |
| 华东 1（杭州） | cn-hangzhou-intranet.log.aliyuncs.com |
| 华东 2（上海） | cn-shanghai-intranet.log.aliyuncs.com |
| 华东 5（南京-本地地域-关停中） | cn-nanjing-intranet.log.aliyuncs.com |
| 华东 6（福州-本地地域-关停中） | cn-fuzhou-intranet.log.aliyuncs.com |
| 华北 1（青岛） | cn-qingdao-intranet.log.aliyuncs.com |
| 华北 2（北京） | cn-beijing-intranet.log.aliyuncs.com |
| 华南 1（深圳） | cn-shenzhen-intranet.log.aliyuncs.com |
| 华南 2（河源） | cn-heyuan-intranet.log.aliyuncs.com |
| 华南 3（广州） | cn-guangzhou-intranet.log.aliyuncs.com |
| 华北 3（张家口） | cn-zhangjiakou-intranet.log.aliyuncs.com |
| 华北 5（呼和浩特） | cn-huhehaote-intranet.log.aliyuncs.com |
| 华北 6（乌兰察布） | cn-wulanchabu-intranet.log.aliyuncs.com |
| 西南 1（成都） | cn-chengdu-intranet.log.aliyuncs.com |
| 中国（香港） | cn-hongkong-intranet.log.aliyuncs.com |
| 美国（硅谷） | us-west-1-intranet.log.aliyuncs.com |
| 日本（东京） | ap-northeast-1-intranet.log.aliyuncs.com |
| 韩国（首尔） | ap-northeast-2-intranet.log.aliyuncs.com |
| 新加坡 | ap-southeast-1-intranet.log.aliyuncs.com |
| 马来西亚（吉隆坡） | ap-southeast-3-intranet.log.aliyuncs.com |
| 印度尼西亚（雅加达） | ap-southeast-5-intranet.log.aliyuncs.com |
| 菲律宾（马尼拉） | ap-southeast-6-intranet.log.aliyuncs.com |
| 泰国（曼谷） | ap-southeast-7-intranet.log.aliyuncs.com |
| 阿联酋（迪拜） | me-east-1-intranet.log.aliyuncs.com |
| 德国（法兰克福） | eu-central-1-intranet.log.aliyuncs.com |
| 美国（弗吉尼亚） | us-east-1-intranet.log.aliyuncs.com |
| 英国（伦敦） | eu-west-1-intranet.log.aliyuncs.com |


## 传输加速

日志服务在私网和公网基础上，新增传输加速的网络类型。相较于普通的公网访问，传输加速在延时和稳定性上具备显著优势，适用于对数据采集、消费延时、可靠性要求较高的场景。更多信息，请参见[管理传输加速](products/sls/documents/transmission-acceleration.md)。

传输加速的服务入口在所有地域一致，服务入口为：

log-global.aliyuncs.com

说明

传输加速功能默认为关闭状态，需要手动开启后才可使用。具体操作，请参见[采集加速](products/sls/documents/enable-the-global-acceleration-feature.md)。

## 通过IPv6地址访问SLS

目前日志服务已支持通过IPv6、IPv4双栈域名访问。

您的IPv6、IPv4客户端均可以使用SLS提供的统一双栈域名访问SLS。DNS服务器将按照您使用的协议版本解析对应的SLS服务器地址。

目前可以通过IPv6协议访问的Endpoint如下：

| 地域 | 服务入口 |
| --- | --- |
| 华东 1（杭州） | cn-hangzhou.dualstack.log.aliyuncs.com |
| 华东 2（上海） | cn-shanghai.dualstack.log.aliyuncs.com |
| 华北 1（青岛） | cn-qingdao.dualstack.log.aliyuncs.com |
| 华北 2（北京） | cn-beijing.dualstack.log.aliyuncs.com |
| 华北 3（张家口） | cn-zhangjiakou.dualstack.log.aliyuncs.com |
| 华北 5（呼和浩特） | cn-huhehaote.dualstack.log.aliyuncs.com |
| 华北 6（乌兰察布） | cn-wulanchabu.dualstack.log.aliyuncs.com |
| 华南 1（深圳） | cn-shenzhen.dualstack.log.aliyuncs.com |
| 华南 2（河源） | cn-heyuan.dualstack.log.aliyuncs.com |
| 华南 3（广州） | cn-guangzhou.dualstack.log.aliyuncs.com |
| 西南 1（成都） | cn-chengdu.dualstack.log.aliyuncs.com |
| 新加坡 | ap-southeast-1.dualstack.log.aliyuncs.com |
| 日本（东京） | ap-northeast-1.dualstack.log.aliyuncs.com |


## 金融云

| 地域 | 公网 | 私网 |
| --- | --- | --- |
| 华东 1 金融云 | cn-hangzhou-finance.log.aliyuncs.com | cn-hangzhou-finance-intranet.log.aliyuncs.com |
| 华东 2 金融云 | cn-shanghai-finance-1.log.aliyuncs.com | cn-shanghai-finance-1-intranet.log.aliyuncs.com |
| 华北 2 金融云（邀测） | cn-beijing-finance-1.log.aliyuncs.com | cn-beijing-finance-1-intranet.log.aliyuncs.com |
| 华南 1 金融云 | cn-shenzhen-finance-1.log.aliyuncs.com | cn-shenzhen-finance-1-intranet.log.aliyuncs.com |


## 阿里政务云

| 地域 | 公网 | 私网 |
| --- | --- | --- |
| 华北 2 阿里政务云 1 | cn-north-2-gov-1.log.aliyuncs.com | cn-north-2-gov-1-intranet.log.aliyuncs.com |


## 自定义域名

自定义域名创建请参见[域名注册](https://help.aliyun.com/zh/dws/getting-started/quickly-register-a-new-domain-name)。

在日志服务控制台绑定完自定义域名后，请前往公网DNS解析添加解析记录，域名绑定才能生效。详情请参见[添加网站解析](https://help.aliyun.com/zh/dns/add-an-a-record-to-a-website-domain)。

[上一篇：API参考附录](products/sls/documents/developer-reference/api-reference-appendix.md)[下一篇：VPC专用内网域名](products/sls/documents/developer-reference/vpc-private-intranet-domain-name.md)

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
