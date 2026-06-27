# 如何创建Nginx模式的Logtail配置采集日志-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/use-the-nginx-configuration-mode-to-collect-logs

# 使用Nginx配置模式采集文本日志
Nginx日志是运维网站的重要信息，日志服务支持通过Nginx模式快速采集Nginx日志并进行多维度分析。本文介绍如何通过日志服务控制台创建Nginx配置模式的Logtail配置采集日志。
## 方案概览
在Nginx配置模式下，Logtail会根据log_format中的定义将日志内容结构化。Nginx访问日志相关的主要指令为log_format和access_log，通常在配置文件/etc/nginx/nginx.conf中配置。log_format用来定义日志格式；access_log用来指定日志文件的存放路径。
日志格式和存放路径
log_format和access_log的默认值如下所示。
log_format main '$remote_addr - $remote_user [$time_local] "$request" ' '$request_time $request_length ' '$status $body_bytes_sent "$http_referer" ' '"$http_user_agent"'; access_log /var/log/nginx/access.log main;
日志字段说明如下所示：
| 字段名称 | 说明 |
| --- | --- |
| remote_addr | 客户端 IP 地址。 |
| remote_user | 客户端用户名。 |
| time_local | 服务器时间，前后必须加上中括号（[]）。 |
| request | 请求的 URI 和 HTTP 协议。 |
| request_time | 整个请求的总时间，单位为秒。 |
| request_length | 请求的长度，包括请求行、请求头和请求正文。 |
| status | 请求状态。 |
| body_bytes_sent | 发送给客户端的字节数，不包括响应头的大小。 |
| http_referer | URL 跳转来源。 |
| http_user_agent | 客户端浏览器等信息。 |
原始日志
Nginx根据log_format的定义生成日志：
192.168.1.1 - - [11/Dec/2024:11:21:03 +0800] "GET /nginx-logo.png HTTP/1.1" 0.000 514 200 368 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
被采集到日志服务LogStore中的日志：日志采集到日志服务后，在查询分析页面选择原始日志视图，可看到每条日志按键值对格式逐字段解析展示，同时附带实例名、日志路径、Unix 时间戳等元信息。
## 前提条件
已创建Logtail机器组并添加相应服务器，创建机器组的步骤，请参见[创建用户自定义标识机器组](manage-machine-groups.md)和[创建](manage-machine-groups.md)[IP](manage-machine-groups.md)[地址机器组](manage-machine-groups.md)。
服务器具备访问远端服务器80端口和443端口的能力，确保Logtail能够将日志数据发送给日志服务。
服务器日志的内容持续新增。Logtail只采集增量日志，如果下发Logtail配置后日志文件无更新，则Logtail不会采集该文件中的日志。更多信息，请参见[采集流程](use-logtail-to-collect-data.md)。
## 操作步骤
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标Logstore。
展开LogStore选项卡，单击Logtail 配置，然后单击添加Logtail配置。
在弹出的快速数据接入页面中，选择Nginx - 文本日志>立即接入。
在机器组配置步骤中，选择已创建的机器组。在机器组配置步骤中，使用场景选择主机场景，安装环境选择ECS。在选择机器组区域，将目标机器组（例如group-ip）从源机器组移至应用机器组，然后单击下一步。
在Logtail配置步骤中，配置以下选项。
配置名称：输入Logtail采集配置名称，例如nginx-logs。
文件路径：输入日志的存放路径，例如/var/log/nginx/**/access*表示/var/log/nginx目录（包含该目录的递归子目录）中以access开头的文件。
处理配置：单击NGINX模式解析，在弹出的处理插件页签中，输入标准NGINX配置文件日志配置部分，通常以log_format开头。日志服务将自动提取对应字段。例如：
log_format main '$remote_addr - $remote_user [$time_local] "$request" ' '$request_time $request_length ' '$status $body_bytes_sent "$http_referer" ' '"$http_user_agent"';
在原始字段中填写content。日志服务将根据配置自动生成正则表达式并提取对应字段。
其他配置项保持默认即可。如需了解更多配置信息，请参见[采集主机文本日志](collect-host-logs.md)。
在查询分析配置步骤中，单击刷新，可预览采集到的数据。
单击下一步，结束配置流程。您可在此单击查询日志，系统将跳转至LogStore查询分析页面。您需要等待1分钟左右，待索引生效后，才能在原始日志页签中，查看已采集到的日志。更多信息，请参见[查询与分析快速指引](quick-guide-to-query-and-analysis.md)。
## 相关文档
日志服务为Linux系统提供Logtail自动诊断工具，可以根据工具提示快速定位并解决问题。请参见[Logtail](use-the-automatic-diagnostic-tool-of-logtail.md)[自动诊断工具](use-the-automatic-diagnostic-tool-of-logtail.md)。
使用Logtail采集日志后，如果预览页面为空或查询页面无数据，请按照[Logtail](what-do-i-do-if-errors-occur-when-i-use-logtail-to-collect-logs.md)[采集日志失败的排查思路](what-do-i-do-if-errors-occur-when-i-use-logtail-to-collect-logs.md)进行排查。
在使用Logtail采集日志时，可能遇到正则解析失败、文件路径不正确、流量超过Shard服务能力等错误。查看Logtail采集错误的步骤，请参见[如何查看](user-guide/how-do-i-view-logtail-collection-errors.md)[Logtail](user-guide/how-do-i-view-logtail-collection-errors.md)[采集错误信息](user-guide/how-do-i-view-logtail-collection-errors.md)。采集数据常见的错误类型请参见[日志服务采集数据常见的错误类型](log-collection-error-type.md)。
默认情况下，一个日志文件只能匹配一个Logtail配置。如果同一份日志需要被采集多份，请参见[如何实现文件中的日志被采集多份](what-do-i-do-if-i-want-to-use-multiple-logtail-configurations-to-collect-logs-from-a-log-file.md)。
将企业内网服务器日志采集到日志服务，请参见[采集企业内网服务器日志](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)。
不同服务器上的日志的保存路径或文件名相同，需要区分不同服务器，请参见[日志主题](log-topics.md)。区分不同用户或实例产生的日志数据，请参见[日志主题](log-topics.md)。
分析网站访问情况、诊断及调优网站和重要场景告警，请参见[分析](collect-and-analyze-nginx-access-logs.md)[Nginx](collect-and-analyze-nginx-access-logs.md)[访问日志](collect-and-analyze-nginx-access-logs.md)。
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
