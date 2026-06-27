# 在日志服务里如何通过控制台快速创建仪表盘-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/dashboard-overview

# 快速创建仪表盘
日志服务的仪表盘是可视化工具，以柱状图、折线图、饼图等形式展示日志数据的查询分析结果，您可以通过仪表盘监控系统、应用或服务的运行状态。本文介绍仪表盘的创建步骤。
## 快速开始
下面我们以[CLB](../../slb/documents/classic-load-balancer/user-guide/clb-access-logs.md)[访问日志](../../slb/documents/classic-load-balancer/user-guide/clb-access-logs.md)为例创建一个仪表盘，用于监控不同请求方法的PV趋势，并使用过滤器查看指定方法的PV趋势。日志样例如下：
{ "body_bytes_sent": "1346", "client_ip": "118.*.*.125", "host": "www.*.*.com", "http_host": "www.*.*.com", "request_length": "15**", "request_method": "PUT", "request_time": "26", "scheme": "https", "slbid": "slb-02", "status": "200", "upstream_addr": "133.*.*.113", "upstream_response_time": "18", "upstream_status": "200", "vip_addr": "39.*.*.121", "__pack_meta__": "1|MTcyNDE*==|120|119", "__topic__": "slb_layer7", "__source__": "127.0.0.1", "__tag__:__receive_time__": "1725349464", "__tag__:__receive_time___0": "1725349464", "__time__": "1725349464" }
在日志服务创建一个仪表盘，只需要3步：
添加仪表盘：我们先在日志服务的控制台添加一个仪表盘，用于容纳多个相关的统计图表。
添加统计图表：然后我们在仪表盘中添加一个统计图表，可视化展示日志的查询分析结果。
添加筛选器：接着我们为统计图表设置筛选条件，根据查询分析语句的字段对统计图表进行筛选。
### 1. 添加仪表盘
登录[日志服务控制台](https://sls.console.aliyun.com/)，选择目标Project，在仪表盘>仪表盘列表页面，添加一个仪表盘。
单击右上角+图标，在下拉菜单中选择添加仪表盘。
### 2. 添加统计图表
单击添加新图表。
配置和保存统计图表：
在页面左侧配置查询时间范围、LogStore、查询分析语句。
在页面右侧配置图表类型为折线图、x轴为t、y轴为pv、聚合列为request_method，单击页面上方的应用查看图表配置效果，然后单击确定保存图表。
查询分析语句如下：
SELECT DATE_FORMAT(DATE_TRUNC('minute', __time__), '%m-%d %H:%i') AS t, request_method, COUNT(*) AS pv GROUP BY t, request_method ORDER BY t ASC LIMIT 10000;
拖动统计图表调整大小，然后单击页面右上角的保存。
在弹出的保存仪表盘对话框中，填写仪表盘名称和备注，然后单击确认完成保存。
### 3. 添加筛选条件
统计图表中显示所有请求方法的PV，如果您只想查看部分方法的PV，可以先添加过滤器，然后在下拉列表选择相应字段，无需修改查询分析语句。
在仪表盘页面，单击页面右上角的编辑，进入编辑模式。单击页面顶部的按钮，创建一个筛选器。
即工具栏最左侧的漏斗形筛选图标。
配置过滤器。
过滤器的原理是在原查询和分析语句的结果中，查找包含Key:Value的日志。我们需要查看请求方法为POST的PV图，即在上面配置的查询分析语句的结果中，筛选包含request_method：POST的日志。
在右侧面板中，将request_method配置为Key值作为筛选条件，然后打开添加动态列表项开关，输入查询分析语句*|select distinct request_method获取日志字段request_method的所有字段值，这些字段值会作为筛选器的筛选项。
单击仪表盘页面右上方的保存。
在下拉列表选择请求方法为POST，统计图表中只显示相应请求方法的PV。
## 相关文档
本文介绍了单个统计图表的创建步骤，您可以将相关的多个统计图表配置在同一个仪表盘中方便查看，配置仪表盘的步骤和更多的统计图表类型，请参见[使用仪表盘](dashboard-real-time-monitoring-and-visualization.md)。
创建仪表盘后，可以分享到钉钉账号、企业微信账号或阿里云账号，或者通过免密链接在浏览器中直接访问，具体操作步骤请参见[免密分享与集成仪表盘](secret-free-sharing-and-integrated-dashboard.md)。
在仪表盘发现异常时，当您需要快速进一步分析，例如在相应LogStore中进行查询分析、打开Trace分析页面或其他仪表盘页面，可以使用交互事件功能，配置步骤请参见[使用仪表盘下钻分析定位异常根因](user-guide/use-instrument-cluster-drill-in-analysis-to-locate-the-root-cause.md)。
在日常仪表盘使用中，我们往往需要及时发现统计图表上指标异常变化。为仪表盘配置图表阈值高亮和告警，操作步骤请参见[使用仪表盘快速发现异常指标](use-dashboards-to-quickly-discover-abnormal-metrics.md)。
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
