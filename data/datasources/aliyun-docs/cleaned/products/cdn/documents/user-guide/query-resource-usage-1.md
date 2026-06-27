# 查询加速域名的用量数据-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/user-guide/query-resource-usage-1

# 用量查询
您可以查询加速域名的用量数据。支持选择不同维度来查询用量，包括流量带宽、HTTPS请求数、QUIC请求数，加速域名、查询时间、计费区域等。
## 注意事项
通过CDN/DCDN控制台（或者OpenAPI）的监控查询、用量查询（实际计费流量）功能查到的加速域名使用的流量数据与通过日志统计的流量数据有差异。通常来说，通过监控查询、用量查询功能查到的加速域名使用的流量数据是通过日志统计的流量数据的1.1倍，详细请参见[为什么监控查询流量、用量查询流量与日志统计流量有差异](../product-overview/traffic-amount-in-the-monitoring-and-usage-analytics-or-in-the-usage-statistics-feature-different-from-the-logged-traffic-amount.md)。
## 用量查询、资源监控、实时监控在数据统计维度上的区别
- 用量查询：按CDN节点维度来统计用量数据，每个CDN节点都唯一归属于某个计费大区，因此用量查询只能按计费大区来查询用量数据，例如，中国内地、亚太1区、北美区等。具体内容请参见[用量查询](query-resource-usage-1.md)。
- 资源监控和实时监控：按客户端IP维度来统计监控数据，每个客户端IP都唯一归属于某个区域或者某个运营商，因此资源监控和实时监控只能按区域或者运营商（可以使用区域+运营商的组合）来查询监控数据。具体内容请参见[资源监控](resource-monitoring.md)和[实时监控](real-time-monitoring.md)。
## 支持查询的时间粒度
通过控制台查询数据和调用相关API接口查询时，单次查询的最大时间跨度和可查询历史数据时间范围存在区别。不同时间粒度对应的单次查询的最大时间跨度、可查询的历史数据时间范围和数据延迟关系如下：
- 通过控制台查询：
| 时间粒度 | 单次查询的最大时间跨度 | 可查询历史数据时间范围 | 数据延迟 |
| --- | --- | --- | --- |
| 5 分钟 | 3 天 | 近 6 个月 | 15 分钟 |
| 1 小时 | 31 天 | 近 6 个月 | 4 小时 |
| 1 天 | 31 天 | 近 6 个月 | 次日凌晨 4 点 |
- 调用相关API接口查询：
| 时间粒度 | 单次查询的最大时间跨度 | 可查询历史数据时间范围 | 数据延迟 |
| --- | --- | --- | --- |
| 5 分钟 | 3 天 | 93 天 | 15 分钟 |
| 1 小时 | 31 天 | 186 天 | 4 小时 |
| 1 天 | 366 天 | 366 天 | 次日凌晨 4 点 |
## 查询用量明细
- 登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
- 在左侧导航栏，选择用量查询>用量查询。
- 在用量查询页面，选择您要查看的项目和查询条件。
下图展示了近30天流量带宽（全部域名）的用量数据，图下方以列表形式显示了每天为粒度的使用数据。
## 相关API
[DescribeDomainUsageData](../api-describedomainusagedata.md)：查询域名在特定计费区域的用量数据。
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
