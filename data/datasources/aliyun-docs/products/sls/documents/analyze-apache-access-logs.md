# 如何维度分析Apache日志评估网站访问情况-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/analyze-apache-access-logs

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

# 分析Apache日志

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

将Apache日志采集到日志服务后，可以添加仪表盘，对PV、UV、访问地域分布、错误请求、客户端类型等维度进行分析，评估网站访问情况。

## 前提条件

已完成Apache日志的Logtail采集配置。Logtail采集配置的步骤请参见[采集主机文本日志](products/sls/documents/collect-host-logs.md)，在操作步骤2中选择Apache-文本日志。

## 背景信息

Apache是一款主流的网站服务器，当您选用Apache搭建网站时，Apache日志是运维网站的重要信息。

日志服务支持通过数据接入向导一站式采集Apache日志，并为Apache日志创建索引和仪表盘。Apache访问日志仪表盘包括来源IP分布、请求状态占比、请求方法占比、访问PV/UV统计、流入流出流量统计、请求UA占比、前十访问来源、访问前十地址和请求时间前十地址等信息，全方位展示网站访问情况。

## 操作步骤

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在控制台左侧，选择仪表盘>仪表盘列表>中，单击${LogStore名称}_Apache访问日志。

apache_Apache访问日志仪表盘包括如下图表：

- 

来源IP分布图展示访问IP地址的来源情况，所关联的查询分析语句如下所示：

* | select ip_to_province(remote_addr) as address, count(1) as c group by ip_to_province(remote_addr) limit 100

- 

请求状态占比图展示最近一天各HTTP状态码的占比情况，所关联的查询分析语句如下所示：

* | select status, count(1) as pv group by status

- 

请求方法占比图展示最近一天各请求方法的占比情况，所关联的查询分析语句如下所示：

* | select request_method, count(1) as pv group by request_method

- 

访问PV/UV统计图展示最近一天内的PV数和UV数，所关联的查询分析语句如下所示：

* | select date_format(date_trunc('hour', __time__), '%m-%d %H:%i') as time, count(1) as pv, approx_distinct(remote_addr) as uv group by date_format(date_trunc('hour', __time__), '%m-%d %H:%i') order by time limit 1000

- 

流入流出流量统计图展示流量的流入和流出情况，所关联的查询分析语句如下所示：

* | select date_format(date_trunc('hour', __time__), '%m-%d %H:%i') as time, sum(bytes_sent) as net_out, sum(bytes_received) as net_in group by time order by time limit 10000

- 

请求UA占比图展示最近一天各种浏览器的占比情况，所关联的查询分析语句如下所示：

* | select case when http_user_agent like '%Chrome%' then 'Chrome' when http_user_agent like '%Firefox%' then 'Firefox' when http_user_agent like '%Safari%' then 'Safari' else 'unKnown' end as http_user_agent, count(1) as pv group by case when http_user_agent like '%Chrome%' then 'Chrome' when http_user_agent like '%Firefox%' then 'Firefox' when http_user_agent like '%Safari%' then 'Safari' else 'unKnown' end order by pv desc limit 10

- 

前十访问来源图展示最近一天PV数最多的前十个访问来源页面，所关联的查询分析语句如下所示：

* | select http_referer, count(1) as pv group by http_referer order by pv desc limit 10

- 

访问前十地址展示最近一天PV数最多的前十个访问地址，所关联的查询分析语句如下所示：

* | select split_part(request_uri,'?',1) as path, count(1) as pv group by split_part(request_uri,'?',1) order by pv desc limit 10

- 

请求时间前十地址图展示最近一天请求响应延时最长的前十个地址，所关联的查询分析语句如下所示：

* | select request_uri as top_latency_request_uri, request_time_sec order by request_time_sec desc limit 10 10

[上一篇：采集和查询分析Nginx监控日志](products/sls/documents/collect-and-analyze-nginx-monitoring-logs.md)[下一篇：分析IIS日志](products/sls/documents/analyze-iis-logs.md)

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
