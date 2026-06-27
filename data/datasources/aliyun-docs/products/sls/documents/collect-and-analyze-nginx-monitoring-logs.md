# 采集及分析Nginx监控日志-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/collect-and-analyze-nginx-monitoring-logs

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

# 采集和查询分析Nginx监控日志

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

通过配置Nginx内置的stub_status模块，您可以启用专用的状态页实时显示Nginx服务器的关键指标，例如活跃的客户端连接数（Active connections）、在读取请求头（Reading）、发送响应（Writing）以及处于等待状态（Waiting）的连接数。您可以通过Logtail插件采集Nginx监控日志并进行查询分析，持续监控Nginx集群的性能。

## 前提条件

已在服务器上安装Logtail。具体操作，请参见[安装](products/sls/documents/install-logtail-on-a-linux-server.md)[Logtail（Linux](products/sls/documents/install-logtail-on-a-linux-server.md)[系统）](products/sls/documents/install-logtail-on-a-linux-server.md)或[安装](products/sls/documents/install-logtail-on-a-windows-server.md)[Logtail（Windows](products/sls/documents/install-logtail-on-a-windows-server.md)[系统）](products/sls/documents/install-logtail-on-a-windows-server.md)。

说明

目前支持Linux Logtail 0.16.0及以上版本，Windows Logtail 1.0.0.8及以上版本。

## 步骤一：配置stub_status模块

说明

本文以Linux系统为例介绍操作步骤。

- 

执行以下命令，安装和启动Nginx。

sudo yum install -y nginx sudo systemctl restart nginx

- 

