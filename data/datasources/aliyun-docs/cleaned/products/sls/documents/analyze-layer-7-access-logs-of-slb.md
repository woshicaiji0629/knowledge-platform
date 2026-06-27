# 查询分析负载均衡7层访问日志，查看客户端PV全球分布、请求方法PV趋势等仪表盘-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/analyze-layer-7-access-logs-of-slb

# 分析负载均衡7层访问日志
采集到SLB 7层负载均衡日志后，您可以在日志服务控制台查询分析日志、查看客户端PV全球分布、请求方法PV趋势、状态码PV趋势、客户端PV热力图、状态码分布等仪表盘。
## 背景信息
对于大部分云上架构而言，负载均衡是基础设施组件，对SLB持续的监控、探测、诊断和报告是一个强需求。阿里云SLB是对多台云服务器进行流量分发的负载均衡服务，可以通过流量分发扩展应用系统对外的服务能力。通过消除单点故障，为应用提供大规模、高可靠的并发Web访问支撑。
SLB访问日志功能当前支持基于HTTP/HTTPS的7层负载均衡，访问日志内容丰富，完整字段说明请参见[日志字段详情](log-fields-26.md)。SLB典型指标如下所示：
PV：客户端发起HTTP、HTTPS请求的次数。
UV：对于相同客户端只计算一次，合计总体请求次数。
请求成功率：状态码为2XX的请求次数占总PV的比例。
请求报文流量：客户端请求报文长度总和。
返回客户端流量：SLB返回给客户端的HTTP Body字节数总和。
请求的热点分布：统计客户端地理位置，按照地理位置统计每个地域的PV情况。
## 前提条件
已采集到SLB 7层负载均衡日志。具体操作，请参见[开通访问日志功能](enable-the-access-log-management-feature.md)。
## 查看仪表盘
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在左侧导航栏，选择仪表盘>仪表盘列表。
在仪表盘列表中，单击目标仪表盘，包括slb-user-log-slb_layer7_operation_center_cn和slb-user-log-slb_layer7_access_center_cn。
说明
在仪表盘卡片的右上角，选择>预览查询语句，查看该图表对应的查询和分析语句。
业务概览
通过过滤器筛选某指定SLB实例的PV、UV随时间的变化趋势。过滤器操作请参见[添加过滤器](user-guide/add-a-filter.md)。
分析流量与延迟情况（slb_layer7_access_center_cn）
统计一定时间范围内请求报文的流量和返回客户端的流量。
统计一定时间范围内请求的响应时间变化趋势和upstream响应时间变化趋势。
统计一定时间范围内高延迟的请求。仪表盘中top upstream响应时间面板以表格形式展示各后端服务器的SLB实例ID、后端服务器、平均upstream响应时间、pv、请求报文流量、返回客户端流量以及2xx/3xx/4xx/5xx状态码比例。
分析用户请求情况（slb_layer7_operation_center_cn）
统计一定时间范围内的请求方法、请求协议分布情况。
统计一定时间范围内各种请求方法的PV趋势。
统计一定时间范围内服务运行情况。
如果出现大量的500状态码则表示后端RealServer的应用程序发生内部错误。
统计一定时间范围内各种状态码的PV变化趋势。
分析请求源
统计客户端所属的网络运营商分布情况。
统计客户端所在的地理位置（国家、省份、城市）。在top客户端 1小时（相对）区域，表格展示访问量最高的客户端统计信息，包括客户端ip、pv、区域、城市、运营商、请求报文流量(MB)和返回客户端流量(MB)，支持按各列排序和搜索筛选。
查看用户代理信息。
通过用户代理（http_user_agent）可得知哪些用户在访问网站或服务。例如搜索引擎会使用爬虫机器人扫描或下载网站资源，一般情况下低频爬虫访问可以帮助搜索引擎及时更新网站内容，有助于网站的推广和SEO。但如果高PV的请求都来自于爬虫，则可能影响服务性能及浪费机器资源。top用户代理页面以表格形式展示按PV降序排列的用户代理访问统计数据，列包括用户代理、pv、请求报文流量(MB)、返回客户端流量(MB)、2xx比例(%)、3xx比例(%)、4xx比例(%)、5xx比例(%)，支持按列排序和筛选。
运营概览
运营人员可基于SLB访问日志分析流量情况，进而辅助业务决策。例如通过分析Host和URI信息获知访客最关注的内容，为网站内容建设提供有力的参考。运营概览仪表盘包含top host 1小时（相对）和top uri 1小时（相对）两个数据表格，分别按 host 和请求 URI 维度展示 SLB 实例的 PV、请求报文流量（MB）、返回客户端流量（MB）以及 2xx、3xx、4xx、5xx 状态码比例等 TOP 排行统计指标。
## 使用桑基图分析请求调度
客户端流量会先被SLB处理，分发到其中一台RealServer中进行实际的业务逻辑处理。SLB可自动检测到不健康的机器并重新分配流量到其它正常服务的RealServer上，等异常机器恢复后再重新分配流量。
为SLB实例添加一个监听，例如服务器（192.168.0.0）同时兼有跳板机职能，其性能是其它三台服务器的4倍，为该服务器设置监听权重为100，其余服务器监听权重为20。执行如下查询分析语句分析请求流量分布情况。
* | select COALESCE(client_ip, vip_addr, upstream_addr) as source, COALESCE(upstream_addr, vip_addr, client_ip) as dest, sum(request_length) as inflow group by grouping sets( (client_ip, vip_addr), (vip_addr, upstream_addr))
[桑基图](display-query-results-in-a-sankey-diagram.md)展示每台RealServer的负载情况，多个客户端向SLB发起请求，请求报文流量基本遵循20:20:20:100比例转发到后端RealServer中。
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
