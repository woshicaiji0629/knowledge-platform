# 使用嵌套子查询实现复杂SQL分析-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/nested-subquery

# 嵌套子查询
嵌套子查询是指将一个SELECT语句嵌套在另一个SELECT语句中。针对复杂的分析场景，您可以使用嵌套子查询。
## 基本语法
使用嵌套子查询时，需在SELECT语句中指定FROM子句。
* | SELECT key FROM (sub_query)
重要
子查询语句需被包裹在半角圆括号()中。
在子查询语句中，需指定关键字FROM log，表示在当前LogStore中执行SQL分析。
## 示例
### 示例1
计算各个请求方法对应的请求数量，然后获取最小的请求数量。
查询和分析语句
* | SELECT min(PV) FROM ( SELECT count(1) as PV FROM log GROUP BY request_method )
查询和分析结果
### 示例2
计算当前1小时和昨天同时段的网站访问量比值。其中，选择查询和分析的时间范围为1小时（整点时间），86400表示当前时间减去86400秒（1天），log表示LogStore名称。
查询和分析语句
* | SELECT diff [1] AS today, diff [2] AS yesterday, diff [3] AS ratio FROM ( SELECT compare(PV, 86400) AS diff FROM ( SELECT count(*) AS PV FROM log ) )
查询和分析结果
3337.0表示当前1小时（例如2020-12-25 14:00:00~2020-12-25 15:00:00）的网站访问量。
3522.0表示昨天同时段（例如2020-12-24 14:00:00~2020-12-24 15:00:00）的网站访问量。
0.947473026689381表示当前1小时与昨天同时段的网站访问量比值。
### 示例3
统计各个访问页面的访问次数及占比。
查询和分析语句
* | SELECT request_uri AS "访问页面", c AS "次数", round(c * 100.0 /(sum(c) over()), 2) AS "百分比%" FROM ( SELECT request_uri AS request_uri, count(*) AS c FROM log GROUP BY request_uri ORDER BY c DESC )
查询和分析结果
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