执行以下命令确认Nginx已具备[status](https://nginx.org/en/docs/http/ngx_http_stub_status_module.html)[功能](https://nginx.org/en/docs/http/ngx_http_stub_status_module.html)。

nginx -V 2>&1 | grep -o with-http_stub_status_module

返回以下信息，表示已支持status功能。

with-http_stub_status_module

- 

配置Nginx服务器。

- 

打开Nginx的配置文件，在server {..}块中添加以下代码。关于nginx_status的更多信息，请参见[Nginx status](https://easyengine.io/tutorials/nginx/status-page/)。

location /nginx_status { stub_status on; #启用stub_status模块 access_log off; allow ${服务器IP}; #允许访问的服务器IP deny all; # 拒绝所有其他 IP 地址访问这个状态页面 }

- 

执行以下命令，验证配置结果。

nginx -t sudo systemctl restart nginx curl http://${服务器IP}/nginx_status

返回以下结果，表示配置成功。

Active connections: 1 server accepts handled requests 2507455 2507455 2512972 Reading: 0 Writing: 1 Waiting: 0

## 步骤二：采集Nginx监控日志

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

单击控制台页面右侧的快速接入数据卡片。

- 

在接入数据页面，查找自定义数据插件并单击。

- 

选择目标Project和LogStore，单击下一步。

- 

创建机器组。

- 

如果您已有可用的机器组，请单击使用现有机器组。

- 

如果您还没有可用的机器组，请执行以下操作（以ECS为例）。

- 

在ECS机器页签中，通过手动选择实例方式选择目标ECS实例，单击创建。

具体操作，请参见[安装](products/sls/documents/install-logtail-on-ecs-instances.md)[Logtail（ECS](products/sls/documents/install-logtail-on-ecs-instances.md)[实例）](products/sls/documents/install-logtail-on-ecs-instances.md)。

重要

如果您的服务器是与日志服务属于不同账号的ECS、其他云厂商的服务器和自建IDC时，您需要手动安装Logtail。更多信息，请参见[安装](products/sls/documents/install-logtail-on-a-linux-server.md)[Logtail（Linux](products/sls/documents/install-logtail-on-a-linux-server.md)[系统）](products/sls/documents/install-logtail-on-a-linux-server.md)或[安装](products/sls/documents/install-logtail-on-a-windows-server.md)[Logtail（Windows](products/sls/documents/install-logtail-on-a-windows-server.md)[系统）](products/sls/documents/install-logtail-on-a-windows-server.md)。

手动安装Logtail后，您必须在该服务器上手动配置用户标识。具体操作，请参见[配置用户标识](products/sls/documents/configure-a-user-identifier.md)。

- 

安装完成后，单击确认安装完毕。

- 

在创建机器组页面，输入名称，单击下一步。

日志服务支持创建IP地址机器组和用户自定义标识机器组，详细参数说明请参见[创建](products/sls/documents/create-an-ip-address-based-machine-group.md)[IP](products/sls/documents/create-an-ip-address-based-machine-group.md)[地址机器组](products/sls/documents/create-an-ip-address-based-machine-group.md)和[创建用户自定义标识机器组](products/sls/documents/create-a-user-defined-identity-machine-group.md)。

- 

确认目标机器组已在应用机器组区域，单击下一步。

重要

创建机器组后立刻应用，可能因为连接未生效，导致心跳为FAIL，您可单击自动重试。如果还未解决，请参见[Logtail](products/sls/documents/troubleshoot-the-errors-related-to-logtail-machine-groups.md)[机器组无心跳](products/sls/documents/troubleshoot-the-errors-related-to-logtail-machine-groups.md)进行排查。

- 

在数据源设置页签中，粘贴以下代码到插件配置栏，其中${服务器IP}请替换成您的服务器IP地址，然后单击下一步。

{ "inputs": [ { "type": "metric_http", "detail": { "IntervalMs": 60000, "Addresses": [ "http://${服务器IP}/nginx_status", "http://${服务器IP}/nginx_status", "http://${服务器IP}/nginx_status" ], "IncludeBody": true } } ], "processors": [ { "type": "processor_regex", "detail": { "SourceKey": "content", "Regex": "Active connections: (\\d+)\\s+server accepts handled requests\\s+(\\d+)\\s+(\\d+)\\s+(\\d+)\\s+Reading: (\\d+) Writing: (\\d+) Waiting: (\\d+)[\\s\\S]*", "Keys": [ "connection", "accepts", "handled", "requests", "reading", "writing", "waiting" ], "FullMatch": true, "NoKeyError": true, "NoMatchError": true, "KeepSource": false } } ] }

- 

inputs为数据源配置，必选项。

重要

一个inputs中只允许配置一个类型的数据源。

- 

processors为处理配置，用于解析数据。可选项，您可以配置一种或多种处理方式。

如果当前的inputs配置无法满足日志解析需求，您可以在插件配置中添加processors配置，即添加Logtail插件处理数据。例如提取字段、提取日志时间、脱敏数据、过滤日志等。更多信息，请参见[使用](products/sls/documents/overview-22.md)[Logtail](products/sls/documents/overview-22.md)[插件处理数据](products/sls/documents/overview-22.md)。

重要参数说明如下表所示：

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 数据源类型，固定为 metric_http 。 |
| IntervalMs | int | 是 | 每次请求的间隔，单位：ms。 |
| Addresses | 数组 | 是 | 配置为您需要监控的 URL 列表。 |
| IncludeBody | boolean | 否 | 是否采集请求体，默认值：false。如果为 true，则采集后，将请求体内容存放在 content 字段中。 |


完成采集配置1分钟后，即可查看日志，样例如下所示。日志服务默认生成nginx_status仪表盘，展示查询和分析结果。

_address_: http://127.0.0.1/nginx_status _method_: GET _result_: success _http_response_code_: 200 _response_time_ms_: 0.418 accepts: 6 connection: 3 handled: 6 reading: 0 requests: 6 waiting: 2 writing: 1

## 步骤三：查询和分析日志

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在日志存储>日志库页签中，单击目标Logstore。

- 

输入查询和分析语句，然后单击最近15分钟，设置查询和分析的时间范围。

更多信息，请参见[步骤一：配置索引](products/sls/documents/quick-guide-to-query-and-analysis.md)。

- 

查询日志

- 

查询某IP地址的相关信息。

_address_: 10.10.0.0

- 

查询响应时间超过100毫秒的请求。

_response_time_ms_ > 100

- 

查询状态码不为200的请求。

not _http_response_code_ : 200

- 

分析日志

- 

每5分钟统计一次waiting、reading、writing、connection的平均值。

*| select avg(waiting) as waiting, avg(reading) as reading, avg(writing) as writing, avg(connection) as connection, from_unixtime( __time__ - __time__ % 300) as time group by __time__ - __time__ % 300 order by time limit 1440

- 

统计最大等待连接数排名前十的服务器。

*| select max(waiting) as max_waiting, _address_, from_unixtime(max(__time__)) as time group by address order by max_waiting desc limit 10

- 

统计IP地址数量。

* | select count(distinct(_address_)) as total

- 

统计请求失败的IP地址数量。

not _result_ : success | select count(distinct(_address_))

- 

统计最近十次请求失败的IP地址。

not _result_ : success | select _address_ as address, from_unixtime(__time__) as time order by __time__ desc limit 10

- 

每5分钟统计一次请求总数。

*| select avg(handled) * count(distinct(_address_)) as total_handled, avg(requests) * count(distinct(address)) as total_requests, from_unixtime( __time__ - __time__ % 300) as time group by __time__ - __time__ % 300 order by time limit 1440

- 

每5分钟统计一次平均请求延迟。

*| select avg(_response_time_ms_) as avg_delay, from_unixtime( __time__ - __time__ % 300) as time group by __time__ - __time__ % 300 order by time limit 1440

- 

统计请求成功的数量和失败的数量。

not _http_response_code_ : 200 | select count(1)_http_response_code_ : 200 | select count(1)

[上一篇：查询轻量消息队列（原MNS）日志](products/sls/documents/query-mns-logs.md)[下一篇：分析Apache日志](products/sls/documents/analyze-apache-access-logs.md)

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
